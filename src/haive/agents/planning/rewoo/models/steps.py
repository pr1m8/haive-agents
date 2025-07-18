"""
Step Models for ReWOO Planning

Abstract step class and concrete implementations with computed fields and validators.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Set
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, computed_field, field_validator


class AbstractStep(BaseModel, ABC):
    """Abstract base step that other steps inherit from."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    # Core identity - every step needs these
    id: str = Field(
        default_factory=lambda: f"step_{uuid4().hex[:8]}",
        description="Unique step identifier",
    )

    description: str = Field(
        ..., min_length=1, max_length=1000, description="What this step does"
    )

    # Dependencies - fundamental to any step
    depends_on: List[str] = Field(
        default_factory=list, description="Step IDs this step depends on"
    )

    # Basic field validators
    @field_validator("id")
    @classmethod
    def validate_id(cls, v: str) -> str:
        """Validate step ID format."""
        if not v.replace("_", "").replace("-", "").isalnum():
            raise ValueError("Step ID must be alphanumeric with underscores/hyphens")
        return v

    @field_validator("depends_on")
    @classmethod
    def validate_dependencies(cls, v: List[str]) -> List[str]:
        """Validate dependency IDs."""
        for dep in v:
            if not dep.replace("_", "").replace("-", "").isalnum():
                raise ValueError(f"Dependency '{dep}' must be alphanumeric")
        return v

    # Computed fields - these are implicit/automatic
    @computed_field
    @property
    def has_dependencies(self) -> bool:
        """Whether this step has dependencies."""
        return len(self.depends_on) > 0

    @computed_field
    @property
    def dependency_count(self) -> int:
        """Number of dependencies."""
        return len(self.depends_on)

    # Abstract methods that subclasses must implement
    @abstractmethod
    def can_execute(self, completed_steps: Set[str]) -> bool:
        """Check if this step can execute given completed steps."""
        pass

    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> Any:
        """Execute this step with given context."""
        pass


class BasicStep(AbstractStep):
    """Basic concrete implementation for testing."""

    def can_execute(self, completed_steps: Set[str]) -> bool:
        """Basic implementation - all dependencies must be completed."""
        return all(dep in completed_steps for dep in self.depends_on)

    def execute(self, context: Dict[str, Any]) -> Any:
        """Basic execution - just return the description."""
        return f"Executed: {self.description}"
