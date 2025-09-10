"""Extended Chain Agent with simplified chain building capabilities.

This module provides the ExtendedChainAgent class and utilities for building
complex multi-step agent workflows with easy-to-use chain syntax.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union, Callable
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate

from haive.core.engine.agent import Agent, AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.state_schema import StateSchema


class ChainNode(BaseModel):
    """A node in a chain workflow."""

    name: str = Field(..., description="Name of the chain node")
    agent: Any = Field(..., description="The agent for this node")
    config: Optional[Dict[str, Any]] = Field(default=None, description="Node configuration")
    dependencies: List[str] = Field(default_factory=list, description="Dependencies on other nodes")


class ChainEdge(BaseModel):
    """An edge connection between chain nodes."""

    from_node: str = Field(..., description="Source node name")
    to_node: str = Field(..., description="Target node name")
    condition: Optional[Callable] = Field(
        default=None, description="Optional condition for edge traversal"
    )


class ChainConfig(AgentConfig):
    """Configuration for ExtendedChainAgent."""

    nodes: List[ChainNode] = Field(default_factory=list, description="Chain nodes")
    edges: List[ChainEdge] = Field(default_factory=list, description="Chain edges")
    execution_mode: str = Field(
        default="sequential", description="Execution mode: sequential, parallel, conditional"
    )
    max_iterations: int = Field(default=10, description="Maximum chain iterations")


class ChainState(StateSchema):
    """State schema for chain execution."""

    current_node: str = Field(default="", description="Current executing node")
    node_results: Dict[str, Any] = Field(default_factory=dict, description="Results from each node")
    iteration_count: int = Field(default=0, description="Current iteration count")
    completed_nodes: List[str] = Field(default_factory=list, description="List of completed nodes")
    chain_complete: bool = Field(default=False, description="Whether chain execution is complete")


class ChainBuilder:
    """Builder class for creating chain workflows."""

    def __init__(self):
        self.nodes: List[ChainNode] = []
        self.edges: List[ChainEdge] = []

    def add_node(
        self, name: str, agent: Any, config: Optional[Dict[str, Any]] = None
    ) -> "ChainBuilder":
        """Add a node to the chain."""
        node = ChainNode(name=name, agent=agent, config=config or {})
        self.nodes.append(node)
        return self

    def add_edge(
        self, from_node: str, to_node: str, condition: Optional[Callable] = None
    ) -> "ChainBuilder":
        """Add an edge between nodes."""
        edge = ChainEdge(from_node=from_node, to_node=to_node, condition=condition)
        self.edges.append(edge)
        return self

    def build(self) -> ChainConfig:
        """Build the chain configuration."""
        return ChainConfig(nodes=self.nodes, edges=self.edges)


class ExtendedChainAgent(Agent):
    """Extended chain agent for complex multi-step workflows.

    This agent provides a simplified interface for building complex chains
    of agents with dependencies, conditional execution, and state management.
    """

    def __init__(self, config: ChainConfig):
        self.chain_config = config
        self.state_schema = ChainState
        super().__init__(config)

    def setup_workflow(self) -> None:
        """Set up the chain workflow."""
        # Implementation would set up the actual graph workflow
        # based on the chain configuration
        pass

    def execute_node(self, node_name: str, state: ChainState) -> Any:
        """Execute a specific node in the chain."""
        # Find the node
        node = next((n for n in self.chain_config.nodes if n.name == node_name), None)
        if not node:
            raise ValueError(f"Node {node_name} not found in chain")

        # Execute the node's agent
        if hasattr(node.agent, "run"):
            return node.agent.run(state.model_dump())
        else:
            return {"error": f"Agent {node.agent} does not have run method"}

    def get_next_nodes(self, current_node: str, state: ChainState) -> List[str]:
        """Get the next nodes to execute based on current state."""
        next_nodes = []
        for edge in self.chain_config.edges:
            if edge.from_node == current_node:
                if edge.condition is None or edge.condition(state):
                    next_nodes.append(edge.to_node)
        return next_nodes


# Utility functions for easy chain building


def chain(*agents: Any) -> ChainBuilder:
    """Create a simple sequential chain from a list of agents.

    Args:
        *agents: Variable number of agents to chain together

    Returns:
        ChainBuilder instance with sequential chain setup
    """
    builder = ChainBuilder()

    # Add nodes
    for i, agent in enumerate(agents):
        node_name = f"step_{i}"
        builder.add_node(node_name, agent)

        # Add edge to next node (except for last)
        if i < len(agents) - 1:
            builder.add_edge(node_name, f"step_{i + 1}")

    return builder


def chain_with_edges(nodes: Dict[str, Any], edges: List[tuple]) -> ChainBuilder:
    """Create a chain with explicit nodes and edges.

    Args:
        nodes: Dictionary mapping node names to agents
        edges: List of (from_node, to_node) tuples

    Returns:
        ChainBuilder instance with the specified structure
    """
    builder = ChainBuilder()

    # Add nodes
    for name, agent in nodes.items():
        builder.add_node(name, agent)

    # Add edges
    for from_node, to_node in edges:
        builder.add_edge(from_node, to_node)

    return builder


# Export commonly used types
__all__ = [
    "ExtendedChainAgent",
    "ChainBuilder",
    "ChainConfig",
    "ChainState",
    "ChainNode",
    "ChainEdge",
    "chain",
    "chain_with_edges",
    "Any",
    "Dict",
]
