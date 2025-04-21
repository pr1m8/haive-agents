
from pydantic import Field

from haive.agents.document_agents.summarizer.iterative_refinement.engines import (
    initial_summary_aug_llm,
    refine_summary_aug_llm,
)
from haive.agents.document_agents.summarizer.iterative_refinement.state import (
    IterativeSummarizerState,
)
from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm.base import AugLLMConfig


class IterativeSummarizerConfig(AgentConfig):
    """The configuration for the iterative summarizer.
    """
    state_schema: IterativeSummarizerState = Field(default=IterativeSummarizerState,description="The state of the iterative summarizer.")
    engines: dict[str,AugLLMConfig] = Field(default={
        "initial_summary":initial_summary_aug_llm,
        "refine_summary":refine_summary_aug_llm
    },description="The configuration for the Augmented LLMs.")
