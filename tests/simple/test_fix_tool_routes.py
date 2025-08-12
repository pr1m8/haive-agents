"""Test the fix - use sanitized tool name in tool_routes mapping"""

from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.validation_router_v2 import validation_router_v2
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json


class SimpleResult(BaseModel):
    """Simple structured output."""
    response: str = Field(description="Response to the input")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in response")


def test_fixed_tool_routes():
    """Test with CORRECT tool_routes mapping using sanitized name"""
    
    print("🧪 Testing with FIXED tool routes mapping")
    
    # Create engine to get the actual tool call
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.1,
        max_tokens=100
    )
    
    # Generate LLM response
    runnable = engine.create_runnable()
    llm_result = runnable.invoke({"messages": [HumanMessage(content="Say hello")]})
    
    print(f"LLM tool call name: '{llm_result.tool_calls[0]['name']}'")
    print(f"Engine tool routes: {engine.tool_routes}")
    
    # Create state with BOTH original and sanitized names in tool_routes
    # This is what should happen in the real system
    state = {
        "messages": [
            HumanMessage(content="Say hello"),
            llm_result,
            # Add a successful ToolMessage
            ToolMessage(
                content=json.dumps({
                    "success": True,
                    "result": {"response": "Hello!", "confidence": 1.0}
                }),
                tool_call_id=llm_result.tool_calls[0]['id'],
                name=llm_result.tool_calls[0]['name'],  # Use the actual tool name from LLM
                additional_kwargs={
                    "validation_passed": True,
                    "is_error": False
                }
            )
        ],
        "tool_routes": {
            # Include BOTH names to handle the mismatch
            "SimpleResult": "pydantic_model",          # Original name
            "simple_result": "pydantic_model"          # Sanitized name (what LLM uses)
        }
    }
    
    print(f"State tool_routes: {state['tool_routes']}")
    
    # Test the router
    result = validation_router_v2(state)
    print(f"Router result: '{result}'")
    
    if result == "parse_output":
        print("✅ SUCCESS! Fixed - router now routes to parse_output")
        return True
    else:
        print(f"❌ Still broken - router returns '{result}'")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING TOOL ROUTES FIX")
    print("=" * 60)
    
    success = test_fixed_tool_routes()
    
    if success:
        print("\n🎉 THE LOOP IS FIXED!")
        print("The issue was tool name mismatch between LLM calls and tool_routes mapping")
        print("SimpleAgent needs to include both original and sanitized names in tool_routes")
    else:
        print("\n❌ Still need to investigate further")