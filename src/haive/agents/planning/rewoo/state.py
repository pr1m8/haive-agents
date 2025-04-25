"""
State schema for the ReWOO agent.
"""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

from agents.rewoo.models import RewooPlan

class ReWOOState(BaseModel):
    """
    State schema for the ReWOO agent.
    
    This state tracks:
    - The task to accomplish
    - The generated plan with evidence references
    - Results collected for each evidence reference
    - The final solution after solving
    """
    task: str = ""  # The original task to accomplish
    plan: Optional[RewooPlan] = None  # The plan with evidence references
    results: Dict[str, Dict[str, str]] = Field(
        default_factory=dict,  
        description="Evidence collected, keyed by evidence_ref -> {tool_name: result}"
    )
    current_step_index: Optional[int] = None  # Index of current step in execution
    final_solution: Optional[List[Dict[str, Any]]] = None  # The final solution
    
    def get_current_step(self):
        """
        Get the current step based on the current_step_index.
        
        Returns:
            The current step or None if no current step
        """
        if (self.plan and self.plan.steps and self.current_step_index is not None
                and 0 <= self.current_step_index < len(self.plan.steps)):
            return self.plan.steps[self.current_step_index]
        return None
    
    def is_plan_complete(self) -> bool:
        """
        Check if the plan is complete.
        
        A plan is complete when all steps have evidence collected.
        
        Returns:
            True if plan is complete, False otherwise
        """
        if not self.plan or not self.plan.steps:
            return False
        
        # Check if results contain entries for all evidence references
        return all(step.evidence_ref in self.results for step in self.plan.steps)