#!/usr/bin/env python3
"""Debug validation with filtered output."""

import asyncio
import logging

from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Configure logging to capture validation messages
logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s - %(message)s"
)

# Set up a custom handler to capture validation messages
class ValidationLogCapture(logging.Handler):
    def __init__(self):
        super().__init__()
        self.messages = []

    def emit(self, record):
        if "validation" in record.name.lower() or "ValidationNode" in record.getMessage():
            self.messages.append(f"{record.levelname}: {record.getMessage()}")

# Add handler to root logger
capture_handler = ValidationLogCapture()
logging.getLogger().addHandler(capture_handler)

# Enable validation logger
validation_logger = logging.getLogger("haive.core.graph.node.validation_node_config_v2")
validation_logger.setLevel(logging.INFO)


async def debug_validation():
    """Debug the validation issue."""
    print("\n🔍 VALIDATION DEBUG")
    print("="*60)

    # Create config
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt,
        temperature=0.3
    )

    # Create agent
    agent = SimpleAgent(name="debug_agent", engine=config)

    # Set recursion limit to fail fast
    runtime_config = {"recursion_limit": 3}

    print("Executing with recursion_limit=3...")

    try:
        result = await agent.arun(
            {"objective": "Build a simple REST API"},
            config=runtime_config
        )
        print("\n✅ SUCCESS!")

    except Exception as e:
        print(f"\n❌ FAILED: {type(e).__name__}")

    # Show captured validation messages
    print("\n📋 VALIDATION MESSAGES:")
    print("-" * 60)
    for msg in capture_handler.messages:
        print(msg)

    if not capture_handler.messages:
        print("(No validation messages captured)")


async def main():
    """Run the debug."""
    await debug_validation()


if __name__ == "__main__":
    asyncio.run(main())
