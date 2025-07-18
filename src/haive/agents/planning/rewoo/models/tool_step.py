"""
Tool Step Model - Generic step that validates against a tool list

A concrete step implementation that works with LangChain tools and validates:
- Tool exists in provided tool list
- Tool arguments match tool schema
- Tool can be executed with given parameters
"""

import inspect
from typing import Any, Dict, List, Optional, Set

from langchain_core.tools import BaseTool
from pydantic import Field, computed_field, field_validator, model_validator

from .steps import AbstractStep


class ToolStep(AbstractStep):
    """A step that executes a specific tool with validated arguments."""

    # Tool execution fields
    tool_name: str = Field(..., description="Name of the tool to execute")

    tool_args: Dict[str, Any] = Field(
        default_factory=dict, description="Arguments to pass to the tool"
    )

    # Tool registry - this will be validated against
    available_tools: List[BaseTool] = Field(
        ..., description="List of available tools for validation"
    )

    # Execution result storage
    result: Optional[Any] = Field(
        default=None, description="Result from tool execution"
    )

    # Computed fields
    @computed_field
    @property
    def tool_names(self) -> List[str]:
        """List of available tool names."""
        return [tool.name for tool in self.available_tools]

    @computed_field
    @property
    def selected_tool(self) -> Optional[BaseTool]:
        """The selected tool instance."""
        return next(
            (tool for tool in self.available_tools if tool.name == self.tool_name), None
        )

    @computed_field
    @property
    def tool_schema(self) -> Optional[Dict[str, Any]]:
        """Schema of the selected tool."""
        if self.selected_tool:
            return (
                self.selected_tool.args_schema.model_json_schema()
                if self.selected_tool.args_schema
                else None
            )
        return None

    @computed_field
    @property
    def required_args(self) -> List[str]:
        """Required arguments for the selected tool."""
        if not self.tool_schema:
            return []

        properties = self.tool_schema.get("properties", {})
        required = self.tool_schema.get("required", [])
        return required

    @computed_field
    @property
    def optional_args(self) -> List[str]:
        """Optional arguments for the selected tool."""
        if not self.tool_schema:
            return []

        properties = self.tool_schema.get("properties", {})
        required = self.tool_schema.get("required", [])
        return [arg for arg in properties.keys() if arg not in required]

    @computed_field
    @property
    def is_tool_valid(self) -> bool:
        """Whether the tool setup is valid."""
        return self.tool_name in self.tool_names and self._are_args_valid()

    # Validators
    @field_validator("tool_name")
    @classmethod
    def validate_tool_name(cls, v: str, info) -> str:
        """Validate tool name exists in available tools."""
        # Note: We can't access other fields here, so this will be checked in model_validator
        if not v:
            raise ValueError("Tool name cannot be empty")
        return v

    @field_validator("available_tools")
    @classmethod
    def validate_tools_not_empty(cls, v: List[BaseTool]) -> List[BaseTool]:
        """Validate tools list is not empty."""
        if not v:
            raise ValueError("Available tools list cannot be empty")

        # Check for duplicate tool names
        tool_names = [tool.name for tool in v]
        if len(tool_names) != len(set(tool_names)):
            raise ValueError("Duplicate tool names found in available_tools")

        return v

    @model_validator(mode="after")
    def validate_tool_exists_and_args(self) -> "ToolStep":
        """Validate tool exists and arguments are correct."""
        # Check tool exists
        if self.tool_name not in self.tool_names:
            raise ValueError(
                f"Tool '{self.tool_name}' not found. Available tools: {', '.join(self.tool_names)}"
            )

        # Validate arguments
        if not self._are_args_valid():
            missing_args = set(self.required_args) - set(self.tool_args.keys())
            if missing_args:
                raise ValueError(
                    f"Missing required arguments for tool '{self.tool_name}': {', '.join(missing_args)}"
                )

            # Check for invalid arguments
            valid_args = set(self.required_args + self.optional_args)
            invalid_args = set(self.tool_args.keys()) - valid_args
            if invalid_args:
                raise ValueError(
                    f"Invalid arguments for tool '{self.tool_name}': {', '.join(invalid_args)}"
                )

        return self

    # Helper methods
    def _are_args_valid(self) -> bool:
        """Check if tool arguments are valid."""
        if not self.selected_tool:
            return False

        # Check required arguments are present
        missing_required = set(self.required_args) - set(self.tool_args.keys())
        if missing_required:
            return False

        # Check no invalid arguments
        valid_args = set(self.required_args + self.optional_args)
        invalid_args = set(self.tool_args.keys()) - valid_args
        if invalid_args:
            return False

        return True

    # Abstract method implementations
    def can_execute(self, completed_steps: Set[str]) -> bool:
        """Check if this step can execute."""
        return (
            all(dep in completed_steps for dep in self.depends_on)
            and self.is_tool_valid
        )

    def execute(self, context: Dict[str, Any]) -> Any:
        """Execute the tool with the provided arguments."""
        if not self.can_execute(context.get("completed_steps", set())):
            raise ValueError(
                "Step cannot be executed - dependencies not met or tool invalid"
            )

        if not self.selected_tool:
            raise ValueError(f"Tool '{self.tool_name}' not found")

        try:
            # Execute the tool
            result = self.selected_tool.invoke(self.tool_args)
            self.result = result
            return result

        except Exception as e:
            error_result = f"Tool execution failed: {str(e)}"
            self.result = error_result
            raise RuntimeError(error_result)

    # Utility methods
    def get_tool_info(self) -> Dict[str, Any]:
        """Get comprehensive tool information."""
        if not self.selected_tool:
            return {"error": "Tool not found"}

        return {
            "name": self.tool_name,
            "description": self.selected_tool.description,
            "required_args": self.required_args,
            "optional_args": self.optional_args,
            "provided_args": list(self.tool_args.keys()),
            "missing_args": list(set(self.required_args) - set(self.tool_args.keys())),
            "schema": self.tool_schema,
            "is_valid": self.is_tool_valid,
        }

    def update_tool_args(self, **kwargs):
        """Update tool arguments and revalidate."""
        self.tool_args.update(kwargs)
        # Pydantic will automatically revalidate

    def clear_tool_args(self):
        """Clear all tool arguments."""
        self.tool_args = {}

    @classmethod
    def create_from_tool(
        cls,
        tool: BaseTool,
        tool_args: Dict[str, Any],
        available_tools: List[BaseTool],
        description: str = None,
        **kwargs,
    ) -> "ToolStep":
        """Factory method to create ToolStep from a tool instance."""
        return cls(
            description=description or f"Execute {tool.name} tool",
            tool_name=tool.name,
            tool_args=tool_args,
            available_tools=available_tools,
            **kwargs,
        )


# Factory functions for common patterns
def create_tool_steps_from_plan(
    tool_plan: List[Dict[str, Any]], available_tools: List[BaseTool]
) -> List[ToolStep]:
    """Create a list of ToolSteps from a plan description."""
    steps = []

    for i, step_info in enumerate(tool_plan):
        step = ToolStep(
            description=step_info.get("description", f"Step {i+1}"),
            tool_name=step_info["tool_name"],
            tool_args=step_info.get("tool_args", {}),
            depends_on=step_info.get("depends_on", []),
            available_tools=available_tools,
        )
        steps.append(step)

    return steps


def validate_tool_compatibility(tools: List[BaseTool]) -> Dict[str, Any]:
    """Validate a list of tools for compatibility issues."""
    tool_names = [tool.name for tool in tools]

    issues = {
        "duplicate_names": [],
        "missing_schemas": [],
        "tools_without_descriptions": [],
        "valid_tools": [],
    }

    # Check for duplicates
    seen_names = set()
    for name in tool_names:
        if name in seen_names:
            issues["duplicate_names"].append(name)
        seen_names.add(name)

    # Check each tool
    for tool in tools:
        if not tool.args_schema:
            issues["missing_schemas"].append(tool.name)

        if not tool.description or tool.description.strip() == "":
            issues["tools_without_descriptions"].append(tool.name)

        if (
            tool.args_schema
            and tool.description
            and tool.description.strip() != ""
            and tool.name not in issues["duplicate_names"]
        ):
            issues["valid_tools"].append(tool.name)

    return issues
