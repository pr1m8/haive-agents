#!/usr/bin/env python3
"""Test EnhancedMultiAgentV4 with V3 agents."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.agents.simple.agent_v3 import SimpleAgentV3


async def main():
    print("Testing EnhancedMultiAgentV4 with V3 agents...")

    # Create SimpleAgentV3
    simple = SimpleAgentV3(
        name="simple",
        engine=AugLLMConfig(
            temperature=0.3, system_message="You are a helpful assistant."
        ),
    )
    print(f"✅ Created SimpleAgentV3: {simple.name}")

    # Create ReactAgentV3
    @tool
    def test_tool(input: str) -> str:
        """Test tool."""
        return f"Processed: {input}"

    react = ReactAgentV3(
        name="react",
        engine=AugLLMConfig(
            system_message="You are a helpful assistant with tools.", tools=[test_tool]
        ),
    )
    print(f"✅ Created ReactAgentV3: {react.name}")

    # Try to create EnhancedMultiAgentV4
    try:
        workflow = EnhancedMultiAgentV4(
            name="test_workflow", agents=[simple, react], execution_mode="sequential"
        )
        print(f"✅ Created EnhancedMultiAgentV4: {workflow.name}")
        print(f"   Agents: {workflow.get_agent_names()}")

        # Try to execute with proper state format
        from langchain_core.messages import HumanMessage

        test_state = {
            "messages": [HumanMessage(content="Hello, test the workflow")],
            "agent_states": {},
            "execution_order": [],
            "current_agent": None,
        }

        result = await workflow.arun(test_state)
        print(f"✅ Workflow executed successfully!")
        print(f"   Result type: {type(result)}")
        print(
            f"   Messages count: {len(result.messages) if hasattr(result, 'messages') else 'N/A'}"
        )
        if hasattr(result, "messages") and result.messages:
            print(f"   Last message: {result.messages[-1].content[:100]}...")

    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"   Error type: {type(e).__name__}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
