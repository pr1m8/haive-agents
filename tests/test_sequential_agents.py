#!/usr/bin/env python3
"""Test creating multiple agents sequentially to debug hanging issue."""

import logging
import os
import sys


# Add packages to path
sys.path.insert(0, "packages/haive-core/src")
sys.path.insert(0, "packages/haive-agents/src")

# Set up logging
logging.basicConfig(level=logging.INFO)  # Less verbose
logger = logging.getLogger(__name__)


def create_multiple_simple_agents():
    """Test creating multiple SimpleAgent instances."""
    try:
        from haive.agents.reasoning_and_critique.self_discover.v2.models import (
            AdaptedModules,
            FinalAnswer,
            ReasoningStructure,
            SelectedModules,
        )
        from haive.agents.reasoning_and_critique.self_discover.v2.prompts import (
            adapt_prompt,
            reasoning_prompt,
            select_prompt,
            structured_prompt,
        )
        from haive.agents.simple.agent import SimpleAgent
        from haive.core.engine.aug_llm import AugLLMConfig

        # Create AugLLM configs for each step
        select_engine = AugLLMConfig(
            name="select_modules",
            structured_output_model=SelectedModules,
            structured_output_version="v2",
            prompt_template=select_prompt,
            temperature=0.7,
        )

        adapt_engine = AugLLMConfig(
            name="adapt_modules",
            structured_output_model=AdaptedModules,
            structured_output_version="v2",
            prompt_template=adapt_prompt,
            temperature=0.7,
        )

        structure_engine = AugLLMConfig(
            name="create_structure",
            structured_output_model=ReasoningStructure,
            structured_output_version="v2",
            prompt_template=structured_prompt,
            temperature=0.3,
        )

        reason_engine = AugLLMConfig(
            name="final_reasoning",
            structured_output_model=FinalAnswer,
            structured_output_version="v2",
            prompt_template=reasoning_prompt,
            temperature=0.1,
        )

        # Create SimpleAgent for each step - this might hang
        select_agent = SimpleAgent(engine=select_engine)

        adapt_agent = SimpleAgent(engine=adapt_engine)

        structure_agent = SimpleAgent(engine=structure_engine)

        reason_agent = SimpleAgent(engine=reason_engine)

        return [select_agent, adapt_agent, structure_agent, reason_agent]

    except Exception:
        import traceback

        traceback.print_exc()
        return None


def test_sequential_agent():
    """Test creating a SequentialAgent with multiple sub-agents."""
    agents = create_multiple_simple_agents()
    if not agents:
        return False

    try:
        from haive.agents.multi.base import SequentialAgent

        # This is where it might hang
        SequentialAgent(agents=agents)
        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run the sequential agent test."""
    # Set some environment variables to potentially avoid issues
    os.environ["HAIVE_DISABLE_PERSISTENCE"] = "0"  # Enable persistence to replicate the issue

    if test_sequential_agent():
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
