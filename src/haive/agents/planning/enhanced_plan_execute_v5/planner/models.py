"""Planner Models - Custom Pydantic models for strategic planning.

This module defines the structured output models used by the planner agent
for creating comprehensive, actionable task plans.
"""

from typing import Literal, Optional, Any

from pydantic import BaseModel, Field


class TaskStep(BaseModel):
    """Individual step in a task plan with rich metadata.

    Represents a single actionable step within a larger plan, including
    all the information needed for successful execution.

    Attributes:
        step_id: Unique identifier for tracking this step
        description: Clear, actionable description of what to do
        expected_outcome: What result this step should produce
        tools_needed: Tools required for execution
        priority: Execution priority level
        estimated_time: Estimated completion time
        dependencies: Steps that must complete before this one

    Examples:
        Basic step::

            step = TaskStep(
                step_id="step_1",
                description="Search for current stock price of AAPL",
                expected_outcome="Current AAPL stock price in USD",
                tools_needed=["web_search"],
                priority="high"
            )

        Step with dependencies::

            step = TaskStep(
                step_id="step_2",
                description="Calculate percentage change from yesterday",
                expected_outcome="Percentage change calculation",
                tools_needed=["calculator"],
                dependencies=["step_1"],
                priority="medium"
            )
    """

    step_id: str = Field(..., description="Unique identifier for this step")
    description: str = Field(..., description="Clear description of what to do")
    expected_outcome: str = Field(..., description="What result this step should produce")
    tools_needed: list[str] = Field(
        default_factory=list, description="Tools required for this step"
    )
    priority: Literal["high", "medium", "low"] = Field(
        default="medium", description="Priority level for execution"
    )
    estimated_time: Optional[str] = Field(
        default=None, description="Estimated time to complete (e.g., '5 minutes')"
    )
    dependencies: list[str] = Field(
        default_factory=list, description="Step IDs that must complete before this one"
    )


class TaskPlan(BaseModel):
    """Comprehensive task plan with metadata and execution strategy.

    Represents a complete strategic plan for accomplishing a complex objective,
    including all steps, reasoning, and success criteria.

    Attributes:
        objective: The main goal we're trying to achieve
        steps: Ordered list of steps to execute
        reasoning: Explanation of the planning approach
        success_criteria: How we'll know the objective is achieved
        estimated_total_time: Total estimated time for all steps
        plan_type: Type of planning strategy used
        risk_factors: Potential risks and mitigation strategies

    Examples:
        Research plan::

            plan = TaskPlan(
                objective="Research Tesla's Q4 2024 financial performance",
                steps=[search_step, analysis_step, summary_step],
                reasoning="Sequential approach: gather data, analyze, summarize",
                success_criteria="Complete financial overview with key metrics",
                plan_type="sequential_research"
            )

        Complex analysis plan::

            plan = TaskPlan(
                objective="Compare renewable energy adoption across countries",
                steps=[data_steps, comparison_steps, visualization_step],
                reasoning="Parallel data gathering followed by comparative analysis",
                success_criteria="Comprehensive comparison with visual insights",
                plan_type="comparative_analysis",
                risk_factors=["Data availability", "Currency conversion accuracy"]
            )
    """

    objective: str = Field(..., description="The main objective we're trying to achieve")
    steps: list[TaskStep] = Field(..., description="List of steps to execute in order")
    reasoning: str = Field(..., description="Explanation of the planning approach")
    success_criteria: str = Field(..., description="How we'll know the objective has been achieved")
    estimated_total_time: Optional[str] = Field(
        default=None, description="Estimated total time for all steps"
    )
    plan_type: Literal[
        "sequential",
        "parallel",
        "sequential_research",
        "comparative_analysis",
        "creative",
        "analytical",
    ] = Field(default="sequential", description="Type of planning strategy used")
    risk_factors: list[str] = Field(
        default_factory=list, description="Potential risks and mitigation strategies"
    )


class PlanningContext(BaseModel):
    """Context information for the planner agent.

    Provides additional context that helps the planner create better,
    more targeted plans based on available resources and constraints.

    Attributes:
        available_tools: Tools that can be used during execution
        time_constraints: Any time limitations to consider
        complexity_level: Desired complexity level for the plan
        domain_focus: Specific domain or area of focus
        previous_attempts: Information about previous planning attempts

    Examples:
        Research context::

            context = PlanningContext(
                available_tools=["web_search", "calculator", "document_reader"],
                time_constraints="Complete within 1 hour",
                complexity_level="detailed",
                domain_focus="financial_analysis"
            )

        Simple task context::

            context = PlanningContext(
                available_tools=["calculator"],
                complexity_level="simple",
                domain_focus="mathematics"
            )
    """

    available_tools: list[str] = Field(
        default_factory=list, description="Tools that can be used during execution"
    )
    time_constraints: Optional[str] = Field(
        default=None, description="Any time limitations to consider"
    )
    complexity_level: Literal["simple", "moderate", "detailed", "comprehensive"] = Field(
        default="moderate", description="Desired complexity level for the plan"
    )
    domain_focus: Optional[str] = Field(
        default=None, description="Specific domain or area of focus"
    )
    previous_attempts: list[str] = Field(
        default_factory=list, description="Information about previous planning attempts"
    )
