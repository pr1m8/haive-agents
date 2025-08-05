"""Test script for Component 4 MultiAgentBase approach."""

import asyncio
from pathlib import Path
import sys


# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Now import our components
from component_4_multiagent_supervisor import (
    test_multiagent_supervisor,
    test_routing_logic,
)


if __name__ == "__main__":
    # Run routing test first
    asyncio.run(test_routing_logic())

    # Run full integration test
    asyncio.run(test_multiagent_supervisor())
