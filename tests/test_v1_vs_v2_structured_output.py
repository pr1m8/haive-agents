"""Test SimpleAgent with both v1 and v2 structured output to see differences."""

from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig


class TestResponse(BaseModel):
    """Test response model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def test_v1_structured_output():
    """Test SimpleAgent with v1 structured output."""
    agent = SimpleAgent(
        name="v1_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestResponse,
        structured_output_version="v1",  # V1
        debug=True,
    )

    # Compile and check graph
    agent.compile()

    # Test execution
    test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
    config = {"configurable": {"thread_id": None}}

    try:
        result = agent._app.invoke(test_input, config=config)

        # Look for structured output
        structured_fields = [k for k in result if k != "messages"]
        if structured_fields:
            for _field in structured_fields:
                pass
        else:
            pass

    except Exception:
        pass

    return result


def test_v2_structured_output():
    """Test SimpleAgent with v2 structured output."""
    agent = SimpleAgent(
        name="v2_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestResponse,
        structured_output_version="v2",  # V2
        debug=True,
    )

    # Compile and check graph
    agent.compile()

    # Test execution
    test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
    config = {"configurable": {"thread_id": None}}

    try:
        result = agent._app.invoke(test_input, config=config)

        # Look for structured output
        structured_fields = [k for k in result if k != "messages"]
        if structured_fields:
            for _field in structured_fields:
                pass
        else:
            pass

    except Exception:
        pass

    return result


def compare_engines():
    """Compare engine setup between v1 and v2."""
    # V1 Engine
    AugLLMConfig(
        llm_config=AzureLLMConfig(model="gpt-4o"),
        structured_output_model=TestResponse,
        structured_output_version="v1",
    )

    # V2 Engine
    AugLLMConfig(
        llm_config=AzureLLMConfig(model="gpt-4o"),
        structured_output_model=TestResponse,
        structured_output_version="v2",
    )


if __name__ == "__main__":

    # Compare engine setup first
    compare_engines()

    # Test V1
    v1_result = test_v1_structured_output()

    # Test V2
    v2_result = test_v2_structured_output()

    if v1_result:
        v1_structured = [k for k in v1_result if k != "messages"]

    if v2_result:
        v2_structured = [k for k in v2_result if k != "messages"]
