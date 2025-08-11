#!/usr/bin/env python3
"""Trace the validation flow to understand the recursion issue."""

import asyncio
import logging
from haive.agents.simple import SimpleAgent
from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.core.engine.aug_llm import AugLLMConfig

# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Also log the validation nodes specifically
validation_logger = logging.getLogger('haive.core.graph.node.validation_node_config_v2')
validation_logger.setLevel(logging.DEBUG)


async def trace_validation_issue():
    """Trace exactly what happens during validation."""
    print("🔍 TRACING VALIDATION FLOW")
    print("=" * 60)
    
    # Create config with recursion limit
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt,
        temperature=0.3
    )
    
    agent = SimpleAgent(name='trace_agent', engine=config)
    
    # Set a small recursion limit to fail faster
    runtime_config = {"recursion_limit": 5}
    
    print("1. Agent configured with recursion_limit=5")
    print(f"   Validation node type: {type(agent.graph.nodes.get('validation'))}")
    
    try:
        print("\n2. Starting execution...")
        result = await agent.arun(
            {"objective": "Build a simple REST API"}, 
            config=runtime_config
        )
        
        print(f"3. Success! Result: {result}")
        
    except Exception as e:
        print(f"\n❌ EXCEPTION: {type(e).__name__}")
        print(f"   Message: {str(e)}")
        
        # Look at the graph state to understand the loop
        if hasattr(agent, 'graph'):
            print(f"\n4. Graph nodes: {list(agent.graph.nodes.keys())}")
            print(f"   Graph edges:")
            for source, targets in agent.graph._edges.items():
                print(f"     {source} → {targets}")


async def main():
    """Run the trace."""
    await trace_validation_issue()


if __name__ == "__main__":
    asyncio.run(main())