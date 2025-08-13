#!/usr/bin/env python3
"""Trace execution from base agent to understand the infinite loop."""

import logging
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def setup_tracing():
    """Setup detailed logging to trace execution."""
    
    # Set up logging for key components
    loggers = [
        'haive.agents.base.agent',
        'haive.core.graph.node.agent_node',
        'haive.core.graph.node.validation_router_v2',
        'haive.core.graph.node.validation_node_v2',
        'haive.core.engine.aug_llm.config',
        'haive.core.graph.base_graph',
        'langgraph'
    ]
    
    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        
        # Create console handler if not exists
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
    
    print("🔍 Tracing setup complete")


def trace_simple_agent_creation():
    """Trace SimpleAgent creation process."""
    
    print("\n" + "="*80)
    print("TRACING SIMPLE AGENT CREATION")
    print("="*80)
    
    print("📋 Step 1: Creating AugLLMConfig with structured output...")
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    print(f"   ✅ Engine created:")
    print(f"      - force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"      - tool_choice_mode: {getattr(engine, 'tool_choice_mode', 'NOT_SET')}")
    print(f"      - tools: {len(engine.tools)} tools")
    print(f"      - tool_routes: {engine.tool_routes}")
    
    print("\n📋 Step 2: Creating SimpleAgent...")
    agent = SimpleAgent(
        name="trace_test",
        engine=engine,
        debug=True
    )
    
    print(f"   ✅ Agent created:")
    print(f"      - type: {type(agent).__name__}")
    print(f"      - engine force_tool_use: {getattr(agent.engine, 'force_tool_use', 'NOT_SET')}")
    print(f"      - state_schema: {agent.state_schema}")
    
    return agent


def trace_graph_structure(agent):
    """Trace the agent's graph structure."""
    
    print("\n" + "="*80)
    print("TRACING GRAPH STRUCTURE")
    print("="*80)
    
    graph = agent.graph
    print(f"📋 Graph type: {type(graph).__name__}")
    print(f"📋 Graph nodes: {list(graph.nodes.keys())}")
    
    print("\n📋 Graph edges:")
    edges = graph.get_edges()
    for source, target in edges:
        print(f"   {source} → {target}")
    
    # Check conditional edges
    print("\n📋 Conditional edges:")
    if hasattr(graph, 'branches'):
        for node, branches in graph.branches.items():
            print(f"   {node} branches:")
            for condition, targets in branches.items():
                print(f"      {condition} → {targets}")
    
    return graph


def trace_single_execution_step(agent):
    """Trace a single execution step to see what happens."""
    
    print("\n" + "="*80)
    print("TRACING SINGLE EXECUTION STEP")
    print("="*80)
    
    print("📋 Starting execution with max_iterations=1...")
    
    # Set max iterations to prevent infinite loop
    if hasattr(agent, 'max_iterations'):
        original_max = agent.max_iterations
        agent.max_iterations = 1
    else:
        original_max = None
    
    try:
        print("📋 Calling agent.run()...")
        result = agent.run("What is 2+2?", debug=True)
        print(f"   ✅ Execution completed: {result}")
        return True, result
        
    except Exception as e:
        print(f"   ❌ Execution failed: {e}")
        return False, str(e)
        
    finally:
        # Restore original max_iterations
        if original_max is not None:
            agent.max_iterations = original_max


def trace_state_creation():
    """Trace how state is created and managed."""
    
    print("\n" + "="*80)
    print("TRACING STATE CREATION")
    print("="*80)
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent = SimpleAgent(
        name="state_trace",
        engine=engine,
        debug=True
    )
    
    print("📋 Creating initial state...")
    state = agent.state_schema()
    
    print(f"   ✅ State created:")
    print(f"      - type: {type(state).__name__}")
    print(f"      - tool_routes: {getattr(state, 'tool_routes', 'NOT_SET')}")
    print(f"      - engine: {type(getattr(state, 'engine', None))}")
    print(f"      - messages: {len(getattr(state, 'messages', []))}")
    
    return state


def main():
    """Run comprehensive tracing."""
    
    print("🚀 STARTING COMPREHENSIVE AGENT TRACING")
    print("🚀 This will help us understand the infinite loop issue")
    
    # Setup tracing
    setup_tracing()
    
    # Trace agent creation
    agent = trace_simple_agent_creation()
    
    # Trace graph structure
    graph = trace_graph_structure(agent)
    
    # Trace state creation
    state = trace_state_creation()
    
    # Trace single execution step (limited to prevent infinite loop)
    success, result = trace_single_execution_step(agent)
    
    print("\n" + "="*80)
    print("TRACING SUMMARY")
    print("="*80)
    print(f"📋 Agent creation: ✅ Success")
    print(f"📋 Graph structure: ✅ Success")
    print(f"📋 State creation: ✅ Success")
    print(f"📋 Execution: {'✅ Success' if success else '❌ Failed'}")
    
    if not success:
        print(f"📋 Execution error: {result}")
        print("📋 This confirms the infinite loop issue exists")
    else:
        print("📋 Execution succeeded - no infinite loop detected")


if __name__ == "__main__":
    main()