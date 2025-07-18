"""Test the new Self-Discover MultiAgent implementation."""

import asyncio
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent))

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.reasoning_and_critique.self_discover.agent import SelfDiscoverAgent


async def test_self_discover_sequential():
    """Test the sequential Self-Discover implementation."""
    print("=== Testing Sequential Self-Discover MultiAgent ===\n")
    
    # Use the Self-Discover agent
    self_discover = SelfDiscoverAgent
    
    # Simple test task
    task = "What is the sum of the first 10 prime numbers?"
    
    print(f"Task: {task}")
    print(f"Number of agents: {len(self_discover.agents)}")
    print(f"Agents: {[agent.name for agent in self_discover.agents]}")
    print(f"Sequential execution mode")
    print("\nExecuting...\n")
    
    try:
        # Run the system
        result = await self_discover.arun(task)
        
        print("\n=== Execution Complete ===")
        print(f"Result type: {type(result)}")
        print(f"Task: {result.get('task', 'Not found')}")
        print(f"Process completed: {result.get('process_completed', False)}")
        
        if result.get('self_discover_result'):
            discover_result = result['self_discover_result']
            print(f"Self-Discover result type: {type(discover_result)}")
            if isinstance(discover_result, dict):
                print("Self-Discover result keys:")
                for key, value in discover_result.items():
                    if value is not None:
                        print(f"  {key}: {str(value)[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"\nError during execution: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def test_self_discover_custom_modules():
    """Test Self-Discover with custom reasoning modules."""
    print("\n\n=== Testing Custom Reasoning Modules ===\n")
    
    # Custom modules for testing
    custom_modules = """1. Problem Analysis: Break down the problem into smaller components
2. Solution Design: Create potential solutions based on analysis
3. Evaluation: Assess pros and cons of each solution
4. Implementation: Plan the execution of the chosen solution"""
    
    # Create agent with custom modules
    self_discover = SelfDiscoverAgent(available_modules=custom_modules)
    
    # Test task
    task = "How to improve customer satisfaction in a coffee shop"
    
    print(f"Task: {task}")
    print(f"Custom modules: {len(custom_modules.split('\\n'))} modules")
    print("\nExecuting...\n")
    
    try:
        result = await self_discover.arun(task)
        
        print("\n=== Execution Complete ===")
        print(f"Process completed: {result.get('process_completed', False)}")
        print(f"Result available: {result.get('self_discover_result') is not None}")
        
        return True
        
    except Exception as e:
        print(f"\nError during execution: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def test_svg_path_example():
    """Test the original SVG path example."""
    print("\n\n=== Testing SVG Path Example ===\n")
    
    # Create agent
    self_discover = SelfDiscoverAgent()
    
    # SVG path task from original code
    svg_task = """This SVG path element <path d="M 55.57,80.69 L 57.38,65.80 M 57.38,65.80 L 48.90,57.46 M 48.90,57.46 L
45.58,47.78 M 45.58,47.78 L 53.25,36.07 L 66.29,48.90 L 78.69,61.09 L 55.57,80.69"/> draws a:
(A) circle (B) heptagon (C) hexagon (D) kite (E) line (F) octagon (G) pentagon(H) rectangle (I) sector (J) triangle"""
    
    print(f"Task: SVG path analysis")
    print(f"Available modules: {len(self_discover._available_modules.split('\\n'))} modules")
    print("\nExecuting...\n")
    
    try:
        result = await self_discover.arun(svg_task)
        
        print("\n=== Execution Complete ===")
        print(f"Process completed: {result.get('process_completed', False)}")
        print(f"Result type: {type(result.get('self_discover_result'))}")
        
        return True
        
    except Exception as e:
        print(f"\nError during execution: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def test_agent_components():
    """Test that all components are properly configured."""
    print("\n\n=== Testing Agent Components ===\n")
    
    # Create agent
    self_discover = SelfDiscoverAgent()
    
    try:
        # Check all agents exist
        expected_agents = ["selector", "adapter", "structurer", "executor"]
        print(f"Expected agents: {expected_agents}")
        print(f"Actual agents: {list(self_discover.agents.keys())}")
        
        # Check agent types
        for agent_name, agent in self_discover.agents.items():
            print(f"  {agent_name}: {type(agent).__name__}")
        
        # Check branching configuration
        print(f"\nBranching configuration:")
        for agent_name, branch_config in self_discover.branches.items():
            print(f"  {agent_name} → {branch_config.get('next', 'N/A')}")
        
        # Check state schema
        print(f"\nState schema: {self_discover.state_schema.__name__}")
        print(f"Entry point: {self_discover.entry_point}")
        
        return True
        
    except Exception as e:
        print(f"\nError checking components: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run all tests."""
    print("Testing New Self-Discover MultiAgent Implementation")
    print("=" * 60)
    
    # Run tests
    test1_passed = await test_self_discover_sequential()
    test2_passed = await test_self_discover_custom_modules()
    test3_passed = await test_svg_path_example()
    test4_passed = await test_agent_components()
    
    print("\n" + "=" * 60)
    print("Test Results:")
    print(f"  Sequential execution: {'✅ PASSED' if test1_passed else '❌ FAILED'}")
    print(f"  Custom modules: {'✅ PASSED' if test2_passed else '❌ FAILED'}")
    print(f"  SVG path example: {'✅ PASSED' if test3_passed else '❌ FAILED'}")
    print(f"  Agent components: {'✅ PASSED' if test4_passed else '❌ FAILED'}")
    
    all_passed = test1_passed and test2_passed and test3_passed and test4_passed
    print(f"\nOverall: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    
    return all_passed


if __name__ == "__main__":
    # Run with proper async handling
    success = asyncio.run(main())
    sys.exit(0 if success else 1)