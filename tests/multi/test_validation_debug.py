#!/usr/bin/env python3
"""Debug the validation process step by step."""

from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_validation_process():
    """Debug validation step by step."""
    
    print("🔍 DEBUGGING VALIDATION PROCESS")
    print("=" * 50)
    
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
    
    print("📋 Step 1: Agent created with structured output")
    print(f"   - force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   - tool_routes: {engine.tool_routes}")
    
    # Check graph
    print("\n📋 Step 2: Graph structure")
    graph = agent.graph
    edges = graph.get_edges()
    for source, target in edges:
        print(f"   {source} → {target}")
    
    print("\n📋 Step 3: Expected flow for SimpleAgent with structured output:")
    print("   1. agent_node (force_tool_use=True) → AIMessage with SimpleResult tool call")
    print("   2. validation → ValidationNodeV2 processes tool call")  
    print("   3. validation_router_v2 → routes to parse_output (success)")
    print("   4. parse_output → processes structured output")
    print("   5. __end__ → completes")
    
    print("\n📋 Step 4: Questions to investigate:")
    print("   Q1: Is ValidationNodeV2 creating successful ToolMessage?")
    print("   Q2: Is validation_router_v2 routing to parse_output?")
    print("   Q3: Is there a loop back to agent_node?")
    print("   Q4: Why does force_tool_use cause infinite LLM calls?")
    
    print("\n📋 Step 5: Key insight from SimpleAgentV2:")
    print("   - ValidationNodeV2 should create ToolMessage for structured output")
    print("   - validation_router_v2 should route successful validation to parse_output")
    print("   - Only errors should route back to agent_node")
    print("   - NO multiple __end__ edges should exist")
    
    return agent


def main():
    """Run validation debugging."""
    agent = test_validation_process()
    
    print("\n📋 HYPOTHESIS:")
    print("The issue might be:")
    print("1. ValidationNodeV2 is creating an ERROR ToolMessage instead of success")
    print("2. validation_router_v2 is routing errors back to agent_node")
    print("3. agent_node with force_tool_use=True keeps making tool calls")
    print("4. Infinite loop ensues")
    
    print("\n📋 NEXT STEPS:")
    print("1. Patch ValidationNodeV2 to log what ToolMessage it creates")
    print("2. Patch validation_router_v2 to log routing decisions")
    print("3. See if validation is failing for some reason")


if __name__ == "__main__":
    main()