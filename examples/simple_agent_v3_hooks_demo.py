"""SimpleAgentV3 with Generalized Hooks Demo.

This demonstrates the generalized hook system working with SimpleAgentV3,
showing how the reflection patterns have been integrated into the enhanced base agent.
"""

import asyncio
import contextlib
import logging

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.base.hooks import HookContext
from haive.agents.simple.agent_v3 import SimpleAgentV3

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def demo_simple_agent_v3_hooks():
    """Demo SimpleAgentV3 with generalized hooks."""
    # Create SimpleAgentV3 with enhanced base agent
    agent = SimpleAgentV3(
        name="demo_writer",
        engine=AugLLMConfig(
            system_message="You are a creative writing assistant.", temperature=0.7
        ),
    )

    # Add hooks using decorators
    @agent.before_run
    def log_start(context: HookContext):
        pass

    @agent.after_run
    def log_completion(context: HookContext):
        if context.output_data:
            str(context.output_data).replace("\n", " ")[:100]

    @agent.pre_process
    def track_pre_processing(context: HookContext):
        pass

    @agent.post_process
    def track_post_processing(context: HookContext):
        pass

    @agent.before_reflection
    def track_reflection_start(context: HookContext):
        pass

    # Add a reflection agent for post-processing
    reflection_agent = SimpleAgentV3(
        name="critic",
        engine=AugLLMConfig(
            system_message="You are a literary critic who improves writing.",
            temperature=0.4,
        ),
    )

    # Set up post-processing with reflection
    agent.post_agent = reflection_agent
    agent.use_post_transform = True
    agent.post_transform_type = "reflection"

    # Execute with hooks and pre/post processing
    try:
        result = await agent.arun("Write a short story about a robot learning to paint")

        if isinstance(result, dict) and "transformations_applied" in result:
            pass

    except Exception:
        import traceback

        traceback.print_exc()


async def demo_factory_pattern():
    """Demo using factory patterns with SimpleAgentV3."""
    from haive.agents.base.pre_post_agent_mixin import create_reflection_agent

    # Create base agent
    base_agent = SimpleAgentV3(
        name="essay_writer",
        engine=AugLLMConfig(
            system_message="You are an academic essay writer.", temperature=0.6
        ),
    )

    # Use factory to add reflection
    enhanced_agent = create_reflection_agent(base_agent)

    # Add monitoring hooks
    @enhanced_agent.after_reflection
    def track_reflection_completion(context: HookContext):
        pass

    with contextlib.suppress(Exception):
        await enhanced_agent.arun(
            "Write an essay about the benefits of renewable energy"
        )


if __name__ == "__main__":
    asyncio.run(demo_simple_agent_v3_hooks())
    asyncio.run(demo_factory_pattern())
