#!/usr/bin/env python3
"""Simple experiment to test SimpleAgent routing."""

import sys
import os

# Add the packages to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def experiment_basic_simple_agent():
    """Test basic SimpleAgent without structured output."""
    
    print("🧪 EXPERIMENT: Basic SimpleAgent (no structured output)")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        
        engine = AugLLMConfig(
            temperature=0.3,
            # No structured output
        )
        
        print(f"   ✅ Engine created")
        print(f"   - force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
        print(f"   - tools: {len(engine.tools)} tools")
        
        from haive.agents.simple.agent import SimpleAgent
        
        agent = SimpleAgent(
            name="basic_test",
            engine=engine,
            debug=True
        )
        
        print(f"   ✅ Agent created")
        
        # Check graph
        graph = agent.graph
        edges = graph.get_edges()
        print(f"\n   Graph edges:")
        for source, target in edges:
            print(f"     {source} → {target}")
        
        print(f"\n   🎯 Testing execution...")
        result = agent.run("What is 2+2?", debug=False)
        print(f"   ✅ SUCCESS: {result}")
        return True
        
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


def experiment_structured_output():
    """Test SimpleAgent with structured output."""
    
    print("\n🧪 EXPERIMENT: SimpleAgent with structured output")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        print(f"   ✅ Engine created")
        print(f"   - force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
        print(f"   - tools: {len(engine.tools)} tools")
        print(f"   - tool_routes: {engine.tool_routes}")
        
        from haive.agents.simple.agent import SimpleAgent
        
        agent = SimpleAgent(
            name="struct_test",
            engine=engine,
            debug=True
        )
        
        print(f"   ✅ Agent created")
        
        # Check graph
        graph = agent.graph
        edges = graph.get_edges()
        print(f"\n   Graph edges:")
        for source, target in edges:
            print(f"     {source} → {target}")
        
        print(f"\n   🎯 Testing execution (10 sec timeout)...")
        
        import signal
        def timeout_handler(signum, frame):
            raise TimeoutError("Timeout after 10 seconds")
        
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(10)
        
        try:
            result = agent.run("What is 2+2?", debug=False)
            signal.alarm(0)
            print(f"   ✅ SUCCESS: {result}")
            return True
        except TimeoutError:
            print(f"   ⏰ TIMEOUT: Infinite loop confirmed")
            return False
        
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run experiments."""
    
    print("🔬 SIMPLE AGENT EXPERIMENTS")
    print("=" * 80)
    
    # Test 1: Basic agent
    basic_works = experiment_basic_simple_agent()
    
    # Test 2: Structured output
    struct_works = experiment_structured_output()
    
    print("\n" + "=" * 80)
    print("🎯 RESULTS:")
    print(f"   Basic SimpleAgent: {'✅ Works' if basic_works else '❌ Broken'}")
    print(f"   Structured Output: {'✅ Works' if struct_works else '❌ Infinite loop'}")
    
    if basic_works and not struct_works:
        print(f"\n🎯 CONCLUSION: Issue is specific to structured output routing")
    elif not basic_works:
        print(f"\n🚨 CONCLUSION: Basic SimpleAgent is broken - deeper issue")
    else:
        print(f"\n🤔 CONCLUSION: Both work - need more investigation")


if __name__ == "__main__":
    main()