"""Engines for Plan-and-Execute V3 Agent.

This module contains the specialized engines used by the Plan-and-Execute V3 agent for
planning, validation, execution, and monitoring.
"""

import json
from datetime import datetime
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import BaseTool

from .models import Plan, PlanValidationResult, Step, StepStatus, StepType
from .prompts import (
    format_executor_prompt,
    format_monitor_prompt,
    format_planner_prompt,
    format_replanner_prompt,
    format_validator_prompt,
)


class PlannerEngine:
    """Engine for generating execution plans."""

    def __init__(self, llm_config: AugLLMConfig, tools: list[BaseTool]):
        """Initialize planner engine.

        Args:
            llm_config: LLM configuration
            tools: Available tools for planning
        """
        self.llm = llm_config.to_aug_llm()
        self.tools = tools
        self.tools_description = self._format_tools_description()

    def _format_tools_description(self) -> str:
        """Format tools description for prompts."""
        descriptions = []
        for tool in self.tools:
            descriptions.append(f"- {tool.name}: {tool.description}")
        return "\n".join(descriptions)

    async def generate_plan(self, goal: str) -> Plan:
        """Generate an execution plan for the given goal.

        Args:
            goal: The goal to achieve

        Returns:
            Generated execution plan
        """
        system_prompt = format_planner_prompt(self.tools_description)

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Create a plan to achieve this goal: {goal}"),
        ]

        response = await self.llm.ainvoke(messages)

        # Parse the response into a Plan object
        plan = self._parse_plan_response(response.content, goal)
        return plan

    def _parse_plan_response(self, response: str, goal: str) -> Plan:
        """Parse LLM response into a Plan object."""
        # This is a simplified parser - in production, use structured output
        plan_id = f"plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        plan = Plan(id=plan_id, goal=goal, steps=[])

        # Extract steps from response
        # This is a placeholder - implement proper parsing based on your needs
        lines = response.strip().split("\n")
        step_count = 0

        for line in lines:
            if line.strip() and any(
                marker in line.lower() for marker in ["step", "1.", "2.", "3."]
            ):
                step_count += 1
                step = Step(
                    id=f"step_{step_count}",
                    type=StepType.TOOL if "tool:" in line.lower() else StepType.THINK,
                    description=line.strip(),
                    dependencies=[],  # Parse dependencies from response
                )
                plan.steps.append(step)

        return plan


class ValidatorEngine:
    """Engine for validating and refining plans."""

    def __init__(self, llm_config: AugLLMConfig, tools: list[BaseTool]):
        """Initialize validator engine."""
        self.llm = llm_config.to_aug_llm()
        self.tools = tools
        self.tools_description = self._format_tools_description()

    def _format_tools_description(self) -> str:
        """Format tools description for prompts."""
        descriptions = []
        for tool in self.tools:
            descriptions.append(f"- {tool.name}: {tool.description}")
        return "\n".join(descriptions)

    async def validate_plan(self, plan: Plan) -> PlanValidationResult:
        """Validate a plan and suggest refinements.

        Args:
            plan: The plan to validate

        Returns:
            Validation result with issues and suggestions
        """
        system_prompt = format_validator_prompt(self.tools_description)

        # Format plan for validation
        plan_description = self._format_plan_for_validation(plan)

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Validate this plan:\n\n{plan_description}"),
        ]

        response = await self.llm.ainvoke(messages)

        # Parse validation response
        return self._parse_validation_response(response.content, plan)

    def _format_plan_for_validation(self, plan: Plan) -> str:
        """Format plan for validation prompt."""
        lines = [f"Goal: {plan.goal}", "Steps:"]
        for step in plan.steps:
            deps = (
                f" (depends on: {', '.join(step.dependencies)})"
                if step.dependencies
                else ""
            )
            lines.append(f"- {step.id}: {step.description}{deps}")
        return "\n".join(lines)

    def _parse_validation_response(
        self, response: str, original_plan: Plan
    ) -> PlanValidationResult:
        """Parse validation response."""
        # Simplified parsing - implement based on your needs
        is_valid = "valid" in response.lower() and "invalid" not in response.lower()

        issues = []
        suggestions = []

        # Extract issues and suggestions from response
        lines = response.strip().split("\n")
        for line in lines:
            if "issue" in line.lower() or "problem" in line.lower():
                issues.append(line.strip())
            elif "suggest" in line.lower() or "improve" in line.lower():
                suggestions.append(line.strip())

        return PlanValidationResult(
            is_valid=is_valid,
            issues=issues,
            suggestions=suggestions,
            refined_plan=None,  # Could generate refined plan if needed
        )


class ExecutorEngine:
    """Engine for executing individual plan steps."""

    def __init__(self, llm_config: AugLLMConfig, tools: list[BaseTool]):
        """Initialize executor engine."""
        self.llm = llm_config.to_aug_llm()
        self.tools = {tool.name: tool for tool in tools}

    async def execute_step(
        self, step: Step, context: dict[str, Any], previous_results: dict[str, Any]
    ) -> tuple[Any, str | None]:
        """Execute a single plan step.

        Args:
            step: The step to execute
            context: Shared execution context
            previous_results: Results from previous steps

        Returns:
            Tuple of (result, error_message)
        """
        try:
            if step.type == StepType.TOOL:
                # Execute tool directly
                if step.tool_name not in self.tools:
                    return None, f"Tool '{step.tool_name}' not found"

                tool = self.tools[step.tool_name]
                result = await tool.ainvoke(step.tool_args or {})
                return result, None

            if step.type == StepType.THINK:
                # Use LLM for reasoning step
                system_prompt = format_executor_prompt(
                    step.description, json.dumps(context), json.dumps(previous_results)
                )

                messages = [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content="Execute this step and provide the result."),
                ]

                response = await self.llm.ainvoke(messages)
                return response.content, None

            return None, f"Unsupported step type: {step.type}"

        except Exception as e:
            return None, str(e)


class MonitorEngine:
    """Engine for monitoring plan execution."""

    def __init__(self, llm_config: AugLLMConfig):
        """Initialize monitor engine."""
        self.llm = llm_config.to_aug_llm()

    async def analyze_execution(self, plan: Plan) -> dict[str, Any]:
        """Analyze plan execution progress.

        Args:
            plan: The plan being executed

        Returns:
            Analysis results with metrics and suggestions
        """
        execution_state = self._format_execution_state(plan)
        system_prompt = format_monitor_prompt(execution_state)

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content="Analyze the current execution state."),
        ]

        response = await self.llm.ainvoke(messages)

        # Parse and return analysis
        return {
            "progress_percentage": plan.progress_percentage,
            "completed_steps": plan.completed_steps,
            "failed_steps": plan.failed_steps,
            "analysis": response.content,
            "timestamp": datetime.now().isoformat(),
        }

    def _format_execution_state(self, plan: Plan) -> str:
        """Format execution state for monitoring."""
        lines = [
            f"Plan: {plan.id}",
            f"Goal: {plan.goal}",
            f"Progress: {plan.completed_steps}/{plan.total_steps} steps ({plan.progress_percentage:.1f}%)",
            "\nStep Status:",
        ]

        for step in plan.steps:
            status_icon = {
                StepStatus.COMPLETED: "✅",
                StepStatus.FAILED: "❌",
                StepStatus.RUNNING: "🔄",
                StepStatus.PENDING: "⏳",
                StepStatus.SKIPPED: "⏭️",
            }.get(step.status, "❓")

            lines.append(f"{status_icon} {step.id}: {step.description}")
            if step.error:
                lines.append(f"   Error: {step.error}")

        return "\n".join(lines)


class ReplannerEngine:
    """Engine for replanning when execution fails."""

    def __init__(self, llm_config: AugLLMConfig, tools: list[BaseTool]):
        """Initialize replanner engine."""
        self.llm = llm_config.to_aug_llm()
        self.tools = tools
        self.tools_description = self._format_tools_description()

    def _format_tools_description(self) -> str:
        """Format tools description for prompts."""
        descriptions = []
        for tool in self.tools:
            descriptions.append(f"- {tool.name}: {tool.description}")
        return "\n".join(descriptions)

    async def create_revised_plan(self, original_plan: Plan, issues: list[str]) -> Plan:
        """Create a revised plan based on execution issues.

        Args:
            original_plan: The plan that encountered issues
            issues: List of issues encountered

        Returns:
            Revised execution plan
        """
        plan_status = self._format_plan_status(original_plan)
        issues_text = "\n".join(f"- {issue}" for issue in issues)

        system_prompt = format_replanner_prompt(
            original_plan.goal, plan_status, issues_text, self.tools_description
        )

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content="Create a revised plan to continue toward the goal."),
        ]

        response = await self.llm.ainvoke(messages)

        # Parse revised plan
        revised_plan = self._parse_plan_response(response.content, original_plan.goal)
        revised_plan.metadata["revision_of"] = original_plan.id

        return revised_plan

    def _format_plan_status(self, plan: Plan) -> str:
        """Format current plan status."""
        lines = []
        for step in plan.steps:
            status = f"[{step.status.upper()}]"
            result = f" -> {step.result}" if step.result else ""
            error = f" (ERROR: {step.error})" if step.error else ""
            lines.append(f"{status} {step.id}: {step.description}{result}{error}")
        return "\n".join(lines)

    def _parse_plan_response(self, response: str, goal: str) -> Plan:
        """Parse LLM response into a Plan object."""
        # Reuse logic from PlannerEngine
        plan_id = f"plan_revised_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        plan = Plan(id=plan_id, goal=goal, steps=[])

        # Simplified parsing - implement proper parsing
        lines = response.strip().split("\n")
        step_count = 0

        for line in lines:
            if line.strip() and any(
                marker in line.lower() for marker in ["step", "1.", "2.", "3."]
            ):
                step_count += 1
                step = Step(
                    id=f"step_{step_count}",
                    type=StepType.TOOL if "tool:" in line.lower() else StepType.THINK,
                    description=line.strip(),
                    dependencies=[],
                )
                plan.steps.append(step)

        return plan
