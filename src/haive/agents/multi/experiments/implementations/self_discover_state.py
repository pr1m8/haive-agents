"""State schema for self-discover multi-agent system.
"""

from typing import Any

from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from pydantic import Field

from haive.agents.reasoning_and_critique.self_discover.v2.models import (
    AdaptedModules,
    FinalAnswer,
    Optional,
    ReasoningStructure,
    SelectedModules,
    from,
    import,
    typing,
)


class SelfDiscoverState(MultiAgentState):
    """State schema for self-discover multi-agent workflow.

    This state schema handles the structured output flow between agents:
    1. select_agent: reasoning_modules + task_description → selected_modules
    2. adapt_agent: selected_modules + task_description → adapted_modules
    3. structure_agent: adapted_modules + task_description → reasoning_structure
    4. reason_agent: reasoning_structure + task_description → final_answer
    """

    # Input fields
    reasoning_modules: list[str] = Field(
        default_factory=list, description="List of available reasoning modules"
    )
    task_description: str = Field(
        default="", description="Description of the task to solve"
    )

    # Structured outputs from each agent
    selected_modules: Optional[SelectedModules] = Field(
        default=None, description="Output from select_agent"
    )
    adapted_modules: Optional[AdaptedModules] = Field(
        default=None, description="Output from adapt_agent"
    )
    reasoning_structure: Optional[ReasoningStructure] = Field(
        default=None, description="Output from structure_agent"
    )
    final_answer: Optional[FinalAnswer] = Field(
        default=None, description="Output from reason_agent"
    )

    def get_select_inputs(self) -> dict[str, Any]:
        """Get inputs for select_agent.
        """
        return {
            "reasoning_modules": self.reasoning_modules,
            "task_description": self.task_description,
        }

    def get_adapt_inputs(self) -> dict[str, Any]:
        """Get inputs for adapt_agent.
        """
        if not self.selected_modules:
            raise ValueError("selected_modules not available for adapt_agent")

        # Extract the selected modules list for the prompt
        selected_modules_str = "\n".join(
            [f"- {module}" for module in self.selected_modules.selected_modules]
        )

        return {
            "selected_modules": selected_modules_str,
            "task_description": self.task_description,
        }

    def get_structure_inputs(self) -> dict[str, Any]:
        """Get inputs for structure_agent.
        """
        if not self.adapted_modules:
            raise ValueError(
                "adapted_modules not available for structure_agent")

        # Format adapted modules for the prompt
        adapted_modules_str = "\n".join(
            [
                f"- {mod['module']}: {mod['adaptation']}"
                for mod in self.adapted_modules.adapted_modules
            ]
        )

        return {
            "adapted_modules": adapted_modules_str,
            "task_description": self.task_description,
        }

    def get_reason_inputs(self) -> dict[str, Any]:
        """Get inputs for reason_agent.
        """
        if not self.reasoning_structure:
            raise ValueError(
                "reasoning_structure not available for reason_agent")

        # Format reasoning structure for the prompt
        import json

        reasoning_structure_str = json.dumps(
            self.reasoning_structure.reasoning_structure, indent=2
        )

        return {
            "reasoning_structure": reasoning_structure_str,
            "task_description": self.task_description,
        }

    def update_from_agent_output(
            self, agent_name: str, output: dict[str, Any]) -> None:
        """Update state with agent output.
        """
        if agent_name == "select_modules":
            if "selected_modules" in output:
                self.selected_modules = SelectedModules(
                    **output["selected_modules"])
        elif agent_name == "adapt_modules":
            if "adapted_modules" in output:
                self.adapted_modules = AdaptedModules(
                    **output["adapted_modules"])
        elif agent_name == "create_structure":
            if "reasoning_structure" in output:
                self.reasoning_structure = ReasoningStructure(
                    **output["reasoning_structure"]
                )
        elif agent_name == "final_reasoning" and "final_answer" in output:
            self.final_answer = FinalAnswer(**output["final_answer"])
