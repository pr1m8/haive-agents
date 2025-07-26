#!/usr/bin/env python3
"""Simple demo showing SimpleAgent v3 with debug mode - no mocks, real LLM execution."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.simple.agent_v3 import SimpleAgentV3


def demo_debug_execution():
    """Demo SimpleAgent v3 with debug=True - real LLM execution."""
    print("\n" + "=" * 80)
    print("🚀 SIMPLE AGENT V3 DEBUG DEMO - Real LLM Execution")
    print("=" * 80)

    # Create real config
    config = AugLLMConfig(
        temperature=0.7, max_tokens=100, llm_config=DeepSeekLLMConfig()
    )

    # Create agent with debug enabled
    agent = SimpleAgentV3(name="demo_agent", engine=config, debug=True, verbose=True)

    print(f"\n✅ Created agent: {agent.name}")
    print(f"   - Engine: {type(agent.engine).__name__}")
    print(f"   - Debug: {agent.debug}")
    print(f"   - State Schema: {agent.state_schema.__name__}")

    # Test message
    message = "Hello! Can you tell me a fun fact about Python programming?"

    print(f"\n📨 Sending message: '{message}'")
    print("\n" + "-" * 60)
    print("🔍 DEBUG OUTPUT:")
    print("-" * 60)

    # Execute with debug - this will show all the internal execution
    result = agent.run(message, debug=True)

    print("-" * 60)
    print("🎯 EXECUTION COMPLETE")
    print("-" * 60)

    # Extract and show the response
    if hasattr(result, "messages"):
        messages = result.messages
        print(f"\n📋 Final state has {len(messages)} messages:")

        for i, msg in enumerate(messages):
            msg_type = msg.__class__.__name__
            print(f"  {i+1}. {msg_type}: {msg.content[:80]}...")

        # Get the AI response
        for msg in reversed(messages):
            if msg.__class__.__name__ == "AIMessage":
                print("\n🤖 AI Response:"e:")
                print(f"   {msg.content}")
                break
    else:
        print(f"\n❓ Unexpected result type: {type(result)}")

    print("\n" + "=" * 80)
    print("✅ Demo complete - Real LLM execution with debug output!")
    print("=" * 80)


if __name__ == "__main__":
    demo_debug_execution()
