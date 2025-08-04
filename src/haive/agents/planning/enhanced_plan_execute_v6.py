"""Enhanced Plan & Execute V6 - Using EnhancedMultiAgentV4 with Universal Structured Output.

This module provides the next-generation Plan & Execute implementation using:
- EnhancedMultiAgentV4 for multi-agent orchestration
- Universal structured output pattern (Agent.with_structured_output)
- BasePlannerAgent and BaseExecutorAgent from base planning components
- Modern Haive architecture with hooks, recompilation, and state management

## Key Features

- **Universal Structured Output**: Any agent can have structured output via mixins
- **EnhancedMultiAgentV4**: Modern multi-agent coordination with conditional routing  
- **Base Planning Components**: Uses BasePlannerAgent and BaseExecutorAgent
- **Real Component Testing**: No mocks, actual LLM execution and tool usage
- **Modern Architecture**: Hooks, recompilation, state management, type safety

## Architecture

```
BasePlannerAgent.with_structured_output(BasePlan)
    ↓ (structured BasePlan output)
BaseExecutorAgent.with_structured_output(ExecutionResult) 
    ↓ (structured ExecutionResult output)
Conditional Routing (should_continue)
    ↓
EnhancedMultiAgentV4 orchestration
```

## Usage

### Basic Usage
```python
from haive.agents.planning.enhanced_plan_execute_v6 import create_enhanced_plan_execute_v6

# Create with default configuration
agent = create_enhanced_plan_execute_v6()
result = await agent.arun("Calculate compound interest on $1000 at 5% for 10 years")

# Create with custom tools
from haive.tools.tools.search_tools import tavily_search_tool
agent = create_enhanced_plan_execute_v6(
    name="research_planner",
    executor_tools=[tavily_search_tool]
)
result = await agent.arun("Research Tesla stock performance and calculate ROI")
```

### Advanced Configuration
```python
agent = create_enhanced_plan_execute_v6(
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
    executor_tools=[tavily_search_tool, calculator_tool],
    max_iterations=15,
    enable_hooks=True
)

# Add custom hooks
@agent.before_run
def track_execution(context):
    """Track Execution implementation."""
    print(f"Starting planning workflow: {context.agent_name}")

result = await agent.arun("Complex multi-step research task")
```

## Status: Production Ready

This implementation showcases the full power of modern Haive architecture:
- EnhancedMultiAgentV4 coordination
- Universal structured output patterns
- Base planning components
- Real component integration
"""

from __future__ import annotations

import logging
import time
from typing import Any, Optional

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.planning.base.agents.planner import BasePlannerAgent
from haive.agents.planning.base.agents.executor import BaseExecutorAgent  
from haive.agents.planning.base.models import BasePlan, PlanContent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from haive.tools.tools.search_tools import tavily_search_tool
from langgraph.graph import END
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# ============================================================================
# STRUCTURED OUTPUT MODELS - For Plan & Execute Workflow
# ============================================================================

class ExecutionResult(BaseModel):
    """Structured execution result from executor agent."""
    
    step_id: str = Field(..., description="ID of the step that was executed")
    success: bool = Field(..., description="Whether the step completed successfully")
    output: str = Field(..., description="The actual output/result from execution")
    tools_used: list[str] = Field(
        default_factory=list, description="Tools that were actually used"
    )
    execution_time: Optional[str] = Field(
        default=None, description="How long the step took to execute"
    )
    issues_encountered: list[str] = Field(
        default_factory=list, description="Any problems or issues during execution"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Suggestions for improving future execution"
    )
    next_step_ready: bool = Field(
        default=True, description="Whether the next step is ready to execute"
    )


class PlanningDecision(BaseModel):
    """Decision model for routing and coordination."""
    
    action: str = Field(..., description="What action to take next: continue, replan, complete")
    reasoning: str = Field(..., description="Why this action was chosen")
    confidence: float = Field(
        ..., ge=0.0, le=1.0, description="Confidence in this decision (0-1)"
    )
    final_answer: Optional[str] = Field(
        default=None, description="Final answer if the task is complete"
    )
    next_step_id: Optional[str] = Field(
        default=None, description="Next step to execute if continuing"
    )


class PlanExecuteState(MultiAgentState):
    """Enhanced state for plan and execute workflow coordination."""
    
    # Core planning fields
    original_objective: str = Field(default="", description="The original user request")
    current_plan: Optional[BasePlan[PlanContent]] = Field(
        default=None, description="The current execution plan"
    )
    execution_results: list[ExecutionResult] = Field(
        default_factory=list, description="Results from completed steps"
    )
    current_step_id: Optional[str] = Field(
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
    last_decision: Optional[PlanningDecision] = Field(
        default=None, description="The most recent planning decision"
    )
    final_answer: Optional[str] = Field(
        default=None, description="Final answer when task is complete"
    )


# ============================================================================
# ROUTING LOGIC - Intelligent Decision Making
# ============================================================================

def should_continue_v6(state: PlanExecuteState) -> str:
    """Enhanced routing logic for V6 workflow."""
    # If we have a final answer, we're done
    if state.final_answer:
        return END
    
    # If we have a decision from coordinator, follow it
    if state.last_decision:
        if state.last_decision.action == "complete":
            return END
        elif state.last_decision.action == "continue":
            return "executor_structured"
        elif state.last_decision.action == "replan":
            return "planner_structured"
    
    # If we have a current plan but no current step, we need to start execution
    if state.current_plan and not state.current_step_id:
        # Get first unexecuted step
        next_step = get_next_step_v6(state.current_plan, state.completed_steps)
        if next_step:
            state.current_step_id = next_step
            return "executor_structured"
        else:
            # All steps completed, finish
            return END
    
    # If we have a current step, continue execution
    if state.current_plan and state.current_step_id:
        return "executor_structured"
    
    # If we have results but no plan, we may need to replan
    if state.execution_results and not state.current_plan:
        return "planner_structured"
    
    # Default: start with planning
    return "planner_structured"


def get_next_step_v6(plan: BasePlan[PlanContent], completed_steps: list[str]) -> Optional[str]:
    """Get the next step ID to execute based on plan and completed steps."""
    if not plan or not plan.steps:
        return None
    
    # Simple sequential execution for now
    for step in plan.steps:
        if hasattr(step, 'step_id') and step.step_id not in completed_steps:
            # Check dependencies if they exist
            if hasattr(step, 'dependencies'):
                if all(dep_id in completed_steps for dep_id in step.dependencies):
                    return step.step_id
            else:
                # No dependencies, can execute
                return step.step_id
    
    return None


# ============================================================================
# STATE PROCESSING FUNCTIONS - Update state between agents
# ============================================================================

def process_planner_output_v6(state: PlanExecuteState, planner_result: BasePlan[PlanContent]) -> dict:
    """Process planner output and update state."""
    updates = {}
    
    if planner_result:
        updates["current_plan"] = planner_result
        
        # Set first step as current if available
        if planner_result.steps:
            first_step = planner_result.steps[0]
            if hasattr(first_step, 'step_id'):
                updates["current_step_id"] = first_step.step_id
        
        # Reset execution tracking for new plan
        updates["completed_steps"] = []
        updates["execution_results"] = []
        updates["iteration_count"] = state.iteration_count + 1
    
    return updates


def process_executor_output_v6(state: PlanExecuteState, executor_result: ExecutionResult) -> dict:
    """Process executor output and update state."""
    updates = {}
    
    if executor_result and state.current_step_id:
        # Add execution result
        updated_results = list(state.execution_results)
        updated_results.append(executor_result)
        updates["execution_results"] = updated_results
        
        # Mark step as completed if successful
        if executor_result.success:
            updated_completed = list(state.completed_steps)
            updated_completed.append(state.current_step_id)
            updates["completed_steps"] = updated_completed
        else:
            # Mark as failed
            updated_failed = list(state.failed_steps)
            updated_failed.append(state.current_step_id)
            updates["failed_steps"] = updated_failed
        
        # Get next step if available and executor says it's ready
        if executor_result.next_step_ready and state.current_plan:
            next_step = get_next_step_v6(state.current_plan, updates.get("completed_steps", state.completed_steps))
            updates["current_step_id"] = next_step
        else:
            updates["current_step_id"] = None
    
    return updates


# ============================================================================
# ENHANCED MULTI-AGENT PLAN & EXECUTE V6
# ============================================================================

def create_enhanced_plan_execute_v6(
    name: str = "EnhancedPlanExecuteV6",
    planner_config: Optional[AugLLMConfig] = None,
    executor_config: Optional[AugLLMConfig] = None,
    executor_tools: Optional[list] = None,
    max_iterations: int = 20,
    enable_hooks: bool = True,
) -> EnhancedMultiAgentV4:
    """Create enhanced Plan & Execute V6 using modern Haive patterns.
    
    Args:
        name: Name for the multi-agent system
        planner_config: Configuration for the planning agent
        executor_config: Configuration for the execution agent
        executor_tools: Tools available to the executor
        max_iterations: Maximum planning iterations
        enable_hooks: Whether to enable the hooks system
    
    Returns:
        EnhancedMultiAgentV4: Complete planning workflow system
    
    Examples:
        Basic usage::
        
            agent = create_enhanced_plan_execute_v6()
            result = await agent.arun("Calculate compound interest")
        
        With custom configuration::
        
            agent = create_enhanced_plan_execute_v6(
                name="research_planner",
                planner_config=AugLLMConfig(model="gpt-4", temperature=0.2),
                executor_tools=[tavily_search_tool],
                max_iterations=15
            )
            result = await agent.arun("Research and analyze market trends")
    """
    # Set default configurations
    if planner_config is None:
        planner_config = AugLLMConfig(
            model="gpt-4o-mini",
            temperature=0.3,
            system_message="You are an expert strategic planner with deep expertise in task decomposition."
        )
    
    if executor_config is None:
        executor_config = AugLLMConfig(
            model="gpt-4o-mini",
            temperature=0.1,
            system_message="You are a skilled task executor who specializes in carrying out specific steps with precision."
        )
    
    if executor_tools is None:
        executor_tools = [tavily_search_tool]
    
    # Create base planning agent with structured output
    base_planner = BasePlannerAgent(
        name="planner",
        engine=planner_config
    )
    
    # Create structured planning workflow
    planner, planner_structurer = BasePlannerAgent.with_structured_output(
        output_model=BasePlan[PlanContent],
        name="planner",
        engine=planner_config
    )
    
    # Create base executor agent with structured output  
    executor, executor_structurer = BaseExecutorAgent.with_structured_output(
        output_model=ExecutionResult,
        name="executor",
        engine=executor_config,
        additional_tools=executor_tools
    )
    
    # Create the multi-agent workflow
    workflow = EnhancedMultiAgentV4(
        name=name,
        agents=[
            planner,           # BasePlannerAgent instance
            planner_structurer, # StructuredOutputAgent for plans  
            executor,          # BaseExecutorAgent instance
            executor_structurer # StructuredOutputAgent for execution results
        ],
        execution_mode="conditional",
        build_mode="auto",
        state_schema=PlanExecuteState
    )
    
    # Configure the workflow routing
    workflow.add_edge("START", "planner")
    
    # Add conditional routing with structured output agents
    workflow.add_conditional_edges(
        from_agent="planner_structured",  # From structured planning output
        condition=lambda state: "executor" if state.current_plan else END,
        routes={
            "executor": "executor",
            END: END
        }
    )
    
    workflow.add_conditional_edges(
        from_agent="executor_structured",  # From structured execution output
        condition=should_continue_v6,
        routes={
            "executor_structured": "executor",
            "planner_structured": "planner", 
            END: END
        }
    )
    
    # Add monitoring hooks if enabled
    if enable_hooks:
        _add_monitoring_hooks_v6(workflow)
    
    logger.info(f"Created enhanced Plan & Execute V6: {name}")
    return workflow


def _add_monitoring_hooks_v6(workflow: EnhancedMultiAgentV4) -> None:
    """Add comprehensive monitoring hooks to the V6 workflow."""
    
    # Workflow-level monitoring hooks
    @workflow.before_run
    def log_workflow_start(context):
        """Log Workflow Start implementation."""
        logger.info(f"🚀 Starting enhanced planning workflow V6: {context.agent_name}")
        if hasattr(context, 'metadata'):
            context.metadata['workflow_start_time'] = time.time()
    
    @workflow.after_run
    def log_workflow_complete(context):
        """Log Workflow Complete implementation."""
        duration = ""
        if hasattr(context, 'metadata') and 'workflow_start_time' in context.metadata:
            duration = f" in {time.time() - context.metadata['workflow_start_time']:.2f}s"
        logger.info(f"✅ Planning workflow V6 completed{duration}: {context.agent_name}")
    
    @workflow.on_error
    def log_workflow_error(context):
        """Log Workflow Error implementation."""
        logger.error(f"❌ Planning workflow V6 error: {context.error}")
        if hasattr(context, 'metadata'):
            context.metadata['error_occurred'] = True
    
    # Add hooks to individual agents for detailed monitoring
    for agent in workflow.agents:
        if hasattr(agent, 'add_hook'):
            # Import HookEvent properly
            from haive.agents.base.hooks import HookEvent
            
            def create_agent_hook(agent_name: str):
                """Create Agent Hook implementation."""
                def agent_execution_hook(context):
                    """Agent Execution Hook implementation."""
                    if context.event == HookEvent.BEFORE_RUN:
                        logger.debug(f"  ▶ Agent starting: {agent_name}")
                    elif context.event == HookEvent.AFTER_RUN:
                        logger.debug(f"  ✓ Agent completed: {agent_name}")
                    elif context.event == HookEvent.ON_ERROR:
                        logger.error(f"  ❌ Agent error in {agent_name}: {context.error}")
                return agent_execution_hook
            
            agent_hook = create_agent_hook(agent.name)
            agent.add_hook(HookEvent.BEFORE_RUN, agent_hook)
            agent.add_hook(HookEvent.AFTER_RUN, agent_hook)
            agent.add_hook(HookEvent.ON_ERROR, agent_hook)


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def create_research_plan_execute_v6(executor_tools: Optional[list] = None) -> EnhancedMultiAgentV4:
    """Create a plan and execute agent optimized for research tasks."""
    research_tools = [tavily_search_tool]
    if executor_tools:
        research_tools.extend(executor_tools)
    
    return create_enhanced_plan_execute_v6(
        name="ResearchPlanExecuteV6",
        planner_config=AugLLMConfig(
            model="gpt-4o-mini",
            temperature=0.2,
            system_message="You are an expert research planner. Focus on information gathering, analysis, and synthesis steps."
        ),
        executor_tools=research_tools
    )


def create_simple_plan_execute_v6(executor_tools: Optional[list] = None) -> EnhancedMultiAgentV4:
    """Create a simple plan and execute agent with default settings."""
    return create_enhanced_plan_execute_v6(
        name="SimplePlanExecuteV6",
        executor_tools=executor_tools or []
    )


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    import asyncio
    
    async def test_enhanced_plan_execute_v6():
        """Test the enhanced plan and execute V6 system."""
        # Create the agent
        agent = create_simple_plan_execute_v6()
        
        # Test with a planning task
        result = await agent.arun("What is the capital of France and what is its current population?")
        print(f"Result: {result}")
    
    # Run the test
    asyncio.run(test_enhanced_plan_execute_v6())