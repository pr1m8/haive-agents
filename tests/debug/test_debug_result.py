"""Debug what SimpleAgent returns."""

import asyncio

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Simple structured output model
class TodoList(BaseModel):
    """A todo list with items."""

    title: str = Field(description="Title of the todo list")
    items: list[str] = Field(description="List of todo items", min_items=3, max_items=8)
    priority: str = Field(description="Overall priority", pattern="^(high|medium|low)$")
    estimated_hours: float = Field(description="Total estimated hours")


async def debug_result():
    """Debug what agent.arun returns."""
    print("\n=== Debugging SimpleAgent Result ===\n")

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
    print(f"2. Result dict? {isinstance(result, dict)}")
    print(f"3. Result dir: {[x for x in dir(result) if not x.startswith('_')][:10]}")

    # Check if it's dict-like
    if hasattr(result, "keys"):
        print(f"\n4. Result keys: {list(result.keys())}")

        # Check for messages
        if "messages" in result:
            messages = result["messages"]
            print(f"\n5. Messages found: {len(messages)} messages")

            # Look at last message
            if messages:
                last_msg = messages[-1]
                print(f"6. Last message type: {type(last_msg)}")
                print(f"7. Last message has tool_calls: {hasattr(last_msg, 'tool_calls')}")

                if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
                    print(f"8. Tool calls: {last_msg.tool_calls}")

                    # Extract structured output
                    for tool_call in last_msg.tool_calls:
                        if isinstance(tool_call, dict) and tool_call.get("name") == "TodoList":
                            import json

                            args = tool_call.get("args", {})
                            if isinstance(args, str):
                                args = json.loads(args)

                            todo_list = TodoList(**args)
                            print("\n✅ Successfully extracted TodoList:")
                            print(f"   Title: {todo_list.title}")
                            print(f"   Priority: {todo_list.priority}")
                            print(f"   Hours: {todo_list.estimated_hours}")
                            print("   Items:")
                            for item in todo_list.items:
                                print(f"     • {item}")
                            break

    # Try to access as object
    if hasattr(result, "messages"):
        print("\n9. Result has messages attribute")
        print(f"   Messages: {result.messages}")


if __name__ == "__main__":
    asyncio.run(debug_result())
