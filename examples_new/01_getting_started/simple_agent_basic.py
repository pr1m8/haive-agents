#!/usr/bin/env python3
"""
Simple Agent Basic Example - Your First Haive Agent

This is the simplest possible example of creating an agent in Haive.
Think of it as the "Hello World" of AI agents!

What you'll learn:
- How to create a basic SimpleAgent
- How to configure it with an LLM
- How to run the agent and get a response
"""

# Suppress logging for a cleaner demo
import logging

logging.getLogger().setLevel(logging.ERROR)

from haive.core.engine.aug_llm import AugLLMConfig

# Import the essential components
from haive.agents.simple.agent import SimpleAgent

# ============================================
# Step 1: Create the LLM Configuration
# ============================================
# This tells the agent which AI model to use and how to behave
config = AugLLMConfig(
    temperature=0.7,  # How creative the AI should be (0=predictable, 2=very creative)
    system_message="You are a friendly and helpful assistant.",  # The AI's personality
)

# ============================================
# Step 2: Create Your First Agent
# ============================================
# SimpleAgent is the most basic type of agent - it just responds to messages
agent = SimpleAgent(
    name="my_first_agent",  # Give your agent a name
    engine=config,  # Use the configuration we created
)

# ============================================
# Step 3: Talk to Your Agent!
# ============================================
print("🤖 Simple Agent Basic Example")
print("=" * 50)

# Send a message to the agent and get a response
response = agent.run("Hello! What's the weather like today?")

# The response is just a string - simple!
print(f"You: Hello! What's the weather like today?")
print(f"\nAgent: {response}")
print("=" * 50)

# ============================================
# Step 4: Have a Conversation
# ============================================
# The agent remembers the conversation history
print("\n📝 Continuing the conversation...")
print("=" * 50)

# Ask a follow-up question
follow_up = agent.run("Can you recommend indoor activities?")
print(f"You: Can you recommend indoor activities?")
print(f"\nAgent: {follow_up}")
print("=" * 50)

# ============================================
# What's Happening Behind the Scenes?
# ============================================
print("\n🔍 Behind the Scenes:")
print("=" * 50)
print("1. The agent receives your message")
print("2. It sends the message to the AI model (LLM)")
print("3. The AI generates a response based on:")
print("   - Your message")
print("   - The system message (personality)")
print("   - The conversation history")
print("4. The agent returns the response to you")
print("\n✅ That's it! You've created your first AI agent!")

# ============================================
# Try It Yourself!
# ============================================
print("\n💡 Try modifying this example:")
print("- Change the system_message to give the agent a different personality")
print("- Adjust the temperature (0.1 for factual, 1.5 for creative)")
print("- Ask the agent different questions")
print("- Create multiple agents with different personalities!")
