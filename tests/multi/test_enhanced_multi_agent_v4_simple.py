"""Test EnhancedMultiAgentV4 with a simple approach."""

import contextlib

from langchain_core.messages import HumanMessage

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


class TestEnhancedMultiAgentV4Simple:
    """Test EnhancedMultiAgentV4 with a simplified approach."""

    def test_single_agent_workflow(self):
        """Test with just a single agent to isolate issues."""
        # Create a single agent
        agent = SimpleAgentV3(
            name="test_agent",
            engine=AugLLMConfig(
                temperature=0.7,
                system_message="You are a helpful assistant.",
            ),
            debug=True,
        )

        # Create workflow with single agent
        workflow = EnhancedMultiAgentV4(
            name="single_agent_workflow",
            agents=[agent],
            execution_mode="manual",
            build_mode="manual",
        )

        # Build graph
        graph = workflow.build_graph()
        assert graph is not None

        # Check nodes

        # Compile
        workflow.compile()

        # Create minimal input - just messages
        input_data = {"messages": [HumanMessage(content="Hello, how are you?")]}

        try:
            # Execute directly
            result = workflow._app.invoke(input_data)

            # Check if we got a response
            if "messages" in result:
                for _i, _msg in enumerate(result["messages"]):
                    pass

        except Exception:
            import traceback

            traceback.print_exc()

    def test_debug_agent_node_creation(self):
        """Debug how agent nodes are created."""
        from haive.core.graph.node.agent_node_v3 import create_agent_node_v3

        # Create agent
        agent = SimpleAgentV3(
            name="debug_agent",
            engine=AugLLMConfig(
                temperature=0.7,
                system_message="Test agent for debugging.",
            ),
        )

        # Create node directly
        node_config = create_agent_node_v3(agent_name="debug_agent", agent=agent)

        # Check if it's a callable
        if callable(node_config):

            # Try calling with a simple state
            test_state = {
                "messages": [HumanMessage(content="Test message")],
                "agents": {},
                "agent_states": {},
            }

            with contextlib.suppress(Exception):
                node_config(test_state)


if __name__ == "__main__":
    test = TestEnhancedMultiAgentV4Simple()

    test.test_single_agent_workflow()

    test.test_debug_agent_node_creation()
