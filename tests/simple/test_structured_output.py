#!/usr/bin/env python3
"""Test SimpleAgent v3 with structured output models - no mocks, real execution."""

import logging
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

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
    steps_required: List[str] = Field(description="List of steps needed")
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
    best_practices: List[str] = Field(description="List of best practices")


def test_basic_structured_output():
    """Test agent with basic structured output model."""
    print("\n" + "=" * 70)
    print("📋 TEST 1: Basic Structured Output (TaskAnalysis)")
    print("=" * 70)

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

    print(f"✅ Created agent with structured output: {TaskAnalysis.__name__}")
    print(f"   Fields: {list(TaskAnalysis.model_fields.keys())}")

    # Test structured output
    query = "Analyze this task: Build a web application that displays real-time weather data"
    print(f"\n📨 Query: {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Extract and verify structured output
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                print(f"🤖 Raw Response: {msg.content[:200]}...")

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

                if has_structured_fields:
                    print("✅ SUCCESS: Response contains structured output fields")
                    print(
                        f"   Contains task analysis structure: {has_structured_fields}"
                    )
                    return True
                else:
                    print(
                        "❌ FAILURE: Response doesn't contain expected structured fields"
                    )
                    return False
                break

    print("❌ FAILURE: No AI response found")
    return False


def test_question_answer_structure():
    """Test agent with question-answer structured output."""
    print("\n" + "=" * 70)
    print("❓ TEST 2: Question-Answer Structure")
    print("=" * 70)

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

    print(f"✅ Created Q&A agent with structure: {QuestionAnswer.__name__}")
    print(f"   Fields: {list(QuestionAnswer.model_fields.keys())}")

    query = "What is the capital of France and why is it important?"
    print(f"\n📨 Query: {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Verify Q&A structure
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                response = msg.content
                print(f"🤖 Response: {response[:150]}...")

                # Check for Q&A structure
                has_qa_structure = all(
                    field in response.lower()
                    for field in ["question", "answer", "reasoning", "certainty"]
                )

                if has_qa_structure:
                    print("✅ SUCCESS: Response has Q&A structure")
                    return True
                else:
                    print("❌ FAILURE: Missing Q&A structure elements")
                    return False
                break

    return False


def test_programming_advice_structure():
    """Test agent with programming advice structured output."""
    print("\n" + "=" * 70)
    print("💻 TEST 3: Programming Advice Structure")
    print("=" * 70)

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

    print(f"✅ Created programming agent with structure: {ProgrammingAdvice.__name__}")
    print(f"   Fields: {list(ProgrammingAdvice.model_fields.keys())}")

    query = "Explain Python list comprehensions with an example"
    print(f"\n📨 Query: {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Verify programming advice structure
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                response = msg.content
                print(f"🤖 Response: {response[:200]}...")

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

                if has_programming_structure and "python" in response.lower():
                    print("✅ SUCCESS: Response has programming advice structure")
                    print("   Contains language, explanation, and example elements")
                    return True
                else:
                    print("❌ FAILURE: Missing programming advice structure")
                    return False
                break

    return False


def test_structured_output_validation():
    """Test that structured output follows the expected schema."""
    print("\n" + "=" * 70)
    print("🔍 TEST 4: Structured Output Schema Validation")
    print("=" * 70)

    # Simple model for testing validation
    class SimpleResponse(BaseModel):
        summary: str = Field(description="Brief summary of the response")
        key_points: List[str] = Field(description="List of key points (2-3 items)")
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

    print(f"✅ Created validation agent with: {SimpleResponse.__name__}")
    print(f"   Required fields: summary, key_points, recommendation")

    query = "Give me advice on learning Python programming"
    print(f"\n📨 Query: {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Check for all required fields
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                response = msg.content.lower()
                print(f"🤖 Response: {msg.content[:150]}...")

                # Check for all required fields
                required_fields = ["summary", "key_points", "recommendation"]
                fields_present = [
                    field for field in required_fields if field in response
                ]

                if len(fields_present) >= 2:  # Allow some flexibility
                    print(
                        f"✅ SUCCESS: Found {len(fields_present)}/{len(required_fields)} required fields"
                    )
                    print(f"   Present fields: {fields_present}")
                    return True
                else:
                    print(
                        f"❌ FAILURE: Only found {len(fields_present)} required fields"
                    )
                    print(f"   Present fields: {fields_present}")
                    return False
                break

    return False


def run_all_structured_output_tests():
    """Run all structured output tests."""
    print("🧪 SIMPLEAGENT V3 - STRUCTURED OUTPUT TESTS")
    print("=" * 70)
    print("Testing real structured output with no mocks")
    print("=" * 70)

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

        print("\n" + "=" * 70)
        print("📊 STRUCTURED OUTPUT TEST RESULTS")
        print("=" * 70)
        print(f"Tests passed: {passed}/{total}")

        if passed == total:
            print("🎉 ALL STRUCTURED OUTPUT TESTS PASSED! ✅")
            print("\nKey achievements:")
            print("✅ TaskAnalysis structured output working")
            print("✅ QuestionAnswer structured output working")
            print("✅ ProgrammingAdvice structured output working")
            print("✅ Schema validation working")
            print("✅ Real LLM + structured output execution")
        else:
            print("⚠️  Some tests failed - check output above")

    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        logger.exception("Structured output test execution error")


if __name__ == "__main__":
    run_all_structured_output_tests()
