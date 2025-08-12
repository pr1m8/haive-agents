"""Direct example of getting structured output from SimpleAgent."""

import asyncio

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Simple structured output model
class TaskList(BaseModel):
    """A simple task list."""

    tasks: list[str] = Field(description="List of tasks")
    priority: str = Field(description="Overall priority level")
    total_hours: float = Field(description="Total estimated hours")


async def test_direct_structured():
    """Test getting structured output directly from SimpleAgent."""
    print("\n=== Direct Structured Output ===\n")

    # Simple prompt
    prompt = ChatPromptTemplate.from_messages(
        [("system", "You are a task planner."), ("human", "Plan tasks for: {request}")]
    )

    # Create agent with structured output
    agent = SimpleAgent(
        name="task_planner",
        engine=AugLLMConfig(
            prompt_template=prompt,
            structured_output_model=TaskList,
            structured_output_version="v2",
        ),
    )

    # Run agent
    result = await agent.arun({"request": "organize a birthday party"})

    # The result is the agent state - we need to extract the structured output
    print(f"Result type: {type(result)}")
    print(f"Result keys: {result.keys() if hasattr(result, 'keys') else 'N/A'}")

    # Get the actual structured output from the state
    if hasattr(result, "messages") and result.messages:
        last_message = result.messages[-1]
        print(f"\nLast message type: {type(last_message)}")

        # Check for tool calls (structured output)
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            for tool_call in last_message.tool_calls:
                print(f"\nTool call: {tool_call}")
                # The structured output is in the tool call
                if isinstance(tool_call, dict) and "function" in tool_call:
                    import json

                    args = tool_call["function"].get("arguments", {})
                    if isinstance(args, str):
                        args = json.loads(args)

                    # Create the structured object
                    task_list = TaskList(**args)

                    print("\n✅ Structured Output Extracted:")
                    print(f"Tasks: {task_list.tasks}")
                    print(f"Priority: {task_list.priority}")
                    print(f"Total Hours: {task_list.total_hours}")
                    break

    # Alternative: Check if there's a direct output field
    if hasattr(result, "task_list"):
        print(f"\nDirect task_list: {result.task_list}")


if __name__ == "__main__":
    asyncio.run(test_direct_structured())
