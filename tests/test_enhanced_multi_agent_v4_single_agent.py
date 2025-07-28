#!/usr/bin/env python3
"""Test EnhancedMultiAgentV4 with single agent to isolate issues."""

import pytest
import asyncio
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

# Import components
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4


@tool
def test_calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"


def test_single_simple_agent_creation():
    """Test EnhancedMultiAgentV4 with single SimpleAgent."""
    print("\n🔍 Testing EnhancedMultiAgentV4 with Single SimpleAgent")
    print("=" * 60)
    
    # Create single SimpleAgent
    simple_agent = SimpleAgentV3(
        name="solo_simple",
        engine=AugLLMConfig(temperature=0.7)
    )
    
    print(f"✅ SimpleAgent created: {simple_agent.name}")
    
    # Create EnhancedMultiAgentV4 with single agent
    try:
        multi_agent = EnhancedMultiAgentV4(
            name="single_simple_workflow",
            agents=[simple_agent],  # Single agent in list
            execution_mode="sequential"
        )
        
        print(f"✅ EnhancedMultiAgentV4 created: {multi_agent.name}")
        print(f"   Agents count: {len(multi_agent.agents)}")
        print(f"   Execution mode: {multi_agent.execution_mode}")
        print(f"   State schema: {multi_agent.state_schema}")
        
        return multi_agent
        
    except Exception as e:
        print(f"❌ EnhancedMultiAgentV4 creation failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_single_react_agent_creation():
    """Test EnhancedMultiAgentV4 with single ReactAgent."""
    print("\n🔍 Testing EnhancedMultiAgentV4 with Single ReactAgent")
    print("=" * 60)
    
    # Create single ReactAgent with tools
    react_agent = ReactAgentV3(
        name="solo_react",
        engine=AugLLMConfig(temperature=0.3, tools=[test_calculator]),
        max_iterations=2
    )
    
    print(f"✅ ReactAgent created: {react_agent.name}")
    
    # Create EnhancedMultiAgentV4 with single agent
    try:
        multi_agent = EnhancedMultiAgentV4(
            name="single_react_workflow",
            agents=[react_agent],  # Single agent in list
            execution_mode="sequential"
        )
        
        print(f"✅ EnhancedMultiAgentV4 created: {multi_agent.name}")
        print(f"   Agents count: {len(multi_agent.agents)}")
        print(f"   Agent has tools: {len(react_agent.config.engines.get('main', {}).get('tools', [])) if hasattr(react_agent, 'config') else 'Unknown'}")
        
        return multi_agent
        
    except Exception as e:
        print(f"❌ EnhancedMultiAgentV4 creation failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_single_agent_graph_building():
    """Test graph building with single agent."""
    print("\n🔍 Testing Graph Building with Single Agent")
    print("=" * 60)
    
    # Create simple agent and multi-agent
    simple_agent = SimpleAgentV3(
        name="graph_test",
        engine=AugLLMConfig(temperature=0.7)
    )
    
    multi_agent = EnhancedMultiAgentV4(
        name="graph_build_test",
        agents=[simple_agent],
        execution_mode="sequential"
    )
    
    print(f"✅ Multi-agent created")
    
    try:
        # Test graph building
        print("\n🔧 Building graph...")
        graph = multi_agent.build_graph()
        
        print(f"✅ Graph built successfully: {type(graph)}")
        print(f"   Graph name: {graph.name}")
        print(f"   Graph nodes: {list(graph.nodes.keys())}")
        print(f"   Graph edges: {len(graph.edges)}")
        print(f"   State schema: {graph.state_schema}")
        
        # Check graph structure
        if graph.nodes:
            print("\n📊 Node Details:")
            for node_name, node in graph.nodes.items():
                print(f"   {node_name}: {type(node)}")
                if hasattr(node, 'agent_name'):
                    print(f"     Agent: {node.agent_name}")
                if hasattr(node, 'metadata'):
                    print(f"     Metadata: {list(node.metadata.keys())}")
        
        return graph
        
    except Exception as e:
        print(f"❌ Graph building failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_single_agent_compilation():
    """Test compilation of single agent multi-agent workflow."""
    print("\n🔍 Testing Single Agent Compilation")
    print("=" * 60)
    
    # Create and build
    simple_agent = SimpleAgentV3(
        name="compile_test",
        engine=AugLLMConfig(temperature=0.7)
    )
    
    multi_agent = EnhancedMultiAgentV4(
        name="compile_test_workflow",
        agents=[simple_agent],
        execution_mode="sequential"
    )
    
    try:
        print("🔧 Building graph...")
        graph = multi_agent.build_graph()
        print(f"✅ Graph built")
        
        print("🔧 Compiling multi-agent...")
        compiled_app = multi_agent.compile()
        
        print(f"✅ Compilation successful!")
        print(f"   Compiled app type: {type(compiled_app)}")
        print(f"   Has invoke method: {hasattr(compiled_app, 'invoke')}")
        print(f"   Has ainvoke method: {hasattr(compiled_app, 'ainvoke')}")
        
        return compiled_app
        
    except Exception as e:
        print(f"❌ Compilation failed: {e}")
        import traceback
        traceback.print_exc()
        return None


@pytest.mark.asyncio
async def test_single_agent_execution():
    """Test actual execution of single agent workflow."""
    print("\n🔍 Testing Single Agent Execution")
    print("=" * 60)
    
    # Create and compile
    simple_agent = SimpleAgentV3(
        name="exec_test",
        engine=AugLLMConfig(temperature=0.7)
    )
    
    multi_agent = EnhancedMultiAgentV4(
        name="exec_test_workflow",
        agents=[simple_agent],
        execution_mode="sequential"
    )
    
    try:
        print("🔧 Compiling...")
        compiled_app = multi_agent.compile()
        print("✅ Compiled successfully")
        
        # Test input
        test_input = {
            "messages": [HumanMessage(content="What is 5 + 7?")]
        }
        
        print(f"📥 Input: {test_input}")
        
        print("🚀 Executing workflow...")
        
        # THIS IS THE CRITICAL TEST - Does execution work?
        result = await multi_agent.arun(test_input)
        
        print(f"✅ Execution successful!")
        print(f"   Result type: {type(result)}")
        print(f"   Result: {str(result)[:200]}...")
        
        # Check result structure
        if hasattr(result, 'messages'):
            print(f"   Messages: {len(result.messages)}")
        if hasattr(result, 'agents'):
            print(f"   Agents: {list(result.agents.keys())}")
        if hasattr(result, 'agent_outputs'):
            print(f"   Agent outputs: {list(result.agent_outputs.keys())}")
            
        return result
        
    except Exception as e:
        print(f"❌ Execution failed: {e}")
        print(f"   Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        return None


@pytest.mark.asyncio
async def test_single_react_agent_execution():
    """Test execution with ReactAgent that uses tools."""
    print("\n🔍 Testing Single ReactAgent Execution with Tools")
    print("=" * 60)
    
    # Create ReactAgent with tools
    react_agent = ReactAgentV3(
        name="tool_test",
        engine=AugLLMConfig(temperature=0.3, tools=[test_calculator]),
        max_iterations=2
    )
    
    multi_agent = EnhancedMultiAgentV4(
        name="tool_test_workflow",
        agents=[react_agent],
        execution_mode="sequential"
    )
    
    try:
        print("🔧 Compiling...")
        compiled_app = multi_agent.compile()
        print("✅ Compiled successfully")
        
        # Test input that should trigger tool use
        test_input = {
            "messages": [HumanMessage(content="Calculate 15 * 23")]
        }
        
        print(f"📥 Input: {test_input}")
        print("🚀 Executing workflow with tool use...")
        
        result = await multi_agent.arun(test_input)
        
        print(f"✅ Tool execution successful!")
        print(f"   Result type: {type(result)}")
        
        # Check for tool usage
        if hasattr(result, 'messages'):
            print(f"   Messages: {len(result.messages)}")
            for i, msg in enumerate(result.messages):
                print(f"     {i}: {type(msg).__name__} - {str(msg.content)[:50]}...")
                if hasattr(msg, 'tool_calls') and msg.tool_calls:
                    print(f"       Tool calls: {len(msg.tool_calls)}")
        
        # Check if calculation was done
        result_str = str(result)
        if "345" in result_str:
            print("   ✅ Calculation result found in output!")
        else:
            print("   ⚠️ Calculation result not found")
            
        return result
        
    except Exception as e:
        print(f"❌ Tool execution failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_state_schema_compatibility():
    """Test that MultiAgentState is compatible with single agents."""
    print("\n🔍 Testing State Schema Compatibility")
    print("=" * 60)
    
    from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
    
    # Create agent and state
    simple_agent = SimpleAgentV3(
        name="state_test",
        engine=AugLLMConfig(temperature=0.7)
    )
    
    try:
        # Test MultiAgentState creation with single agent
        state = MultiAgentState(
            messages=[HumanMessage(content="Test")],
            agents={"state_test": simple_agent}
        )
        
        print(f"✅ MultiAgentState created")
        print(f"   Agent count: {state.agent_count}")
        print(f"   Has messages: {len(state.messages)}")
        print(f"   Agents: {list(state.agents.keys())}")
        
        # Test state methods
        print("\n📋 Testing state methods:")
        
        # Get agent
        retrieved_agent = state.get_agent("state_test")
        print(f"   get_agent(): {retrieved_agent.name if retrieved_agent else 'None'}")
        
        # Set active agent
        state.set_active_agent("state_test")
        print(f"   set_active_agent(): {state.active_agent}")
        
        # Test state conversion to dict
        state_dict = state.model_dump()
        print(f"   model_dump(): {type(state_dict)} with {len(state_dict)} keys")
        
        # Test dict access methods
        try:
            # These should work if StateSchema implements dict-like methods
            messages = state.get("messages", [])
            print(f"   state.get('messages'): {len(messages)} messages")
        except Exception as e:
            print(f"   state.get() failed: {e}")
        
        try:
            # Test if __getitem__ works
            messages = state["messages"]
            print(f"   state['messages']: {len(messages)} messages")
        except Exception as e:
            print(f"   state['messages'] failed: {e}")
            
        return state
        
    except Exception as e:
        print(f"❌ State schema test failed: {e}")
        import traceback
        traceback.print_exc()
        return None


async def main():
    """Run all single agent tests."""
    print("🚀 EnhancedMultiAgentV4 Single Agent Testing Suite")
    print("=" * 80)
    
    # Test creation
    simple_multi = test_single_simple_agent_creation()
    react_multi = test_single_react_agent_creation()
    
    # Test graph building
    graph = test_single_agent_graph_building()
    
    # Test compilation
    compiled_app = test_single_agent_compilation()
    
    # Test state compatibility
    state = test_state_schema_compatibility()
    
    # Test execution
    simple_result = await test_single_agent_execution()
    react_result = await test_single_react_agent_execution()
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 SINGLE AGENT TEST RESULTS SUMMARY")
    print("=" * 80)
    print(f"Simple Agent Creation:     {'✅ PASS' if simple_multi else '❌ FAIL'}")
    print(f"React Agent Creation:      {'✅ PASS' if react_multi else '❌ FAIL'}")
    print(f"Graph Building:            {'✅ PASS' if graph else '❌ FAIL'}")
    print(f"Compilation:               {'✅ PASS' if compiled_app else '❌ FAIL'}")
    print(f"State Compatibility:       {'✅ PASS' if state else '❌ FAIL'}")
    print(f"Simple Agent Execution:    {'✅ PASS' if simple_result else '❌ FAIL'}")
    print(f"React Agent Execution:     {'✅ PASS' if react_result else '❌ FAIL'}")
    
    # Overall assessment
    all_pass = all([simple_multi, react_multi, graph, compiled_app, state, simple_result, react_result])
    print(f"\n🎯 OVERALL RESULT: {'✅ ALL TESTS PASS' if all_pass else '❌ SOME TESTS FAILED'}")
    
    if all_pass:
        print("✅ EnhancedMultiAgentV4 works perfectly with single agents!")
        print("   The issue is likely in multi-agent coordination, not basic functionality.")
    else:
        print("❌ Found issues with basic single-agent functionality.")
        print("   Need to fix fundamental problems before multi-agent coordination.")


if __name__ == "__main__":
    asyncio.run(main())