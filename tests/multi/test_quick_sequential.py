#!/usr/bin/env python3
"""Simple Sequential Multi-Agent Test

Minimal test of sequential execution without tools to isolate the issue.
"""

import asyncio
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage

from haive.agents.simple.agent import SimpleAgent
from haive.agents.multi.agent import MultiAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Define structured output models
class Analysis(BaseModel):
    """Analysis from first agent."""
    topic: str = Field(description="Topic being analyzed")
    key_points: list[str] = Field(description="Key points discovered")
    
class Report(BaseModel):
    """Final report from second agent."""
    title: str = Field(description="Report title")
    summary: str = Field(description="Executive summary")
    recommendations: list[str] = Field(description="Action items")


async def main():
    print("=== Simple Sequential Multi-Agent Test ===\n")
    
    # Create first agent - analyzer
    analyzer = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(
            structured_output_model=Analysis,
            temperature=0.7,
            system_message="You are an analyst. Analyze the topic and provide key insights."
        )
    )
    
    # Create second agent - report writer  
    reporter = SimpleAgent(
        name="reporter",
        engine=AugLLMConfig(
            structured_output_model=Report,
            temperature=0.5,
            system_message="You are a report writer. Create an executive report from the analysis."
        )
    )
    
    # Create sequential workflow
    workflow = MultiAgent(
        name="analysis_workflow",
        agents=[analyzer, reporter],
        execution_mode="sequential"
    )
    
    # Execute
    task = "Analyze the impact of AI on healthcare in 2025"
    print(f"Task: {task}\n")
    
    result = await workflow.arun({
        "messages": [HumanMessage(content=task)]
    })
    
    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    
    # Check for structured outputs
    if hasattr(result, 'agent_outputs'):
        print("\nAgent Outputs:")
        for agent_name, output in result.agent_outputs.items():
            print(f"\n{agent_name}:")
            print(output)
            
    # Check messages
    if hasattr(result, 'messages'):
        print(f"\nTotal messages: {len(result.messages)}")
        for i, msg in enumerate(result.messages[-3:]):  # Last 3 messages
            print(f"\nMessage {i}: {type(msg).__name__}")
            if hasattr(msg, 'content'):
                print(f"Content: {msg.content[:200]}...")
            if hasattr(msg, 'additional_kwargs') and 'parsed' in msg.additional_kwargs:
                print(f"Parsed: {msg.additional_kwargs['parsed']}")


if __name__ == "__main__":
    asyncio.run(main())