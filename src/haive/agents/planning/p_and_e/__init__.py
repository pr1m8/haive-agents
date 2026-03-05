"""Module exports."""

import logging

from haive.agents.planning.p_and_e.agent import PlanAndExecuteAgent, check_plan_complete
from haive.agents.planning.p_and_e.engines import (
    create_executor_aug_llm_config,
    create_planner_aug_llm_config,
    create_replan_aug_llm_config,
)
from haive.agents.planning.p_and_e.models import (
    Act,
    ExecutionResult,
    Plan,
    PlanStep,
    ReplanDecision,
    Response,
    StepStatus,
    StepType,
)
from haive.agents.planning.p_and_e.state import PlanExecuteState

logger = logging.getLogger(__name__)

__all__ = [
    "Act",
    "ExecutionResult",
    "Plan",
    "PlanAndExecuteAgent",
    "PlanExecuteState",
    "PlanStep",
    "ReplanDecision",
    "Response",
    "StepStatus",
    "StepType",
    "check_plan_complete",
    "create_executor_aug_llm_config",
    "create_planner_aug_llm_config",
    "create_replan_aug_llm_config",
]

# Optional imports — legacy multi-agent helpers depend on archived ConfigurableMultiAgent
try:
    from haive.agents.planning.p_and_e.enhanced_multi_agent import (
        EnhancedMultiAgent,
        PlanAndExecuteMultiAgent,
    )
    from haive.agents.planning.p_and_e.example import calculate, search
    from haive.agents.planning.p_and_e.multi_agent import (
        create_custom_branching_system,
        create_custom_plan_execute_system,
        create_plan_execute_system,
        create_simple_sequential_system,
    )

    __all__ += [
        "EnhancedMultiAgent",
        "PlanAndExecuteMultiAgent",
        "calculate",
        "create_custom_branching_system",
        "create_custom_plan_execute_system",
        "create_plan_execute_system",
        "create_simple_sequential_system",
        "search",
    ]
except (ImportError, Exception) as e:
    logger.debug("p_and_e: optional imports unavailable: %s", e)
