#!/usr/bin/env python3
"""Debug with full traceback to find the error source."""

import asyncio
import sys
import traceback

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig


async def test_with_traceback():
    """Test with full traceback."""
    try:
        # Create config
        config = AugLLMConfig(temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig())

        # Create agent
        agent = SimpleAgentV3(
            name="traceback_agent",
            engine=config,
            debug=True,  # Enable debug
        )

        # Check if we can create state instance directly
        try:
            # Try creating with empty dict
            agent.state_schema()
        except Exception:
            traceback.print_exc()

        # Try to prepare input
        test_input = "Hello world"
        try:
            agent._prepare_input(test_input)
        except Exception:
            traceback.print_exc()

        # Try execution
        try:
            await agent.arun(test_input)
        except Exception as e:
            traceback.print_exc()

            # Extra debugging - check the actual error location
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb_list = traceback.extract_tb(exc_traceback)
            for _i, (filename, _line_num, _func_name, _text) in enumerate(tb_list):
                if "haive" in filename:
                    pass

            # Check the actual validation error
            if hasattr(e, "errors"):
                for _error in e.errors():
                    pass

            return False

        return True

    except Exception:
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_with_traceback())
