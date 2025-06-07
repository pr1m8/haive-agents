# from haive.core.engine.retriever import RetrieverConfig  # Correct import
from typing import get_origin

from haive.core.engine.retriever import BaseRetrieverConfig
from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langgraph.graph import END, START
from pydantic import Field

from haive.agents.base.agent import Agent


class SimpleRAGAgent(Agent):
    """Simple RAG agent that performs retrieval."""

    name: str = "Simple RAG Agent"
    engine: BaseRetrieverConfig = Field(..., description="Retriever Engine")

    def build_graph(self) -> BaseGraph:
        """Build the RAG agent graph."""
        # Create base graph with proper name
        graph = BaseGraph(name="SimpleRAGAgent")

        # Add the retrieval node
        retrieval_node = EngineNodeConfig(engine=self.engine, name="retrieval_node")
        graph.add_node("retrieval_node", retrieval_node)

        # Set up proper flow: START -> retrieval_node -> END
        graph.add_edge(START, "retrieval_node")
        graph.add_edge("retrieval_node", END)

        return graph
