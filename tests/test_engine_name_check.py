"""Check if engine_name is being added to AIMessage by engine node."""

from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig


class TestResponse(BaseModel):
    """Test response model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def check_engine_name_in_messages():
    """Check if engine_name is properly added to AIMessage."""
    # Test with structured output
    agent = SimpleAgent(
        name="engine_name_test",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestResponse,
        structured_output_version="v2",
        debug=True,
    )

    agent.compile()

    # Test execution
    test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
    config = {"configurable": {"thread_id": None}}

    result = agent._app.invoke(test_input, config=config)

    messages = result.get("messages", [])

    for _i, msg in enumerate(messages):

        # Check additional_kwargs
        if hasattr(msg, "additional_kwargs"):

            # Look for engine_name specifically
            if "engine_name" in msg.additional_kwargs:
                pass
            else:
                pass

            # Show all kwargs for analysis
            for key, value in msg.additional_kwargs.items():
                if key != "tool_calls":  # Tool calls are verbose
                    pass

        # Check response_metadata
        if hasattr(msg, "response_metadata") and "engine_name" in msg.response_metadata:
            pass

        # Check for tool_calls
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for _j, _tool_call in enumerate(msg.tool_calls):
                pass

    # Check if engine_name is anywhere in the result
    for key, value in result.items():
        if key == "engine_name" or (isinstance(value, dict) and "engine_name" in value):
            pass


def check_direct_engine_output():
    """Check what the engine directly produces."""
    # Create engine directly
    engine = AugLLMConfig(
        llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1),
        structured_output_model=TestResponse,
        structured_output_version="v2",
    )

    # Test direct engine execution
    from langchain_core.messages import HumanMessage

    input_data = {"messages": [HumanMessage(content="What is 2+2?")]}

    try:
        result = engine.invoke(input_data)

        if hasattr(result, "additional_kwargs"):
            if "engine_name" in result.additional_kwargs:
                pass
            else:
                pass

    except Exception:
        pass


if __name__ == "__main__":
    check_engine_name_in_messages()
    check_direct_engine_output()
