#!/usr/bin/env python3
"""Simple Agent Example - Basic conversational agent demonstration.

This example shows how to create and use a basic SimpleAgent for
conversational interactions.
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.simple import SimpleAgent


async def main():
    """Run the simple agent example."""
    # Create agent configuration
    config = AugLLMConfig(
        model="gpt-4",
        temperature=0.7,
        system_message="You are a helpful AI assistant created by Haive.",
    )

    # Create the agent
    agent = SimpleAgent(name="helpful_assistant", engine=config)

    # Example conversations
    conversations = [
        "Hello! What can you help me with?",
        "What is the Haive framework used for?",
        "Can you explain what makes you different from other AI assistants?",
        "Thank you for the help!",
    ]

    for _i, user_input in enumerate(conversations, 1):

        # Get agent response
        await agent.arun(user_input)

        # Add small delay between messages
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
