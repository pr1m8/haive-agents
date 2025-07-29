"""Test input preparation with MemoryStateWithTokens.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.memory_reorganized.agents.simple import (
    SimpleMemoryAgent,
    TokenAwareMemoryConfig,
)


def test_input_preparation():
    """Test how input is prepared for MemoryStateWithTokens.
    """
    # Create agent
    agent = SimpleMemoryAgent(
        name="test_prep",
        engine=AugLLMConfig(llm_config=DeepSeekLLMConfig(model="deepseek-chat")),
        memory_config=TokenAwareMemoryConfig(
            max_context_tokens=2000, storage_backend="in_memory"
        ),
    )

    print(f"State schema: {agent.state_schema}")
    print(f"Input schema: {agent.input_schema}")

    # Check schema fields
    if agent.state_schema:
        print("\nState schema fields:")
        for field_name, field_info in agent.state_schema.model_fields.items():
            print(f"  - {field_name}: {field_info.annotation}")
            if field_name in ["messages", "current_memories", "token_usage"]:
                print(f"    Required: {field_info.is_required()}")
                print(f"    Default: {field_info.default}")

    # Test prepare input
    try:
        # Test string input
        prepared = agent._prepare_input("Hello world")
        print(f"\nPrepared from string: {prepared}")
        print(f"Prepared type: {type(prepared)}")

        # Test dict input
        dict_input = {"messages": [HumanMessage(content="Hello")]}
        prepared2 = agent._prepare_input(dict_input)
        print(f"\nPrepared from dict: {prepared2}")

    except Exception as e:
        print(f"\nError preparing input: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_input_preparation()
