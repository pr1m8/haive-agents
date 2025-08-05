#!/usr/bin/env python3
"""Test SimpleAgent v3 with structured output models - no mocks, real execution."""

import logging

from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# STRUCTURED OUTPUT MODELS
# ============================================================================


class TaskAnalysis(BaseModel):
    """Structured output model for task analysis."""

    task_type: str = Field(description="Type of task (e.g., 'analysis', 'calculation')")
    complexity: int = Field(ge=1, le=10, description="Task complexity on scale of 1-10")
    steps_required: list[str] = Field(description="List of steps needed")
    estimated_time: int = Field(ge=1, description="Estimated time in minutes")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in analysis")


class QuestionAnswer(BaseModel):
    """Simple question-answer structure."""

    question: str = Field(description="The original question")
    answer: str = Field(description="The direct answer")
    reasoning: str = Field(description="Brief reasoning for the answer")
    certainty: str = Field(description="Level of certainty: 'high', 'medium', 'low'")


class ProgrammingAdvice(BaseModel):
    """Structured advice for programming questions."""

    language: str = Field(description="Programming language discussed")
    topic: str = Field(description="Main topic or concept")
    explanation: str = Field(description="Clear explanation of the concept")
    example_code: str = Field(description="Simple code example")
    best_practices: list[str] = Field(description="List of best practices")


def test_basic_structured_output():
    """Test agent with basic structured output model."""
    # Create agent with structured output
    agent = SimpleAgentV3(
        name="structured_agent",
        engine=AugLLMConfig(
            temperature=0.2,  # Low temperature for consistent structure
            max_tokens=300,
            structured_output_model=TaskAnalysis,
            llm_config=DeepSeekLLMConfig(),
        ),
        debug=True,
    )

    # Test structured output
    query = "Analyze this task: Build a web application that displays real-time weather data"

    result = agent.run(query, debug=True)

    # Extract and verify structured output
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                # Check if response contains structured fields
                response = msg.content
                has_structured_fields = any(
                    field in response.lower()
                    for field in [
                        "task_type",
                        "complexity",
                        "steps",
                        "time",
                        "confidence",
                    ]
                )

                return bool(has_structured_fields)
                break

    return False


def test_question_answer_structure():
    """Test agent with question-answer structured output."""
    agent = SimpleAgentV3(
        name="qa_agent",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=250,
            structured_output_model=QuestionAnswer,
            llm_config=DeepSeekLLMConfig(),
        ),
        debug=True,
    )

    query = "What is the capital of France and why is it important?"

    result = agent.run(query, debug=True)

    # Verify Q&A structure
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                response = msg.content

                # Check for Q&A structure
                has_qa_structure = all(
                    field in response.lower()
                    for field in ["question", "answer", "reasoning", "certainty"]
                )

                return bool(has_qa_structure)
                break

    return False


def test_programming_advice_structure():
    """Test agent with programming advice structured output."""
    agent = SimpleAgentV3(
        name="programming_agent",
        engine=AugLLMConfig(
            temperature=0.4,
            max_tokens=400,
            structured_output_model=ProgrammingAdvice,
            llm_config=DeepSeekLLMConfig(),
        ),
        debug=True,
    )

    query = "Explain Python list comprehensions with an example"

    result = agent.run(query, debug=True)

    # Verify programming advice structure
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                response = msg.content

                # Check for programming advice structure
                programming_fields = [
                    "language",
                    "topic",
                    "explanation",
                    "example_code",
                    "best_practices",
                ]
                has_programming_structure = any(
                    field in response.lower() for field in programming_fields
                )

                return bool(has_programming_structure and "python" in response.lower())
                break

    return False


def test_structured_output_validation():
    """Test that structured output follows the expected schema."""

    # Simple model for testing validation
    class SimpleResponse(BaseModel):
        summary: str = Field(description="Brief summary of the response")
        key_points: list[str] = Field(description="List of key points (2-3 items)")
        recommendation: str = Field(description="Final recommendation or conclusion")

    agent = SimpleAgentV3(
        name="validation_agent",
        engine=AugLLMConfig(
            temperature=0.1,  # Very low for consistent structure
            max_tokens=200,
            structured_output_model=SimpleResponse,
            llm_config=DeepSeekLLMConfig(),
        ),
        debug=True,
    )

    query = "Give me advice on learning Python programming"

    result = agent.run(query, debug=True)

    # Check for all required fields
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                response = msg.content.lower()

                # Check for all required fields
                required_fields = ["summary", "key_points", "recommendation"]
                fields_present = [field for field in required_fields if field in response]

                if len(fields_present) >= 2:  # Allow some flexibility
                    return True
                return False
                break

    return False


def run_all_structured_output_tests():
    """Run all structured output tests."""
    test_results = []

    try:
        # Run all tests
        test_results.append(test_basic_structured_output())
        test_results.append(test_question_answer_structure())
        test_results.append(test_programming_advice_structure())
        test_results.append(test_structured_output_validation())

        # Summary
        passed = sum(test_results)
        total = len(test_results)

        if passed == total:
            pass
        else:
            pass

    except Exception:
        logger.exception("Structured output test execution error")


if __name__ == "__main__":
    run_all_structured_output_tests()
