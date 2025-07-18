#!/usr/bin/env python3
"""
Simple Agent Example - Basic conversational agent demonstration.

This example shows how to create and use a basic SimpleAgent for
conversational interactions.
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.simple import SimpleAgent


async def main():
    """Run the simple agent example."""
    print("🤖 Haive SimpleAgent Example")
    print("=" * 40)

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

    print("\n🗨️  Starting conversation...")
    print("-" * 40)

    for i, user_input in enumerate(conversations, 1):
        print(f"\n👤 User: {user_input}")

        # Get agent response
        response = await agent.arun(user_input)
        print(f"🤖 Agent: {response}")

        # Add small delay between messages
        await asyncio.sleep(1)

    print("\n✅ Example completed successfully!")
    print(f"\nAgent '{agent.name}' processed {len(conversations)} messages.")


if __name__ == "__main__":
    asyncio.run(main())
