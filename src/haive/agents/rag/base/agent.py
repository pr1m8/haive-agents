import logging
import time
from typing import Any, Dict, Union, List

from langgraph.types import Command
from langgraph.graph import END, START

from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.graph.GraphRegistry import register_graph_component
from haive.core.graph.GraphBuilder import DynamicGraph
from haive.core.graph.branches import Branch

from haive.agents.rag.base.config import BaseRAGConfig
from haive.agents.rag.base.state import BaseRAGState

logger = logging.getLogger(__name__)

@register_agent(BaseRAGConfig)
@register_graph_component(
    "agent", 
    "BaseRAGAgent", 
    tags=["rag", "retrieval", "agent"],
    metadata={
        "description": "Base Retrieval-Augmented Generation agent"
    }
)
class BaseRAGAgent(Agent[BaseRAGConfig]):
    """
    Base RAG agent that focuses on document retrieval.
    
    This agent implements a basic workflow:
    1. Receive a query
    2. Retrieve relevant documents
    """

    def __init__(self, config: BaseRAGConfig):
        """
        Initialize the RAG agent with configuration.
        
        Args:
            config: Configuration for the RAG agent
        """
        # Lazy initialization of retriever
        self._retriever = None
        
        # Call parent initialization
        super().__init__(config)

    @property
    def retriever(self):
        """Lazy initialization of retriever."""
        if self._retriever is None:
            # Ensure retriever is created from config
            self._retriever = self.config.retriever_config.create_runnable()
        return self._retriever

    def retrieve_documents(self, state: BaseRAGState) -> Command:
        """
        Retrieve relevant documents based on the query.
        
        Args:
            state: Current state with query
            
        Returns:
            Command for updating state with retrieved documents
        """
        logger.info(f"Retrieving documents for query: {state.query}")
        start_time = time.time()
        
        try:
            # Use retriever to get documents
            documents = self.retriever.invoke(state.query)
            
            logger.info(f"Retrieved {len(documents)} documents in {time.time() - start_time:.2f}s")
            
            # Update state with retrieved documents
            return Command(
                update={"retrieved_documents": documents}
            )
        
        except Exception as e:
            logger.error(f"Error retrieving documents: {str(e)}")
            return Command(
                update={"error": f"Error retrieving documents: {str(e)}"}
            )

    def setup_workflow(self) -> None:
        """
        Set up the dynamic workflow for the RAG agent.
        
        Creates a flexible graph for document retrieval.
        """
        # Create a dynamic graph builder
        graph_builder = DynamicGraph(
            name=f"{self.config.name}_workflow",
            components=[self.retriever],
            state_schema=BaseRAGState
        )
        
        # Add retrieval node
        graph_builder.add_node(
            "retrieve_documents", 
            self.retrieve_documents, 
            command_goto=END
        )
        
        # Set workflow edges
        graph_builder.add_edge(START, "retrieve_documents")
        
        # Compile the graph
        self.graph = graph_builder.build()
        
        logger.info(f"Basic retrieval workflow set up for {self.config.name}")