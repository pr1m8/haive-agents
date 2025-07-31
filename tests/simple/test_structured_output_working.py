"""Working example of extracting structured output from SimpleAgent."""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent


# Simple structured output model
class TodoList(BaseModel):
    """A todo list with items."""

    title: str = Field(description="Title of the todo list")
    items: List[str] = Field(description="List of todo items", min_items=3, max_items=8)
    priority: str = Field(description="Overall priority", pattern="^(high|medium|low)$")
    estimated_hours: float = Field(description="Total estimated hours")


def extract_structured_output_from_messages(messages, model_class):
    """Extract structured output from message list."""
    # Look for AI messages with tool calls
    for msg in reversed(messages):
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for tool_call in msg.tool_calls:
                if isinstance(tool_call, dict):
                    # Check if it's our model
                    if tool_call.get("name") == model_class.__name__:
                        import json

                        args = tool_call.get("args", {})
                        if isinstance(args, str):
                            args = json.loads(args)
                        return model_class(**args)

                    # Handle OpenAI format
                    elif "function" in tool_call:
                        func = tool_call["function"]
                        if func.get("name") == model_class.__name__:
                            args = func.get("arguments", {})
                            if isinstance(args, str):
                                args = json.loads(args)
                            return model_class(**args)
    return None


async def test_structured_output():
    """Test getting structured output from SimpleAgent."""
    print("\n=== Structured Output Extraction (Working) ===\n")

    # Create prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful task planner."),
            ("human", "Create a todo list for: {task}"),
        ]
    )

    # Create agent with structured output
    agent = SimpleAgent(
        name="todo_planner",
        engine=AugLLMConfig(
            prompt_template=prompt,
            structured_output_model=TodoList,
            structured_output_version="v2",
            temperature=0.7,
        ),
    )

    # Run agent
    print("Running agent...")
    result = await agent.arun({"task": "prepare for a job interview"})

    print(f"\n1. Result type: {type(result)}")
    print(f"2. Result has messages: {hasattr(result, 'messages')}")

    # Extract structured output from messages
    if hasattr(result, "messages"):
        print(f"3. Number of messages: {len(result.messages)}")

        # Extract structured output
        todo_list = extract_structured_output_from_messages(result.messages, TodoList)

        if todo_list:
            print("\n✅ Successfully extracted TodoList:")
            print(f"   Title: {todo_list.title}")
            print(f"   Priority: {todo_list.priority}")
            print(f"   Hours: {todo_list.estimated_hours}")
            print(f"   Items ({len(todo_list.items)}):")
            for item in todo_list.items:
                print(f"     • {item}")
        else:
            print("\n❌ Could not extract structured output")

            # Debug: Show last AI message
            for msg in reversed(result.messages):
                if hasattr(msg, "tool_calls"):
                    print(
                        f"\nDebug - Found AI message with tool_calls: {msg.tool_calls}"
                    )
                    break


async def test_multiple_examples():
    """Test multiple structured output examples."""
    print("\n\n=== Multiple Examples ===\n")

    # Define another model
    class ProjectPlan(BaseModel):
        """A project plan."""

        name: str = Field(description="Project name")
        phases: List[str] = Field(
            description="Project phases", min_items=2, max_items=5
        )
        duration_weeks: int = Field(description="Total duration in weeks", ge=1, le=52)
        budget: float = Field(description="Budget in thousands", ge=0)

    # Test different models
    test_cases = [
        {
            "model": TodoList,
            "prompt": "Create a todo list for: {task}",
            "input": {"task": "organize a birthday party"},
            "name": "todo_agent",
        },
        {
            "model": ProjectPlan,
            "prompt": "Create a project plan for: {project}",
            "input": {"project": "building a mobile app"},
            "name": "project_agent",
        },
    ]

    for test_case in test_cases:
        print(f"\n--- Testing {test_case['model'].__name__} ---")

        # Create prompt
        prompt = ChatPromptTemplate.from_messages(
            [("system", "You are a helpful assistant."), ("human", test_case["prompt"])]
        )

        # Create agent
        agent = SimpleAgent(
            name=test_case["name"],
            engine=AugLLMConfig(
                prompt_template=prompt,
                structured_output_model=test_case["model"],
                structured_output_version="v2",
            ),
        )

        # Run agent
        result = await agent.arun(test_case["input"])

        # Extract output
        if hasattr(result, "messages"):
            output = extract_structured_output_from_messages(
                result.messages, test_case["model"]
            )

            if output:
                print(f"✅ Extracted {test_case['model'].__name__}:")
                for field, value in output.model_dump().items():
                    if isinstance(value, list):
                        print(f"   {field}: {len(value)} items")
                        for item in value:
                            print(f"     • {item}")
                    else:
                        print(f"   {field}: {value}")
            else:
                print(f"❌ Failed to extract {test_case['model'].__name__}")


async def main():
    await test_structured_output()
    await test_multiple_examples()


if __name__ == "__main__":
    asyncio.run(main())
