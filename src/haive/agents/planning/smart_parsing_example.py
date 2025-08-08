"""Smart Output Parsing Integration Example for Planning Agents.

This example demonstrates how to use smart output parsing with post-hooks
to handle different types of agent outputs intelligently.
"""

import asyncio
import logging
from typing import Any, Dict

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.agents.base.smart_output_parsing import (
    SmartOutputParsingMixin,
    create_smart_engine_node,
    create_smart_parsing_callable,
    detect_content_type,
    parse_json_content,
    parse_structured_content,
)
from haive.agents.multi.agent import MultiAgent
from haive.agents.planning.base.agents.executor import BaseExecutorAgent
from haive.agents.planning.base.agents.planner import BasePlannerAgent
from haive.agents.planning.base.models import BasePlan, ExecutionResult, PlanContent

logger = logging.getLogger(__name__)


# Enhanced agents with smart output parsing capabilities


class SmartPlannerAgent(SmartOutputParsingMixin, BasePlannerAgent):
    """BasePlannerAgent enhanced with smart output parsing."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("SmartPlannerAgent initialized with smart output parsing")


class SmartExecutorAgent(SmartOutputParsingMixin, BaseExecutorAgent):
    """BaseExecutorAgent enhanced with smart output parsing."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("SmartExecutorAgent initialized with smart output parsing")


class SmartSimpleAgent(SmartOutputParsingMixin, SimpleAgentV3):
    """SimpleAgentV3 enhanced with smart output parsing."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("SmartSimpleAgent initialized with smart output parsing")


# Example models for different parsing scenarios


class TaskAnalysis(BaseModel):
    """Model for task analysis output."""

    complexity: str = Field(..., description="Task complexity: simple, medium, complex")
    estimated_time: str = Field(..., description="Estimated completion time")
    required_tools: list[str] = Field(default_factory=list, description="Tools needed")
    risk_factors: list[str] = Field(default_factory=list, description="Potential risks")


class ProgressReport(BaseModel):
    """Model for progress reporting."""

    completed_steps: int = Field(..., description="Number of completed steps")
    total_steps: int = Field(..., description="Total number of steps")
    current_status: str = Field(..., description="Current status description")
    next_actions: list[str] = Field(
        default_factory=list, description="Next actions to take"
    )


class DecisionPoint(BaseModel):
    """Model for decision points in workflow."""

    decision_type: str = Field(..., description="Type of decision needed")
    options: list[str] = Field(..., description="Available options")
    recommendation: str = Field(..., description="Recommended choice")
    reasoning: str = Field(..., description="Reasoning for recommendation")


# Smart parsing workflow examples


async def create_smart_planning_workflow():
    """Create a planning workflow with smart output parsing."""

    # Configuration for different agents
    planner_config = AugLLMConfig(
        model="gpt-4o-mini",
        temperature=0.3,
        system_message="You are an expert strategic planner. Always respond with structured JSON when possible.",
    )

    executor_config = AugLLMConfig(
        model="gpt-4o-mini",
        temperature=0.1,
        system_message="You are a skilled executor. Provide detailed execution reports in structured format.",
    )

    analyzer_config = AugLLMConfig(
        model="gpt-4o-mini",
        temperature=0.5,
        system_message="You are an expert task analyzer. Analyze tasks and provide structured analysis.",
    )

    # Create smart agents with output parsing
    smart_planner = SmartPlannerAgent(name="smart_planner", engine=planner_config)

    smart_executor = SmartExecutorAgent(name="smart_executor", engine=executor_config)

    smart_analyzer = SmartSimpleAgent(name="smart_analyzer", engine=analyzer_config)

    # Add custom parsing hooks for specific models
    smart_analyzer._output_parsing_hooks["task_analysis"] = (
        lambda ctx: _parse_task_analysis(ctx)
    )
    smart_executor._output_parsing_hooks["progress_report"] = (
        lambda ctx: _parse_progress(ctx)
    )

    # Create the multi-agent workflow
    workflow = MultiAgent(
        name="smart_parsing_workflow",
        agents=[smart_analyzer, smart_planner, smart_executor],
        execution_mode="sequential",
        build_mode="auto",
    )

    return workflow


def _parse_task_analysis(context) -> TaskAnalysis | None:
    """Custom parser for task analysis output."""
    try:
        if hasattr(context.result, "content"):
            import json

            content = context.result.content
            # Try to extract JSON from content
            if "{" in content and "}" in content:
                # Extract JSON part
                start = content.find("{")
                end = content.rfind("}") + 1
                json_str = content[start:end]

                data = json.loads(json_str)
                return TaskAnalysis.model_validate(data)
    except Exception as e:
        logger.debug(f"Task analysis parsing failed: {e}")
    return None


def _parse_progress(context) -> ProgressReport | None:
    """Custom parser for progress report output."""
    try:
        if hasattr(context.result, "content"):
            import json
            import re

            content = context.result.content

            # Look for structured data patterns
            completed_match = re.search(r"completed.*?(\d+)", content, re.IGNORECASE)
            total_match = re.search(r"total.*?(\d+)", content, re.IGNORECASE)

            if completed_match and total_match:
                return ProgressReport(
                    completed_steps=int(completed_match.group(1)),
                    total_steps=int(total_match.group(1)),
                    current_status="In progress",
                    next_actions=["Continue execution"],
                )
    except Exception as e:
        logger.debug(f"Progress parsing failed: {e}")
    return None


# Advanced smart parsing with callable nodes


def create_adaptive_parsing_workflow():
    """Create workflow with adaptive parsing based on content detection."""

    # Create content type detection callable
    content_detector = create_smart_parsing_callable(
        name="content_detector",
        parsing_functions={
            "json": parse_json_content,
            "structured": parse_structured_content,
            "task_analysis": _parse_task_analysis_callable,
            "progress": _parse_progress_callable,
        },
        detection_function=_enhanced_content_detection,
        goto_mapping={
            "json": "json_processor",
            "structured": "structured_processor",
            "task_analysis": "analysis_processor",
            "progress": "progress_processor",
        },
        default_goto="text_processor",
    )

    return content_detector


def _enhanced_content_detection(state) -> str:
    """Enhanced content detection for different parsing strategies."""
    messages = getattr(state, "messages", [])
    if not messages:
        return "empty"

    last_message = messages[-1]

    # Check for tool calls first
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "structured"

    content = getattr(last_message, "content", "").lower()

    # Look for specific patterns
    if any(
        word in content for word in ["complexity", "estimated_time", "risk_factors"]
    ):
        return "task_analysis"
    elif any(word in content for word in ["completed", "progress", "steps"]):
        return "progress"
    elif content.strip().startswith("{") and "json" in content:
        return "json"
    elif content.strip().startswith("["):
        return "list"
    else:
        return "text"


def _parse_task_analysis_callable(state) -> Dict[str, Any]:
    """Callable version of task analysis parser."""
    try:
        messages = getattr(state, "messages", [])
        if messages:
            content = getattr(messages[-1], "content", "")

            # Simple pattern matching for demo
            analysis = {
                "complexity": "medium",
                "estimated_time": "2-3 hours",
                "required_tools": [],
                "risk_factors": [],
            }

            if "complex" in content.lower():
                analysis["complexity"] = "complex"
                analysis["estimated_time"] = "4-6 hours"
            elif "simple" in content.lower():
                analysis["complexity"] = "simple"
                analysis["estimated_time"] = "30-60 minutes"

            return analysis
    except Exception as e:
        logger.debug(f"Task analysis callable failed: {e}")
    return {}


def _parse_progress_callable(state) -> Dict[str, Any]:
    """Callable version of progress parser."""
    try:
        messages = getattr(state, "messages", [])
        if messages:
            content = getattr(messages[-1], "content", "")

            import re

            # Extract numbers for progress
            completed_match = re.search(r"completed.*?(\d+)", content, re.IGNORECASE)
            total_match = re.search(r"total.*?(\d+)", content, re.IGNORECASE)

            progress = {
                "completed_steps": (
                    int(completed_match.group(1)) if completed_match else 0
                ),
                "total_steps": int(total_match.group(1)) if total_match else 1,
                "current_status": "In progress",
                "next_actions": ["Continue with next step"],
            }

            return progress
    except Exception as e:
        logger.debug(f"Progress callable failed: {e}")
    return {}


# Example usage and testing


async def test_smart_parsing_workflow():
    """Test the smart parsing workflow with different input types."""

    logger.info("Creating smart parsing workflow...")
    workflow = await create_smart_planning_workflow()

    # Test cases with different output types
    test_cases = [
        {
            "name": "JSON Analysis",
            "input": "Analyze this task: Build a web scraper. Respond with JSON including complexity, time estimate, and required tools.",
            "expected_parsing": "json",
        },
        {
            "name": "Progress Report",
            "input": "Report progress: Completed 3 out of 5 steps. Currently working on data processing.",
            "expected_parsing": "progress",
        },
        {
            "name": "Task Analysis",
            "input": "This is a complex machine learning task requiring data preprocessing, model training, and evaluation. Estimated time is 4-6 hours with risk factors including data quality issues.",
            "expected_parsing": "task_analysis",
        },
    ]

    for test_case in test_cases:
        logger.info(f"\n{'=' * 60}")
        logger.info(f"Running test: {test_case['name']}")
        logger.info(f"Expected parsing: {test_case['expected_parsing']}")
        logger.info(f"{'=' * 60}")

        try:
            result = await workflow.arun(test_case["input"])

            logger.info(f"Result: {result}")

            # Check if smart parsing was applied
            if hasattr(result, "metadata") and "parsed_output" in result.metadata:
                logger.info(
                    f"✅ Smart parsing applied: {result.metadata['parsing_strategy']}"
                )
                logger.info(f"Parsed data: {result.metadata['parsed_output']}")
            else:
                logger.info("ℹ️  No smart parsing metadata found")

        except Exception as e:
            logger.error(f"❌ Test failed: {e}")

    logger.info("\n🎉 Smart parsing workflow tests completed!")


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Run the test
    asyncio.run(test_smart_parsing_workflow())
