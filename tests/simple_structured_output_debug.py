"""Simple isolated test to debug structured output behavior step by step."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent


class SimpleResponse(BaseModel):
    """Very simple response model for testing."""

    answer: str = Field(description="The answer to the question")
    confidence: float = Field(description="Confidence 0-1")


def test_simple_structured_output():
    """Step-by-step debug of SimpleAgent structured output."""

    print("=== STEP 1: Creating SimpleAgent with Structured Output ===")

    # Create the simplest possible agent
    agent = SimpleAgent(
        name="debug_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=SimpleResponse,
        structured_output_version="v2",
        debug=True,
    )

    print("✅ Agent created")
    print(f"   - Name: {agent.name}")
    print(f"   - Structured model: {agent.structured_output_model}")
    print(f"   - Version: {agent.structured_output_version}")

    print("\n=== STEP 2: Before Compilation ===")
    print(f"   - Engine type: {type(agent.engine)}")
    print(f"   - Engine output schema: {getattr(agent.engine, 'output_schema', None)}")
    print(f"   - Agent state schema: {getattr(agent, 'state_schema', None)}")

    print("\n=== STEP 3: Compiling Agent ===")
    agent.compile()

    print("✅ Agent compiled")
    print(
        f"   - Engine output schema after: {getattr(agent.engine, 'output_schema', None)}"
    )
    print(f"   - Agent state schema after: {agent.state_schema}")
    print(f"   - State schema fields: {list(agent.state_schema.model_fields.keys())}")

    # Look for our structured output field
    expected_field_names = ["simpleresponse", "simple_response", "response", "answer"]
    structured_fields = []
    for field_name in agent.state_schema.model_fields.keys():
        if any(expected in field_name.lower() for expected in expected_field_names):
            structured_fields.append(field_name)

    print(f"   - Potential structured output fields found: {structured_fields}")

    print("\n=== STEP 4: Preparing Test Input ===")
    test_input = {
        "messages": [HumanMessage(content="What is 2+2? Answer with confidence.")]
    }
    # Use the agent's default thread_id instead of None (required for PostgreSQL persistence)
    config = agent.get_effective_runnable_config()

    print(f"   - Input: {test_input}")
    print(f"   - Config: {config}")

    print("\n=== STEP 5: Executing Agent ===")
    try:
        result = agent._app.invoke(test_input, config=config)

        print("✅ Execution completed")
        print(f"   - Result type: {type(result)}")
        print(f"   - Result keys: {list(result.keys())}")
        print(f"   - Full result: {result}")

        print("\n=== STEP 6: Analyzing Output ===")

        # Check for messages
        if "messages" in result:
            messages = result["messages"]
            print(f"   - Messages found: {len(messages)} messages")
            for i, msg in enumerate(messages):
                print(f"     Message {i}: {type(msg)} - {str(msg)[:100]}...")

        # Check for structured output fields
        structured_output_found = False
        for key, value in result.items():
            if key != "messages":
                print(f"   - Non-message field '{key}': {type(value)} = {value}")
                if isinstance(value, SimpleResponse):
                    print(
                        f"     ✅ Found SimpleResponse: answer={value.answer}, confidence={value.confidence}"
                    )
                    structured_output_found = True
                elif hasattr(value, "answer") and hasattr(value, "confidence"):
                    print(
                        f"     ✅ Found structured data: answer={getattr(value, 'answer', 'N/A')}"
                    )
                    structured_output_found = True

        if not structured_output_found:
            print("   ❌ No structured output found in result")

        return result

    except Exception as e:
        print(f"❌ Execution failed: {e}")
        if "msgpack" in str(e):
            print("   - This is a serialization issue, execution may have worked")
        raise


def test_engine_directly():
    """Test the engine directly to see if it can produce structured output."""

    print("\n" + "=" * 60)
    print("=== TESTING ENGINE DIRECTLY ===")

    # Create engine with structured output
    engine = AugLLMConfig(
        llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1),
        structured_output_model=SimpleResponse,
        structured_output_version="v2",
    )

    print("✅ Engine created with structured output")
    print(f"   - Type: {type(engine)}")
    print(f"   - Structured model: {getattr(engine, 'structured_output_model', None)}")
    print(f"   - Output schema: {getattr(engine, 'output_schema', None)}")

    # Try to execute engine directly
    try:
        test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
        result = engine.invoke(test_input)

        print("✅ Direct engine execution completed")
        print(f"   - Result type: {type(result)}")
        print(f"   - Result: {result}")

        return result

    except Exception as e:
        print(f"❌ Direct engine execution failed: {e}")
        return None


if __name__ == "__main__":
    print("🔍 DEBUGGING STRUCTURED OUTPUT BEHAVIOR")
    print("=" * 60)

    # Test 1: Full agent
    try:
        agent_result = test_simple_structured_output()
    except Exception as e:
        print(f"Agent test failed: {e}")
        agent_result = None

    # Test 2: Engine directly
    try:
        engine_result = test_engine_directly()
    except Exception as e:
        print(f"Engine test failed: {e}")
        engine_result = None

    print("\n" + "=" * 60)
    print("=== SUMMARY ===")
    print(f"Agent result: {agent_result is not None}")
    print(f"Engine result: {engine_result is not None}")

    if agent_result:
        print(
            f"Agent structured fields: {[k for k in agent_result.keys() if k != 'messages']}"
        )
    if engine_result:
        print(f"Engine result type: {type(engine_result)}")
