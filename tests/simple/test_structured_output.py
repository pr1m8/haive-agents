"""Test SimpleAgent with structured output routing - debug the infinite loop"""

from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured output."""
    response: str = Field(description="Response to the input")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in response")


def test_simple_agent_structured_output():
    """Test SimpleAgent with structured output using agent.run(debug=True)"""
    
    # Create SimpleAgent with structured output
    simple_agent = SimpleAgent(
        name="simple_test",
        engine=AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.1,
            max_tokens=100
        ),
        debug=False  # Turn off extra debug to see just routing
    )
    
    print(f"\n🔍 Testing SimpleAgent with structured output:")
    print(f"   - Name: {simple_agent.name}")
    print(f"   - Has structured_output_model: {bool(simple_agent.engine.structured_output_model)}")
    
    # Use agent.run(debug=True) as requested
    result = simple_agent.run("Say hello", debug=True)
    
    print(f"\n✅ Result: {result}")
    print(f"Result type: {type(result)}")
    
    assert result is not None
