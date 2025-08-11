#!/usr/bin/env python3
"""Debug validation with detailed output to understand the issue."""

import asyncio
import logging
from haive.agents.simple import SimpleAgent
from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.utils.naming import sanitize_tool_name

# Configure logging to show only validation-related messages
logging.basicConfig(
    level=logging.WARNING,
    format='%(name)s - %(levelname)s - %(message)s'
)

# Enable specific loggers we care about
validation_logger = logging.getLogger('haive.core.graph.node.validation_node_config_v2')
validation_logger.setLevel(logging.INFO)

aug_llm_logger = logging.getLogger('haive.core.engine.aug_llm')
aug_llm_logger.setLevel(logging.INFO)


async def debug_validation():
    """Debug the validation issue with focused output."""
    print("\n" + "="*80)
    print("🔍 VALIDATION DEBUG - Understanding the Issue")
    print("="*80)
    
    # Show the model and its sanitized name
    model_class = Plan[Task]
    original_name = model_class.__name__
    sanitized_name = sanitize_tool_name(original_name)
    
    print(f"\n1. Model Information:")
    print(f"   - Original name: {original_name}")
    print(f"   - Sanitized name: {sanitized_name}")
    print(f"   - Model class: {model_class}")
    
    # Create config
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt,
        temperature=0.3
    )
    
    # Check what tools are registered
    print(f"\n2. AugLLMConfig State:")
    print(f"   - Tools: {[type(t).__name__ for t in config.tools]}")
    print(f"   - Tool routes: {config.tool_routes}")
    print(f"   - Force tool choice: {config.force_tool_choice}")
    
    # Create agent
    agent = SimpleAgent(name='debug_agent', engine=config)
    
    # Check graph structure
    print(f"\n3. Graph Structure:")
    print(f"   - Nodes: {list(agent.graph.nodes.keys())}")
    print(f"   - Edges:")
    if hasattr(agent.graph, 'edges'):
        for source, target in agent.graph.edges:
            print(f"     {source} → {target}")
    else:
        print("     (Unable to access edges)")
    
    # Set recursion limit to fail fast
    runtime_config = {"recursion_limit": 3}
    
    print(f"\n4. Executing with recursion_limit=3...")
    print("-" * 40)
    
    try:
        result = await agent.arun(
            {"objective": "Build a simple REST API"}, 
            config=runtime_config
        )
        print(f"\n✅ SUCCESS! Result type: {type(result)}")
        if hasattr(result, 'model_dump'):
            print(f"   Result: {result.model_dump()}")
        else:
            print(f"   Result: {result}")
            
    except Exception as e:
        print(f"\n❌ FAILED with {type(e).__name__}: {str(e)}")
        
        # Check if we can get more info about the loop
        if "recursion" in str(e).lower():
            print("\n5. Recursion Details:")
            print("   The graph is looping between nodes.")
            print("   This suggests validation is failing and routing back to agent_node.")
            print("   The agent then makes the same tool call, creating an infinite loop.")


async def main():
    """Run the debug."""
    await debug_validation()


if __name__ == "__main__":
    asyncio.run(main())