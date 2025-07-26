"""Correct way to get structured output from SimpleAgent."""

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


async def test_structured_output_extraction():
    """Test proper extraction of structured output from SimpleAgent."""
    print("\n=== Structured Output Extraction ===\n")

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

    # Run agent with debug=True
    print("Running agent with debug=True...")
    result = await agent.arun({"task": "prepare for a job interview"}, debug=True)

    print(f"\n1. Raw result type: {type(result)}")

    # Method 1: Use get_latest_structured_output()
    if hasattr(result, "get_latest_structured_output"):
        structured_msg = result.get_latest_structured_output()
        print(f"\n2. Structured output message: {structured_msg}")

        if structured_msg and hasattr(structured_msg, "content"):
            # Parse the content as our model
            import json

            try:
                if isinstance(structured_msg.content, str):
                    data = json.loads(structured_msg.content)
                else:
                    data = structured_msg.content

                todo_list = TodoList(**data)
                print("\n✅ Successfully extracted TodoList:":")
                print(f"   Title: {todo_list.title}")
                print(f"   Priority: {todo_list.priority}")
                print(f"   Hours: {todo_list.estimated_hours}")
                print(f"   Items ({len(todo_list.items)}):")
                for item in todo_list.items:
                    print(f"     • {item}")
            except Exception as e:
                print(f"Error parsing structured output: {e}")

    # Method 2: Check the last AI message for tool calls
    if hasattr(result, "get_last_ai_message"):
        last_ai_msg = result.get_last_ai_message()
        if (
            last_ai_msg
            and hasattr(last_ai_msg, "tool_calls")
            and last_ai_msg.tool_calls
        ):
            print(f"\n3. Tool calls found: {len(last_ai_msg.tool_calls)}")
            for tool_call in last_ai_msg.tool_calls:
                if isinstance(tool_call, dict):
                    func = tool_call.get("function", tool_call)
                    if func.get("name") == "TodoList":
                        import json

                        args = func.get("arguments", func.get("args", {}))
                        if isinstance(args, str):
                            args = json.loads(args)

                        todo_list = TodoList(**args)
                        print("\n✅ Extracted from tool call:":")
                        print(f"   Title: {todo_list.title}")
                        print(f"   Items: {todo_list.items}")
                        break

    # Method 3: Check for parsed tool calls
    if hasattr(result, "get_parsed_tool_calls"):
        parsed_calls = result.get_parsed_tool_calls()
        print(f"\n4. Parsed tool calls: {len(parsed_calls) if parsed_calls else 0}")


# Helper function to extract structured output
def extract_structured_output(agent_result, model_class):
    """Generic helper to extract structured output from agent result."""
    # Try get_latest_structured_output first
    if hasattr(agent_result, "get_latest_structured_output"):
        structured_msg = agent_result.get_latest_structured_output()
        if structured_msg and hasattr(structured_msg, "content"):
            import json

            content = structured_msg.content
            if isinstance(content, str):
                content = json.loads(content)
            return model_class(**content)

    # Try last AI message tool calls
    if hasattr(agent_result, "get_last_ai_message"):
        last_ai = agent_result.get_last_ai_message()
        if last_ai and hasattr(last_ai, "tool_calls"):
            for tool_call in last_ai.tool_calls or []:
                if isinstance(tool_call, dict):
                    func = tool_call.get("function", tool_call)
                    if func.get("name") == model_class.__name__:
                        import json

                        args = func.get("arguments", func.get("args", {}))
                        if isinstance(args, str):
                            args = json.loads(args)
                        return model_class(**args)

    return None


async def test_with_helper():
    """Test using the helper function."""
    print("\n\n=== Using Helper Function ===\n")

    # Create agent
    agent = SimpleAgent(
        name="planner",
        engine=AugLLMConfig(
            structured_output_model=TodoList, structured_output_version="v2"
        ),
    )

    # Run and extract with debug=True
    result = await agent.arun("Plan a weekend trip to the mountains", debug=True)
    todo_list = extract_structured_output(result, TodoList)

    if todo_list:
        print("✅ Extracted TodoList using helper:":")
        print(f"   Title: {todo_list.title}")
        print(f"   Priority: {todo_list.priority}")
        print(f"   Total Hours: {todo_list.estimated_hours}")
        print("   Todo Items:")
        for item in todo_list.items:
            print(f"     • {item}")
    else:
        print("❌ Could not extract structured output")


async def main():
    await test_structured_output_extraction()
    await test_with_helper()


if __name__ == "__main__":
    asyncio.run(main())
