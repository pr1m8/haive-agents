"""Enhanced Plan & Execute V5 - Modern Haive Implementation with Custom Models and Agents.

This module provides a completely redesigned Plan & Execute implementation using the latest
Haive architecture patterns, enhanced agents, and modern multi-agent orchestration.

## Key Features

- **MultiAgent**: Latest multi-agent orchestration with state management
- **SimpleAgentV3**: Enhanced planning and replanning with hooks system
- **ReactAgent**: Advanced tool-based execution with real-time feedback
- **Custom Pydantic Models**: Structured output designed for planning workflows
- **Modern Prompt Engineering**: Context-aware prompts with structured templates
- **Comprehensive Monitoring**: Full hooks system for execution tracking
- **Dynamic Recompilation**: Real-time agent updates and tool management

## Architecture

        PlannerAgentV3 (SimpleAgentV3)
            ↓ (structured Plan model)
        ExecutorAgentV3 (ReactAgent) ←─┐
            ↓ (execution results)       │
        Routing Logic ──→ Continue ────┘
            ↓
        ReplannerAgentV3 (SimpleAgentV3)
            ↓ (structured Decision model)
        Final Response or Loop Back

## Usage

### Basic Usage
        from haive.agents.planning.enhanced_plan_execute_v5 import create_enhanced_plan_execute_v5

        # Create with default tools
        agent = create_enhanced_plan_execute_v5()
        result = await agent.arun("Calculate compound interest on $1000 at 5% for 10 years")

        # Create with custom tools
        from haive.tools import web_search_tool, calculator_tool
        agent = create_enhanced_plan_execute_v5(
            name="research_planner",
            tools=[web_search_tool, calculator_tool]
        )
        result = await agent.arun("Research Tesla stock performance and calculate ROI")

### Advanced Configuration
        agent = create_enhanced_plan_execute_v5(
            name="advanced_planner",
            planner_config=AugLLMConfig(
                model="gpt-4",
                temperature=0.2,
                system_message="You are an expert strategic planner."
            ),
            executor_config=AugLLMConfig(
                model="gpt-4-turbo",
                temperature=0.1
            ),
            tools=[custom_tool1, custom_tool2],
            max_iterations=10,
            enable_hooks=True
        )

        # Add custom hooks
        @agent.before_run
        def track_execution(context):
            print(f"Starting planning workflow: {context.agent_name}")

        result = await agent.arun("Complex multi-step research task")

## Custom Models

The implementation uses custom Pydantic models designed specifically for planning:

- **TaskPlan**: Structured plan with steps, priorities, and dependencies
- **ExecutionStatus**: Rich execution tracking with success/failure states
- **PlanningDecision**: Intelligent routing decisions with reasoning
- **PlanExecuteState**: Enhanced state management for multi-agent coordination

## When to Use

✅ **Use this implementation when**:
- You need modern Haive architecture patterns
- Enhanced monitoring and debugging is important
- You want structured output and type safety
- Dynamic agent recompilation is needed
- Production-ready error handling is required

❌ **Consider alternatives when**:
- Simple tasks that don't need planning (use ReactAgent directly)
- Legacy compatibility is required (use clean_plan_execute)
- Minimal complexity is preferred (use SimpleAgent)

## Status: Next-Generation Planning

This is the future of planning agents in Haive, showcasing the full power
of the enhanced base agent pattern and modern multi-agent orchestration.
"""

from __future__ import annotations

import logging
from typing import Literal

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced.multi_agent_v4 import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent

logger = logging.getLogger(__name__)

# ============================================================================
# CUSTOM PYDANTIC MODELS - Designed for Modern Planning
# ============================================================================


class TaskStep(BaseModel):
    """Individual step in a task plan with rich metadata."""

    step_id: str = Field(..., description="Unique identifier for this step")
    description: str = Field(..., description="Clear description of what to do")
    expected_outcome: str = Field(
        ..., description="What result this step should produce"
    )
    tools_needed: list[str] = Field(
        default_factory=list, description="Tools required for this step"
    )
    priority: Literal["high", "medium", "low"] = Field(
        default="medium", description="Priority level for execution"
    )
    estimated_time: str | None = Field(
        default=None, description="Estimated time to complete (e.g., '5 minutes')"
    )
    dependencies: list[str] = Field(
        default_factory=list, description="Step IDs that must complete before this one"
    )


class TaskPlan(BaseModel):
    """Comprehensive task plan with metadata and tracking."""

    objective: str = Field(
        ..., description="The main objective we're trying to achieve"
    )
    steps: list[TaskStep] = Field(..., description="List of steps to execute in order")
    reasoning: str = Field(..., description="Explanation of the planning approach")
    success_criteria: str = Field(
        ..., description="How we'll know the objective has been achieved"
    )
    estimated_total_time: str | None = Field(
        default=None, description="Estimated total time for all steps"
    )


class ExecutionResult(BaseModel):
    """Rich execution result with detailed feedback."""

    step_id: str = Field(..., description="The step that was executed")
    success: bool = Field(..., description="Whether the step completed successfully")
    output: str = Field(..., description="The actual output/result from execution")
    tools_used: list[str] = Field(
        default_factory=list, description="Tools that were actually used"
    )
    execution_time: str | None = Field(
        default=None, description="How long the step took to execute"
    )
    issues_encountered: list[str] = Field(
        default_factory=list, description="Any problems or issues during execution"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Suggestions for improving future execution"
    )


class PlanningDecision(BaseModel):
    """Intelligent decision model for routing and replanning."""

    action: Literal["continue", "replan", "complete"] = Field(
        ..., description="What action to take next"
    )
    reasoning: str = Field(..., description="Why this action was chosen")
    confidence: float = Field(
        ..., ge=0.0, le=1.0, description="Confidence in this decision (0-1)"
    )
    final_answer: str | None = Field(
        default=None, description="Final answer if the task is complete"
    )
    new_plan: TaskPlan | None = Field(
        default=None, description="Revised plan if replanning is needed"
    )
    next_step_id: str | None = Field(
        default=None, description="Next step to execute if continuing"
    )


class EnhancedPlanExecuteState(MultiAgentState):
    """Enhanced state for plan and execute workflow with rich tracking."""

    # Core planning fields
    original_objective: str = Field(default="", description="The original user request")
    current_plan: TaskPlan | None = Field(
        default=None, description="The current execution plan"
    )
    execution_results: list[ExecutionResult] = Field(
        default_factory=list, description="Results from completed steps"
    )
    current_step_id: str | None = Field(
        default=None, description="ID of step currently being executed"
    )

    # Progress tracking
    completed_steps: list[str] = Field(
        default_factory=list, description="IDs of successfully completed steps"
    )
    failed_steps: list[str] = Field(
        default_factory=list, description="IDs of steps that failed"
    )
    iteration_count: int = Field(default=0, description="Number of planning iterations")
    replan_count: int = Field(default=0, description="Number of times we've replanned")

    # Decision tracking
    last_decision: PlanningDecision | None = Field(
        default=None, description="The most recent planning decision made"
    )
    final_answer: str | None = Field(
        default=None, description="Final answer when task is complete"
    )

    # Metadata
    planning_start_time: str | None = Field(
        default=None, description="When planning started"
    )
    total_execution_time: str | None = Field(
        default=None, description="Total time for entire workflow"
    )


# ============================================================================
# ENHANCED PROMPT TEMPLATES - Modern Context-Aware Design
# ============================================================================

PLANNER_SYSTEM_MESSAGE = """You are an expert strategic planner specializing in breaking down complex objectives into actionable, well-structured plans.

Your role is to:
1. Analyze the given objective thoroughly
2. Create a comprehensive, step-by-step plan
3. Ensure each step is specific, actionable, and measurable
4. Consider dependencies between steps
5. Estimate effort and identify required tools

Key Principles:
- Be specific and actionable in step descriptions
- Consider what tools or resources each step needs
- Think about the logical order and dependencies
- Provide clear success criteria for the overall objective
- Include your reasoning for the planning approach

Focus on creating plans that are:
- CLEAR: Each step is unambiguous
- COMPLETE: Nothing important is missed
- ACTIONABLE: Each step can be executed immediately
- MEASURABLE: Success can be determined objectively
"""

PLANNER_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", PLANNER_SYSTEM_MESSAGE),
        (
            "human",
            """Please create a detailed plan for this objective:.

Objective: {objective}

Consider what tools and resources might be needed, the logical sequence of steps, and provide clear success criteria. Be thorough but practical.""",
        ),
    ]
)

EXECUTOR_SYSTEM_MESSAGE = """You are a skilled task executor who specializes in carrying out specific steps in a larger plan with precision and attention to detail.

Your role is to:
1. Execute the given step exactly as described
2. Use available tools effectively and appropriately
3. Provide clear, detailed output about what was accomplished
4. Note any issues or recommendations for future steps
5. Be thorough in documenting the execution process

Key Principles:
- Focus on the specific step - don't try to do more than asked
- Use tools when they can help achieve better results
- Provide detailed output that others can build upon
- Note any problems or unexpected results
- Make recommendations for improving the process

When using tools:
- Choose the most appropriate tool for the task
- Use tools efficiently and effectively
- Document what tools were used and why
- Report on the quality and usefulness of tool outputs
"""

EXECUTOR_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", EXECUTOR_SYSTEM_MESSAGE),
        (
            "human",
            """Execute this specific step from our plan:.

Step: {step_description}
Expected Outcome: {expected_outcome}
Tools Available: {available_tools}

Previous Steps Completed:
{previous_results}

Focus on this step only. Use tools as needed and provide detailed results.""",
        ),
    ]
)

REPLANNER_SYSTEM_MESSAGE = """You are an expert planning analyst who specializes in evaluating progress and making intelligent decisions about next steps.

Your role is to:
1. Analyze the current progress against the original plan
2. Determine if the objective has been achieved
3. Decide whether to continue, replan, or complete the task
4. Provide clear reasoning for your decisions
5. Create revised plans when necessary

Key Principles:
- Consider the original objective - has it been achieved?
- Evaluate the quality and completeness of results so far
- Be realistic about what still needs to be done
- Don't continue unnecessarily if the objective is met
- Create better plans based on what you've learned

Decision Guidelines:
- COMPLETE: The objective has been fully achieved
- CONTINUE: The plan is working, proceed with next step
- REPLAN: The current approach needs adjustment or improvement
"""

REPLANNER_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", REPLANNER_SYSTEM_MESSAGE),
        (
            "human",
            """Analyze the current progress and make a decision about next steps:.

Original Objective: {objective}
Current Plan: {current_plan}

Steps Completed: {completed_steps}
Recent Execution Results: {recent_results}

Current Status: {current_status}

Based on this progress, what should we do next? Have we achieved the objective, should we continue with the current plan, or do we need to revise our approach?""",
        ),
    ]
)


# ============================================================================
# ROUTING LOGIC - Intelligent Decision Making
# ============================================================================


def should_continue_enhanced(state: EnhancedPlanExecuteState) -> str:
    """Enhanced routing logic based on current state and decisions."""
    # If we have a final answer, we're done
    if state.final_answer:
        return END

    # If we have a decision from the replanner, follow it
    if state.last_decision:
        if state.last_decision.action == "complete":
            return END
        if state.last_decision.action == "continue":
            return "executor"
        if state.last_decision.action == "replan":
            return "replanner"

    # If we have a current plan and next step, continue execution
    if state.current_plan and state.current_step_id:
        return "executor"

    # If we have results but no decision, go to replanner
    if state.execution_results:
        return "replanner"

    # Default fallback
    return "replanner"


def get_next_step_id(plan: TaskPlan, completed_steps: list[str]) -> str | None:
    """Get the next step ID to execute based on plan and completed steps."""
    if not plan or not plan.steps:
        return None

    for step in plan.steps:
        if step.step_id not in completed_steps:
            # Check if all dependencies are completed
            if all(dep_id in completed_steps for dep_id in step.dependencies):
                return step.step_id

    return None


# ============================================================================
# ENHANCED MULTI-AGENT PLAN & EXECUTE SYSTEM
# ============================================================================


def create_enhanced_plan_execute_v5(
    name: str = "EnhancedPlanExecuteV5",
    planner_config: AugLLMConfig | None = None,
    executor_config: AugLLMConfig | None = None,
    replanner_config: AugLLMConfig | None = None,
    tools: list | None = None,
    max_iterations: int = 20,
    enable_hooks: bool = True,
) -> MultiAgent:
    """Create enhanced Plan & Execute agent using modern Haive patterns.

    Args:
        name: Name for the multi-agent system
        planner_config: Configuration for the planning agent
        executor_config: Configuration for the execution agent
        replanner_config: Configuration for the replanning agent
        tools: Tools available to the executor
        max_iterations: Maximum planning iterations
        enable_hooks: Whether to enable the hooks system

    Returns:
        MultiAgent: Complete planning workflow system

    Examples:
        Basic usage::

            agent = create_enhanced_plan_execute_v5()
            result = await agent.arun("Calculate compound interest")

        With custom configuration::

            agent = create_enhanced_plan_execute_v5(
                name="research_planner",
                planner_config=AugLLMConfig(model="gpt-4", temperature=0.2),
                tools=[web_search_tool, calculator_tool],
                max_iterations=15
            )
            result = await agent.arun("Research and analyze market trends")
    """
    # Set default configurations
    if planner_config is None:
        planner_config = AugLLMConfig(
            model="gpt-4o-mini", temperature=0.3, system_message=PLANNER_SYSTEM_MESSAGE
        )

    if executor_config is None:
        executor_config = AugLLMConfig(
            model="gpt-4o-mini", temperature=0.1, system_message=EXECUTOR_SYSTEM_MESSAGE
        )

    if replanner_config is None:
        replanner_config = AugLLMConfig(
            model="gpt-4o-mini",
            temperature=0.2,
            system_message=REPLANNER_SYSTEM_MESSAGE,
        )

    if tools is None:
        tools = []

    # Create enhanced planning agent
    planner = SimpleAgent(
        name="planner",
        engine=planner_config,
        prompt_template=PLANNER_PROMPT_TEMPLATE,
        structured_output_model=TaskPlan,
        debug=True,
        hooks_enabled=enable_hooks,
    )

    # Create enhanced execution agent
    executor = ReactAgent(
        name="executor",
        engine=executor_config,
        prompt_template=EXECUTOR_PROMPT_TEMPLATE,
        tools=tools,
        structured_output_model=ExecutionResult,
        debug=True,
        hooks_enabled=enable_hooks,
    )

    # Create enhanced replanning agent
    replanner = SimpleAgent(
        name="replanner",
        engine=replanner_config,
        prompt_template=REPLANNER_PROMPT_TEMPLATE,
        structured_output_model=PlanningDecision,
        debug=True,
        hooks_enabled=enable_hooks,
    )

    # Create the multi-agent workflow
    workflow = MultiAgent(
        name=name,
        agents=[planner, executor, replanner],
        execution_mode="conditional",
        build_mode="auto",
        state_schema=EnhancedPlanExecuteState,
    )

    # Configure the workflow routing
    workflow.add_edge(START, "planner")

    # Add intelligent conditional routing
    workflow.add_multi_conditional_edge(
        from_agent="planner",
        condition=lambda state: "executor" if state.current_plan else "replanner",
        routes={"executor": "executor", "replanner": "replanner"},
        default="replanner",
    )

    workflow.add_multi_conditional_edge(
        from_agent="executor",
        condition=should_continue_enhanced,
        routes={"executor": "executor", "replanner": "replanner", END: END},
        default="replanner",
    )

    workflow.add_multi_conditional_edge(
        from_agent="replanner",
        condition=should_continue_enhanced,
        routes={"executor": "executor", "replanner": "replanner", END: END},
        default=END,
    )

    # Add monitoring hooks if enabled
    if enable_hooks:
        _add_monitoring_hooks(workflow)

    logger.info(f"Created enhanced Plan & Execute V5: {name}")
    return workflow


def _add_monitoring_hooks(workflow: MultiAgent) -> None:
    """Add comprehensive monitoring hooks to the workflow."""

    @workflow.before_run
    def log_workflow_start(context):
        """Log Workflow Start.

        Args:
            context: [TODO: Add description]
        """
        logger.info(f"🚀 Starting enhanced planning workflow: {context.agent_name}")

    @workflow.after_run
    def log_workflow_complete(context):
        """Log Workflow Complete.

        Args:
            context: [TODO: Add description]
        """
        logger.info(f"✅ Planning workflow completed: {context.agent_name}")

    @workflow.on_error
    def log_workflow_error(context):
        """Log Workflow Error.

        Args:
            context: [TODO: Add description]
        """
        logger.error(f"❌ Planning workflow error: {context.error}")


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================


def create_simple_enhanced_plan_execute(tools: list | None = None) -> MultiAgent:
    """Create a simple enhanced plan and execute agent with default settings."""
    return create_enhanced_plan_execute_v5(
        name="SimpleEnhancedPlanExecute", tools=tools or []
    )


def create_research_plan_execute(tools: list | None = None) -> MultiAgent:
    """Create a plan and execute agent optimized for research tasks."""
    from haive.tools import duckduckgo_search_tool

    research_tools = [duckduckgo_search_tool]
    if tools:
        research_tools.extend(tools)

    return create_enhanced_plan_execute_v5(
        name="ResearchPlanExecute",
        planner_config=AugLLMConfig(
            model="gpt-4o-mini",
            temperature=0.2,
            system_message=PLANNER_SYSTEM_MESSAGE
            + "\n\nYou specialize in research planning. Focus on information gathering, analysis, and synthesis steps.",
        ),
        tools=research_tools,
    )


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    import asyncio

    async def test_enhanced_plan_execute():
        """Test the enhanced plan and execute system."""
        # Create the agent
        agent = create_simple_enhanced_plan_execute()

        # Test with a simple task
        result = await agent.arun(
            "What is the capital of France and what is its population?"
        )
        print(f"Result: {result}")

    # Run the test
    asyncio.run(test_enhanced_plan_execute())
