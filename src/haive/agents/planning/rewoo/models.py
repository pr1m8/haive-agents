from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import List, Union, Optional, Type, Dict, ClassVar,Any
from langchain_core.tools import BaseTool, StructuredTool
from agents.plan_and_execute.models import Step, Plan
from pydantic_core.core_schema import ValidationInfo
from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import List, Union, Optional, Type, Dict, ClassVar
from langchain_core.tools import BaseTool, StructuredTool
from pydantic_core.core_schema import ValidationInfo


class ToolCall(BaseModel):
    """Represents a tool call referencing LangChain tools, structured tools, or LLM."""

    name: str = Field(description="Name of the tool to use (or 'LLM')")
    input: Optional[Union[str, Dict[Any]]] = Field(
        description="Input to pass to the tool (or task for LLM)", default=None
    )
    tool: Optional[Union[BaseTool, StructuredTool]] = None  # Supports multiple tool types

    available_tools: ClassVar[Dict[str, Union[Type[BaseTool], Type[StructuredTool]]]] = {}

    @classmethod
    def set_available_tools(cls, tools: List[Union[BaseTool, StructuredTool]]):
        """Registers available tools and ensures their input schemas are accessible."""
        cls.available_tools = {tool.name: tool for tool in tools}
        cls.available_tools["LLM"] = None  # ✅ LLM special case

    @field_validator("name")
    def validate_tool_name(cls, v, values: ValidationInfo):
        """Ensures the tool name exists in the available tool list."""
        if v not in cls.available_tools:
            raise ValueError(f"Invalid tool name '{v}'. Must be one of {list(cls.available_tools.keys())}")
        return v

    @field_validator("input", mode="before")
    def validate_tool_input(cls, v, values: ValidationInfo):
        """Ensures the input format matches the expected tool input structure."""
        name = values.data.get("name")

        if v is None:
            return None  # ✅ Allow None

        if isinstance(v, str) and v.startswith("#E"):
            return v  # ✅ Keep evidence references as placeholders


class RewooStep(Step):
    """Extends Step to include evidence references and optional tool calls."""

    evidence_ref: Optional[str] = Field(
        default=None, description="Reference ID for this evidence (e.g., #E1). None if no evidence."
    )
    tool_calls: Optional[List[ToolCall]] = Field(
        default=None, description="List of tool calls (optional, LLM may handle step)."
    )
    result: Optional[str] = Field(default=None, description="Result of this step.")

    @field_validator("evidence_ref", mode="before")
    def validate_evidence_ref(cls, v):
        """Ensure evidence references start with #E and allow None."""
        if v is not None and not v.startswith("#E"):
            raise ValueError("Evidence reference must start with #E")
        return v
class RewooPlan(Plan):
    """Extends Plan to integrate Rewoo-style steps and update evidence references."""

    steps: List[RewooStep] = Field(default_factory=list, description="Rewoo-style steps in the plan")

    def add_rewoo_step(self, step: RewooStep):
        """Adds a new RewooStep to the plan."""
        self.steps.append(step)

    def remove_completed_steps(self):
        """Removes completed steps from the plan."""
        self.steps = [step for step in self.steps if not step.is_complete()]

    def update_evidence_references(self, results: Dict[str, str]):
        """Ensures evidence references correctly map to results."""
        for step in self.steps:
            if step.evidence_ref and step.evidence_ref in results:
                step.result = results[step.evidence_ref]  # ✅ Update step with evidence result
