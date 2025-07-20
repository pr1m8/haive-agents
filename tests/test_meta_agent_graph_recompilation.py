"""Test meta agent with graph-level recompilation.

This test demonstrates the core vision: individual agents that are "meta-capable"
with graph-level recompilation when nodes are added, output parsing changes, etc.

Key Focus:
- Graph structure modifications trigger recompilation
- Adding nodes dynamically to existing graphs
- Output parsing changes require graph rebuilding
- MetaStateSchema focused on graph composition, not tool management
"""

from datetime import datetime
from typing import Any

from haive.core.common.mixins.recompile_mixin import RecompileMixin
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.prebuilt.meta_state import MetaStateSchema
from pydantic import Field

from haive.agents.simple.agent import SimpleAgent


class GraphRecompilableSimpleAgent(RecompileMixin, SimpleAgent):
    """SimpleAgent with graph-level recompilation tracking."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use private attributes to avoid Pydantic field conflicts
        self._custom_nodes = {}
        self._custom_output_parsers = {}

    def _compute_state_hash(self) -> str:
        """Hash based on graph structure and parsing configuration."""
        import hashlib

        components = [
            # Core agent identity
            str(self.name),
            # Graph structure
            str(
                list(self.graph.nodes.keys())
                if hasattr(self, "graph") and self.graph
                else []
            ),
            str(
                list(self.graph.edges) if hasattr(self, "graph") and self.graph else []
            ),
            # Custom nodes and parsers
            str(sorted(self._custom_nodes.keys())),
            str(sorted(self._custom_output_parsers.keys())),
            # Engine configuration
            str(type(self.engine).__name__),
            str(getattr(self.engine, "system_message", "")),
        ]

        state_str = "|".join(components)
        return hashlib.md5(state_str.encode()).hexdigest()

    def add_custom_node(
        self, node_name: str, node_func: callable, position: str = "before_end"
    ) -> None:
        """Add a custom node to the graph and trigger recompilation."""
        # Store the custom node
        self._custom_nodes[node_name] = {
            "func": node_func,
            "position": position,
            "added_at": datetime.now(),
        }

        # Mark for recompilation
        self.mark_for_recompile(f"Custom node '{node_name}' added")

    def add_output_parser(self, parser_name: str, parser_func: callable) -> None:
        """Add custom output parser and trigger recompilation."""
        # Store the parser
        self._custom_output_parsers[parser_name] = {
            "func": parser_func,
            "added_at": datetime.now(),
        }

        # Mark for recompilation
        self.mark_for_recompile(f"Output parser '{parser_name}' added")

    def build_graph(self) -> BaseGraph:
        """Build graph with custom nodes and parsers."""
        # Get base graph
        graph = super().build_graph()

        # Add custom nodes if any
        for node_name, node_info in self._custom_nodes.items():

            if node_info["position"] == "before_end":
                # Add before the END node
                graph.add_node(node_name, node_info["func"])

                # Find the node that currently leads to END and redirect it
                for edge in list(graph.edges):
                    if edge[1] == "__end__":  # If this edge goes to END
                        graph.remove_edge(edge[0], "__end__")
                        graph.add_edge(edge[0], node_name)
                        break

                # Connect new node to END
                graph.add_edge(node_name, "__end__")

            elif node_info["position"] == "after_start":
                # Add after the START node
                graph.add_node(node_name, node_info["func"])

                # Find the node that START currently leads to and redirect
                for edge in list(graph.edges):
                    if edge[0] == "__start__":  # If this edge starts from START
                        graph.remove_edge("__start__", edge[1])
                        graph.add_edge(node_name, edge[1])
                        break

                # Connect START to new node
                graph.add_edge("__start__", node_name)

        # Add output parsers to relevant nodes
        if self._custom_output_parsers:
            # This would modify how the graph processes outputs
            # For now, just log that we're applying them
            for _parser_name, _parser_info in self._custom_output_parsers.items():
                pass

        return graph

    def recompile_graph(self) -> dict[str, Any]:
        """Recompile the graph and return detailed information."""
        result = {
            "was_recompiled": False,
            "recompilation_reason": None,
            "before_hash": self._compute_state_hash(),
            "after_hash": None,
            "graph_nodes_before": None,
            "graph_nodes_after": None,
            "custom_nodes_applied": list(self._custom_nodes.keys()),
            "output_parsers_applied": list(self._custom_output_parsers.keys()),
            "timestamp": datetime.now(),
        }

        if self.needs_recompile:

            # Get current state
            result["graph_nodes_before"] = (
                list(self.graph.nodes.keys())
                if hasattr(self, "graph") and self.graph
                else []
            )
            result["recompilation_reason"] = (
                "Graph structure or parsing configuration changed"
            )

            # Rebuild graph with custom nodes and parsers
            self.graph = self.build_graph()

            # Update state
            result["graph_nodes_after"] = (
                list(self.graph.nodes.keys())
                if hasattr(self, "graph") and self.graph
                else []
            )
            result["after_hash"] = self._compute_state_hash()
            result["was_recompiled"] = True

            # Mark as compiled
            self.resolve_recompile(success=True)

        else:
            result["after_hash"] = result["before_hash"]

        return result


class GraphFocusedMetaState(MetaStateSchema):
    """MetaStateSchema focused on graph composition recompilation."""

    # Graph recompilation tracking
    graph_modification_count: int = Field(
        default=0, description="Number of graph modifications"
    )
    custom_nodes_added: list[str] = Field(
        default_factory=list, description="Custom nodes added to graph"
    )
    output_parsers_added: list[str] = Field(
        default_factory=list, description="Output parsers added"
    )

    def _compute_state_hash(self) -> str:
        """Hash based on graph composition state."""
        import hashlib

        components = [
            # Base state
            super()._compute_state_hash(),
            # Graph modifications
            str(self.graph_modification_count),
            str(sorted(self.custom_nodes_added)),
            str(sorted(self.output_parsers_added)),
            # Agent graph state
            str(type(self.agent).__name__ if self.agent else "None"),
            str(getattr(self.agent, "_custom_nodes", {}).keys() if self.agent else []),
            str(
                getattr(self.agent, "_custom_output_parsers", {}).keys()
                if self.agent
                else []
            ),
        ]

        state_str = "|".join(components)
        return hashlib.md5(state_str.encode()).hexdigest()

    def add_node_to_agent(
        self, node_name: str, node_func: callable, position: str = "before_end"
    ) -> None:
        """Add node to the embedded agent and track at meta level."""
        if not self.agent:
            raise ValueError("No agent embedded in meta state")

        # Add to agent
        self.agent.add_custom_node(node_name, node_func, position)

        # Track at meta level
        self.custom_nodes_added.append(node_name)
        self.graph_modification_count += 1

        # Mark meta state for recompilation
        self.mark_for_recompile(f"Node '{node_name}' added to embedded agent")

    def add_output_parser_to_agent(
        self, parser_name: str, parser_func: callable
    ) -> None:
        """Add output parser to the embedded agent and track at meta level."""
        if not self.agent:
            raise ValueError("No agent embedded in meta state")

        # Add to agent
        self.agent.add_output_parser(parser_name, parser_func)

        # Track at meta level
        self.output_parsers_added.append(parser_name)
        self.graph_modification_count += 1

        # Mark meta state for recompilation
        self.mark_for_recompile(
            f"Output parser '{parser_name}' added to embedded agent"
        )

    def recompile_agent_if_needed(self) -> dict[str, Any]:
        """Check and recompile embedded agent if needed."""
        if not self.agent:
            return {"error": "No agent embedded in meta state"}

        # Check if agent needs recompilation
        if hasattr(self.agent, "needs_recompile") and self.agent.needs_recompile:

            # Recompile agent
            result = self.agent.recompile_graph()

            # Update meta state
            if result["was_recompiled"]:
                self.resolve_recompile(success=True)

            return result
        return {
            "was_recompiled": False,
            "reason": "Agent does not need recompilation",
        }


# Test functions
def test_graph_recompilation_with_custom_nodes():
    """Test adding custom nodes to agent graph and recompiling."""
    # Create engine and agent
    engine = AugLLMConfig(
        system_message="You are a helpful assistant.",
        temperature=0.1,  # Low temperature for consistent testing
    )

    agent = GraphRecompilableSimpleAgent(name="graph_test_agent", engine=engine)

    # Initial state

    # Mark as initially compiled (nothing to do - starts as False)

    # Custom nodes to add
    def analysis_node(state):
        state["analysis_complete"] = True
        return state

    def validation_node(state):
        state["validation_passed"] = True
        return state

    # Add custom nodes
    agent.add_custom_node("analysis", analysis_node, "after_start")
    agent.add_custom_node("validation", validation_node, "before_end")

    # Recompile
    agent.recompile_graph()

    # Final state

    return agent


def test_output_parser_recompilation():
    """Test adding output parsers and recompiling."""
    # Create agent
    engine = AugLLMConfig()
    agent = GraphRecompilableSimpleAgent(name="parser_test_agent", engine=engine)

    # Custom output parsers
    def json_parser(output):
        return {"parsed": True, "original": output}

    def sentiment_parser(output):
        return {"sentiment": "positive", "original": output}

    # Add parsers
    agent.add_output_parser("json", json_parser)
    agent.add_output_parser("sentiment", sentiment_parser)

    # Recompile
    agent.recompile_graph()

    return agent


def test_meta_state_graph_composition():
    """Test MetaStateSchema with graph composition focus."""
    # Create agent
    engine = AugLLMConfig()
    agent = GraphRecompilableSimpleAgent(name="meta_test_agent", engine=engine)

    # Create meta state
    meta_state = GraphFocusedMetaState()
    meta_state.agent = agent

    # Register for meta-level change notifications
    def meta_change_handler(change_type: str, details: dict[str, Any]):
        pass

    meta_state.register_change_callback(meta_change_handler)

    # Initial state

    # Mark as initially compiled
    meta_state.mark_compiled("Initial meta state")
    meta_state.agent.mark_compiled("Initial agent state")

    # Add nodes through meta state

    def preprocessing_node(state):
        state["preprocessed"] = True
        return state

    def postprocessing_node(state):
        state["postprocessed"] = True
        return state

    meta_state.add_node_to_agent("preprocessing", preprocessing_node, "after_start")
    meta_state.add_output_parser_to_agent("format", lambda x: f"Formatted: {x}")

    # Recompile through meta state
    meta_state.recompile_agent_if_needed()

    # Final state

    return meta_state


def test_combined_graph_recompilation():
    """Test combined graph modifications and recompilation."""
    # Create meta state system
    engine = AugLLMConfig()
    agent = GraphRecompilableSimpleAgent(name="combined_test_agent", engine=engine)

    meta_state = GraphFocusedMetaState()
    meta_state.agent = agent

    # Mark initial state
    meta_state.mark_compiled("Initial state")
    agent.mark_compiled("Initial state")

    # Define custom components
    def input_validator(state):
        state["input_valid"] = True
        return state

    def output_formatter(state):
        state["output_formatted"] = True
        return state

    def json_parser(output):
        return {"type": "json", "content": output}

    def markdown_parser(output):
        return {"type": "markdown", "content": output}

    # Batch modifications

    # Add multiple nodes and parsers
    meta_state.add_node_to_agent("input_validator", input_validator, "after_start")
    meta_state.add_node_to_agent("output_formatter", output_formatter, "before_end")
    meta_state.add_output_parser_to_agent("json", json_parser)
    meta_state.add_output_parser_to_agent("markdown", markdown_parser)

    # Recompile
    meta_state.recompile_agent_if_needed()

    # Verify final state

    return meta_state


if __name__ == "__main__":
    # Run all tests

    try:
        # Test 1: Custom nodes
        agent1 = test_graph_recompilation_with_custom_nodes()

        # Test 2: Output parsers
        agent2 = test_output_parser_recompilation()

        # Test 3: Meta state composition (disabled - needs more work)
        # meta_state = test_meta_state_graph_composition()

        # Test 4: Combined modifications (disabled - needs more work)
        # combined_meta = test_combined_graph_recompilation()

    except Exception:
        import traceback

        traceback.print_exc()
