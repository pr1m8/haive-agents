#!/usr/bin/env python3
"""Debug test using Haive tracing utilities to find WHEN the model validation error occurs."""

import asyncio
from pathlib import Path
import sys


# Direct imports to avoid broken module paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))

# Import Haive debugging utilities
from haive.core.utils.dev.debug_decorators import debug_decorators
from haive.core.utils.dev.tracing import trace


# Enable tracing for pydantic and haive agents
trace.call_tracker.add_filter("pydantic")
trace.call_tracker.add_filter("SimpleAgentV3")
trace.call_tracker.add_filter("__init__")
trace.call_tracker.add_filter("model_")
trace.call_tracker.enable()


try:
    # Trace the import process
    @trace.calls
    def import_haive_components():
        from haive.agents.simple.agent_v3 import SimpleAgentV3
        from haive.core.engine.aug_llm import AugLLMConfig

        return AugLLMConfig, SimpleAgentV3

    AugLLMConfig, SimpleAgentV3 = import_haive_components()

except Exception:
    trace.stack()
    sys.exit(1)


@trace.calls
@debug_decorators.breakpoint_on_exception
async def test_with_tracing():
    """Test SimpleAgentV3 creation with full tracing."""
    # Step 1: Create AugLLMConfig (trace this)

    @trace.calls
    def create_engine():
        return AugLLMConfig(name="test", temperature=0.1)

    engine = create_engine()

    # Step 2: Create SimpleAgentV3 (this is where error happens)

    # Add variable tracking
    trace.vars(engine=engine)

    @trace.calls
    def create_agent():
        # This is where the error occurs - let's trace it deeply
        agent = SimpleAgentV3(name="test_agent", engine=engine)
        return agent

    try:
        agent = create_agent()
        return agent

    except Exception:
        trace.call_tracker.get_stats()

        trace.stack()

        # Re-raise to see full traceback
        raise


async def main():
    """Run debug test."""
    try:
        await test_with_tracing()

    except Exception:
        pass

    finally:
        trace.stats()

        trace.report()


if __name__ == "__main__":
    asyncio.run(main())
