"""Simple test to understand multi-agent workflow execution."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


async def test_basic_workflow():
    """Test basic multi-agent workflow."""
    print("Creating simple agents...")

    # Create two simple agents
    agent1 = SimpleAgentV3(
        name="agent1",
        engine=AugLLMConfig(
            temperature=0.1,
            max_tokens=100,
            system_message="You are agent 1. Say hello.",
        ),
        debug=True,
    )

    agent2 = SimpleAgentV3(
        name="agent2",
        engine=AugLLMConfig(
            temperature=0.1,
            max_tokens=100,
            system_message="You are agent 2. Respond to agent 1.",
        ),
        debug=True,
    )

    print("\nCreating workflow...")
    workflow = EnhancedMultiAgentV4(
        name="test_workflow", agents=[agent1, agent2], execution_mode="sequential"
    )

    print(f"\nWorkflow created. Type: {type(workflow)}")
    print(f"Workflow agents: {workflow.get_agent_names()}")

    # Create simple input
    input_data = {
        "messages": [HumanMessage(content="Hello, please process this message.")]
    }

    print(f"\nInput data: {input_data}")

    try:
        print("\nExecuting workflow...")
        result = await workflow.arun(input_data)

        print("\n=== EXECUTION COMPLETE ===")
        print(f"Result type: {type(result)}")
        print(f"Result class: {result.__class__.__name__}")

        # Check what attributes the result has
        attrs = [attr for attr in dir(result) if not attr.startswith("_")]
        print(f"\nResult has {len(attrs)} attributes")
        print("Key attributes:")

        # Check for common state attributes
        if hasattr(result, "messages"):
            print(f"  - messages: {len(result.messages)} messages")
            for i, msg in enumerate(result.messages[-3:]):  # Last 3 messages
                print(f"    [{i}] {type(msg).__name__}: {msg.content[:50]}...")

        if hasattr(result, "agent_outputs"):
            print(f"  - agent_outputs: {list(result.agent_outputs.keys())}")

        if hasattr(result, "agent_states"):
            print(f"  - agent_states: {list(result.agent_states.keys())}")

        if hasattr(result, "agent_execution_order"):
            print(f"  - agent_execution_order: {result.agent_execution_order}")

        # Check for structured output fields
        for agent_name in ["agent1", "agent2"]:
            if hasattr(result, agent_name):
                print(f"  - {agent_name}: {getattr(result, agent_name)}")

        return result

    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    print("Testing Basic Multi-Agent Workflow")
    print("=" * 50)
    result = asyncio.run(test_basic_workflow())
