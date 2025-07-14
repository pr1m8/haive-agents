"""Check if engine_name is being added to AIMessage by engine node."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent


class TestResponse(BaseModel):
    """Test response model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def check_engine_name_in_messages():
    """Check if engine_name is properly added to AIMessage."""
    print("🔍 CHECKING ENGINE NAME IN AIMESSAGE")
    print("=" * 60)

    # Test with structured output
    agent = SimpleAgent(
        name="engine_name_test",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestResponse,
        structured_output_version="v2",
        debug=True,
    )

    print(f"Engine name: {agent.engine.name}")

    agent.compile()

    # Test execution
    test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
    config = {"configurable": {"thread_id": None}}

    result = agent._app.invoke(test_input, config=config)

    print("\n=== MESSAGE ANALYSIS ===")
    messages = result.get("messages", [])
    print(f"Found {len(messages)} messages")

    for i, msg in enumerate(messages):
        print(f"\nMessage {i}: {type(msg).__name__}")
        print(f"  Content: {msg.content[:100]}...")

        # Check additional_kwargs
        if hasattr(msg, "additional_kwargs"):
            print(f"  Additional kwargs keys: {list(msg.additional_kwargs.keys())}")

            # Look for engine_name specifically
            if "engine_name" in msg.additional_kwargs:
                print(f"  ✅ Engine name found: {msg.additional_kwargs['engine_name']}")
            else:
                print("  ❌ No engine_name in additional_kwargs"s")

            # Show all kwargs for analysis
            for key, value in msg.additional_kwargs.items():
                if key != "tool_calls":  # Tool calls are verbose
                    print(f"    {key}: {value}")

        # Check response_metadata
        if hasattr(msg, "response_metadata"):
            print(f"  Response metadata keys: {list(msg.response_metadata.keys())}")
            if "engine_name" in msg.response_metadata:
                print(
                    f"  ✅ Engine name in metadata: {msg.response_metadata['engine_name']}"
                )

        # Check for tool_calls
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            print(f"  Tool calls: {len(msg.tool_calls)}")
            for j, tool_call in enumerate(msg.tool_calls):
                print(f"    Tool {j}: {tool_call['name']} -> {tool_call['args']}")

    print("\n=== STATE ANALYSIS ===")
    print(f"Result keys: {list(result.keys())}")

    # Check if engine_name is anywhere in the result
    for key, value in result.items():
        if key == "engine_name":
            print(f"  ✅ Engine name in result: {value}")
        elif isinstance(value, dict) and "engine_name" in value:
            print(f"  ✅ Engine name in {key}: {value['engine_name']}")


def check_direct_engine_output():
    """Check what the engine directly produces."""
    print("\n🔍 CHECKING DIRECT ENGINE OUTPUT")
    print("=" * 60)

    # Create engine directly
    engine = AugLLMConfig(
        llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1),
        structured_output_model=TestResponse,
        structured_output_version="v2",
    )

    print(f"Engine name: {engine.name}")
    print(f"Engine force_tool_choice: {getattr(engine, 'force_tool_choice', None)}")

    # Test direct engine execution
    from langchain_core.messages import HumanMessage

    input_data = {"messages": [HumanMessage(content="What is 2+2?")]}

    try:
        result = engine.invoke(input_data)
        print(f"Direct engine result type: {type(result)}")
        print(f"Direct engine result: {result}")

        if hasattr(result, "additional_kwargs"):
            print(f"Additional kwargs: {list(result.additional_kwargs.keys())}")
            if "engine_name" in result.additional_kwargs:
                print(
                    f"✅ Engine name in direct result: {result.additional_kwargs['engine_name']}"
                )
            else:
                print("❌ No engine_name in direct result"t")

    except Exception as e:
        print(f"Direct engine error: {e}")


if __name__ == "__main__":
    check_engine_name_in_messages()
    check_direct_engine_output()
