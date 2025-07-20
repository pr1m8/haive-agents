#!/usr/bin/env python3
"""Simple Agent Tutorial - Your First Haive Agent.

Difficulty: ⭐ Beginner
Estimated Time: 5 minutes
Learning Objectives:
  • Create a basic conversational agent
  • Understand agent configuration
  • Run simple interactions

Next Steps:
  → Try react_agent_tutorial.py for tool-enabled agents
  → Explore multi_agent_basics.py for coordination
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.simple import SimpleAgent


async def main():
    """Run the simple agent tutorial."""
    # Step 1: Create agent configuration
    config = AugLLMConfig(
        temperature=0.7,  # Balance between creativity and consistency
        system_message="You are a helpful assistant who provides clear, concise answers.",
    )

    # Step 2: Create the agent
    agent = SimpleAgent(
        name="tutorial_agent",
        engine=config,
        # Disable persistence for tutorial
        enable_persistence=False,
    )

    # Step 3: Run some interactions

    # Example conversation
    user_inputs = [
        "Hello! What is Haive?",
        "Can you explain what an AI agent is?",
        "What are the benefits of using AI agents?",
    ]

    for _i, user_input in enumerate(user_inputs, 1):

        # Get agent response
        await agent.arun(user_input)

        # Small pause between conversations
        await asyncio.sleep(0.5)


if __name__ == "__main__":
    asyncio.run(main())
