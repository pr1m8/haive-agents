#!/usr/bin/env python3
"""Step by step execution trace to see what happens after agent_node."""

from pydantic import BaseModel, Field


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def patch_graph_execution():
    """Patch graph execution to trace each step."""
    
    import haive.core.graph.state_graph.base_graph2 as graph_module
    from langgraph.graph import END
    
    step_count = 0
    
    # Patch the graph step execution
    original_step = None
    
    def debug_step(self, input_data, config=None):
        nonlocal step_count
        step_count += 1
        
        print(f"\n🔍 GRAPH STEP {step_count}")
        print(f"   Input keys: {list(input_data.keys()) if isinstance(input_data, dict) else 'Not dict'}")
        
        if step_count > 5:  # Prevent infinite loop
            print(f"   🛑 STOPPING after {step_count} steps to prevent infinite loop")
            raise KeyboardInterrupt("Manual stop")
        
        # Call original step
        result = original_step(self, input_data, config)
        
        print(f"   Output: {type(result)} - {str(result)[:100]}...")
        
        return result
    
    # Find and patch the execution method
    if hasattr(graph_module.BaseGraph, '_step'):
        original_step = graph_module.BaseGraph._step
        graph_module.BaseGraph._step = debug_step
        return True
    else:
        print("Could not find _step method to patch")
        return False


def patch_conditional_edges():
    """Patch conditional edge evaluation to see routing decisions."""
    
    # We need to patch whatever function handles conditional edges
    # This will vary depending on the LangGraph implementation
    print("🔍 Setting up conditional edge tracing...")
    
    # Patch any routing functions we can find
    import haive.agents.simple.agent as simple_module
    
    # Look for routing functions in simple agent
    if hasattr(simple_module, 'SimpleAgent'):
        agent_class = simple_module.SimpleAgent
        if hasattr(agent_class, 'build_graph'):
            print("   Found build_graph method - will examine graph structure")
            return True
    
    return False


def test_step_by_step_execution():
    """Test SimpleAgent execution step by step."""
    
    print("🔍 STEP BY STEP EXECUTION TRACE")
    print("=" * 60)
    
    # Set up patches
    graph_patched = patch_graph_execution()
    conditional_patched = patch_conditional_edges()
    
    print(f"   Graph execution patched: {graph_patched}")
    print(f"   Conditional edges patched: {conditional_patched}")
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.agents.simple.agent import SimpleAgent
        
        # Create agent
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        agent = SimpleAgent(
            name="step_trace",
            engine=engine,
            debug=True
        )
        
        print(f"\n📋 Agent created:")
        print(f"   - force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
        print(f"   - tool_routes: {engine.tool_routes}")
        
        # Examine graph structure BEFORE execution
        print(f"\n📋 Graph structure:")
        graph = agent.graph
        nodes = list(graph.nodes.keys())
        print(f"   - nodes: {nodes}")
        
        edges = graph.get_edges()
        print(f"   - edges:")
        for source, target in edges:
            print(f"     {source} → {target}")
        
        # Check for conditional edges
        if hasattr(graph, 'branches'):
            print(f"   - conditional edges:")
            for node, branches in graph.branches.items():
                print(f"     {node}:")
                for condition, targets in branches.items():
                    print(f"       condition {condition} → {targets}")
        
        print(f"\n🎯 Starting execution...")
        print(f"   Input: 'What is 2+2?'")
        
        # Execute with tracing
        result = agent.run("What is 2+2?", debug=False)
        
        print(f"\n✅ Execution completed: {result}")
        
    except KeyboardInterrupt:
        print(f"\n🛑 Execution stopped manually after tracing steps")
    except Exception as e:
        print(f"\n❌ Execution failed: {e}")
        import traceback
        traceback.print_exc()


def examine_agent_node_output():
    """Examine what the agent_node is outputting."""
    
    print("\n🔍 EXAMINING AGENT NODE OUTPUT")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.agents.simple.agent import SimpleAgent
        
        # Create minimal setup
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        agent = SimpleAgent(
            name="output_test",
            engine=engine,
            debug=True
        )
        
        # Get the agent node directly
        graph = agent.graph
        agent_node = graph.nodes.get('agent_node')
        
        print(f"   Agent node type: {type(agent_node)}")
        print(f"   Agent node: {agent_node}")
        
        # Create a test state
        state = agent.state_schema()
        state.messages = [{"role": "user", "content": "What is 2+2?"}]
        
        print(f"\n📋 Test state created:")
        print(f"   - messages: {len(state.messages)}")
        print(f"   - tool_routes: {getattr(state, 'tool_routes', 'NOT_SET')}")
        
        print(f"\n🎯 Calling agent_node directly...")
        
        # This should show us what agent_node produces
        # But might also loop, so we'll be careful
        
    except Exception as e:
        print(f"   ❌ Failed to examine agent node: {e}")


def main():
    """Run step by step analysis."""
    
    print("🔬 STEP BY STEP EXECUTION ANALYSIS")
    print("=" * 80)
    
    # Test 1: Step by step execution
    test_step_by_step_execution()
    
    # Test 2: Examine agent node output
    examine_agent_node_output()
    
    print(f"\n📋 KEY QUESTIONS TO ANSWER:")
    print(f"1. What does agent_node output? (AIMessage with tool calls?)")
    print(f"2. What conditional edge function is called after agent_node?")
    print(f"3. What does the conditional edge function return?")
    print(f"4. Why doesn't execution move to the next node?")


if __name__ == "__main__":
    main()