"""Enhanced BaseRAGAgent implementation using Agent[RetrieverEngine].

BaseRAGAgent = Agent[RetrieverEngine] - the engine type defines RAG capability.
"""

import logging
from typing import Any, Dict, List, Optional, TypeVar, Union

from langchain_core.documents import Document
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.retrievers import BaseRetriever
from langgraph.graph import END, START
from pydantic import Field, field_validator, model_validator

from haive.core.engine.base import InvokableEngine
from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.node.retriever_node import RetrieverNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph

# Define RetrieverEngine type
class RetrieverEngine(InvokableEngine):
    """Engine that includes retrieval capabilities.
    
    This engine type is what makes an agent a RAG agent.
    It combines LLM capabilities with document retrieval.
    """
    
    retriever: BaseRetriever = Field(..., description="Document retriever")
    llm_config: Any = Field(..., description="LLM configuration")
    
    # RAG-specific settings
    k: int = Field(default=4, description="Number of documents to retrieve")
    score_threshold: Optional[float] = Field(default=None, description="Minimum relevance score")
    
    async def aretrieve(self, query: str) -> List[Document]:
        """Async retrieve documents."""
        if hasattr(self.retriever, 'aget_relevant_documents'):
            return await self.retriever.aget_relevant_documents(query)
        else:
            # Fallback to sync in thread
            import asyncio
            return await asyncio.to_thread(
                self.retriever.get_relevant_documents, query
            )
    
    def retrieve(self, query: str) -> List[Document]:
        """Sync retrieve documents."""
        return self.retriever.get_relevant_documents(query)


# Import base enhanced agent when available
# from haive.agents.base.enhanced_agent import Agent
from haive.agents.simple.enhanced_simple_real import EnhancedAgentBase as Agent

logger = logging.getLogger(__name__)


class BaseRAGAgent(Agent):  # Will be Agent[RetrieverEngine] when imports fixed
    """Enhanced BaseRAGAgent with retrieval-augmented generation.
    
    BaseRAGAgent = Agent[RetrieverEngine].
    
    The RetrieverEngine type is what makes this a RAG agent. It provides:
    1. Document retrieval capabilities
    2. Context-aware generation
    3. Source attribution
    4. Relevance filtering
    
    This is the base class for all RAG variants (Simple, Conversational, etc).
    
    Attributes:
        retriever: Document retriever (becomes part of engine)
        k: Number of documents to retrieve
        score_threshold: Minimum relevance score
        include_sources: Whether to include source citations
        
    Examples:
        Basic RAG with vector store::
        
            from langchain.vectorstores import FAISS
            
            vectorstore = FAISS.from_texts(documents, embeddings)
            rag_agent = BaseRAGAgent(
                name="knowledge_assistant",
                retriever=vectorstore.as_retriever(),
                k=5
            )
            
            answer = rag_agent.run("What is the capital of France?")
            # Returns answer with context from retrieved documents
            
        With score filtering::
        
            rag_agent = BaseRAGAgent(
                name="precise_rag",
                retriever=vectorstore.as_retriever(),
                score_threshold=0.7,  # Only use highly relevant docs
                include_sources=True
            )
            
            result = rag_agent.run("Complex technical question")
            # Returns answer with sources and high relevance
    """
    
    # RAG-specific fields (these configure the RetrieverEngine)
    retriever: BaseRetriever = Field(
        ...,
        description="Document retriever"
    )
    
    k: int = Field(
        default=4,
        ge=1,
        le=20,
        description="Number of documents to retrieve"
    )
    
    score_threshold: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Minimum relevance score for documents"
    )
    
    include_sources: bool = Field(
        default=True,
        description="Include source citations in response"
    )
    
    rerank_documents: bool = Field(
        default=False,
        description="Whether to rerank retrieved documents"
    )
    
    context_window: int = Field(
        default=3000,
        description="Maximum context length in tokens"
    )
    
    # LLM configuration for generation
    temperature: float = Field(default=0.3, ge=0.0, le=2.0)
    system_message: Optional[str] = Field(default=None)
    
    @model_validator(mode="before")
    @classmethod
    def create_retriever_engine(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Create RetrieverEngine from components."""
        if not isinstance(values, dict):
            return values
        
        # If engine not provided, create RetrieverEngine
        if "engine" not in values or values["engine"] is None:
            retriever = values.get("retriever")
            if not retriever:
                raise ValueError("BaseRAGAgent requires a retriever")
            
            # Import here to avoid circular imports
            from haive.core.engine.aug_llm.config import AugLLMConfig
            
            # Create RetrieverEngine
            values["engine"] = RetrieverEngine(
                retriever=retriever,
                llm_config=AugLLMConfig(
                    temperature=values.get("temperature", 0.3),
                    system_message=values.get("system_message")
                ),
                k=values.get("k", 4),
                score_threshold=values.get("score_threshold")
            )
        
        return values
    
    def setup_agent(self) -> None:
        """Setup RAG agent with appropriate prompt."""
        if isinstance(self.engine, RetrieverEngine):
            # Update engine settings
            self.engine.k = self.k
            self.engine.score_threshold = self.score_threshold
            
            # Set RAG-specific prompt if not custom
            if hasattr(self.engine.llm_config, 'system_message'):
                if not self.engine.llm_config.system_message:
                    self.engine.llm_config.system_message = self._get_default_rag_prompt()
    
    def _get_default_rag_prompt(self) -> str:
        """Get default RAG prompt."""
        return """You are a helpful assistant with access to a knowledge base.

When answering questions:
1. Use the provided context from retrieved documents
2. Be accurate and cite sources when requested
3. If the context doesn't contain relevant information, say so
4. Synthesize information from multiple sources when available
5. Maintain consistency with the retrieved information

Always base your answers on the retrieved context."""
    
    async def retrieve(self, query: str) -> List[Document]:
        """Retrieve relevant documents.
        
        This method is available because engine is RetrieverEngine.
        
        Args:
            query: Search query
            
        Returns:
            List of relevant documents
        """
        if isinstance(self.engine, RetrieverEngine):
            return await self.engine.aretrieve(query)
        else:
            raise RuntimeError("Engine is not a RetrieverEngine")
    
    def retrieve_sync(self, query: str) -> List[Document]:
        """Synchronous document retrieval."""
        if isinstance(self.engine, RetrieverEngine):
            return self.engine.retrieve(query)
        else:
            raise RuntimeError("Engine is not a RetrieverEngine")
    
    def format_context(self, documents: List[Document]) -> str:
        """Format retrieved documents as context.
        
        Args:
            documents: Retrieved documents
            
        Returns:
            Formatted context string
        """
        if not documents:
            return "No relevant documents found."
        
        context_parts = []
        for i, doc in enumerate(documents, 1):
            content = doc.page_content.strip()
            
            # Include source if available
            if self.include_sources and doc.metadata:
                source = doc.metadata.get("source", f"Document {i}")
                context_parts.append(f"[{source}]\n{content}")
            else:
                context_parts.append(f"Document {i}:\n{content}")
        
        return "\n\n".join(context_parts)
    
    def build_graph(self) -> BaseGraph:
        """Build RAG agent graph with retrieval flow."""
        graph = BaseGraph(name=f"{self.name}_rag_graph")
        
        # Add retriever node
        retriever_node = RetrieverNodeConfig(
            name="retrieve",
            retriever=self.retriever,
            k=self.k
        )
        graph.add_node("retrieve", retriever_node)
        
        # Add generation node
        if hasattr(self.engine, 'llm_config'):
            generation_node = EngineNodeConfig(
                name="generate",
                engine=self.engine.llm_config
            )
        else:
            generation_node = EngineNodeConfig(
                name="generate",
                engine=self.engine
            )
        graph.add_node("generate", generation_node)
        
        # Flow: START -> Retrieve -> Generate -> END
        graph.add_edge(START, "retrieve")
        graph.add_edge("retrieve", "generate")
        graph.add_edge("generate", END)
        
        return graph
    
    def __repr__(self) -> str:
        """String representation showing engine type."""
        engine_type = type(self.engine).__name__ if self.engine else "None"
        return (
            f"BaseRAGAgent[{engine_type}]("
            f"name='{self.name}', "
            f"k={self.k}, "
            f"sources={self.include_sources})"
        )


# Convenience function for creating RAG agents
def create_rag_agent(
    name: str,
    vectorstore: Any,
    k: int = 4,
    score_threshold: Optional[float] = None,
    **kwargs
) -> BaseRAGAgent:
    """Create a RAG agent from a vector store.
    
    Args:
        name: Agent name
        vectorstore: Vector store with as_retriever() method
        k: Number of documents to retrieve
        score_threshold: Minimum relevance score
        **kwargs: Additional agent arguments
        
    Returns:
        Configured BaseRAGAgent
    """
    if hasattr(vectorstore, 'as_retriever'):
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": k}
        )
    else:
        retriever = vectorstore
    
    return BaseRAGAgent(
        name=name,
        retriever=retriever,
        k=k,
        score_threshold=score_threshold,
        **kwargs
    )


# Example usage
if __name__ == "__main__":
    # Mock retriever for demo
    class MockRetriever(BaseRetriever):
        """Mock retriever for demonstration."""
        
        def _get_relevant_documents(self, query: str) -> List[Document]:
            return [
                Document(
                    page_content=f"Mock document about {query}",
                    metadata={"source": "knowledge_base.txt"}
                ),
                Document(
                    page_content=f"Additional information on {query}",
                    metadata={"source": "reference.pdf"}
                )
            ]
        
        async def _aget_relevant_documents(self, query: str) -> List[Document]:
            return self._get_relevant_documents(query)
    
    # Create RAG agent
    rag_agent = BaseRAGAgent(
        name="knowledge_assistant",
        retriever=MockRetriever(),
        k=5,
        include_sources=True,
        temperature=0.3
    )
    
    print(f"Created: {rag_agent}")
    print(f"Retrieval settings: k={rag_agent.k}, sources={rag_agent.include_sources}")
    
    # Example retrieval
    import asyncio
    
    async def demo():
        docs = await rag_agent.retrieve("Python programming")
        print(f"\nRetrieved {len(docs)} documents")
        
        context = rag_agent.format_context(docs)
        print(f"\nFormatted context:\n{context}")
    
    # asyncio.run(demo())