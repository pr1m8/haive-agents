#!/usr/bin/env python3
"""Patch validation to see what's happening during tool processing."""

import sys
from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def patch_validation_node():
    """Patch ValidationNodeV2 to log what ToolMessages it creates."""
    
    import haive.core.graph.node.validation_node_v2 as validation_module
    
    # Save original method
    original_create_tool_message = validation_module.ValidationNodeV2._create_tool_message_for_pydantic
    
    def debug_create_tool_message(self, tool_name, tool_id, args, model_class):
        """Debug wrapper for _create_tool_message_for_pydantic."""
        print(f"\n🔍 VALIDATION: Creating ToolMessage for {tool_name}")
        print(f"   - tool_id: {tool_id}")
        print(f"   - args: {args}")
        print(f"   - model_class: {model_class}")
        
        try:
            # Call original method
            result = original_create_tool_message(self, tool_name, tool_id, args, model_class)
            
            print(f"   ✅ SUCCESS: ToolMessage created")
            print(f"   - content: {result.content[:100]}...")
            print(f"   - additional_kwargs: {result.additional_kwargs}")
            
            return result
            
        except Exception as e:
            print(f"   ❌ ERROR: {e}")
            raise
    
    # Apply patch
    validation_module.ValidationNodeV2._create_tool_message_for_pydantic = debug_create_tool_message
    print("✅ Patched ValidationNodeV2._create_tool_message_for_pydantic")


def patch_validation_router():
    """Patch validation_router_v2 to log routing decisions."""
    
    import haive.core.graph.node.validation_router_v2 as router_module
    
    # Save original function
    original_router = router_module.validation_router_v2
    
    def debug_validation_router(state):
        """Debug wrapper for validation_router_v2."""
        print(f"\n🎯 ROUTER: validation_router_v2 called")
        
        messages = state.get('messages', [])
        tool_routes = state.get('tool_routes', {})
        
        print(f"   - messages count: {len(messages)}")
        print(f"   - tool_routes: {tool_routes}")
        
        # Show last few messages
        for i, msg in enumerate(messages[-3:]):
            print(f"   - msg[{i}]: {type(msg).__name__} - {str(msg)[:50]}...")
        
        # Call original router
        result = original_router(state)
        
        print(f"   🎯 ROUTER DECISION: '{result}'")
        
        if result == "agent_node":
            print("   ⚠️  ROUTING BACK TO AGENT_NODE - THIS CAUSES THE LOOP!")
        elif result == "parse_output":
            print("   ✅ ROUTING TO PARSE_OUTPUT - CORRECT FOR STRUCTURED OUTPUT")
        
        return result
    
    # Apply patch
    router_module.validation_router_v2 = debug_validation_router
    print("✅ Patched validation_router_v2")


def test_with_patches():
    """Test SimpleAgent with patches to see validation process."""
    
    print("🔍 TESTING WITH VALIDATION PATCHES")
    print("=" * 50)
    
    # Apply patches
    patch_validation_node()
    patch_validation_router()
    
    # Create agent
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent = SimpleAgent(
        name="patch_test",
        engine=engine,
        debug=True
    )
    
    print("\n📋 Starting execution (limited to prevent infinite loop)...")
    
    try:
        # This will likely timeout, but we'll see the validation process
        import signal
        
        def timeout_handler(signum, frame):
            raise TimeoutError("Execution timeout - stopping to analyze logs")
        
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(10)  # 10 second timeout
        
        result = agent.run("What is 2+2?", debug=False)
        signal.alarm(0)  # Cancel timeout
        
        print(f"   ✅ Execution completed: {result}")
        
    except TimeoutError:
        print(f"   ⏰ Execution timed out - this confirms infinite loop")
        print(f"   📋 Check the validation logs above to see the issue")
        
    except Exception as e:
        print(f"   ❌ Execution failed: {e}")


def main():
    """Run patched test."""
    test_with_patches()
    
    print("\n📋 ANALYSIS:")
    print("Look at the validation and router logs above to see:")
    print("1. Is ValidationNodeV2 creating successful or error ToolMessages?")
    print("2. Is validation_router_v2 routing to parse_output or agent_node?")
    print("3. If routing to agent_node, why is validation failing?")


if __name__ == "__main__":
    main()