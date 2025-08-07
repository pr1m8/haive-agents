"""Debug multi-agent execution to understand state flow."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


class SimpleOutput(BaseModel):
    """Simple structured output."""

    response: str = Field(description="Agent response")
    agent_name: str = Field(description="Name of responding agent")


async def debug_execution():
    """Debug multi-agent execution."""

    print("Creating agents with structured output...")

    # Create agents with structured output
    agent1 = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.1,
            max_tokens=100,
            system_message="You are an analyzer. Provide a brief analysis.",
        ),
        structured_output_model=SimpleOutput,
        debug=True,
    )

    agent2 = SimpleAgentV3(
        name="summarizer",
        engine=AugLLMConfig(
            temperature=0.1,
            max_tokens=100,
            system_message="You are a summarizer. Summarize the analysis.",
        ),
        structured_output_model=SimpleOutput,
        debug=True,
    )

    print("\nCreating workflow...")
    workflow = EnhancedMultiAgentV4(
        name="debug_workflow", agents=[agent1, agent2], execution_mode="sequential"
    )

    # Input
    input_state = {"messages": [HumanMessage(content="Analyze the weather today.")]}

    print("\n=== INPUT STATE ===")
    print(f"Type: {type(input_state)}")
    print(f"Keys: {list(input_state.keys())}")
    print(f"Messages: {len(input_state['messages'])}")

    # Execute
    print("\n=== EXECUTING WORKFLOW ===")
    result = await workflow.arun(input_state)

    print("\n=== OUTPUT STATE ===")
    print(f"Type: {type(result).__name__}")
    print(f"Result class: {result.__class__}")

    # Check state fields
    print("\n=== STATE ANALYSIS ===")

    # Messages
    if hasattr(result, "messages"):
        print(f"\nMessages ({len(result.messages)}):")
        for i, msg in enumerate(result.messages):
            print(f"  [{i}] {type(msg).__name__}: {msg.content[:50]}...")

    # Agent outputs
    if hasattr(result, "agent_outputs"):
        print(f"\nAgent outputs: {list(result.agent_outputs.keys())}")
        for agent, output in result.agent_outputs.items():
            print(f"  {agent}: {str(output)[:100]}...")

    # Structured output fields
    print("\nStructured output fields:")
    for field_name in ["analyzer", "summarizer"]:
        if hasattr(result, field_name):
            field_value = getattr(result, field_name)
            print(f"  {field_name}: {field_value}")
        else:
            print(f"  {field_name}: NOT FOUND")

    # Agent states
    if hasattr(result, "agent_states"):
        print(f"\nAgent states: {list(result.agent_states.keys())}")
        for agent, state in result.agent_states.items():
            print(f"  {agent}: {len(state)} fields")

    # Execution tracking
    if hasattr(result, "agent_execution_order"):
        print(f"\nExecution order: {result.agent_execution_order}")

    if hasattr(result, "active_agent"):
        print(f"Active agent: {result.active_agent}")

    # Debug info
    if hasattr(result, "display_debug_info"):
        print("\n=== DETAILED DEBUG INFO ===")
        result.display_debug_info("Final State")


if __name__ == "__main__":
    print("Debug Multi-Agent Execution")
    print("=" * 50)
    asyncio.run(debug_execution())
