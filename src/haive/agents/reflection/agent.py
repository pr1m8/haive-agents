"""Simple Reflection Agent using ProperMultiAgent pattern."""

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.reflection.models import Critique, Improvement, ReflectionAction
from haive.agents.reflection.prompts import (
    CRITIC_PROMPT,
    IMPROVER_PROMPT,
    REFLECTION_DIRECTOR_PROMPT,
)
from haive.agents.reflection.state import ReflectionState
from haive.agents.simple.agent import SimpleAgent


class ReflectionAgent(ProperMultiAgent):
    """Simple reflection agent using multi-agent sequential pattern.

    Flow: Critic → Director → Improver (loop until done)
    """

    @classmethod
    def create_default(cls, base_agent=None, **kwargs):
        """Create reflection agent with default configuration."""

        # Create critic agent
        critic_agent = SimpleAgent(
            name="critic",
            engine=AugLLMConfig(
                name="critic",
                prompt_template=CRITIC_PROMPT,
                structured_output_model=Critique,
                structured_output_version="v2",
                temperature=0.3,
            ),
        )

        # Create director agent (decides improve vs finalize)
        director_agent = SimpleAgent(
            name="director",
            engine=AugLLMConfig(
                name="director",
                prompt_template=REFLECTION_DIRECTOR_PROMPT,
                structured_output_model=ReflectionAction,
                structured_output_version="v2",
                temperature=0.1,
            ),
        )

        # Create improver agent
        improver_agent = SimpleAgent(
            name="improver",
            engine=AugLLMConfig(
                name="improver",
                prompt_template=IMPROVER_PROMPT,
                structured_output_model=Improvement,
                structured_output_version="v2",
                temperature=0.5,
            ),
        )

        # Create sequential multi-agent
        name = kwargs.pop("name", "Reflection Agent")
        return cls(
            name=name,
            agents=[critic_agent, director_agent, improver_agent],
            execution_mode="sequential",
            state_schema=ReflectionState,
            **kwargs,
        )

    @classmethod
    def enhance_agent(cls, base_agent, **kwargs):
        """Enhance any agent with reflection capability."""
        # Create reflection agent
        reflection_agent = cls.create_default(**kwargs)

        # Create enhanced multi-agent: base_agent → reflection_agent
        enhanced_name = kwargs.pop("name", f"{base_agent.name}_with_reflection")

        return ProperMultiAgent(
            name=enhanced_name,
            agents=[base_agent, reflection_agent],
            execution_mode="sequential",
            **kwargs,
        )
