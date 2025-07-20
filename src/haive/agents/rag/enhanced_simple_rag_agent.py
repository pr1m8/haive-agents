"""Enhanced SimpleRAGAgent - the simplest RAG implementation.

SimpleRAGAgent = BaseRAGAgent with minimal configuration.
"""

import logging
from typing import Any, Dict, Optional

from langchain_core.documents import Document
from pydantic import Field

from haive.agents.rag.enhanced_base_rag_agent import BaseRAGAgent, RetrieverEngine

logger = logging.getLogger(__name__)


class SimpleRAGAgent(BaseRAGAgent):
    """Simple RAG agent with minimal configuration.
    
    SimpleRAGAgent is just BaseRAGAgent with sensible defaults.
    It provides the easiest way to create a RAG agent.
    
    Key features:
    1. Minimal configuration required
    2. Automatic prompt generation
    3. Simple retrieve-generate flow
    4. No conversation history by default
    
    Examples:
        Quick setup with vector store::
        
            from langchain.vectorstores import FAISS
            from langchain.embeddings import OpenAIEmbeddings
            
            # Create vector store
            texts = ["Paris is the capital of France", "London is the capital of UK"]
            vectorstore = FAISS.from_texts(texts, OpenAIEmbeddings())
            
            # Create simple RAG agent
            rag = SimpleRAGAgent(
                name="simple_qa",
                retriever=vectorstore.as_retriever()
            )
            
            answer = rag.run("What is the capital of France?")
            # Returns: "Based on the context, Paris is the capital of France."
            
        With basic configuration::
        
            rag = SimpleRAGAgent(
                name="configured_rag",
                retriever=retriever,
                k=3,  # Retrieve only 3 documents
                temperature=0.1  # More deterministic
            )
    """
    
    # SimpleRAG specific defaults
    k: int = Field(
        default=3,  # Fewer documents for simple use cases
        description="Number of documents to retrieve"
    )
    
    temperature: float = Field(
        default=0.1,  # More deterministic for simple Q&A
        description="LLM temperature"
    )
    
    include_sources: bool = Field(
        default=False,  # Simpler output by default
        description="Include source citations"
    )
    
    # Simplified prompt
    simple_prompt_template: Optional[str] = Field(
        default=None,
        description="Optional simple prompt template"
    )
    
    def setup_agent(self) -> None:
        """Setup simple RAG agent."""
        super().setup_agent()
        
        # Use simple prompt if not overridden
        if isinstance(self.engine, RetrieverEngine) and hasattr(self.engine.llm_config, 'system_message'):
            if not self.engine.llm_config.system_message and not self.simple_prompt_template:
                self.engine.llm_config.system_message = self._get_simple_rag_prompt()
            elif self.simple_prompt_template:
                self.engine.llm_config.system_message = self.simple_prompt_template
    
    def _get_simple_rag_prompt(self) -> str:
        """Get simple RAG prompt for basic Q&A."""
        return """You are a helpful question-answering assistant.

Use the provided context to answer questions accurately and concisely.
If the context doesn't contain the answer, say "I don't have enough information to answer that question."

Keep answers brief and to the point."""
    
    async def quick_answer(self, question: str) -> str:
        """Get a quick answer to a question.
        
        Simplified interface that handles retrieval and generation.
        
        Args:
            question: The question to answer
            
        Returns:
            Answer string
        """
        # Retrieve documents
        docs = await self.retrieve(question)
        
        # Format context
        context = self.format_context(docs)
        
        # Generate answer
        prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
        
        # In real implementation, would use the LLM
        # For now, return a mock response
        return f"Based on the retrieved context about '{question}', here is the answer..."
    
    def format_context(self, documents: list[Document]) -> str:
        """Format documents in a simple way."""
        if not documents:
            return "No relevant information found."
        
        # Simple formatting without sources
        if not self.include_sources:
            contents = [doc.page_content.strip() for doc in documents]
            return "\n".join(contents)
        
        # With sources
        return super().format_context(documents)
    
    def __repr__(self) -> str:
        """Simple representation."""
        return f"SimpleRAGAgent(name='{self.name}', k={self.k})"


# Factory function for even simpler creation
def create_simple_rag(
    name: str,
    vectorstore: Any,
    **kwargs
) -> SimpleRAGAgent:
    """Create a SimpleRAGAgent from a vector store with minimal config.
    
    Args:
        name: Agent name  
        vectorstore: Vector store instance
        **kwargs: Optional configuration
        
    Returns:
        Configured SimpleRAGAgent
        
    Example:
        rag = create_simple_rag("my_rag", vectorstore)
    """
    retriever = vectorstore.as_retriever() if hasattr(vectorstore, 'as_retriever') else vectorstore
    
    return SimpleRAGAgent(
        name=name,
        retriever=retriever,
        **kwargs
    )


# Example usage
if __name__ == "__main__":
    from haive.agents.rag.enhanced_base_rag_agent import MockRetriever
    
    # Create simple RAG agent
    simple_rag = SimpleRAGAgent(
        name="simple_assistant",
        retriever=MockRetriever(),
        k=2  # Only retrieve 2 documents
    )
    
    print(f"Created: {simple_rag}")
    print(f"Settings: k={simple_rag.k}, temp={simple_rag.temperature}")
    
    # Even simpler with factory
    # rag = create_simple_rag("quick_rag", vectorstore)
    
    # Usage patterns
    print("\nUsage patterns:")
    print("1. Basic Q&A: rag.run('What is X?')")
    print("2. Quick answer: await rag.quick_answer('question')")
    print("3. With sources: rag.include_sources = True")
    
    # The key insight: SimpleRAGAgent is just BaseRAGAgent[RetrieverEngine]
    # with sensible defaults for simple use cases!