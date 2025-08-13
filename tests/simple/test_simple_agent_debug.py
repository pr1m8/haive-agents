#!/usr/bin/env python3
"""Debug SimpleAgent with structured output step by step."""

from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def debug_simple_agent_step_by_step():
    """Debug SimpleAgent execution step by step."""
    
    print("🔍 DEBUGGING SIMPLE AGENT WITH STRUCTURED OUTPUT")
    print("=" * 60)
    
    # Step 1: Create engine
    print("\n📋 Step 1: Creating AugLLMConfig...")
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    print(f"   Engine properties:")
    print(f"   - force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   - tool_choice_mode: {getattr(engine, 'tool_choice_mode', 'NOT_SET')}")  
    print(f"   - tools count: {len(engine.tools)}")
    print(f"   - tool_routes: {engine.tool_routes}")
    
    # Step 2: Create agent
    print("\n📋 Step 2: Creating SimpleAgent...")
    agent = SimpleAgent(
        name="debug_simple",
        engine=engine,
        debug=True
    )
    
    print(f"   Agent properties:")
    print(f"   - type: {type(agent).__name__}")
    print(f"   - state_schema: {agent.state_schema}")
    
    # Step 3: Check graph structure
    print("\n📋 Step 3: Examining graph structure...")
    graph = agent.graph
    print(f"   - graph type: {type(graph).__name__}")
    print(f"   - nodes: {list(graph.nodes.keys())}")
    
    edges = graph.get_edges()
    print(f"   - edges:")
    for source, target in edges:
        print(f"     {source} → {target}")
    
    # Step 4: Check what SimpleAgent graph should look like
    print("\n📋 Step 4: Expected SimpleAgent flow with structured output:")
    print("   Expected: agent_node → validation → parse_output → __end__")
    print("   Key: SimpleAgent should NOT loop back to agent_node")
    print("   Key: force_tool_use=True should make agent_node always produce tool calls")
    
    # Step 5: Try to understand why it's looping
    print("\n📋 Step 5: Potential issues:")
    print("   Issue 1: Is agent_node producing multiple tool calls?")
    print("   Issue 2: Is validation routing back to agent_node?")
    print("   Issue 3: Is parse_output not ending properly?")
    
    return agent


def debug_simple_agent_state():
    """Debug the state creation and setup."""
    
    print("\n📋 DEBUGGING STATE CREATION")
    print("=" * 40)
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent = SimpleAgent(
        name="state_debug",
        engine=engine,
        debug=True
    )
    
    # Create state
    state = agent.state_schema()
    
    print(f"   State properties:")
    print(f"   - type: {type(state).__name__}")
    print(f"   - tool_routes: {getattr(state, 'tool_routes', 'NOT_SET')}")
    print(f"   - messages: {len(getattr(state, 'messages', []))}")
    print(f"   - engine: {type(getattr(state, 'engine', None))}")
    
    return state


def debug_single_step_execution():
    """Try to execute just one step to see what happens."""
    
    print("\n📋 DEBUGGING SINGLE STEP EXECUTION")
    print("=" * 40)
    
    # We know this will timeout, but let's see the first few steps
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent = SimpleAgent(
        name="single_step",
        engine=engine,
        debug=False  # Reduce noise
    )
    
    print("   Attempting execution (will timeout, but let's see initial steps)...")
    print("   Input: 'What is 2+2?'")
    print("   Expected: agent_node should produce AIMessage with tool_calls")
    print("   Expected: validation should process tool_calls")
    print("   Expected: parse_output should handle successful validation")
    print("   Expected: should end after parse_output")
    
    # Note: This will likely timeout, but we can see the pattern


def main():
    """Run step-by-step debugging."""
    
    # Debug agent creation
    agent = debug_simple_agent_step_by_step()
    
    # Debug state creation  
    state = debug_simple_agent_state()
    
    # Debug execution (will timeout but shows pattern)
    debug_single_step_execution()
    
    print("\n📋 KEY QUESTIONS TO INVESTIGATE:")
    print("1. Why does agent_node keep producing tool calls?")
    print("2. Is the LLM being forced to call tools repeatedly?")
    print("3. Does SimpleAgent have the right graph structure for structured output?")
    print("4. Should SimpleAgent with structured output even use force_tool_use=True?")


if __name__ == "__main__":
    main()