#!/usr/bin/env python3
"""ReactAgent with Tools Example - Give Your Agent Superpowers!

This example shows how to create a ReactAgent that can use tools.
ReactAgent uses a "Reason-Act" pattern to think about problems and use tools to solve them.

What you'll learn:
- How to create simple tools using the @tool decorator
- How to create a ReactAgent with tools
- How ReactAgent thinks step-by-step to solve problems"""

# Suppress logging for a cleaner demo
import logging

logging.getLogger().setLevel(logging.ERROR)

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

# Import the components we need
from haive.agents.react.agent import ReactAgent

# ============================================
# Step 1: Create Simple Tools
# ============================================
# Tools are functions that your agent can call to perform actions
# We'll create a calculator and a word counter


@tool
def calculator(expression: str) -> str:
    """A simple calculator that can evaluate mathematical expressions.

    Args:
        expression: A mathematical expression like "2 + 2" or "10 * 5"

    Returns:
        The result of the calculation as a string"""
    try:
        # Safely evaluate the mathematical expression
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error calculating: {e!s}"


@tool
def word_counter(text: str) -> str:
    """Count the number of words in a text.

    Args:
        text: The text to count words in

    Returns:
        The word count as a string"""
    word_count = len(text.split())
    return f"The text contains {word_count} words"


# ============================================
# Step 2: Create the ReactAgent
# ============================================
# ReactAgent is smarter than SimpleAgent - it can reason about problems
# and decide which tools to use

config = AugLLMConfig(
    temperature=0.1,  # Low temperature for more predictable reasoning
    system_message="You are a helpful assistant that can calculate math and count words.",
)

# Create the agent with our tools
agent = ReactAgent(
    name="math_assistant",
    engine=config,
    tools=[calculator, word_counter],  # Give the agent access to our tools
)

# ============================================
# Step 3: Watch the Agent Think and Act!
# ============================================
print("🤖 ReactAgent with Tools Example")
print("=" * 50)

# Ask the agent to do some math
print("You: What is 15 multiplied by 23?")
print("\n🧠 Agent is thinking...")

response = agent.run("What is 15 multiplied by 23?")
print(f"\nAgent: {response}")
print("=" * 50)

# ============================================
# Step 4: Multiple Tool Usage
# ============================================
print("\n📊 Using Multiple Tools")
print("=" * 50)

# Ask a question that requires multiple tools
complex_question = """I have a sentence: "The quick brown fox jumps over the lazy dog"
1. How many words are in this sentence?
2. If each word costs $3.50, what's the total cost?"""

print(f"You: {complex_question}")
print("\n🧠 Agent is thinking (this might use multiple tools)...")

response = agent.run(complex_question)
print(f"\nAgent: {response}")
print("=" * 50)

# ============================================
# Behind the Scenes: The ReAct Pattern
# ============================================
print("\n🔍 How ReactAgent Works:")
print("=" * 50)
print("1. REASON: The agent thinks about the problem")
print("2. ACT: The agent decides which tool to use")
print("3. OBSERVE: The agent sees the tool's result")
print("4. REPEAT: The agent may use more tools or provide the final answer")
print("\nThis is called the ReAct (Reason + Act) pattern!")

# ============================================
# Step 5: When Tools Aren't Needed
# ============================================
print("\n💬 Sometimes No Tools Are Needed")
print("=" * 50)

simple_question = "What's the capital of France?"
print(f"You: {simple_question}")

response = agent.run(simple_question)
print(f"\nAgent: {response}")
print("\n(Notice: The agent didn't need tools for this question!)")
print("=" * 50)

# ============================================
# Try It Yourself!
# ============================================
print("\n💡 Ideas to Expand This Example:")
print("- Create a weather tool that returns random weather")
print("- Add a tool that tells jokes")
print("- Create a tool that converts units (miles to km, etc.)")
print("- Make a tool that generates random numbers")
print("\nRemember: Tools give your agent superpowers! 🚀")
