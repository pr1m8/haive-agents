#!/usr/bin/env python3
"""Investigate the tool sync mechanism and naming mismatch."""

import sys
import os

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_tool_name_sanitization():
    """Test the tool name sanitization process."""
    
    print("🔍 TOOL NAME SANITIZATION TEST")
    print("=" * 60)
    
    try:
        from haive.core.utils.naming import sanitize_tool_name
        
        raw_name = "SimpleResult"
        sanitized_name = sanitize_tool_name(raw_name)
        
        print(f"📋 Name conversion:")
        print(f"   Raw name: '{raw_name}'")
        print(f"   Sanitized name: '{sanitized_name}'")
        
        # Test with generics too
        generic_examples = ["Plan[Task]", "Model[String]", "Result[int]"]
        for generic_name in generic_examples:
            sanitized = sanitize_tool_name(generic_name)
            print(f"   {generic_name} → {sanitized}")
        
        return sanitized_name
        
    except Exception as e:
        print(f"❌ Error testing sanitization: {e}")
        return None


def test_tool_route_mixin_analysis():
    """Test how ToolRouteMixin analyzes tools and sets routes."""
    
    print(f"\n🔍 TOOL ROUTE MIXIN ANALYSIS")
    print("=" * 60)
    
    try:
        from haive.core.common.mixins.tool_route_mixin import ToolRouteMixin
        from haive.core.utils.naming import sanitize_tool_name
        
        # Create a test class that uses ToolRouteMixin
        class TestMixin(ToolRouteMixin):
            def __init__(self):
                super().__init__()
                self.tool_routes = {}
                self.tool_metadata = {}
        
        mixin = TestMixin()
        
        # Test tool analysis
        route, metadata = mixin._analyze_tool(SimpleResult)
        print(f"📋 Tool analysis for SimpleResult:")
        print(f"   Route: {route}")
        print(f"   Metadata: {metadata}")
        
        # Test tool name generation
        tool_name = mixin._generate_tool_name(SimpleResult, "", 0)
        print(f"   Generated name: '{tool_name}'")
        
        # Test what sanitized name would be
        if 'class_name' in metadata:
            raw_class_name = metadata['class_name']
            sanitized_name = sanitize_tool_name(raw_class_name)
            print(f"   Raw class name: '{raw_class_name}'")
            print(f"   Sanitized would be: '{sanitized_name}'")
        
        return tool_name, route, metadata
        
    except Exception as e:
        print(f"❌ Error testing ToolRouteMixin: {e}")
        import traceback
        traceback.print_exc()
        return None, None, None


def test_structured_output_mixin_sync():
    """Test how StructuredOutputMixin sets up tool routes."""
    
    print(f"\n🔍 STRUCTURED OUTPUT MIXIN SYNC")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        
        # Create engine - this triggers StructuredOutputMixin logic
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        print(f"📋 Engine after setup:")
        print(f"   Tools: {[str(tool) for tool in engine.tools]}")
        print(f"   Tool routes: {engine.tool_routes}")
        print(f"   Tool metadata: {engine.tool_metadata}")
        
        # Check if the route was set with sanitized name or raw name
        route_keys = list(engine.tool_routes.keys())
        print(f"   Route keys: {route_keys}")
        
        if route_keys:
            route_key = route_keys[0]
            print(f"   First route key: '{route_key}'")
            
            from haive.core.utils.naming import sanitize_tool_name
            expected_sanitized = sanitize_tool_name("SimpleResult")
            print(f"   Expected sanitized: '{expected_sanitized}'")
            print(f"   Names match: {route_key == expected_sanitized}")
        
        return engine
        
    except Exception as e:
        print(f"❌ Error testing StructuredOutputMixin: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_engine_tool_name_actual():
    """Test what tool name the engine actually produces."""
    
    print(f"\n🔍 ENGINE ACTUAL TOOL NAME")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        # Get actual output
        result = engine.invoke({"messages": [{"role": "user", "content": "What is 2+2?"}]})
        
        if result.tool_calls:
            actual_tool_name = result.tool_calls[0].get('name')
            print(f"📋 Actual engine output:")
            print(f"   Tool call name: '{actual_tool_name}'")
            
            # Compare with what's in tool_routes
            route_keys = list(engine.tool_routes.keys())
            print(f"   Tool route keys: {route_keys}")
            
            # Check if any route key matches
            route_found = actual_tool_name in engine.tool_routes
            print(f"   Route found for actual name: {route_found}")
            
            if not route_found:
                print(f"   ❌ MISMATCH: Tool produces '{actual_tool_name}' but routes have {route_keys}")
                
                # Check if any case-insensitive match
                for key in route_keys:
                    if key.lower() == actual_tool_name.lower():
                        print(f"   🔍 Case mismatch: '{key}' vs '{actual_tool_name}'")
            
            return actual_tool_name, route_keys
        
    except Exception as e:
        print(f"❌ Error testing engine output: {e}")
        return None, None


def main():
    """Run tool sync investigation."""
    
    print("🔬 TOOL SYNC INVESTIGATION")
    print("=" * 80)
    
    # Test 1: Name sanitization
    sanitized_name = test_tool_name_sanitization()
    
    # Test 2: ToolRouteMixin analysis  
    tool_name, route, metadata = test_tool_route_mixin_analysis()
    
    # Test 3: StructuredOutputMixin sync
    engine = test_structured_output_mixin_sync()
    
    # Test 4: Actual engine output
    actual_name, route_keys = test_engine_tool_name_actual()
    
    print(f"\n" + "=" * 80)
    print("🎯 SYNC ANALYSIS SUMMARY:")
    print(f"   Sanitized name: '{sanitized_name}'")
    print(f"   ToolRouteMixin generated: '{tool_name}'")
    print(f"   Route keys in engine: {route_keys}")
    print(f"   Actual tool call name: '{actual_name}'")
    
    if actual_name and route_keys:
        if actual_name in route_keys:
            print(f"\n✅ SYNC IS WORKING: Names match correctly")
        else:
            print(f"\n❌ SYNC IS BROKEN: Name mismatch between routes and actual calls")
            print(f"   The StructuredOutputMixin needs to use sanitized names for route keys")
            print(f"   Route should be set with key '{actual_name}' not '{route_keys[0] if route_keys else 'None'}'")


if __name__ == "__main__":
    main()