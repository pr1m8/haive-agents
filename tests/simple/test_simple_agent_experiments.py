#!/usr/bin/env python3
"""Experiments to isolate SimpleAgent routing issues."""

from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def experiment_1_no_force_tool_use():
    """Test SimpleAgent with structured output but force_tool_use=False."""
    
    print("🧪 EXPERIMENT 1: SimpleAgent with force_tool_use=False")
    print("=" * 60)
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        force_tool_use=False  # DISABLE force tool use
    )
    
    agent = SimpleAgent(
        name="no_force_test",
        engine=engine,
        debug=True
    )
    
    print(f"   Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   Engine tool_choice_mode: {getattr(engine, 'tool_choice_mode', 'NOT_SET')}")
    print(f"   Engine tool_routes: {engine.tool_routes}")
    
    # Check graph
    graph = agent.graph
    edges = graph.get_edges()
    print(f"\n   Graph edges:")
    for source, target in edges:
        print(f"     {source} → {target}")
    
    print(f"\n   Expected: agent_node should have conditional edge")
    print(f"   Expected: If LLM makes tool call → validation")
    print(f"   Expected: If LLM doesn't make tool call → END")
    
    try:
        print(f"\n   🎯 Testing execution...")
        import signal
        def timeout_handler(signum, frame):
            raise TimeoutError("Timeout")
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(10)
        
        result = agent.run("What is 2+2?", debug=False)
        signal.alarm(0)
        print(f"   ✅ SUCCESS: {result}")
        return True
        
    except TimeoutError:
        print(f"   ⏰ TIMEOUT: Still infinite loop even without force_tool_use")
        return False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        return False


def experiment_2_no_structured_output():
    """Test SimpleAgent without structured output (baseline)."""
    
    print("\n🧪 EXPERIMENT 2: SimpleAgent without structured output")
    print("=" * 60)
    
    engine = AugLLMConfig(
        temperature=0.3,
        # No structured_output_model
    )
    
    agent = SimpleAgent(
        name="no_struct_test",
        engine=engine,
        debug=True
    )
    
    print(f"   Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   Engine tools: {len(engine.tools)} tools")
    print(f"   Engine tool_routes: {engine.tool_routes}")
    
    # Check graph
    graph = agent.graph
    edges = graph.get_edges()
    print(f"\n   Graph edges:")
    for source, target in edges:
        print(f"     {source} → {target}")
    
    print(f"\n   Expected: agent_node → END (simple case)")
    
    try:
        print(f"\n   🎯 Testing execution...")
        result = agent.run("What is 2+2?", debug=False)
        print(f"   ✅ SUCCESS: {result}")
        return True
        
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        return False


def experiment_3_check_routing_function():
    """Test the routing function that decides where agent_node goes."""
    
    print("\n🧪 EXPERIMENT 3: Test routing function directly")
    print("=" * 60)
    
    # Create agent with force_tool_use=True
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent = SimpleAgent(
        name="routing_test",
        engine=engine,
        debug=True
    )
    
    print(f"   Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    
    # Check graph structure in detail
    graph = agent.graph
    print(f"\n   Graph nodes: {list(graph.nodes.keys())}")
    
    # Check conditional edges
    if hasattr(graph, 'branches'):
        print(f"   Conditional edges:")
        for node, branches in graph.branches.items():
            print(f"     {node}:")
            for condition, targets in branches.items():
                print(f"       {condition} → {targets}")
    
    # Check regular edges
    edges = graph.get_edges()
    print(f"\n   Regular edges:")
    for source, target in edges:
        print(f"     {source} → {target}")
    
    print(f"\n   Key questions:")
    print(f"   Q1: Does agent_node have DIRECT edge to validation?")
    print(f"   Q2: Or does it have CONDITIONAL edge that might be broken?")
    print(f"   Q3: Are there multiple conflicting edges?")


def experiment_4_trace_first_step():
    """Trace just the first step to see what happens after agent_node."""
    
    print("\n🧪 EXPERIMENT 4: Trace first execution step")
    print("=" * 60)
    
    # Patch graph execution to see routing
    import haive.core.graph.state_graph.base_graph2 as graph_module
    
    original_invoke = None
    step_count = 0
    
    def debug_invoke(self, *args, **kwargs):
        nonlocal step_count
        step_count += 1
        print(f"\n   📋 GRAPH STEP {step_count}")
        
        if step_count > 3:  # Limit to prevent infinite
            raise TimeoutError("Stopped after 3 steps to prevent infinite loop")
        
        return original_invoke(self, *args, **kwargs)
    
    try:
        # Apply patch
        if hasattr(graph_module.BaseGraph, 'invoke'):
            original_invoke = graph_module.BaseGraph.invoke
            graph_module.BaseGraph.invoke = debug_invoke
        
        # Test
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        agent = SimpleAgent(
            name="trace_test",
            engine=engine,
            debug=True
        )
        
        print(f"   Starting execution...")
        result = agent.run("What is 2+2?", debug=False)
        print(f"   ✅ Completed: {result}")
        
    except TimeoutError as e:
        print(f"   ⏰ Stopped after 3 steps: {e}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    finally:
        # Restore original
        if original_invoke:
            graph_module.BaseGraph.invoke = original_invoke


def main():
    """Run all experiments."""
    
    print("🔬 SIMPLE AGENT ROUTING EXPERIMENTS")
    print("=" * 80)
    
    # Experiment 1: No force tool use
    success_1 = experiment_1_no_force_tool_use()
    
    # Experiment 2: No structured output (baseline)
    success_2 = experiment_2_no_structured_output()
    
    # Experiment 3: Check routing details
    experiment_3_check_routing_function()
    
    # Experiment 4: Trace execution steps
    experiment_4_trace_first_step()
    
    print("\n" + "=" * 80)
    print("🎯 EXPERIMENT RESULTS:")
    print(f"   1. force_tool_use=False: {'✅ Works' if success_1 else '❌ Still loops'}")
    print(f"   2. No structured output: {'✅ Works' if success_2 else '❌ Broken baseline'}")
    print(f"   3. Routing details: See graph structure above")
    print(f"   4. Step tracing: See execution trace above")
    
    if not success_2:
        print(f"\n🚨 CRITICAL: Even basic SimpleAgent without structured output fails!")
        print(f"   This suggests the issue is deeper than structured output routing.")
    elif not success_1:
        print(f"\n🎯 INSIGHT: Issue is related to structured output, not force_tool_use")
        print(f"   The problem occurs with structured output regardless of force_tool_use.")
    else:
        print(f"\n🤔 UNEXPECTED: Both experiments work - need deeper investigation")


if __name__ == "__main__":
    main()