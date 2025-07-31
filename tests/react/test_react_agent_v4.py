"""Test ReactAgentV4 - verify inheritance and looping behavior."""

import logging

from langchain_core.tools import tool

from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


logger = logging.getLogger(__name__)


@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error: {e!s}"


class TestReactAgentV4:
    """Test ReactAgentV4 inheritance and graph structure."""

    def test_inheritance_from_simple_agent_v3(self):
        """Verify ReactAgentV4 properly inherits from SimpleAgentV3."""
        agent = ReactAgentV4(name="test_react", engine=AugLLMConfig())

        # Check inheritance
        assert isinstance(agent, SimpleAgentV3)
        assert isinstance(agent, ReactAgentV4)

        # Check inherited attributes exist
        assert hasattr(agent, "name")
        assert hasattr(agent, "engine")
        assert hasattr(agent, "graph")
        assert hasattr(agent, "debug")

        # Check methods exist
        assert hasattr(agent, "build_graph")
        assert hasattr(agent, "run")
        assert hasattr(agent, "arun")

    def test_graph_structure_with_tools(self):
        """Test that tool_node loops back to agent_node."""
        agent = ReactAgentV4(
            name="test_react_tools",
            engine=AugLLMConfig(tools=[calculator], temperature=0.1),
            debug=True,
        )

        # Build the graph
        graph = agent.build_graph()

        # Check nodes exist
        assert "agent_node" in graph.nodes
        assert "validation" in graph.nodes
        assert "tool_node" in graph.nodes

        # Check the loop - tool_node should connect to agent_node
        # Get edges from the compiled graph
        edges = []
        for node, node_edges in graph._graph.edges.items():
            for edge in node_edges:
                edges.append((node, edge))

        # Check tool_node goes to agent_node (not END)
        tool_edges = [e for e in edges if e[0] == "tool_node"]
        assert any(
            e[1] == "agent_node" for e in tool_edges
        ), "tool_node should loop to agent_node"
        assert not any(
            e[1] == END for e in tool_edges
        ), "tool_node should NOT go to END"

        logger.info(f"Graph edges: {edges}")

    def test_graph_structure_without_tools(self):
        """Test graph structure when no tools are present."""
        agent = ReactAgentV4(
            name="test_react_no_tools", engine=AugLLMConfig(temperature=0.1), debug=True
        )

        # Build the graph
        graph = agent.build_graph()

        # Should still have agent_node
        assert "agent_node" in graph.nodes

        # Should not have tool_node
        assert "tool_node" not in graph.nodes

    def test_simple_execution(self):
        """Test basic execution works."""
        agent = ReactAgentV4(
            name="test_execution",
            engine=AugLLMConfig(
                tools=[calculator],
                temperature=0.1,
                system_message="You are a helpful calculator. Use the calculator tool to solve math problems.",
            ),
            debug=True,
        )

        # This tests that the agent can be created and graph built
        # Real execution would require a real LLM
        assert agent.graph is not None
        assert agent.name == "test_execution"

    def test_debug_logging(self):
        """Test that debug logging works in ReactAgent."""
        agent = ReactAgentV4(
            name="test_debug", engine=AugLLMConfig(tools=[calculator]), debug=True
        )

        # Build graph and check debug was used
        agent.build_graph()

        # Agent should have debug enabled
        assert agent.debug is True
