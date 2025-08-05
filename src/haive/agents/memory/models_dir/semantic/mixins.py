from datetime import datetime
from typing import Any, Literal
from pydantic import BaseModel, Field, field_validator, model_validator


class UserContextMixin:
    """Mixin for user-specific context management."""

    def get_context_summary(self) -> str:
        """Generate contextual summary."""
        raise NotImplementedError

    def update_context(self, new_data: dict[str, Any]) -> None:
        """Update contextual information."""
        raise NotImplementedError


class TemporalMixin:
    """Mixin for temporal memory management."""

    @field_validator("temporal_weight")
    @classmethod
    def validate_temporal_weight(cls, v: float) -> float:
        """Validate temporal decay weight."""
        if not 0.0 <= v <= 1.0:
            raise ValueError("Temporal weight must be between 0.0 and 1.0")
        return v

    def calculate_temporal_relevance(self) -> float:
        """Calculate temporal relevance based on age and access patterns."""
        age_days = (datetime.now() - self.created_at).days
        decay_factor = 0.95**age_days
        access_boost = min(self.access_count * 0.1, 0.5)
        return min(decay_factor + access_boost, 1.0)


class PersonalityTraits(BaseModel):
    """Sophisticated personality modeling."""

    communication_style: Literal["formal", "casual", "technical", "friendly", "direct"] = Field(
        default="friendly", description="Preferred communication style"
    )
    expertise_areas: list[str] = Field(default_factory=list, description="Known expertise areas")
    interaction_preferences: dict[str, Any] = Field(
        default_factory=dict, description="Interaction preferences"
    )
    cultural_context: str | None = Field(None, description="Cultural background context")
    language_preferences: list[str] = Field(
        default_factory=lambda: ["English"], description="Preferred languages"
    )

    @field_validator("expertise_areas")
    @classmethod
    def validate_expertise(cls, v: list[str]) -> list[str]:
        """Validate and normalize expertise areas."""
        if len(v) > 15:
            raise ValueError("Maximum 15 expertise areas allowed")
        return [area.strip().title() for area in v if area.strip()]

    @model_validator(mode="after")
    def validate_personality_consistency(self) -> "PersonalityTraits":
        """Ensure personality traits are consistent."""
        if self.communication_style == "technical" and "Technology" not in self.expertise_areas:
            self.expertise_areas.append("Technology")
        return self


class UserPreferences(BaseModel):
    """Enhanced user preferences with validation."""

    notification_settings: dict[str, bool] = Field(default_factory=dict)
    privacy_level: Literal["public", "private", "restricted"] = Field(default="private")
    data_retention_days: int = Field(default=365, ge=1, le=3650)
    preferred_response_length: Literal["brief", "moderate", "detailed"] = Field(default="moderate")
    topics_of_interest: list[str] = Field(default_factory=list)
    avoided_topics: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_topic_consistency(self) -> "UserPreferences":
        """Ensure no overlap between interested and avoided topics."""
        interest_set = set(self.topics_of_interest)
        avoided_set = set(self.avoided_topics)
        overlap = interest_set & avoided_set
        if overlap:
            raise ValueError(f"Topics cannot be both interesting and avoided: {overlap}")
        return self


# Standalone functions for export
def calculate_temporal_relevance(memory_item) -> float:
    """Calculate temporal relevance of memory item."""
    # Mock implementation - would use actual temporal calculation
    return 0.8


def validate_expertise(areas: list[str]) -> list[str]:
    """Validate expertise areas."""
    if len(areas) > 20:
        raise ValueError("Too many expertise areas (max 20)")
    return [area.strip() for area in areas if area.strip()]


def validate_personality_consistency(traits: list[str]) -> list[str]:
    """Validate personality trait consistency."""
    if len(traits) > 10:
        raise ValueError("Too many personality traits (max 10)")
    return traits


def validate_temporal_weight(weight: float) -> float:
    """Validate temporal weight value."""
    if not 0.0 <= weight <= 1.0:
        raise ValueError("Temporal weight must be between 0.0 and 1.0")
    return weight


def validate_topic_consistency(
    interests: list[str], avoided: list[str]
) -> tuple[list[str], list[str]]:
    """Validate topic consistency between interests and avoided topics."""
    interest_set = set(interests)
    avoided_set = set(avoided)
    overlap = interest_set & avoided_set
    if overlap:
        raise ValueError(f"Topics cannot be both interesting and avoided: {overlap}")
    return interests, avoided
