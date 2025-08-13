#!/usr/bin/env python3
"""Agent with Hooks Example - Intermediate Level

This example demonstrates how to use the hooks system for pre/post processing
in SimpleAgentV3. Hooks allow you to intercept and modify agent behavior at
various points in the execution lifecycle.

Key concepts covered:
- Pre-processing hooks (before agent runs)
- Post-processing hooks (after agent runs)
- Reflection hooks (for self-analysis)
- Hook context and data flow
- Practical monitoring and enhancement patterns"""

import asyncio
from datetime import datetime
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

from haive.agents.base.hooks import HookContext, HookEvent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Create monitoring hooks
def monitor_start(context: HookContext) -> None:
    """Log when agent execution starts."""
    print(f"\n🚀 [HOOK] Agent '{context.agent_name}' starting execution")
    print(f"   Timestamp: {datetime.now().strftime('%H:%M:%S')}")
    if context.data.get("input"):
        print(f"   Input preview: {str(context.data['input'])[:100]}...")


def monitor_end(context: HookContext) -> None:
    """Log when agent execution ends."""
    print(f"\n✅ [HOOK] Agent '{context.agent_name}' completed execution")
    if context.data.get("output"):
        print(f"   Output preview: {str(context.data['output'])[:100]}...")
    if context.data.get("duration"):
        print(f"   Duration: {context.data['duration']:.2f}s")


def enhance_input(context: HookContext) -> dict[str, Any]:
    """Pre-process input to add context."""
    original_input = context.data.get("input", {})

    # Add timestamp to input
    if isinstance(original_input, dict):
        original_input["timestamp"] = datetime.now().isoformat()
        original_input["enhanced"] = True
        print("\n🔧 [HOOK] Enhanced input with timestamp")

    return {"input": original_input}


def analyze_output(context: HookContext) -> dict[str, Any]:
    """Post-process output to add analysis."""
    output = context.data.get("output", "")

    # Simple sentiment analysis (mock)
    sentiment = (
        "positive"
        if any(word in output.lower() for word in ["good", "great", "excellent"])
        else "neutral"
    )
    word_count = len(output.split())

    analysis = {
        "sentiment": sentiment,
        "word_count": word_count,
        "analyzed_at": datetime.now().isoformat(),
    }

    print(f"\n📊 [HOOK] Output analysis: sentiment={sentiment}, words={word_count}")

    return {"analysis": analysis}


async def main():
    """Demonstrate agent with hooks."""
    print("=" * 60)
    print("Agent with Hooks Example")
    print("=" * 60)

    # Create agent with custom hooks
    agent = SimpleAgentV3(
        name="writing_assistant",
        engine=AugLLMConfig(
            temperature=0.7,
            system_message="You are a helpful writing assistant. Be concise but informative.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [("system", "{system_message}"), ("human", "{query}")]
        ),
    )

    # Add monitoring hooks
    agent.add_hook(HookEvent.PRE_RUN, monitor_start)
    agent.add_hook(HookEvent.POST_RUN, monitor_end)

    # Add processing hooks
    agent.add_hook(HookEvent.PRE_PROCESS, enhance_input)
    agent.add_hook(HookEvent.POST_PROCESS, analyze_output)

    # Example 1: Basic execution with hooks
    print("\n1. Basic Writing Task with Hooks")
    print("-" * 40)

    result = await agent.arun(
        {"query": "Write a short paragraph about the benefits of reading books"}
    )

    print(f"\n📝 Agent Response:\n{result}")

    # Example 2: Reflection hook for self-improvement
    print("\n\n2. Agent with Reflection Hook")
    print("-" * 40)

    def reflection_hook(context: HookContext) -> dict[str, Any]:
        """Analyze agent's own output for improvement."""
        output = context.data.get("output", "")

        # Mock reflection analysis
        improvements = []
        if len(output) < 50:
            improvements.append("Response might be too brief")
        if "example" not in output.lower():
            improvements.append("Consider adding examples")

        print(f"\n🤔 [REFLECTION] Identified {len(improvements)} areas for improvement")
        for imp in improvements:
            print(f"   - {imp}")

        return {"improvements": improvements}

    # Add reflection hook
    agent.add_hook(HookEvent.BEFORE_REFLECTION, reflection_hook)

    result = await agent.arun({"query": "Explain machine learning in one sentence"})

    print(f"\n📝 Agent Response:\n{result}")

    # Example 3: Chain multiple agents with hooks
    print("\n\n3. Chained Agents with Shared Hooks")
    print("-" * 40)

    # Create a reviewer agent with hooks
    reviewer = SimpleAgentV3(
        name="reviewer",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a strict editor. Review the text and suggest improvements.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("human", "Review this text and suggest improvements:\n\n{text}"),
            ]
        ),
    )

    # Share monitoring hooks
    reviewer.add_hook(HookEvent.PRE_RUN, monitor_start)
    reviewer.add_hook(HookEvent.POST_RUN, monitor_end)

    # First agent writes
    draft = await agent.arun({"query": "Write about the importance of clean code"})

    # Second agent reviews
    review = await reviewer.arun({"text": draft})

    print(f"\n📝 Review:\n{review}")

    # Example 4: Custom hook factory pattern
    print("\n\n4. Hook Factory Pattern")
    print("-" * 40)

    def create_performance_hooks(threshold_ms: int = 1000):
        """Factory for creating performance monitoring hooks."""

        def check_performance(context: HookContext) -> None:
            duration = context.data.get("duration", 0) * 1000  # Convert to ms
            if duration > threshold_ms:
                print(
                    f"\n⚠️  [PERFORMANCE] Slow execution: {duration:.0f}ms (threshold: {threshold_ms}ms)"
                )
            else:
                print(f"\n⚡ [PERFORMANCE] Fast execution: {duration:.0f}ms")

        return check_performance

    # Create performance-monitored agent
    fast_agent = SimpleAgentV3(
        name="fast_responder",
        engine=AugLLMConfig(temperature=0.1),  # Low temp for speed
        prompt_template=ChatPromptTemplate.from_messages(
            [("human", "Answer in 5 words or less: {query}")]
        ),
    )

    # Add performance hook
    fast_agent.add_hook(HookEvent.POST_RUN, create_performance_hooks(500))

    result = await fast_agent.arun({"query": "What is Python?"})

    print(f"\n📝 Fast Response: {result}")

    # Show hook management
    print("\n\n5. Hook Management")
    print("-" * 40)

    print(f"Total hooks on writing_assistant: {len(agent.hooks)}")
    print(f"Hook events registered: {list(agent.hooks.keys())}")

    # Remove specific hook
    agent.remove_hook(HookEvent.POST_PROCESS, analyze_output)
    print(
        f"\nAfter removal: {len(agent.hooks.get(HookEvent.POST_PROCESS, []))} POST_PROCESS hooks"
    )

    # Clear all hooks
    agent.clear_hooks()
    print(f"After clearing: {len(agent.hooks)} total hooks")


if __name__ == "__main__":
    asyncio.run(main())
