"""Simple test to understand Enhanced MultiAgent V3 behavior."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.messages_state import MessagesState
from langchain_core.messages import HumanMessage

from haive.agents.multi.enhanced_multi_agent_v3 import EnhancedMultiAgent
from haive.agents.simple.agent import SimpleAgent


async def test_simple_multiagent():
    """Test basic Enhanced MultiAgent V3 functionality."""

    # Create simple agents
    config = AugLLMConfig(temperature=0.1)

    agent1 = SimpleAgent(name="agent1", engine=config)
    agent2 = SimpleAgent(name="agent2", engine=config)

    # Create multi-agent with unique name to avoid PostgreSQL conflicts
    import uuid

    unique_name = f"test_multi_{str(uuid.uuid4())[:8]}"

    multi_agent = EnhancedMultiAgent(
        name=unique_name,
        agents={"first": agent1, "second": agent2},
        execution_mode="sequential",
        state_schema=MessagesState,
        debug_mode=True,
        entry_point="first",  # Explicitly set entry point
    )

    # Test execution
    print("=== Testing Enhanced MultiAgent V3 ===")

    # Create initial state
    initial_state = MessagesState(messages=[HumanMessage(content="Hello")])

    try:
        # Execute
        result = await multi_agent.arun(initial_state)
        print(f"Result type: {type(result)}")
        print(f"Result: {result}")

        # Check result attributes
        if hasattr(result, "__dict__"):
            print(f"Result attributes: {result.__dict__.keys()}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_simple_multiagent())
