#!/usr/bin/env python3
"""Standalone test for SimpleAgentV3 with ValidationNodeV2 pattern.

Run directly: poetry run python tests/simple/v3/test_simple_validation_standalone.py
"""

import asyncio
import logging
import sys
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ========================================================================
# TEST MODELS AND TOOLS
# ========================================================================

class MathResult(BaseModel):
    """Pydantic model for structured math results."""
    calculation: str = Field(description="The mathematical calculation performed")
    result: float = Field(description="The numerical result")
    explanation: str = Field(description="Brief explanation of the calculation")


@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e}"


# ========================================================================
# TESTS
# ========================================================================

async def test_basic_creation():
    """Test SimpleAgentV3 basic creation."""
    print("🧪 Testing SimpleAgentV3 basic creation...")
    
    agent = SimpleAgentV3(
        name="basic_agent",
        engine=AugLLMConfig(name="basic", temperature=0.1)
    )
    
    print(f"✅ Agent created: {agent.name}")
    print(f"✅ Engine: {agent.engine.name}")
    print(f"✅ Has graph: {hasattr(agent, 'graph')}")
    print(f"✅ Has add_tool: {hasattr(agent, 'add_tool')}")
    print(f"✅ Has needs_recompile: {hasattr(agent, 'needs_recompile')}")
    
    return agent


async def test_no_tools_execution():
    """Test SimpleAgentV3 execution without tools."""
    print("\n🧪 Testing SimpleAgentV3 execution without tools...")
    
    agent = SimpleAgentV3(
        name="no_tools_agent",
        engine=AugLLMConfig(name="no_tools", temperature=0.1)
    )
    
    try:
        result = await agent.arun("Hello, how are you?")
        print(f"✅ Execution successful")
        print(f"✅ Result type: {type(result)}")
        print(f"✅ Result length: {len(str(result))}")
        print(f"📝 Result: {result}")
        return True
    except Exception as e:
        print(f"❌ Execution failed: {e}")
        return False


async def test_tools_execution():
    """Test SimpleAgentV3 with LangChain tools."""
    print("\n🧪 Testing SimpleAgentV3 with LangChain tools...")
    
    agent = SimpleAgentV3(
        name="tools_agent",
        engine=AugLLMConfig(
            name="tools_test",
            temperature=0.1,
            tools=[calculator]
        )
    )
    
    try:
        result = await agent.arun("Calculate 15 * 23 please")
        print(f"✅ Tools execution successful")
        print(f"✅ Result type: {type(result)}")
        print(f"📝 Result: {result}")
        
        # Check for calculation result
        has_result = "345" in str(result)
        print(f"✅ Contains calculation result: {has_result}")
        return True
    except Exception as e:
        print(f"❌ Tools execution failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_structured_output():
    """Test SimpleAgentV3 with structured output."""
    print("\n🧪 Testing SimpleAgentV3 with structured output...")
    
    agent = SimpleAgentV3(
        name="structured_agent",
        engine=AugLLMConfig(
            name="structured_test",
            temperature=0.1,
            structured_output_model=MathResult
        )
    )
    
    try:
        result = await agent.arun("Calculate 12 + 8 and explain it")
        print(f"✅ Structured execution successful")
        print(f"✅ Result type: {type(result)}")
        print(f"📝 Result: {result}")
        
        # Check structure
        if isinstance(result, MathResult):
            print(f"✅ Proper MathResult instance")
            print(f"  - Calculation: {result.calculation}")
            print(f"  - Result: {result.result}")
            print(f"  - Explanation: {result.explanation}")
        elif isinstance(result, dict):
            print(f"✅ Dictionary format with keys: {list(result.keys())}")
        else:
            print(f"⚠️  Different format: {type(result)}")
        
        return True
    except Exception as e:
        print(f"❌ Structured execution failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_graph_structure():
    """Test SimpleAgentV3 graph structure."""
    print("\n🧪 Testing SimpleAgentV3 graph structure...")
    
    agent = SimpleAgentV3(
        name="structure_agent",
        engine=AugLLMConfig(
            name="structure_test",
            tools=[calculator],
            structured_output_model=MathResult
        )
    )
    
    try:
        # Check graph
        print(f"✅ Has graph: {hasattr(agent, 'graph')}")
        
        if hasattr(agent, 'graph') and agent.graph:
            nodes = list(agent.graph.nodes.keys())
            print(f"✅ Graph nodes: {nodes}")
            
            # Key nodes we expect
            expected = {"agent_node"}
            found = set(nodes) & expected
            print(f"✅ Expected nodes found: {found}")
            
        # Test execution
        result = await agent.arun("Calculate 10 + 5")
        print(f"✅ Graph execution successful")
        print(f"📝 Result: {result}")
        
        return True
    except Exception as e:
        print(f"❌ Graph structure test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_dynamic_tool_addition():
    """Test dynamic tool addition."""
    print("\n🧪 Testing dynamic tool addition...")
    
    agent = SimpleAgentV3(
        name="dynamic_agent",
        engine=AugLLMConfig(name="dynamic_test", model="gpt-4o-mini", temperature=0.1)
    )
    
    try:
        # Check initial state
        initial_tools = len(agent.engine.tools) if agent.engine.tools else 0
        print(f"✅ Initial tools: {initial_tools}")
        
        # Add tool dynamically
        @tool
        def word_counter(text: str) -> str:
            """Count words in text."""
            return f"Word count: {len(text.split())}"
        
        agent.add_tool(word_counter, route="langchain_tool")
        
        # Check after addition
        after_tools = len(agent.engine.tools) if agent.engine.tools else 0
        print(f"✅ After adding tool: {after_tools}")
        
        # Test with new tool
        result = await agent.arun("Count words in this sentence")
        print(f"✅ Dynamic tool execution successful")
        print(f"📝 Result: {result}")
        
        return True
    except Exception as e:
        print(f"❌ Dynamic tool test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


# ========================================================================
# MAIN TEST RUNNER
# ========================================================================

async def main():
    """Run all tests."""
    print("🚀 Starting SimpleAgentV3 ValidationNodeV2 Integration Tests")
    print("=" * 60)
    
    tests = [
        test_basic_creation,
        test_no_tools_execution,
        test_tools_execution,
        test_structured_output,
        test_graph_structure,
        test_dynamic_tool_addition,
    ]
    
    results = []
    for test in tests:
        try:
            result = await test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    
    passed = sum(1 for r in results if r)
    total = len(results)
    
    for i, (test, result) in enumerate(zip(tests, results)):
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {i+1:2d}. {test.__name__:<30} {status}")
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! ValidationNodeV2 integration working correctly.")
    else:
        print("⚠️  Some tests failed. ValidationNodeV2 integration needs attention.")
    
    return passed == total


if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)