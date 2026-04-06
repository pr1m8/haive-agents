"""Optional preset configurations for the Reflexion agent."""

from pydantic import BaseModel, Field


class ReflexionConfig(BaseModel):
    """Preset configuration for the Reflexion agent.

    Use this to create a ReflexionAgent with sensible defaults::

        cfg = ReflexionConfig()
        agent = ReflexionAgent(**cfg.model_dump())
    """

    name: str = Field(default="reflexion")
    max_iterations: int = Field(default=3, ge=1, description="Maximum draft-reflect-revise loops.")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    model: str = Field(default="gpt-4o-mini")
