import logging
import time

from langchain_core.messages import HumanMessage
from langgraph.graph import END, START
from langgraph.types import Command

from haive.agents.rag.base.config import BaseRAGState
from haive.agents.rag.llm_rag.config import LLMRAGConfig
from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.engine.aug_llm.base import AugLLMConfig

logger = logging.getLogger(__name__)

@register_agent(LLMRAGConfig)
class LLMRAGAgent(Agent[LLMRAGConfig]):
    """Enhanced RAG agent that adds an answer generation step after document retrieval.
    """

    def __init__(self, config: LLMRAGConfig):
        # Ensure full initialization from parent Agent class
        super().__init__(config)

    def generate_answer(self, state: BaseRAGState) -> Command:
        """Generate an answer based on retrieved documents.

        Args:
            state: Current state with query and retrieved documents
            
        Returns:
            Command with generated answer
        """
        query = state.query
        documents = state.retrieved_documents

        if not documents:
            return Command(update={"answer": "I couldn't find any relevant documents to answer your query."})

        # Combine document contents for context
        context = "\n\n".join([doc.page_content for doc in documents])

        # Attempt to get answer generator
        try:
            # Resolve the engine for answer generation
            answer_generator = self._resolve_answer_generator()

            # Prepare input for the model
            messages = [
                HumanMessage(content=f"Context:\n{context}\n\nQuery: {query}\n\nBased on the context, please provide a detailed answer to the query."),
            ]

            # Invoke the answer generator
            answer = answer_generator.invoke(messages)

            # Extract content if it's an AIMessage or similar
            if hasattr(answer, "content"):
                answer = answer.content

        except Exception as e:
            logger.error(f"Error generating answer: {e}")
            return Command(update={"answer": f"Error generating answer: {e}"})

        return Command(update={"answer": answer})

    def _resolve_answer_generator(self):
        """Resolve the answer generator from the configuration.
        
        Returns:
            A runnable answer generator
        """
        # Check if using dictionary of engines
        if isinstance(self.config.engine, dict):
            # Try to get answer generator from the dictionary
            answer_generator = self.config.engine.get("answer_generator")
        else:
            # Use the main engine
            answer_generator = self.config.engine

        # If it's an AugLLMConfig, create a runnable
        if isinstance(answer_generator, AugLLMConfig):
            answer_generator = answer_generator.create_runnable()

        # Validate that the answer generator has an invoke method
        if not hasattr(answer_generator, "invoke"):
            raise ValueError("Answer generator must have an 'invoke' method")

        return answer_generator

    def setup_workflow(self) -> None:
        """Set up the retrieval and answer generation workflow graph."""
        # First, retrieve documents
        self.graph.add_node("retrieve", self._retrieve_documents)

        # Then generate answer
        self.graph.add_node("generate_answer", self.generate_answer)

        # Define workflow: START -> retrieve -> generate_answer -> END
        self.graph.add_edge(START, "retrieve")
        self.graph.add_edge("retrieve", "generate_answer")
        self.graph.add_edge("generate_answer", END)

        logger.info(f"Retrieval and answer generation workflow set up for {self.config.name}")

    def _retrieve_documents(self, state: BaseRAGState) -> Command:
        """Retrieve relevant documents based on the query.
        
        Args:
            state: Current state with query
            
        Returns:
            Command for updating state with retrieved documents
        """
        logger.info(f"Retrieving documents for query: {state.query}")
        start_time = time.time()

        try:
            # Lazy initialize retriever
            if not hasattr(self, "_retriever") or self._retriever is None:
                self._retriever = self.config.retriever_config.create_runnable()

            # Use retriever to get documents
            documents = self._retriever.invoke(state.query)

            logger.info(f"Retrieved {len(documents)} documents in {time.time() - start_time:.2f}s")

            # Update state with retrieved documents
            return Command(
                update={"retrieved_documents": documents}
            )

        except Exception as e:
            logger.error(f"Error retrieving documents: {e!s}")
            return Command(
                update={"error": f"Error retrieving documents: {e!s}"}
            )

    def _ensure_pool_open(self):
        """Wrapper method to ensure compatibility with parent class pool management.
        Delegates to the parent class method if it exists.
        """
        try:
            # Check if parent method exists and call it
            parent_method = super()._ensure_pool_open
            return parent_method()
        except AttributeError:
            # Fallback if method doesn't exist
            logger.debug("No parent _ensure_pool_open method found")
            return None
