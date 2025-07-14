"""Test SimpleAgent with both v1 and v2 structured output to see differences."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent


class TestResponse(BaseModel):
    """Test response model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def test_v1_structured_output():
    """Test SimpleAgent with v1 structured output."""

    print("🔍 TESTING V1 STRUCTURED OUTPUT")
    print("=" * 50)

    agent = SimpleAgent(
        name="v1_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestResponse,
        structured_output_version="v1",  # V1
        debug=True,
    )

    print(f"✅ V1 Agent created")
    print(f"   - Structured model: {agent.structured_output_model}")
    print(f"   - Version: {agent.structured_output_version}")
    print(f"   - Force tool use: {agent._has_force_tool_use()}")

    # Compile and check graph
    agent.compile()

    print(f"   - Graph nodes: {list(agent.graph.nodes.keys())}")
    print(f"   - Graph edges: {list(agent.graph.edges)}")

    # Test execution
    test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
    config = {"configurable": {"thread_id": None}}

    print(f"\n--- V1 EXECUTION ---")
    try:
        result = agent._app.invoke(test_input, config=config)
        print(f"V1 Result keys: {list(result.keys())}")
        print(f"V1 Result: {result}")

        # Look for structured output
        structured_fields = [k for k in result.keys() if k != "messages"]
        if structured_fields:
            print(f"✅ V1 found structured fields: {structured_fields}")
            for field in structured_fields:
                print(f"   {field}: {result[field]}")
        else:
            print(f"❌ V1 no structured fields found")

    except Exception as e:
        print(f"V1 execution error: {e}")

    return result


def test_v2_structured_output():
    """Test SimpleAgent with v2 structured output."""

    print("\n🔍 TESTING V2 STRUCTURED OUTPUT")
    print("=" * 50)

    agent = SimpleAgent(
        name="v2_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestResponse,
        structured_output_version="v2",  # V2
        debug=True,
    )

    print(f"✅ V2 Agent created")
    print(f"   - Structured model: {agent.structured_output_model}")
    print(f"   - Version: {agent.structured_output_version}")
    print(f"   - Force tool use: {agent._has_force_tool_use()}")

    # Compile and check graph
    agent.compile()

    print(f"   - Graph nodes: {list(agent.graph.nodes.keys())}")
    print(f"   - Graph edges: {list(agent.graph.edges)}")

    # Test execution
    test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
    config = {"configurable": {"thread_id": None}}

    print(f"\n--- V2 EXECUTION ---")
    try:
        result = agent._app.invoke(test_input, config=config)
        print(f"V2 Result keys: {list(result.keys())}")
        print(f"V2 Result: {result}")

        # Look for structured output
        structured_fields = [k for k in result.keys() if k != "messages"]
        if structured_fields:
            print(f"✅ V2 found structured fields: {structured_fields}")
            for field in structured_fields:
                print(f"   {field}: {result[field]}")
        else:
            print(f"❌ V2 no structured fields found")

    except Exception as e:
        print(f"V2 execution error: {e}")

    return result


def compare_engines():
    """Compare engine setup between v1 and v2."""

    print("\n🔍 COMPARING ENGINE SETUP")
    print("=" * 50)

    # V1 Engine
    v1_engine = AugLLMConfig(
        llm_config=AzureLLMConfig(model="gpt-4o"),
        structured_output_model=TestResponse,
        structured_output_version="v1",
    )

    # V2 Engine
    v2_engine = AugLLMConfig(
        llm_config=AzureLLMConfig(model="gpt-4o"),
        structured_output_model=TestResponse,
        structured_output_version="v2",
    )

    print(f"V1 Engine:")
    print(f"   - force_tool_use: {getattr(v1_engine, 'force_tool_use', None)}")
    print(f"   - force_tool_choice: {getattr(v1_engine, 'force_tool_choice', None)}")
    print(f"   - tools: {getattr(v1_engine, 'tools', None)}")
    print(f"   - tool_choice_mode: {getattr(v1_engine, 'tool_choice_mode', None)}")

    print(f"\nV2 Engine:")
    print(f"   - force_tool_use: {getattr(v2_engine, 'force_tool_use', None)}")
    print(f"   - force_tool_choice: {getattr(v2_engine, 'force_tool_choice', None)}")
    print(f"   - tools: {getattr(v2_engine, 'tools', None)}")
    print(f"   - tool_choice_mode: {getattr(v2_engine, 'tool_choice_mode', None)}")


if __name__ == "__main__":
    print("🚀 COMPARING V1 vs V2 STRUCTURED OUTPUT")
    print("=" * 60)

    # Compare engine setup first
    compare_engines()

    # Test V1
    v1_result = test_v1_structured_output()

    # Test V2
    v2_result = test_v2_structured_output()

    print("\n" + "=" * 60)
    print("📊 COMPARISON SUMMARY")
    print("=" * 60)
    print(f"V1 successful: {v1_result is not None}")
    print(f"V2 successful: {v2_result is not None}")

    if v1_result:
        v1_structured = [k for k in v1_result.keys() if k != "messages"]
        print(f"V1 structured fields: {v1_structured}")

    if v2_result:
        v2_structured = [k for k in v2_result.keys() if k != "messages"]
        print(f"V2 structured fields: {v2_structured}")
