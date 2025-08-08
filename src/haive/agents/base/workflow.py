"""Workflow base class - Pure workflow orchestration without engine dependencies.

This module provides the abstract Workflow class for building pure orchestration
workflows that handle routing, transformation, and coordination without requiring
language model engines.

Classes:
    Workflow: Abstract base class for pure workflow orchestration.

Example:
    Creating a simple data processing workflow::

        from haive.agents.base.workflow import Workflow

        class DataProcessor(Workflow):
            async def execute(self, data):
                # Pure processing logic, no LLM
                processed = transform_data(data)
                validated = validate_data(processed)
                return validated

        processor = DataProcessor(name="data_processor")
        result = await processor.execute(raw_data)

See Also:
    :class:`haive.agents.base.agent.Agent`: Full agent with engine support
"""

import re
from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field, model_validator


class Workflow(BaseModel, ABC):
    """Pure workflow orchestration without engine dependencies.

    Workflow handles pure orchestration - routing, transformation,
    coordination - without requiring engines. This is the foundation
    for building lightweight workflow components.

    Attributes:
        name: Name of the workflow, auto-generated from class name if not provided.
        verbose: Enable verbose logging for detailed execution information.
        debug: Enable debug mode for additional diagnostics.

    Examples:
        Data processing workflow::

            class DataProcessor(Workflow):
                async def execute(self, data):
                    # Pure processing, no LLM
                    return processed_data

        Routing workflow::

            class Router(Workflow):
                async def execute(self, request):
                    # Route to appropriate handler
                    return route_decision

    Note:
        This is an abstract base class. Subclasses must implement the
        execute() method to define the workflow logic.
    """

    name: str = Field(default="Workflow", description="Name of the workflow")
    verbose: bool = Field(default=False, description="Enable verbose logging")
    debug: bool = Field(default=False, description="Enable debug mode")

    @model_validator(mode="before")
    @classmethod
    def auto_generate_name(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Auto-generate workflow name from class name if not provided.

        Converts CamelCase class names to space-separated names for better
        readability in logs and debugging.

        Args:
            values: Dictionary of field values before validation.

        Returns:
            Updated values dictionary with auto-generated name if needed.
        """
        if not isinstance(values, dict):
            return values
        if "name" not in values or not values["name"] or values["name"] == "Workflow":
            class_name = cls.__name__
            # Convert CamelCase to space-separated
            name = re.sub("([a-z0-9])([A-Z])", "\\1 \\2", class_name)
            values["name"] = name
        return values

    @abstractmethod
    async def execute(self, input_data: Any) -> Any:
        """Execute the workflow logic.

        This method must be implemented by subclasses to define the
        specific workflow behavior.

        Args:
            input_data: Input data for the workflow. Type depends on the
                specific workflow implementation.

        Returns:
            Output data from the workflow. Type depends on the specific
            workflow implementation.

        Raises:
            NotImplementedError: If not implemented by subclass.
        """

    def __repr__(self) -> str:
        """String representation of the workflow."""
        return f"{self.__class__.__name__}(name='{self.name}')"
