#!/usr/bin/env python3
"""Simple Branching Demo - Working V3/V4 Branching with Structured Output.

This simplified demo shows the core branching concepts:
1. Classifier produces structured output
2. Router uses structured output to choose next agent
3. Different specialized agents handle different cases
4. All use V3/V4 architecture consistently
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models
class TaskType(BaseModel):
    """Simple task classification."""

    category: str = Field(description="creative, technical, or general")
    confidence: float = Field(ge=0.0, le=1.0)


class ProcessingResult(BaseModel):
    """Result from specialized processing."""

    output: str = Field(description="Processed output")
    approach: str = Field(description="Processing approach used")
    quality_score: float = Field(ge=0.0, le=1.0)


async def main():
    """Demonstrate simple branching with structured output."""
    # Step 1: Create classifier
    classifier = SimpleAgentV3(
        name="classifier",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="Classify tasks into categories.",
            structured_output_model=TaskType,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [("system", "{system_message}"), ("human", "Classify this task: {task}")]
        ),
    )

    # Step 2: Create specialized processors
    creative_agent = SimpleAgentV3(
        name="creative_processor",
        engine=AugLLMConfig(
            temperature=0.8,
            system_message="Handle creative tasks with imagination.",
            structured_output_model=ProcessingResult,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [("system", "{system_message}"), ("human", "Process creatively: {task}")]
        ),
    )

    technical_agent = SimpleAgentV3(
        name="technical_processor",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="Handle technical tasks with precision.",
            structured_output_model=ProcessingResult,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [("system", "{system_message}"), ("human", "Process technically: {task}")]
        ),
    )

    general_agent = SimpleAgentV3(
        name="general_processor",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message="Handle general tasks efficiently.",
            structured_output_model=ProcessingResult,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [("system", "{system_message}"), ("human", "Process generally: {task}")]
        ),
    )

    # Step 3: Test individual components first
    test_tasks = [
        "Write a poem about robots",
        "Design a REST API for user management",
        "Explain quantum computing",
    ]

    for _i, task in enumerate(test_tasks, 1):
        # Test classifier
        classification_input = {
            "task": task,
            "messages": [HumanMessage(content=f"Classify: {task}")],
        }

        try:
            classification_result = await classifier.arun(classification_input)

            if isinstance(classification_result, dict) and "category" in classification_result:
                category = classification_result["category"]
                classification_result.get("confidence", 0.0)

                # Route to appropriate processor
                if category == "creative":
                    processor = creative_agent
                elif category == "technical":
                    processor = technical_agent
                else:
                    processor = general_agent

                # Process with selected agent
                processing_input = {
                    "task": task,
                    "messages": [HumanMessage(content=f"Process: {task}")],
                }

                processing_result = await processor.arun(processing_input)

                if isinstance(processing_result, dict):
                    processing_result.get("approach", "N/A")
                    processing_result.get("quality_score", 0.0)
                    processing_result.get("output", "")[:100]

            else:
                pass

        except Exception:
            pass


if __name__ == "__main__":
    asyncio.run(main())
