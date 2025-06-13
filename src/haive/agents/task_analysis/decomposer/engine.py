# src/haive/agents/task_analysis/decomposer/engine.py

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.task_analysis.decomposer.base import create_base_llm_config
from haive.agents.task_analysis.decomposer.models import TaskNode
from haive.agents.task_analysis.decomposer.prompt import TASK_DECOMPOSITION_TEMPLATE


def create_decomposer_engine(
    name: str = "task_decomposer", temperature: float = 0.3, max_tokens: int = 3000
) -> AugLLMConfig:
    """Create task decomposition engine."""

    llm_config = create_base_llm_config(
        temperature=temperature,  # Slightly higher for creative decomposition
        max_tokens=max_tokens,  # More tokens for complex structures
    )

    return AugLLMConfig(
        name=name,
        llm_config=llm_config,
        prompt_template=TASK_DECOMPOSITION_TEMPLATE,
        structured_output_model=TaskNode,
        system_message="You are an expert at hierarchical task decomposition.",
    )
