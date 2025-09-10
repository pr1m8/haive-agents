"""Structured output handler for clean extraction from LangGraph state.

This module provides utilities to handle LangGraph's AddableValuesDict
return type and extract structured output cleanly.
"""

import re
from typing import Any, Dict, Generic, Optional, Type, TypeVar, Union

from langgraph.pregel.io import AddableValuesDict
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class StructuredOutputHandler(Generic[T]):
    """Handler for extracting structured output from LangGraph results.

    This class provides a clean interface for working with LangGraph's
    AddableValuesDict return type, making it easy to extract structured
    output from graph execution results.

    Examples:
        Basic usage::

            handler = StructuredOutputHandler(AnalysisResult)
            result = await agent.arun(input_data)
            analysis = handler.extract(result)

        With custom field name::

            handler = StructuredOutputHandler(
                AnalysisResult,
                field_name="custom_output"
            )

        With validation::

            analysis = handler.extract_or_raise(result)
            # Raises ValueError if not found
    """

    def __init__(
        self,
        output_model: Type[T],
        field_name: Optional[str] = None,
        common_fields: Optional[list[str]] = None,
    ):
        """Initialize the handler.

        Args:
            output_model: The Pydantic model class for structured output
            field_name: Optional specific field name to extract
            common_fields: Additional field names to check
        """
        self.output_model = output_model
        self.field_name = field_name or self._generate_field_name()
        self.common_fields = common_fields or [
            "analysis_result",
            "task_result",
            "structured_output",
            "output",
            "result",
            self.field_name,
        ]

    def _generate_field_name(self) -> str:
        """Generate field name from model name using robust naming utilities."""
        from haive.core.utils.naming import sanitize_tool_name

        raw_name = self.output_model.__name__

        # Use robust naming utilities to handle generic classes properly
        base_name = sanitize_tool_name(raw_name)

        # Handle common suffixes
        if base_name.endswith("_result"):
            name = base_name[:-7]  # Remove '_result'
        elif base_name.endswith("_output"):
            name = base_name[:-7]  # Remove '_output'
        else:
            name = base_name

        # Add _result suffix
        name += "_result"

        return name

    def extract(self, result: Union[Dict, AddableValuesDict, Any]) -> Optional[T]:
        """Extract structured output from result.

        This method handles various result types including AddableValuesDict,
        regular dicts, and objects with dict-like interfaces.

        Args:
            result: The result from LangGraph execution

        Returns:
            The extracted structured output or None if not found
        """
        # Handle dict-like objects
        if hasattr(result, "items") or isinstance(result, dict):
            # Try configured field name first
            if self.field_name in result:
                value = result[self.field_name]
                if isinstance(value, self.output_model):
                    return value
                elif isinstance(value, dict):
                    # Try to construct from dict
                    try:
                        return self.output_model(**value)
                    except Exception:
                        pass

            # Try common field names
            for field in self.common_fields:
                if field in result:
                    value = result[field]
                    if isinstance(value, self.output_model):
                        return value
                    elif isinstance(value, dict):
                        try:
                            return self.output_model(**value)
                        except Exception:
                            continue

            # Search all fields for the model type
            for key, value in result.items():
                if isinstance(value, self.output_model):
                    return value
                # Also check if it's a dict that can be converted
                elif isinstance(value, dict) and key not in ["messages", "metadata"]:
                    try:
                        # Attempt to validate as our model
                        validated = self.output_model(**value)
                        return validated
                    except Exception:
                        continue

        # Handle direct model instance
        if isinstance(result, self.output_model):
            return result

        return None

    def extract_or_raise(self, result: Any) -> T:
        """Extract structured output or raise an error.

        Args:
            result: The result from LangGraph execution

        Returns:
            The extracted structured output

        Raises:
            ValueError: If structured output not found
        """
        output = self.extract(result)
        if output is None:
            available_keys = []
            if hasattr(result, "keys"):
                available_keys = list(result.keys())

            raise ValueError(
                f"Could not find {self.output_model.__name__} in result. "
                f"Searched fields: {self.common_fields}. "
                f"Available keys: {available_keys}"
            )
        return output

    def extract_or_default(
        self, result: Any, default: Optional[T] = None
    ) -> Optional[T]:
        """Extract structured output or return default.

        Args:
            result: The result from LangGraph execution
            default: Default value to return if not found

        Returns:
            The extracted output or default value
        """
        return self.extract(result) or default

    @property
    def expected_fields(self) -> list[str]:
        """Get list of field names that will be searched."""
        return self.common_fields


def extract_structured_output(
    result: Any, output_model: Type[T], field_name: Optional[str] = None
) -> Optional[T]:
    """Convenience function to extract structured output.

    Args:
        result: The result from LangGraph execution
        output_model: The expected Pydantic model type
        field_name: Optional specific field name

    Returns:
        The extracted structured output or None

    Examples:
        Basic extraction::

            analysis = extract_structured_output(result, AnalysisResult)

        With field name::

            output = extract_structured_output(
                result,
                CustomOutput,
                field_name="my_output"
            )
    """
    handler = StructuredOutputHandler(output_model, field_name)
    return handler.extract(result)


def require_structured_output(
    result: Any, output_model: Type[T], field_name: Optional[str] = None
) -> T:
    """Extract structured output or raise error.

    Args:
        result: The result from LangGraph execution
        output_model: The expected Pydantic model type
        field_name: Optional specific field name

    Returns:
        The extracted structured output

    Raises:
        ValueError: If output not found

    Examples:
        Require output::

            analysis = require_structured_output(result, AnalysisResult)
            # Raises ValueError if not found
    """
    handler = StructuredOutputHandler(output_model, field_name)
    return handler.extract_or_raise(result)


# Type alias for clarity
LangGraphResult = Union[Dict[str, Any], AddableValuesDict]
