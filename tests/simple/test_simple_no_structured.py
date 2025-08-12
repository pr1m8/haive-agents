"""Test SimpleAgent WITHOUT structured output to see if it terminates properly"""

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


def test_simple_agent_no_structured_output():
    """Test SimpleAgent WITHOUT structured output using agent.run(debug=True)"""
    
    # Create SimpleAgent WITHOUT structured output
    simple_agent = SimpleAgent(
        name="simple_no_struct",
        engine=AugLLMConfig(
            temperature=0.1,
            max_tokens=100
        ),
        debug=False  # Turn off extra debug to see just routing
    )
    
    print(f"\n🔍 Testing SimpleAgent WITHOUT structured output:")
    print(f"   - Name: {simple_agent.name}")
    print(f"   - Has structured_output_model: {bool(simple_agent.engine.structured_output_model)}")
    
    # Use agent.run(debug=True) as requested
    result = simple_agent.run("Say hello", debug=True)
    
    print(f"\n✅ Result: {result}")
    print(f"Result type: {type(result)}")
    
    assert result is not None


if __name__ == "__main__":
    test_simple_agent_no_structured_output()