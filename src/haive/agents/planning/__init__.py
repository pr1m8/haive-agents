"""Module exports."""

# Temporarily commenting out imports with missing dependencies
# TODO: Fix these imports after resolving missing haive.agents.multi.enhanced_base

# from .clean_plan_execute import (
#     Act,
#     Plan,
#     PlanExecuteState,
#     create_clean_plan_execute_agent,
#     create_simple_plan_execute,
#     route_after_replan,
#     should_continue,
# )
# from .langgraph_plan_execute import (
#     Act,
#     Plan,
#     PlanExecuteState,
#     Response,
#     create_langgraph_plan_execute,
#     create_plan_execute_agent,
#     route_replan,
#     should_continue,
# )
# from .plan_and_execute_multi import (
#     PlanAndExecuteAgent,
#     create_plan_execute_branches,
#     should_continue,
#     should_end,
# )
# from .proper_plan_execute import (
#     create_plan_execute_with_search,
#     create_proper_plan_execute,
#     process_executor_output,
#     process_planner_output,
#     process_replanner_output,
#     route_after_replan,
#     should_continue,
# )
# from .rewoo_tree_agent_v2 import (
#     ParallelReWOOAgent,
#     PlanTask,
#     ReWOOExecutorAgent,
#     ReWOOPlan,
#     ReWOOPlannerAgent,
#     ReWOOTreeAgent,
#     ReWOOTreeState,
#     TaskPriority,
#     TaskStatus,
#     TaskType,
#     ToolAlias,
#     add_task,
#     add_tool_alias,
#     create_plan,
#     create_rewoo_agent_with_tools,
#     execute_task,
#     get_ready_tasks,
#     validate_alias,
#     validate_id,
# )
# from .rewoo_tree_agent_v3 import (
#     ParallelReWOOAgent,
#     ReWOOPlan,
#     ReWOOTreeAgent,
#     ReWOOTreeState,
#     TaskType,
#     ToolAlias,
#     add_tool_alias,
#     create_rewoo_agent_with_tools,
#     validate_alias,
# )

# LLM Compiler V3 - Enhanced MultiAgent V3 Implementation
try:
    from .llm_compiler_v3 import (
        CompilerInput,
        CompilerOutput,
        CompilerPlan,
        CompilerTask,
        ExecutionMode,
        LLMCompilerV3Agent,
        LLMCompilerV3Config,
    )

    _HAS_LLM_COMPILER_V3 = True
except ImportError:
    _HAS_LLM_COMPILER_V3 = False

__all__ = [
    # Temporarily commented out due to missing dependencies
    # "Act",
    # "ParallelReWOOAgent",
    # "Plan",
    # "PlanAndExecuteAgent",
    # "PlanExecuteState",
    # "PlanTask",
    # "ReWOOExecutorAgent",
    # "ReWOOPlan",
    # "ReWOOPlannerAgent",
    # "ReWOOTreeAgent",
    # "ReWOOTreeState",
    # "Response",
    # "TaskPriority",
    # "TaskStatus",
    # "TaskType",
    # "ToolAlias",
    # "add_task",
    # "add_tool_alias",
    # "create_clean_plan_execute_agent",
    # "create_langgraph_plan_execute",
    # "create_plan",
    # "create_plan_execute_agent",
    # "create_plan_execute_branches",
    # "create_plan_execute_with_search",
    # "create_proper_plan_execute",
    # "create_rewoo_agent_with_tools",
    # "create_simple_plan_execute",
    # "execute_task",
    # "get_ready_tasks",
    # "process_executor_output",
    # "process_planner_output",
    # "process_replanner_output",
    # "route_after_replan",
    # "route_replan",
    # "should_continue",
    # "should_end",
    # "validate_alias",
    # "validate_id",
]

# Add LLM Compiler V3 exports if available
if _HAS_LLM_COMPILER_V3:
    __all__.extend(
        [
            "LLMCompilerV3Agent",
            "LLMCompilerV3Config",
            "CompilerTask",
            "CompilerPlan",
            "CompilerInput",
            "CompilerOutput",
            "ExecutionMode",
        ]
    )
