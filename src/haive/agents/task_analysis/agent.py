# src/haive/agents/task_analysis/agent.py

import logging
from typing import Any, Dict, List, Literal, Optional, Type, Union

from haive.core.common.structures.tree import AutoTree
from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.schema_composer import SchemaComposer
from langgraph.graph import END, START
from langgraph.types import Command, Send
from pydantic import BaseModel, Field, field_validator

from haive.agents.base.agent import Agent
from haive.agents.task_analysis.analysis.engines import (
    FeasibilityAssessorEngine,
    IntegratedAnalyzerEngine,
    OptimizationRecommenderEngine,
)
from haive.agents.task_analysis.complexity.engines import (
    ComplexityAssessorEngine,
    ComplexityComparisonEngine,
    ComplexityFactorsEngine,
)
from haive.agents.task_analysis.context.engines import (
    ContextAnalyzerEngine,
    ContextFlowEngine,
    ContextOptimizerEngine,
    DomainExpertiseEngine,
)

# Import all engines
from haive.agents.task_analysis.decomposer.engines import (
    RecursiveDecomposerEngine,
    TaskDecomposerEngine,
    TaskValidationEngine,
)
from haive.agents.task_analysis.execution.engines import (
    ExecutionPlannerEngine,
    JoinPointStrategyEngine,
    PhaseOptimizerEngine,
    ResourceAllocatorEngine,
)
from haive.agents.task_analysis.tree.engines import (
    CriticalPathAnalyzerEngine,
    TreePatternRecognizerEngine,
    TreeStructureAnalyzerEngine,
)

# Import models
from .base.models import TaskNode, TaskPlan
from .complexity.models import ComplexityAnalysis, ComplexityVector
from .context.models import ContextAnalysis, ContextRequirement
from .execution.models import ExecutionPlan, JoinPoint
from .tree.models import TaskTree

logger = logging.getLogger(__name__)

# ============================================================================
# ROUTING FUNCTIONS
# ============================================================================


def route_after_decomposition(
    state: Dict[str, Any],
) -> Literal["parallel_analysis", "validate_decomposition", "recursive_decompose"]:
    """Route after initial decomposition."""
    task_node = state.get("task_node")

    if not task_node:
        return "validate_decomposition"

    # Check if we need recursive decomposition
    needs_expansion = any(
        subtask.can_expand
        for subtask in task_node.subtasks
        if hasattr(subtask, "can_expand")
    )

    if needs_expansion and state.get("current_depth", 0) < state.get("max_depth", 3):
        return "recursive_decompose"

    # Validate first
    if not state.get("validation_complete"):
        return "validate_decomposition"

    # Then parallel analysis
    return "parallel_analysis"


def route_after_validation(
    state: Dict[str, Any],
) -> Literal["parallel_analysis", "decompose_task", "recursive_decompose"]:
    """Route after validation."""
    validation_result = state.get("validation_result", {})

    if validation_result.get("needs_redecomposition"):
        return "decompose_task"

    if validation_result.get("needs_expansion"):
        return "recursive_decompose"

    return "parallel_analysis"


def route_after_analysis(
    state: Dict[str, Any],
) -> Literal["execution_planning", "optimization", "integrate_analysis"]:
    """Route after parallel analysis completes."""
    # Check if all analyses are complete
    has_complexity = state.get("complexity_vector") is not None
    has_context = state.get("context_requirement") is not None
    has_tree_analysis = state.get("tree_analysis") is not None

    if not (has_complexity and has_context and has_tree_analysis):
        # Should not happen with proper Send usage
        return "integrate_analysis"

    # Check complexity score
    complexity = state.get("complexity_vector")
    if complexity and complexity.total_score() > 7:
        return "optimization"

    return "execution_planning"


def route_final_decision(
    state: Dict[str, Any],
) -> Literal["feasibility_assessment", "optimization", END]:
    """Make final routing decision."""
    execution_plan = state.get("execution_plan")
    integrated_analysis = state.get("integrated_analysis")

    if not execution_plan:
        return END

    # Check if optimization needed
    if execution_plan.optimization_opportunities:
        return "optimization"

    # Check if feasibility assessment needed
    if not state.get("feasibility_assessed"):
        return "feasibility_assessment"

    return END


# ============================================================================
# NODE FUNCTIONS WITH PROPER SIGNATURES
# ============================================================================


def parallel_analysis_orchestrator(
    state: Dict[str, Any],
) -> Command[Literal["complexity_assessment", "context_analysis", "tree_analysis"]]:
    """Orchestrate parallel analysis using Send."""
    task_node = state["task_node"]
    task_tree = TaskTree(task_node)

    # Prepare data for each analysis
    tree_summary = task_tree.get_analysis_summary()

    # Create Send objects for parallel execution
    sends = []

    # Send to complexity assessment
    sends.append(
        Send(
            "complexity_assessment",
            {
                **state,
                "task_details": task_node.description,
                "depth": tree_summary["max_depth"],
                "breadth": len(task_tree.get_parallel_groups()),
                "total_nodes": tree_summary["total_tasks"],
                "dependency_count": len(task_node.dependencies),
                "has_cycles": False,
                "task_tree_summary": str(task_node),
                "parallel_count": len(task_tree.get_parallel_groups()),
                "join_points": tree_summary["join_points"],
                "critical_path_length": tree_summary["critical_path_length"],
            },
        )
    )

    # Send to context analysis
    sends.append(
        Send(
            "context_analysis",
            {
                **state,
                "task_description": task_node.description,
                "task_type": task_node.task_type.value,
                "domain": state.get("domain", "general"),
                "subtask_list": "\n".join(
                    [f"- {st.name}" for st in task_node.subtasks]
                ),
                "dependencies": str(task_node.dependencies),
            },
        )
    )

    # Send to tree structure analysis
    sends.append(
        Send(
            "tree_analysis",
            {
                **state,
                "tree_visualization": (
                    task_tree.pretty_print()
                    if hasattr(task_tree, "pretty_print")
                    else str(task_tree)
                ),
                "max_depth": tree_summary["max_depth"],
                "max_breadth": len(task_tree.get_parallel_groups()),
                "total_nodes": tree_summary["total_tasks"],
                "leaf_nodes": len([n for n in task_node.get_all_steps()]),
                "balance_factor": 0.8,  # Simplified
            },
        )
    )

    return Command(goto=sends)


def join_analyses(
    state: Dict[str, Any],
) -> Command[Literal["execution_planning", "optimization", "integrate_analysis"]]:
    """Join parallel analyses and route next."""
    # All analyses should be complete at this point
    return Command(update={"analyses_complete": True}, goto=route_after_analysis(state))


def recursive_expansion_orchestrator(
    state: Dict[str, Any],
) -> Command[Literal["recursive_decompose", "validate_decomposition"]]:
    """Orchestrate recursive decomposition."""
    task_node = state["task_node"]

    # Find expandable subtasks
    expandable_tasks = [
        subtask
        for subtask in task_node.subtasks
        if isinstance(subtask, TaskNode) and subtask.can_expand
    ]

    if not expandable_tasks:
        return Command(goto="validate_decomposition")

    # Take first expandable task
    task_to_expand = expandable_tasks[0]

    # Send to recursive decomposer
    return Command(
        update={
            "parent_task_name": task_node.name,
            "parent_context": task_node.description,
            "task_description": task_to_expand.description,
            "expansion_reason": task_to_expand.expansion_hints or "Needs more detail",
            "current_depth": state.get("current_depth", 0) + 1,
            "inherited_constraints": [],
        },
        goto="recursive_decompose",
    )


# ============================================================================
# MAIN AGENT CLASS
# ============================================================================


class TaskAnalysisAgent(Agent):
    """
    Comprehensive task analysis agent that orchestrates multiple analysis engines.

    This agent:
    1. Decomposes tasks hierarchically
    2. Analyzes complexity across multiple dimensions
    3. Identifies parallelization opportunities
    4. Plans execution with resource allocation
    5. Provides integrated analysis and recommendations
    """

    # ========================================================================
    # ENGINE DEFINITIONS
    # ========================================================================

    engines: Dict[str, Any] = Field(
        default_factory=lambda: {
            # Decomposition engines
            "task_decomposer": TaskDecomposerEngine,
            "recursive_decomposer": RecursiveDecomposerEngine,
            "task_validator": TaskValidationEngine,
            # Analysis engines
            "complexity_assessor": ComplexityAssessorEngine,
            "complexity_factors": ComplexityFactorsEngine,
            "context_analyzer": ContextAnalyzerEngine,
            "tree_analyzer": TreeStructureAnalyzerEngine,
            # Planning engines
            "execution_planner": ExecutionPlannerEngine,
            "join_strategist": JoinPointStrategyEngine,
            # Integration engines
            "integrated_analyzer": IntegratedAnalyzerEngine,
            "feasibility_assessor": FeasibilityAssessorEngine,
            "optimizer": OptimizationRecommenderEngine,
        }
    )

    # Configuration
    max_decomposition_depth: int = Field(
        default=4, description="Maximum task decomposition depth"
    )
    enable_recursive_decomposition: bool = Field(
        default=True, description="Enable recursive task expansion"
    )
    parallel_analysis: bool = Field(
        default=True, description="Run analyses in parallel"
    )

    # ========================================================================
    # SCHEMA SETUP
    # ========================================================================

    def setup_agent(self):
        """Set up the agent with proper schema composition."""
        # Ensure schema generation
        self.set_schema = True

        # Create comprehensive state schema
        composer = SchemaComposer(name="TaskAnalysisState")

        # Core fields
        composer.add_field(
            "task_description", str, default="", description="Original task description"
        )
        composer.add_field("domain", str, default="general", description="Task domain")
        composer.add_field(
            "additional_context", str, default="", description="Additional context"
        )

        # Decomposition fields
        composer.add_field("task_node", Optional[TaskNode], default=None)
        composer.add_field("task_plan", Optional[TaskPlan], default=None)
        composer.add_field("current_depth", int, default=0)
        composer.add_field("max_depth", int, default=4)

        # Analysis results
        composer.add_field(
            "complexity_vector", Optional[ComplexityVector], default=None
        )
        composer.add_field(
            "context_requirement", Optional[ContextRequirement], default=None
        )
        composer.add_field("tree_analysis", Optional[Dict[str, Any]], default=None)
        composer.add_field("execution_plan", Optional[ExecutionPlan], default=None)

        # Process tracking
        composer.add_field("validation_complete", bool, default=False)
        composer.add_field("analyses_complete", bool, default=False)
        composer.add_field("feasibility_assessed", bool, default=False)

        # Results
        composer.add_field(
            "integrated_analysis", Optional[Dict[str, Any]], default=None
        )
        composer.add_field("recommendations", List[str], default_factory=list)
        composer.add_field("final_report", Optional[str], default=None)

        self.state_schema = composer.build()

    # ========================================================================
    # GRAPH BUILDING
    # ========================================================================

    def build_graph(self) -> BaseGraph:
        """Build the task analysis workflow graph."""
        graph = BaseGraph(name="Task Analysis Workflow")

        # ====================================================================
        # DECOMPOSITION PHASE
        # ====================================================================

        # Initial decomposition
        graph.add_node(
            "decompose_task",
            EngineNodeConfig(
                name="decompose_task", engine=self.engines["task_decomposer"]
            ),
        )
        graph.add_edge(START, "decompose_task")

        # Validation
        graph.add_node(
            "validate_decomposition",
            EngineNodeConfig(
                name="validate_decomposition", engine=self.engines["task_validator"]
            ),
        )

        # Recursive decomposition
        if self.enable_recursive_decomposition:
            graph.add_node(
                "recursive_decompose",
                EngineNodeConfig(
                    name="recursive_decompose",
                    engine=self.engines["recursive_decomposer"],
                ),
            )
            graph.add_node("recursive_orchestrator", recursive_expansion_orchestrator)

        # ====================================================================
        # PARALLEL ANALYSIS PHASE
        # ====================================================================

        # Orchestrator node
        graph.add_node("parallel_analysis", parallel_analysis_orchestrator)

        # Analysis nodes
        graph.add_node(
            "complexity_assessment",
            EngineNodeConfig(
                name="complexity_assessment", engine=self.engines["complexity_assessor"]
            ),
        )

        graph.add_node(
            "context_analysis",
            EngineNodeConfig(
                name="context_analysis", engine=self.engines["context_analyzer"]
            ),
        )

        graph.add_node(
            "tree_analysis",
            EngineNodeConfig(
                name="tree_analysis", engine=self.engines["tree_analyzer"]
            ),
        )

        # Join node
        graph.add_node("join_analyses", join_analyses)

        # ====================================================================
        # PLANNING PHASE
        # ====================================================================

        graph.add_node(
            "execution_planning",
            EngineNodeConfig(
                name="execution_planning", engine=self.engines["execution_planner"]
            ),
        )

        # ====================================================================
        # INTEGRATION PHASE
        # ====================================================================

        graph.add_node(
            "integrate_analysis",
            EngineNodeConfig(
                name="integrate_analysis", engine=self.engines["integrated_analyzer"]
            ),
        )

        graph.add_node(
            "feasibility_assessment",
            EngineNodeConfig(
                name="feasibility_assessment",
                engine=self.engines["feasibility_assessor"],
            ),
        )

        graph.add_node(
            "optimization",
            EngineNodeConfig(name="optimization", engine=self.engines["optimizer"]),
        )

        # ====================================================================
        # EDGES AND ROUTING
        # ====================================================================

        # From decomposition
        graph.add_conditional_edges(
            "decompose_task",
            route_after_decomposition,
            {
                "validate_decomposition": "validate_decomposition",
                "recursive_decompose": "recursive_orchestrator",
                "parallel_analysis": "parallel_analysis",
            },
        )

        # From validation
        graph.add_conditional_edges(
            "validate_decomposition",
            route_after_validation,
            {
                "decompose_task": "decompose_task",
                "recursive_decompose": "recursive_orchestrator",
                "parallel_analysis": "parallel_analysis",
            },
        )

        # From recursive decomposition
        if self.enable_recursive_decomposition:
            graph.add_edge("recursive_decompose", "validate_decomposition")
            graph.add_edge("recursive_orchestrator", "recursive_decompose")

        # From parallel analyses back to join
        graph.add_edge("complexity_assessment", "join_analyses")
        graph.add_edge("context_analysis", "join_analyses")
        graph.add_edge("tree_analysis", "join_analyses")

        # From join to next phase
        graph.add_conditional_edges(
            "join_analyses",
            route_after_analysis,
            {
                "execution_planning": "execution_planning",
                "optimization": "optimization",
                "integrate_analysis": "integrate_analysis",
            },
        )

        # From execution planning
        graph.add_edge("execution_planning", "integrate_analysis")

        # From integration
        graph.add_conditional_edges(
            "integrate_analysis",
            route_final_decision,
            {
                "feasibility_assessment": "feasibility_assessment",
                "optimization": "optimization",
                END: END,
            },
        )

        # From feasibility
        graph.add_edge("feasibility_assessment", END)

        # From optimization
        graph.add_edge("optimization", "execution_planning")

        return graph

    # ========================================================================
    # CONVENIENCE METHODS
    # ========================================================================

    def analyze_task(
        self,
        task_description: str,
        domain: str = "general",
        additional_context: str = "",
        max_depth: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Analyze a task comprehensively.

        Args:
            task_description: Natural language task description
            domain: Task domain (e.g., "software", "research", "creative")
            additional_context: Any additional context
            max_depth: Maximum decomposition depth (uses default if None)

        Returns:
            Comprehensive analysis results
        """
        return self.invoke(
            {
                "task_description": task_description,
                "domain": domain,
                "additional_context": additional_context,
                "max_depth": max_depth or self.max_decomposition_depth,
            }
        )

    def get_execution_plan(
        self, analysis_result: Dict[str, Any]
    ) -> Optional[ExecutionPlan]:
        """Extract execution plan from analysis results."""
        return analysis_result.get("execution_plan")

    def get_complexity_assessment(
        self, analysis_result: Dict[str, Any]
    ) -> Optional[ComplexityVector]:
        """Extract complexity assessment from analysis results."""
        return analysis_result.get("complexity_vector")

    def get_recommendations(self, analysis_result: Dict[str, Any]) -> List[str]:
        """Extract recommendations from analysis results."""
        return analysis_result.get("recommendations", [])
