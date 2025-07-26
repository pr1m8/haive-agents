#!/usr/bin/env python3
"""Test SimpleAgent v3 with debug flag enabled."""


from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.simple.agent_v3 import SimpleAgentV3


def test_with_debug():
    """Test execution with debug=True."""
    print("\n" + "=" * 70)
    print("🔍 DEBUG TEST: SimpleAgent v3 with debug=True")
    print("=" * 70)

    # Create config
    config = AugLLMConfig(
        temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig()
    )

    # Create agent with debug=True
    agent = SimpleAgentV3(
        name="debug_test_agent",
        engine=config,
        debug=True,  # Enable debug mode
        verbose=True,  # Also enable verbose mode
    )

    # Enable more detailed logging
    import logging

    logging.getLogger("haive.core.graph.node.engine_node_generic").setLevel(
        logging.DEBUG
    )
    logging.getLogger("haive.agents.simple.agent_v3").setLevel(logging.DEBUG)

    print("\n✅ Agent created with debug=True")
    print(f"   - Agent name: {agent.name}")
    print(f"   - Debug mode: {agent.debug}")
    print(f"   - Verbose mode: {agent.verbose}")
    print(f"   - Hooks enabled: {agent.hooks_enabled}")
    print(f"   - State schema: {agent.state_schema.__name__}")

    # Test execution with debug
    print("\n🚀 Executing with debug enabled...")
    try:
        # Run with debug=True in the execution call as well
        result = agent.run(
            "Say 'Debug mode is active!' and tell me what 2+2 equals.",
            debug=True,  # Also pass debug to execution
        )

        print("\n✅ Execution successful!")
        print(f"\nResponse type: {type(result)}")

        # Extract AI response from result
        if isinstance(result, str):
            print(f"\nAI Response: {result}")
        elif hasattr(result, "messages"):
            # Get last AI message from state object
            messages = getattr(result, "messages", [])
            print(f"\n🔍 Found {len(messages)} messages")

            # Find the last AI message
            for msg in reversed(messages):
                if msg.__class__.__name__ == "AIMessage" and hasattr(msg, "content"):
                    print(f"\n🎯 AI Response: {msg.content}")
                    break
            else:
                print("\n⚠️  No AIMessage found in messages"ges")
        else:
            print(f"\nUnexpected result type: {type(result)}")

    except Exception as e:
        print(f"\n❌ Execution failed: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    print("\n🔧 Testing SimpleAgent v3 with full debug output...\n")
    test_with_debug()
    print("\n✅ Debug test complete!")
