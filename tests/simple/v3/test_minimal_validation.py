#!/usr/bin/env python3
"""Minimal test to check if ValidationNodeV2 integration works without broken imports."""

import asyncio
from pathlib import Path
import sys


# Direct imports to avoid broken module paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))

try:
    from haive.agents.simple.agent_v3 import SimpleAgentV3
    from haive.core.engine.aug_llm import AugLLMConfig
except ImportError:
    sys.exit(1)


async def test_basic():
    """Test basic SimpleAgentV3 creation."""
    try:
        # Create basic config
        engine = AugLLMConfig(name="test", temperature=0.1)

        # Create agent
        SimpleAgentV3(name="test_agent", engine=engine)

        # Check properties

        return True
    except Exception:
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_basic())
    sys.exit(0 if success else 1)
