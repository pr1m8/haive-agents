"""Configuration for Plan-and-Execute V3 Agent.

This module defines configuration options for the Plan-and-Execute V3 agent.
"""

from pydantic import BaseModel, ConfigDict, Field


class PlanExecuteV3Config(BaseModel):
    """Configuration for Plan-and-Execute V3 agent.

    Attributes:
        max_steps: Maximum number of steps allowed in a plan
        max_retries: Maximum retry attempts per step
        timeout_per_step: Timeout in seconds for each step
        parallel_execution: Enable parallel step execution
        validate_plan: Validate plan before execution
        replan_on_failure: Automatically replan on execution failure
        enable_monitoring: Enable execution monitoring
        max_replanning_attempts: Maximum replanning attempts
        verbose: Enable verbose logging
        save_execution_history: Save execution history to state
        step_result_in_context: Store step results in shared context
    """

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    max_steps: int = Field(
        default=10, ge=1, le=50, description="Maximum number of steps allowed in a plan"
    )

    max_retries: int = Field(
        default=3, ge=0, le=10, description="Maximum retry attempts per step"
    )

    timeout_per_step: float = Field(
        default=30.0, gt=0, le=300, description="Timeout in seconds for each step"
    )

    parallel_execution: bool = Field(
        default=False, description="Enable parallel step execution"
    )

    validate_plan: bool = Field(
        default=True, description="Validate plan before execution"
    )

    replan_on_failure: bool = Field(
        default=True, description="Automatically replan on execution failure"
    )

    enable_monitoring: bool = Field(
        default=True, description="Enable execution monitoring"
    )

    max_replanning_attempts: int = Field(
        default=3, ge=0, le=10, description="Maximum replanning attempts"
    )

    verbose: bool = Field(default=False, description="Enable verbose logging")

    save_execution_history: bool = Field(
        default=True, description="Save execution history to state"
    )

    step_result_in_context: bool = Field(
        default=True, description="Store step results in shared context"
    )

    # Planning-specific configuration
    planning_temperature: float | None = Field(
        default=None,
        ge=0.0,
        le=2.0,
        description="Temperature for planning LLM (None uses engine default)",
    )

    execution_temperature: float | None = Field(
        default=None,
        ge=0.0,
        le=2.0,
        description="Temperature for execution LLM (None uses engine default)",
    )

    # Tool-specific configuration
    prefer_parallel_tools: bool = Field(
        default=True, description="Prefer parallel execution for independent tool calls"
    )

    tool_timeout_override: float | None = Field(
        default=None, gt=0, description="Override timeout for tool execution"
    )

    def get_planning_temperature(self, default: float) -> float:
        """Get planning temperature or use default."""
        return (
            self.planning_temperature
            if self.planning_temperature is not None
            else default
        )

    def get_execution_temperature(self, default: float) -> float:
        """Get execution temperature or use default."""
        return (
            self.execution_temperature
            if self.execution_temperature is not None
            else default
        )
