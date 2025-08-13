#!/usr/bin/env python3
"""Debug validation_router_v2 to see exactly what it receives and why it routes to agent_node."""

from pydantic import BaseModel, Field


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def patch_validation_router_v2():
    """Patch validation_router_v2 to see its exact input and decision logic."""
    
    import haive.core.graph.node.validation_router_v2 as router_module
    
    original_router = router_module.validation_router_v2
    
    def debug_validation_router_v2(state):
        print(f"\n🎯 VALIDATION_ROUTER_V2 CALLED")
        print(f"=" * 50)
        
        # Examine state
        messages = state.get('messages', [])
        tool_routes = state.get('tool_routes', {})
        
        print(f"📋 STATE ANALYSIS:")
        print(f"   - Messages count: {len(messages)}")
        print(f"   - Tool routes: {tool_routes}")
        
        # Show last few messages in detail
        print(f"\n📋 LAST 3 MESSAGES:")
        for i, msg in enumerate(messages[-3:]):
            msg_type = type(msg).__name__
            content = str(msg.content)[:100] if hasattr(msg, 'content') else 'No content'
            additional_kwargs = getattr(msg, 'additional_kwargs', {})
            tool_calls = getattr(msg, 'tool_calls', None)
            tool_call_id = getattr(msg, 'tool_call_id', None)
            
            print(f"   [{i}] {msg_type}:")
            print(f"       content: {content}...")
            print(f"       tool_calls: {tool_calls}")
            print(f"       tool_call_id: {tool_call_id}")
            print(f"       additional_kwargs: {additional_kwargs}")
        
        # Get the last AIMessage with tool calls
        last_ai_message = None
        for msg in reversed(messages):
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                last_ai_message = msg
                break
        
        if last_ai_message:
            print(f"\n📋 LAST AI MESSAGE WITH TOOL CALLS:")
            print(f"   - Tool calls: {last_ai_message.tool_calls}")
            
            # Analyze each tool call
            for i, tool_call in enumerate(last_ai_message.tool_calls):
                tool_name = tool_call.get('name')
                tool_id = tool_call.get('id')
                args = tool_call.get('args', {})
                
                print(f"\n   [Tool Call {i}] {tool_name}:")
                print(f"       - id: {tool_id}")
                print(f"       - args: {args}")
                print(f"       - route: {tool_routes.get(tool_name, 'UNKNOWN')}")
                
                # Find corresponding ToolMessage
                tool_message = None
                for msg in messages:
                    if (hasattr(msg, 'tool_call_id') and 
                        getattr(msg, 'tool_call_id', None) == tool_id):
                        tool_message = msg
                        break
                
                if tool_message:
                    print(f"       - ToolMessage found:")
                    print(f"         content: {tool_message.content}")
                    print(f"         additional_kwargs: {getattr(tool_message, 'additional_kwargs', {})}")
                    
                    # Check if it's an error
                    is_error = False
                    if hasattr(tool_message, 'additional_kwargs'):
                        is_error = tool_message.additional_kwargs.get('is_error', False)
                    
                    print(f"         IS_ERROR: {is_error}")
                    
                    if is_error:
                        print(f"         ❌ ERROR TOOLMESSAGE - Will route to agent_node")
                    else:
                        print(f"         ✅ SUCCESS TOOLMESSAGE - Should route to parse_output")
                else:
                    print(f"       - ❌ NO TOOLMESSAGE FOUND - This is a problem!")
        
        # Call original router
        print(f"\n🎯 CALLING ORIGINAL ROUTER...")
        result = original_router(state)
        
        print(f"\n🎯 ROUTER DECISION: '{result}'")
        
        if result == "agent_node":
            print(f"   ❌ ROUTING TO AGENT_NODE - This causes infinite loop!")
            print(f"   📋 This means the router detected an error condition")
        elif result == "parse_output":
            print(f"   ✅ ROUTING TO PARSE_OUTPUT - This is correct for structured output")
        else:
            print(f"   🤔 ROUTING TO: {result}")
        
        return result
    
    # Apply patch
    router_module.validation_router_v2 = debug_validation_router_v2
    print("✅ Patched validation_router_v2 for debugging")


def patch_validation_node_v2():
    """Patch ValidationNodeV2 to see what ToolMessages it creates."""
    
    import haive.core.graph.node.validation_node_v2 as validation_module
    
    original_create_tool_message = validation_module.ValidationNodeV2._create_tool_message_for_pydantic
    
    def debug_create_tool_message_for_pydantic(self, tool_name, tool_id, args, model_class):
        print(f"\n🔍 VALIDATION_NODE_V2: Creating ToolMessage")
        print(f"   - tool_name: {tool_name}")
        print(f"   - tool_id: {tool_id}")
        print(f"   - args: {args}")
        print(f"   - model_class: {model_class}")
        
        try:
            # Call original method
            result = original_create_tool_message(self, tool_name, tool_id, args, model_class)
            
            print(f"   ✅ ToolMessage created successfully:")
            print(f"      - content: {result.content}")
            print(f"      - additional_kwargs: {result.additional_kwargs}")
            
            # Check if it's marked as error
            is_error = result.additional_kwargs.get('is_error', False)
            validation_passed = result.additional_kwargs.get('validation_passed', True)
            
            print(f"      - is_error: {is_error}")
            print(f"      - validation_passed: {validation_passed}")
            
            if is_error or not validation_passed:
                print(f"      ❌ MARKED AS ERROR - Will cause router to go to agent_node")
            else:
                print(f"      ✅ MARKED AS SUCCESS - Should cause router to go to parse_output")
            
            return result
            
        except Exception as e:
            print(f"   ❌ ERROR creating ToolMessage: {e}")
            print(f"      This will create an error ToolMessage")
            raise
    
    # Apply patch
    validation_module.ValidationNodeV2._create_tool_message_for_pydantic = debug_create_tool_message_for_pydantic
    print("✅ Patched ValidationNodeV2._create_tool_message_for_pydantic for debugging")


def test_validation_debug():
    """Test SimpleAgent with full validation debugging."""
    
    print("🔍 VALIDATION ROUTER DEBUG TEST")
    print("=" * 80)
    
    # Apply patches
    patch_validation_router_v2()
    patch_validation_node_v2()
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.agents.simple.agent import SimpleAgent
        
        # Create agent
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        agent = SimpleAgent(
            name="validation_debug",
            engine=engine,
            debug=True
        )
        
        print(f"\n📋 Agent created:")
        print(f"   - force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
        print(f"   - tool_routes: {engine.tool_routes}")
        
        print(f"\n🎯 Starting execution (will timeout, but we'll see the validation logic)...")
        
        import signal
        def timeout_handler(signum, frame):
            raise TimeoutError("Timeout - stopping to analyze debug output")
        
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(15)  # 15 second timeout
        
        try:
            result = agent.run("What is 2+2?", debug=False)
            signal.alarm(0)
            print(f"\n✅ Execution completed: {result}")
        except TimeoutError:
            print(f"\n⏰ Execution timed out - check debug output above")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Run validation debugging."""
    test_validation_debug()
    
    print(f"\n📋 KEY QUESTIONS ANSWERED:")
    print(f"1. What ToolMessage does ValidationNodeV2 create?")
    print(f"2. Is it marked as error or success?")
    print(f"3. Why does validation_router_v2 route to agent_node?")
    print(f"4. What's the exact condition that causes the infinite loop?")


if __name__ == "__main__":
    main()