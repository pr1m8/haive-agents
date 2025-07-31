"""Simple isolated test to debug structured output behavior step by step."""

from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig


class SimpleResponse(BaseModel):
    """Very simple response model for testing."""

    answer: str = Field(description="The answer to the question")
    confidence: float = Field(description="Confidence 0-1")


def test_simple_structured_output():
    """Step-by-step debug of SimpleAgent structured output."""
    # Create the simplest possible agent
    agent = SimpleAgent(
        name="debug_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=SimpleResponse,
        structured_output_version="v2",
        debug=True,
    )

    agent.compile()

    # Look for our structured output field
    expected_field_names = ["simpleresponse", "simple_response", "response", "answer"]
    structured_fields = []
    for field_name in agent.state_schema.model_fields:
        if any(expected in field_name.lower() for expected in expected_field_names):
            structured_fields.append(field_name)

    test_input = {
        "messages": [HumanMessage(content="What is 2+2? Answer with confidence.")]
    }
    # Use the agent's default thread_id instead of None (required for PostgreSQL persistence)
    config = agent.get_effective_runnable_config()

    try:
        result = agent._app.invoke(test_input, config=config)

        # Check for messages
        if "messages" in result:
            messages = result["messages"]
            for _i, _msg in enumerate(messages):
                pass

        # Check for structured output fields
        structured_output_found = False
        for key, value in result.items():
            if key != "messages":
                if isinstance(value, SimpleResponse) or (
                    hasattr(value, "answer") and hasattr(value, "confidence")
                ):
                    structured_output_found = True

        if not structured_output_found:
            pass

        return result

    except Exception as e:
        if "msgpack" in str(e):
            pass
        raise


def test_engine_directly():
    """Test the engine directly to see if it can produce structured output."""
    # Create engine with structured output
    engine = AugLLMConfig(
        llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1),
        structured_output_model=SimpleResponse,
        structured_output_version="v2",
    )

    # Try to execute engine directly
    try:
        test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
        result = engine.invoke(test_input)

        return result

    except Exception:
        return None


if __name__ == "__main__":

    # Test 1: Full agent
    try:
        agent_result = test_simple_structured_output()
    except Exception:
        agent_result = None

    # Test 2: Engine directly
    try:
        engine_result = test_engine_directly()
    except Exception:
        engine_result = None

    if agent_result:
        pass
    if engine_result:
        pass
