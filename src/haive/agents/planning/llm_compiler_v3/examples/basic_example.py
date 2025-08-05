"""Basic example of LLM Compiler V3 Agent usage.

This example demonstrates the core functionality of the LLM Compiler V3 Agent
with simple tools and a straightforward query.
"""

import asyncio

from langchain_core.tools import tool

from haive.agents.planning.llm_compiler_v3 import LLMCompilerV3Agent


# Define some basic tools for the example
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression.replace("^", "**"))  # Handle exponents
        return str(result)
    except Exception as e:
        return f"Error: {e}"


@tool
def text_analyzer(text: str) -> str:
    """Analyze text and return basic statistics."""
    words = text.split()
    chars = len(text)
    sentences = text.count(".") + text.count("!") + text.count("?")

    return f"Text Analysis: {len(words)} words, {chars} characters, {sentences} sentences"


@tool
def word_reverser(text: str) -> str:
    """Reverse the order of words in text."""
    return " ".join(text.split()[::-1])


async def basic_llm_compiler_example():
    """Basic example demonstrating LLM Compiler V3 functionality."""
    # Create tools
    tools = [calculator, text_analyzer, word_reverser]

    # Create agent with default configuration
    agent = LLMCompilerV3Agent(name="basic_compiler", tools=tools)

    # Example query that can benefit from parallelization
    query = """
    Please help me with these tasks:
    1. Calculate the result of (15 + 27) * 3
    2. Analyze this text: "The quick brown fox jumps over the lazy dog"
    3. Reverse the words in: "Hello world from LLM Compiler"

    Provide a summary of all results.
    """

    # Execute the query
    start_time = asyncio.get_event_loop().time()

    try:
        result = await agent.arun(query)

        end_time = asyncio.get_event_loop().time()
        end_time - start_time

        # Display results

        if result.parallel_efficiency:
            pass

        # Show detailed execution breakdown
        if result.execution_results:
            for _i, task_result in enumerate(result.execution_results, 1):
                if task_result.error_message:
                    pass

        # Show reasoning trace
        if result.reasoning_trace:
            for _i, _step in enumerate(result.reasoning_trace, 1):
                pass

        return result

    except Exception:
        return None


async def parallel_efficiency_demo():
    """Demonstrate parallel execution efficiency."""
    # Create agent
    agent = LLMCompilerV3Agent(
        name="efficiency_demo", tools=[calculator, text_analyzer, word_reverser]
    )

    # Query with multiple independent tasks
    parallel_query = """
    Perform these independent calculations and analyses:
    1. Calculate 123 + 456
    2. Calculate 789 * 12
    3. Analyze the text: "Parallel processing enables efficient task execution"
    4. Reverse the words: "Efficiency through parallelization"
    5. Calculate the square of 25
    """

    # Execute and measure
    result = await agent.arun(parallel_query)

    if result.parallel_efficiency:
        pass

    return result


async def error_handling_demo():
    """Demonstrate error handling and replanning."""

    # Tool that will fail
    @tool
    def failing_tool(input_text: str) -> str:
        """A tool that always fails."""
        raise Exception("This tool always fails for demonstration")

    # Create agent with failing tool
    agent = LLMCompilerV3Agent(name="error_demo", tools=[calculator, failing_tool, text_analyzer])

    # Query that will trigger the failing tool
    error_query = """
    Please:
    1. Calculate 10 + 20
    2. Use the failing tool on "test input"
    3. Analyze this text: "Error handling is important"

    Provide results even if some tasks fail.
    """

    result = await agent.arun(error_query)

    # Show failed tasks
    failed_tasks = result.get_failed_tasks()
    if failed_tasks:
        for _failed in failed_tasks:
            pass

    return result


def main():
    """Run all examples."""
    # Run examples
    asyncio.run(basic_llm_compiler_example())

    asyncio.run(parallel_efficiency_demo())

    asyncio.run(error_handling_demo())


if __name__ == "__main__":
    main()
