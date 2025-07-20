#!/usr/bin/env python3
"""Debug script for self-discover agent hanging issue."""

import logging
import os
import sys

# Add packages to path
sys.path.insert(0, "packages/haive-core/src")
sys.path.insert(0, "packages/haive-agents/src")

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_basic_imports():
    """Test if basic imports work without hanging."""
    try:

        # Try importing the models

        return True
    except Exception:
        return False


def test_engine_creation():
    """Test creating AugLLM engines without agents."""
    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.reasoning_and_critique.self_discover.v2.models import (
            SelectedModules,
        )
        from haive.agents.reasoning_and_critique.self_discover.v2.prompts import (
            select_prompt,
        )

        # Create a simple engine config
        AugLLMConfig(
            name="test_engine",
            structured_output_model=SelectedModules,
            structured_output_version="v2",
            prompt_template=select_prompt,
            temperature=0.7,
        )
        return True
    except Exception:
        return False


def test_simple_agent_creation():
    """Test creating a single SimpleAgent."""
    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.reasoning_and_critique.self_discover.v2.models import (
            SelectedModules,
        )
        from haive.agents.reasoning_and_critique.self_discover.v2.prompts import (
            select_prompt,
        )
        from haive.agents.simple.agent import SimpleAgent

        # Create engine config
        engine_config = AugLLMConfig(
            name="test_engine",
            structured_output_model=SelectedModules,
            structured_output_version="v2",
            prompt_template=select_prompt,
            temperature=0.7,
        )

        # This is where it might hang
        SimpleAgent(engine=engine_config)
        return True
    except Exception:
        return False


def main():
    """Run debug tests step by step."""
    # Disable PostgreSQL persistence for testing
    os.environ["HAIVE_DISABLE_PERSISTENCE"] = "1"

    # Test step by step
    if not test_basic_imports():
        return 1

    if not test_engine_creation():
        return 1

    if not test_simple_agent_creation():
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
