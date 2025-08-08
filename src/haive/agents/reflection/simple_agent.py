"""Simple Reflection Agent using clean MultiAgent pattern."""

from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.agent import MultiAgent
from haive.agents.reflection.models import Critique, Improvement
from haive.agents.simple.agent import SimpleAgent


class ReflectionAgent(MultiAgent):
    """Simple reflection agent using clean MultiAgent pattern."""

    @classmethod
    def create(
        cls,
        name: str = "reflection_agent",
        max_iterations: int = 2,
        quality_threshold: float = 0.8,
        **kwargs,
    ) -> "ReflectionAgent":
        """Create a simple reflection agent."""
        # Create critic
        critic = SimpleAgent(
            name="critic",
            engine=AugLLMConfig(
                prompt_template="""Analyze the content and provide structured feedback.

                Content: {content}

                Evaluate:
                1. Clarity and coherence
                2. Completeness
                3. Quality

                Give a score from 0.0 to 1.0 and identify strengths/weaknesses.
                """,
                structured_output_model=Critique,
                structured_output_version="v2",
                temperature=0.2,
            ),
        )

        # Create improver
        improver = SimpleAgent(
            name="improver",
            engine=AugLLMConfig(
                prompt_template="""Improve the content based on the critique.

                Original: {content}
                Strengths: {strengths}
                Weaknesses: {weaknesses}

                Create an improved version addressing the weaknesses.
                """,
                structured_output_model=Improvement,
                structured_output_version="v2",
                temperature=0.5,
            ),
        )

        return cls(
            name=name, agents=[critic, improver], execution_mode="sequential", **kwargs
        )

    @classmethod
    def enhance_agent(
        cls, base_agent: Any, name: str | None = None, **kwargs
    ) -> "ReflectionAgent":
        """Enhance any agent with reflection capability."""
        # Create reflection agent
        reflection_agent = cls.create(name=f"{base_agent.name}_reflection", **kwargs)

        # Create enhanced multi-agent: base → reflection
        enhanced_name = name or f"{base_agent.name}_with_reflection"

        return MultiAgent.create(
            agents=[base_agent, reflection_agent],
            name=enhanced_name,
            execution_mode="sequential",
        )

    async def _run_sequential(self, input_data, **kwargs):
        """Custom sequential execution with reflection loop."""
        # Step 1: Critique - SimpleAgent will automatically map {content} from
        # input_data
        critic = self.agents["critic"]
        critique_result = await critic.arun(input_data, **kwargs)

        # Step 2: Improve if needed
        if critique_result.needs_improvement:
            improver = self.agents["improver"]
            # SimpleAgent will automatically map {content}, {strengths},
            # {weaknesses}
            improvement_result = await improver.arun(
                {
                    "content": input_data,
                    "strengths": critique_result.strengths,
                    "weaknesses": critique_result.weaknesses,
                },
                **kwargs,
            )

            return improvement_result.improved_content

        return input_data


# Standalone functions for compatibility
def create(*args, **kwargs) -> ReflectionAgent:
    """Create a simple reflection agent."""
    return ReflectionAgent.create(*args, **kwargs)


def enhance_agent(base_agent: Any, **kwargs) -> ReflectionAgent:
    """Enhance any agent with reflection capability."""
    return ReflectionAgent.enhance_agent(base_agent, **kwargs)
