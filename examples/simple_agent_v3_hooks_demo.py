"""SimpleAgentV3 with Generalized Hooks Demo.

This demonstrates the generalized hook system working with SimpleAgentV3,
showing how the reflection patterns have been integrated into the enhanced base agent.
"""

import asyncio
import logging

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.base.hooks import HookContext, HookEvent
from haive.agents.simple.agent_v3 import SimpleAgentV3

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def demo_simple_agent_v3_hooks():
    """Demo SimpleAgentV3 with generalized hooks."""
    print("🎯 SimpleAgentV3 with Generalized Hooks Demo")
    print("=" * 50)

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
        print(f"🚀 Starting {context.agent_name}")
        print(f"   Input: {str(context.input_data)[:50]}...")

    @agent.after_run
    def log_completion(context: HookContext):
        print(f"✅ Completed {context.agent_name}")
        if context.output_data:
            output_str = str(context.output_data).replace("\n", " ")[:100]
            print(f"   Output: {output_str}...")

    @agent.pre_process
    def track_pre_processing(context: HookContext):
        print(f"📝 Pre-processing for {context.agent_name}")

    @agent.post_process
    def track_post_processing(context: HookContext):
        print(f"🔄 Post-processing completed for {context.agent_name}")

    @agent.before_reflection
    def track_reflection_start(context: HookContext):
        print(f"💭 Starting reflection for {context.agent_name}")

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

    print("\n📋 Agent Configuration:")
    print(f"   Main agent: {agent.name}")
    print(f"   Post agent: {agent.post_agent.name if agent.post_agent else 'None'}")
    print(f"   Post transform: {agent.use_post_transform}")
    print(f"   Transform type: {agent.post_transform_type}")

    # Execute with hooks and pre/post processing
    print("\n🎬 Executing agent with hooks...")
    try:
        result = await agent.arun("Write a short story about a robot learning to paint")

        print(f"\n🎉 Execution completed!")
        if isinstance(result, dict):
            print(f"   Processing stages: {result.get('processing_stages', {})}")
            if "transformations_applied" in result:
                print(f"   Transformations: {result['transformations_applied']}")

    except Exception as e:
        print(f"❌ Execution failed: {e}")
        import traceback

        traceback.print_exc()


async def demo_factory_pattern():
    """Demo using factory patterns with SimpleAgentV3."""
    print("\n\n🏭 Factory Pattern Demo")
    print("=" * 30)

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

    print(f"✨ Enhanced agent created:")
    print(f"   Main agent: {enhanced_agent.name}")
    print(
        f"   Post agent: {enhanced_agent.post_agent.name if enhanced_agent.post_agent else 'None'}"
    )
    print(f"   Reflection enabled: {enhanced_agent.use_post_transform}")

    # Add monitoring hooks
    @enhanced_agent.after_reflection
    def track_reflection_completion(context: HookContext):
        print(f"🔍 Reflection completed for {context.agent_name}")

    try:
        result = await enhanced_agent.arun(
            "Write an essay about the benefits of renewable energy"
        )
        print(f"📄 Essay completed with reflection enhancement!")

    except Exception as e:
        print(f"❌ Essay writing failed: {e}")


if __name__ == "__main__":
    asyncio.run(demo_simple_agent_v3_hooks())
    asyncio.run(demo_factory_pattern())
