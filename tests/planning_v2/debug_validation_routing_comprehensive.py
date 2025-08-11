#!/usr/bin/env python3
"""Comprehensive debug plan for validation routing with breakpoints and tracing."""

import logging
from typing import List
from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)

def debug_step_1_agent_creation():
    """Step 1: Debug agent creation and route assignment."""
    print("=" * 80)
    print("STEP 1: AGENT CREATION AND ROUTE ASSIGNMENT")
    print("=" * 80)
    
    # Create agent with debug
    agent = SimpleAgent(
        name="debug_agent",
        engine=AugLLMConfig(
            structured_output_model=Plan[Task],
            temperature=0.1
        ),
        debug=True
    )
    
    # Check 1: Tool Routes
    print("1.1 Tool Routes:")
    for name, route in agent.engine.tool_routes.items():
        print(f"   {name} → {route}")
        if route != "parse_output" and "plan" in name.lower():
            print(f"   ❌ ISSUE: {name} should have parse_output route, got {route}")
    
    # Check 2: Engine Configuration
    print("\n1.2 Engine Configuration:")
    print(f"   structured_output_model: {agent.engine.structured_output_model}")
    print(f"   force_tool_use: {agent.engine.force_tool_use}")
    print(f"   force_tool_choice: {getattr(agent.engine, 'force_tool_choice', None)}")
    
    # Check 3: Agent State
    print("\n1.3 Agent State:")
    print(f"   force_tool_use: {agent.force_tool_use}")
    print(f"   _has_structured_output(): {agent._has_structured_output()}")
    print(f"   _always_needs_validation(): {agent._always_needs_validation()}")
    
    return agent

def debug_step_2_graph_structure(agent):
    """Step 2: Debug graph structure and edges."""
    print("\n" + "=" * 80)
    print("STEP 2: GRAPH STRUCTURE AND EDGES")
    print("=" * 80)
    
    # Check 1: Nodes
    print("2.1 Graph Nodes:")
    for node in agent.graph.nodes.keys():
        print(f"   - {node}")
    
    # Check 2: Regular Edges
    print("\n2.2 Regular Edges:")
    for edge in agent.graph.edges:
        print(f"   {edge[0]} → {edge[1]}")
    
    # Check 3: Conditional Edges (Branches)
    print("\n2.3 Conditional Edges (Branches):")
    if hasattr(agent.graph, 'branches'):
        for branch_id, branch in agent.graph.branches.items():
            print(f"   Branch from {branch.source_node}:")
            print(f"     Destinations: {branch.destinations}")
            print(f"     Function: {branch.function}")
            
            # BREAKPOINT 1: Check if validation has conditional edges
            if branch.source_node == "validation":
                print(f"     ✅ FOUND VALIDATION BRANCH")
                if "parse_output" not in branch.destinations:
                    print(f"     ❌ MISSING parse_output destination!")
                if "agent_node" not in branch.destinations:
                    print(f"     ❌ MISSING agent_node destination!")
    else:
        print("   ❌ NO BRANCHES FOUND")

def debug_step_3_validation_routing_logic():
    """Step 3: Debug validation routing logic."""
    print("\n" + "=" * 80)
    print("STEP 3: VALIDATION ROUTING LOGIC")
    print("=" * 80)
    
    # Import the router function
    from haive.core.graph.node.validation_router_v2 import validation_router_v2
    
    print("3.1 Validation Router Function:")
    print(f"   Function: {validation_router_v2}")
    print(f"   Module: {validation_router_v2.__module__}")
    
    # Test the router with mock state
    mock_state = {
        "messages": [],
        "tool_routes": {"plan_task_generic": "parse_output"},
    }
    
    print("\n3.2 Testing Router with Mock State:")
    print(f"   Mock tool_routes: {mock_state['tool_routes']}")
    
    try:
        result = validation_router_v2(mock_state)
        print(f"   Router result: {result}")
    except Exception as e:
        print(f"   ❌ Router error: {e}")

def debug_step_4_execution_tracing(agent):
    """Step 4: Trace execution with breakpoints."""
    print("\n" + "=" * 80)
    print("STEP 4: EXECUTION TRACING")
    print("=" * 80)
    
    print("4.1 Pre-execution State:")
    print(f"   Messages: {len(agent.get_state().messages)}")
    
    # BREAKPOINT 2: Hook into LangGraph execution
    original_invoke = agent.graph.invoke
    step_count = 0
    
    def traced_invoke(input_data, config=None):
        nonlocal step_count
        step_count += 1
        print(f"\n   STEP {step_count}: LangGraph invoke called")
        print(f"     Input keys: {list(input_data.keys()) if isinstance(input_data, dict) else type(input_data)}")
        
        if step_count > 5:
            print(f"   ❌ TOO MANY STEPS! Stopping at {step_count}")
            raise Exception("Too many execution steps - likely infinite loop")
            
        result = original_invoke(input_data, config)
        print(f"     Output keys: {list(result.keys()) if isinstance(result, dict) else type(result)}")
        
        # Check for tool messages
        if isinstance(result, dict) and "messages" in result:
            messages = result["messages"]
            tool_messages = [m for m in messages if hasattr(m, 'name') and 'plan' in str(getattr(m, 'name', ''))]
            if tool_messages:
                print(f"     Found {len(tool_messages)} tool messages")
                for tm in tool_messages[-1:]:  # Show last one
                    print(f"       Tool: {getattr(tm, 'name', 'unknown')}")
                    print(f"       Content: {str(getattr(tm, 'content', ''))[:100]}...")
        
        return result
    
    # Monkey patch for tracing
    agent.graph.invoke = traced_invoke
    
    try:
        print("\n4.2 Starting execution with tracing...")
        result = agent.run("Create a simple plan", debug=True)
        print(f"\n4.3 ✅ EXECUTION COMPLETED in {step_count} steps")
        print(f"   Result type: {type(result)}")
        return True, result
    except Exception as e:
        print(f"\n4.3 ❌ EXECUTION FAILED after {step_count} steps: {e}")
        return False, str(e)
    finally:
        # Restore original function
        agent.graph.invoke = original_invoke

def run_comprehensive_debug():
    """Run all debug steps systematically."""
    print("🔍 COMPREHENSIVE VALIDATION ROUTING DEBUG")
    print("=" * 80)
    
    try:
        # Step 1: Agent Creation
        agent = debug_step_1_agent_creation()
        
        # Step 2: Graph Structure  
        debug_step_2_graph_structure(agent)
        
        # Step 3: Routing Logic
        debug_step_3_validation_routing_logic()
        
        # Step 4: Execution Tracing
        success, result = debug_step_4_execution_tracing(agent)
        
        print("\n" + "=" * 80)
        print("FINAL DIAGNOSIS")
        print("=" * 80)
        
        if success:
            print("✅ Execution successful - fix is working!")
        else:
            print("❌ Execution failed - need to investigate further")
            print(f"   Error: {result}")
            
    except Exception as e:
        print(f"\n💥 DEBUG SCRIPT ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_comprehensive_debug()