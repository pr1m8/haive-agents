"""Test memory operations with fixed SimpleMemoryAgent.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.memory_reorganized.agents.simple import (
    SimpleMemoryAgent,
    TokenAwareMemoryConfig,
)


def test_memory_operations():
    """Test various memory operations.
    """
    # Create agent with DeepSeek
    agent = SimpleMemoryAgent(
        name="memory_test",
        engine=AugLLMConfig(
            llm_config=DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)
        ),
        memory_config=TokenAwareMemoryConfig(
            max_context_tokens=2000, storage_backend="in_memory"
        ),
    )

    print("✅ SimpleMemoryAgent created with MemoryStateWithTokens!")
    print(f"State schema: {agent.state_schema.__name__}")
    print(f"Use prebuilt base: {agent.use_prebuilt_base}")

    # Test 1: Store memories
    print("\n📝 Testing memory storage...")
    result1 = agent.run("Remember that I'm a software engineer working on AI projects")
    print(f"Store result: {result1}")

    result2 = agent.run("Remember that I prefer Python and have 10 years of experience")
    print(f"Store result 2: {result2}")

    result3 = agent.run("Remember that I'm interested in multi-agent systems and RAG")
    print(f"Store result 3: {result3}")

    # Test 2: Retrieve memories
    print("\n🔍 Testing memory retrieval...")
    result = agent.run("What do you know about my background?")
    print(f"Retrieval result: {result}")

    # Test 3: Search memories
    print("\n🔎 Testing memory search...")
    result = agent.run("Search for information about my programming experience")
    print(f"Search result: {result}")

    # Test 4: Check memory status
    print("\n📊 Checking memory status...")
    status = agent.get_memory_status()
    print(f"Memory status: {status}")

    # Test 5: Check if state is correct
    print("\n✅ State validation:")
    if hasattr(agent, "_app") and agent._app:
        # The graph should be using MemoryStateWithTokens
        state_name = agent._app.get_state.__annotations__.get("return", "Unknown")
        print(f"Graph state type: {state_name}")


if __name__ == "__main__":
    test_memory_operations()
