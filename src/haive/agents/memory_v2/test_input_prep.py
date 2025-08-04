"""Test input preparation with MemoryStateWithTokens."""

import traceback

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.memory_v2.simple_memory_agent import (
    SimpleMemoryAgent,
    TokenAwareMemoryConfig)


def test_input_preparation():
    """Test how input is prepared for MemoryStateWithTokens."""
    # Create agent
    agent = SimpleMemoryAgent(
        name="test_prep",
        engine=AugLLMConfig(llm_config=DeepSeekLLMConfig(model="deepseek-chat")),
        memory_config=TokenAwareMemoryConfig(
            max_context_tokens=2000, storage_backend="in_memory"
        ))

    # Check schema fields
    if agent.state_schema:
        for field_name, _field_info in agent.state_schema.model_fields.items():
            if field_name in ["messages", "current_memories", "token_usage"]:
                pass

    # Test prepare input
    try:
        # Test string input
        agent._prepare_input("Hello world")

        # Test dict input
        dict_input = {"messages": [HumanMessage(content="Hello")]}
        agent._prepare_input(dict_input)

    except Exception:

        traceback.print_exc()


if __name__ == "__main__":
    test_input_preparation()
