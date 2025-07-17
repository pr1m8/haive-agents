"""Test the agents field fix."""

import asyncio
import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent


async def test_fix():
    """Test that the agents field fix works."""

    print("🔧 Testing agents field fix...")

    # Create simple agents
    agent1 = SimpleAgent(name="test1", engine=AugLLMConfig(system_message="Agent 1"))
    agent2 = SimpleAgent(name="test2", engine=AugLLMConfig(system_message="Agent 2"))

    # Create multi-agent
    multi = ProperMultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )

    print(f"✅ Created multi-agent with agents: {list(multi.agents.keys())}")

    # Test input WITHOUT agents field
    test_input = {"messages": [HumanMessage(content="Hello")]}
    print(f"📝 Test input: {list(test_input.keys())}")

    # Try execution
    try:
        result = await multi.ainvoke(test_input)
        print(f"✅ Execution succeeded!")
        print(f"Result type: {type(result)}")
        return True

    except Exception as e:
        print(f"❌ Execution failed: {e}")
        if "not found in agents" in str(e):
            print("   🔍 This is still the 'agents field empty' error")
        return False


if __name__ == "__main__":
    success = asyncio.run(test_fix())
    if success:
        print("\n🎉 Fix is working!")
    else:
        print("\n💔 Fix didn't work - need to debug more")
