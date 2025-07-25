"""Test EnhancedMultiAgentV4 with a simple approach."""

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


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
        print(f"\nGraph nodes: {list(graph.nodes.keys())}")
        
        # Compile
        workflow.compile()
        
        # Create minimal input - just messages
        input_data = {
            "messages": [HumanMessage(content="Hello, how are you?")]
        }
        
        try:
            # Execute directly
            result = workflow._app.invoke(input_data)
            print(f"\nResult type: {type(result)}")
            print(f"Result keys: {result.keys() if isinstance(result, dict) else 'Not a dict'}")
            
            # Check if we got a response
            if "messages" in result:
                print(f"Messages count: {len(result['messages'])}")
                for i, msg in enumerate(result["messages"]):
                    print(f"Message {i}: {type(msg).__name__} - {msg.content[:50]}...")
                    
        except Exception as e:
            print(f"\nError: {e}")
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
        print(f"\nNode config type: {type(node_config)}")
        print(f"Node config: {node_config}")
        
        # Check if it's a callable
        if callable(node_config):
            print("Node config is callable")
            
            # Try calling with a simple state
            test_state = {
                "messages": [HumanMessage(content="Test message")],
                "agents": {},
                "agent_states": {}
            }
            
            try:
                result = node_config(test_state)
                print(f"Node result type: {type(result)}")
                print(f"Node result: {result}")
            except Exception as e:
                print(f"Error calling node: {e}")


if __name__ == "__main__":
    test = TestEnhancedMultiAgentV4Simple()
    
    print("=" * 60)
    print("Testing Single Agent Workflow")
    print("=" * 60)
    test.test_single_agent_workflow()
    
    print("\n" + "=" * 60)
    print("Debugging Agent Node Creation")
    print("=" * 60)
    test.test_debug_agent_node_creation()