"""ReWOO V3 State Schema with computed fields for dynamic prompts.

This module defines the state schema for ReWOO V3 Agent using our proven
MessagesState + computed fields pattern from Plan-and-Execute V3 success.
"""

from datetime import datetime
from typing import Any

from haive.core.schema.prebuilt.messages_state import MessagesState
from pydantic import Field, computed_field

from .models import EvidenceCollection, ReWOOPlan


class ReWOOV3State(MessagesState):
    """State schema for ReWOO V3 with computed fields for prompt templates.

    ReWOO (Reasoning WithOut Observation) separates planning, execution, and synthesis:
    1. Planner creates complete plan upfront with evidence placeholders
    2. Worker executes all tool calls to collect evidence
    3. Solver synthesizes all evidence into final answer

    This state tracks the complete ReWOO workflow with dynamic computed fields
    for prompt template variable substitution.
    """

    # Core workflow data
    original_query: str = Field(description="Original user query to solve")
    current_phase: str = Field(default="planning", description="Current ReWOO phase")

    # Agent results (stored as dicts for state persistence, typed through models)
    reasoning_plan: dict[str, Any] | None = Field(
        default=None,
        description="Planner agent structured output with evidence placeholders",
    )
    evidence_collection: dict[str, Any] | None = Field(
        default=None, description="Worker agent evidence collection results"
    )
    final_solution: dict[str, Any] | None = Field(
        default=None, description="Solver agent final synthesized answer"
    )

    # Execution tracking
    started_at: datetime = Field(default_factory=datetime.now)
    planning_completed_at: datetime | None = Field(default=None)
    execution_completed_at: datetime | None = Field(default=None)
    solving_completed_at: datetime | None = Field(default=None)

    # Metadata
    tools_available: list[str] = Field(
        default_factory=list, description="Available tool names"
    )
    execution_metadata: dict[str, Any] = Field(default_factory=dict)

    # CRITICAL: Computed fields for ChatPromptTemplate placeholders

    @computed_field
    @property
    def available_tools(self) -> str:
        """Formatted list of available tools for planner prompt."""
        if not self.tools_available:
            return "No tools available"
        return ", ".join(self.tools_available)

    @computed_field
    @property
    def plan_summary(self) -> str:
        """Formatted plan for worker agent prompt."""
        if not self.reasoning_plan:
            return "No plan available"

        try:
            plan = ReWOOPlan(**self.reasoning_plan)
            summary = f"Plan ID: {plan.plan_id}\n"
            summary += f"Objective: {plan.objective}\n\n"
            summary += f"Approach: {plan.approach}\n\n"
            summary += "Execution Steps:\n"

            for i, step in enumerate(plan.steps, 1):
                summary += f"{i}. {step.description}\n"
                summary += f"   Evidence Placeholder: {step.evidence_id}\n"
                if step.tool_call:
                    summary += f"   Suggested Tool: {step.tool_call}\n"
                if step.depends_on:
                    summary += f"   Depends on: {', '.join(step.depends_on)}\n"
                summary += "\n"

            summary += "Expected Evidence Map:\n"
            for evidence_id, description in plan.expected_evidence.items():
                summary += f"- {evidence_id}: {description}\n"

            return summary
        except Exception as e:
            return f"Plan parsing error: {e}"

    @computed_field
    @property
    def evidence_summary(self) -> str:
        """Formatted evidence for solver agent prompt."""
        if not self.evidence_collection:
            return "No evidence collected"

        try:
            collection = EvidenceCollection(**self.evidence_collection)
            summary = f"Evidence Collection ID: {collection.collection_id}\n"
            summary += f"Collection Summary: {collection.summary}\n\n"
            summary += f"Success Rate: {collection.success_count}/{collection.success_count + collection.failure_count}\n"
            summary += f"Tools Used: {', '.join(collection.tools_used)}\n\n"

            summary += "Collected Evidence:\n"
            for evidence in collection.evidence_items:
                summary += f"\n{evidence.evidence_id} (Step: {evidence.step_id}):\n"
                summary += f"Status: {evidence.status.value}\n"
                summary += f"Source: {evidence.source}\n"
                summary += f"Content: {evidence.content}\n"
                if evidence.metadata:
                    summary += f"Metadata: {evidence.metadata}\n"

            if collection.execution_notes:
                summary += "\nExecution Notes:\n"
                for note in collection.execution_notes:
                    summary += f"- {note}\n"

            return summary
        except Exception as e:
            return f"Evidence parsing error: {e}"

    @computed_field
    @property
    def execution_status(self) -> str:
        """Current ReWOO workflow status for prompts."""
        if not self.reasoning_plan:
            return "Planning phase - creating reasoning plan"
        if not self.evidence_collection:
            return "Execution phase - collecting evidence from tools"
        if not self.final_solution:
            return "Synthesis phase - combining evidence into final answer"
        return "ReWOO workflow completed"

    @computed_field
    @property
    def workflow_context(self) -> str:
        """Complete workflow context for solver synthesis."""
        context = f"Original Query: {self.original_query}\n\n"
        context += f"Current Status: {self.execution_status}\n\n"

        if self.reasoning_plan:
            context += "REASONING PLAN:\n"
            context += f"{self.plan_summary}\n\n"

        if self.evidence_collection:
            context += "EVIDENCE COLLECTED:\n"
            context += f"{self.evidence_summary}\n\n"

        # Add timing information
        if self.planning_completed_at:
            planning_time = (
                self.planning_completed_at - self.started_at
            ).total_seconds()
            context += f"Planning Time: {planning_time:.2f}s\n"

        if self.execution_completed_at and self.planning_completed_at:
            execution_time = (
                self.execution_completed_at - self.planning_completed_at
            ).total_seconds()
            context += f"Execution Time: {execution_time:.2f}s\n"

        return context

    @computed_field
    @property
    def phase_progress(self) -> str:
        """Progress through ReWOO phases for prompts."""
        phases = []
        if self.reasoning_plan:
            phases.append("✅ Planning")
        else:
            phases.append("🔄 Planning")

        if self.evidence_collection:
            phases.append("✅ Execution")
        else:
            phases.append("⏸️ Execution")

        if self.final_solution:
            phases.append("✅ Synthesis")
        else:
            phases.append("⏸️ Synthesis")

        return " → ".join(phases)

    # State update methods
    def update_planning_result(self, plan_result: dict[str, Any]) -> None:
        """Update with planner agent result."""
        self.reasoning_plan = plan_result
        self.current_phase = "execution"
        self.planning_completed_at = datetime.now()

    def update_execution_result(self, execution_result: dict[str, Any]) -> None:
        """Update with worker agent result."""
        self.evidence_collection = execution_result
        self.current_phase = "synthesis"
        self.execution_completed_at = datetime.now()

    def update_solution_result(self, solution_result: dict[str, Any]) -> None:
        """Update with solver agent result."""
        self.final_solution = solution_result
        self.current_phase = "completed"
        self.solving_completed_at = datetime.now()
