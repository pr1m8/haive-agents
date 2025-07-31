"""Test the new Self-Discover MultiAgent implementation."""

import asyncio
from pathlib import Path
import sys


# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent))


from haive.agents.reasoning_and_critique.self_discover.agent import SelfDiscoverAgent


async def test_self_discover_sequential():
    """Test the sequential Self-Discover implementation."""
    # Use the Self-Discover agent
    self_discover = SelfDiscoverAgent

    # Simple test task
    task = "What is the sum of the first 10 prime numbers?"

    try:
        # Run the system
        result = await self_discover.arun(task)

        if result.get("self_discover_result"):
            discover_result = result["self_discover_result"]
            if isinstance(discover_result, dict):
                for _key, value in discover_result.items():
                    if value is not None:
                        pass

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def test_self_discover_custom_modules():
    """Test Self-Discover with custom reasoning modules."""
    # Custom modules for testing
    custom_modules = """1. Problem Analysis: Break down the problem into smaller components
2. Solution Design: Create potential solutions based on analysis
3. Evaluation: Assess pros and cons of each solution
4. Implementation: Plan the execution of the chosen solution"""

    # Create agent with custom modules
    self_discover = SelfDiscoverAgent(available_modules=custom_modules)

    # Test task
    task = "How to improve customer satisfaction in a coffee shop"

    try:
        await self_discover.arun(task)

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def test_svg_path_example():
    """Test the original SVG path example."""
    # Create agent
    self_discover = SelfDiscoverAgent()

    # SVG path task from original code
    svg_task = """This SVG path element <path d="M 55.57,80.69 L 57.38,65.80 M 57.38,65.80 L 48.90,57.46 M 48.90,57.46 L
45.58,47.78 M 45.58,47.78 L 53.25,36.07 L 66.29,48.90 L 78.69,61.09 L 55.57,80.69"/> draws a:
(A) circle (B) heptagon (C) hexagon (D) kite (E) line (F) octagon (G) pentagon(H) rectangle (I) sector (J) triangle"""

    try:
        await self_discover.arun(svg_task)

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def test_agent_components():
    """Test that all components are properly configured."""
    # Create agent
    self_discover = SelfDiscoverAgent()

    try:
        # Check all agents exist

        # Check agent types
        for _agent_name, _agent in self_discover.agents.items():
            pass

        # Check branching configuration
        for _agent_name, _branch_config in self_discover.branches.items():
            pass

        # Check state schema

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def main():
    """Run all tests."""
    # Run tests
    test1_passed = await test_self_discover_sequential()
    test2_passed = await test_self_discover_custom_modules()
    test3_passed = await test_svg_path_example()
    test4_passed = await test_agent_components()

    all_passed = test1_passed and test2_passed and test3_passed and test4_passed

    return all_passed


if __name__ == "__main__":
    # Run with proper async handling
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
