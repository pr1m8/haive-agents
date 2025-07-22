"""Configuration models for LLM Compiler V3 Agent."""

from typing import Any, Dict, List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, ConfigDict, Field

from haive.agents.planning.llm_compiler_v3.models import ExecutionMode


class LLMCompilerV3Config(BaseModel):
    """Configuration for LLM Compiler V3 Agent."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    # Agent identification
    name: str = Field(
        default="llm_compiler_v3", description="Name of the compiler agent instance"
    )

    # Engine configurations for different sub-agents
    planner_engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.3,  # Lower temperature for consistent planning
            max_tokens=2000,
            system_message="You are an expert task planner specializing in parallel execution optimization.",
        ),
        description="Configuration for the planner agent",
    )

    task_fetcher_engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.1,  # Very low temperature for consistent coordination
            max_tokens=1000,
            system_message="You are a task coordination specialist managing parallel execution.",
        ),
        description="Configuration for the task fetcher agent",
    )

    executor_engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.2,  # Low temperature for consistent execution
            max_tokens=1500,
            system_message="You are a tool execution specialist focused on reliable task completion.",
        ),
        description="Configuration for the parallel executor agent",
    )

    joiner_engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.4,  # Slightly higher for creative synthesis
            max_tokens=2000,
            system_message="You are a results synthesis expert creating comprehensive final answers.",
        ),
        description="Configuration for the joiner agent",
    )

    # Execution settings
    execution_mode: ExecutionMode = Field(
        default=ExecutionMode.HYBRID, description="Default execution mode for tasks"
    )

    max_parallel_tasks: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Maximum number of tasks to execute in parallel",
    )

    task_timeout: float = Field(
        default=120.0,
        gt=0.0,
        description="Timeout for individual task execution in seconds",
    )

    total_timeout: float = Field(
        default=600.0,
        gt=0.0,
        description="Total timeout for entire plan execution in seconds",
    )

    # Replanning settings
    max_replan_attempts: int = Field(
        default=2, ge=0, le=5, description="Maximum number of replanning attempts"
    )

    replan_on_failure_threshold: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Failure rate threshold that triggers replanning",
    )

    enable_auto_replan: bool = Field(
        default=True, description="Whether to automatically replan on failures"
    )

    # Tool management
    tool_names: List[str] = Field(
        default_factory=list, description="Names of tools available to the compiler"
    )

    tool_priorities: Dict[str, int] = Field(
        default_factory=dict,
        description="Priority mapping for tools (higher number = higher priority)",
    )

    exclude_tools: List[str] = Field(
        default_factory=list, description="Tools to exclude from planning"
    )

    # Performance optimization
    enable_task_caching: bool = Field(
        default=True, description="Whether to cache task results for reuse"
    )

    enable_smart_batching: bool = Field(
        default=True, description="Whether to intelligently batch similar tasks"
    )

    parallel_efficiency_target: float = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        description="Target efficiency score for parallel execution",
    )

    # Debugging and monitoring
    enable_detailed_logging: bool = Field(
        default=False, description="Whether to enable detailed execution logging"
    )

    log_task_timings: bool = Field(
        default=True, description="Whether to log individual task execution times"
    )

    enable_execution_tracing: bool = Field(
        default=True, description="Whether to maintain detailed execution traces"
    )

    # Custom settings
    custom_settings: Dict[str, Any] = Field(
        default_factory=dict, description="Custom configuration settings"
    )

    def get_engine_for_agent(self, agent_name: str) -> AugLLMConfig:
        """Get the engine configuration for a specific agent."""
        engine_map = {
            "planner": self.planner_engine,
            "task_fetcher": self.task_fetcher_engine,
            "parallel_executor": self.executor_engine,
            "joiner": self.joiner_engine,
        }

        return engine_map.get(agent_name, self.planner_engine)

    def should_enable_tool(self, tool_name: str) -> bool:
        """Check if a tool should be enabled based on configuration."""
        if tool_name in self.exclude_tools:
            return False

        if self.tool_names and tool_name not in self.tool_names:
            return False

        return True

    def get_tool_priority(self, tool_name: str) -> int:
        """Get priority for a tool (higher = more preferred)."""
        return self.tool_priorities.get(tool_name, 1)

    def create_execution_config(self) -> Dict[str, Any]:
        """Create configuration dictionary for execution."""
        return {
            "execution_mode": self.execution_mode,
            "max_parallel_tasks": self.max_parallel_tasks,
            "task_timeout": self.task_timeout,
            "total_timeout": self.total_timeout,
            "enable_caching": self.enable_task_caching,
            "enable_batching": self.enable_smart_batching,
            "efficiency_target": self.parallel_efficiency_target,
            "max_replan_attempts": self.max_replan_attempts,
            "auto_replan": self.enable_auto_replan,
            "failure_threshold": self.replan_on_failure_threshold,
        }


class ToolExecutionConfig(BaseModel):
    """Configuration for individual tool execution."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    tool_name: str = Field(..., description="Name of the tool")

    timeout: float = Field(
        default=60.0, gt=0.0, description="Timeout for this specific tool"
    )

    retry_attempts: int = Field(
        default=2, ge=0, le=5, description="Number of retry attempts on failure"
    )

    priority: int = Field(
        default=1, ge=1, le=10, description="Tool priority (higher = preferred)"
    )

    enable_caching: bool = Field(
        default=True, description="Whether to cache results for this tool"
    )

    custom_args: Dict[str, Any] = Field(
        default_factory=dict, description="Tool-specific configuration arguments"
    )
