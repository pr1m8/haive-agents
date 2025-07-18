"""State schema for Plan and Execute Agent v2."""

from typing import List, Optional

from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from pydantic import Field

from haive.agents.planning.plan_and_execute.v2.models import Plan, Step


class PlanAndExecuteState(MultiAgentState):
    """State for Plan and Execute Agent v2."""

    input: str = Field(..., description="The original user query or objective")
    plan: Optional[Plan] = Field(
        default=None, description="The current plan with steps"
    )
    past_steps: List[Step] = Field(
        default_factory=list, description="List of completed steps"
    )
    response: Optional[str] = Field(
        default=None, description="Current response or output"
    )
    final_response: Optional[str] = Field(
        default=None, description="Final response when complete"
    )

    def update_past_steps(self, step: Step) -> None:
        """Add completed step to past_steps."""
        if step.is_complete():
            self.past_steps.append(step)
            if self.plan:
                self.plan.update_status()

    def get_next_step(self) -> Optional[Step]:
        """Get the next incomplete step."""
        if not self.plan:
            return None
        return self.plan.get_next_step()

    def is_plan_complete(self) -> bool:
        """Check if the plan is complete."""
        return self.plan is not None and self.plan.status == "complete"
