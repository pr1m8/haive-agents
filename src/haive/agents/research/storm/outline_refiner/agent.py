"""Outline refiner for STORM research pipeline.

Refines and improves wiki article outlines based on research.
"""

from haive.agents.research.storm.outline_refiner.prompt import refine_outline_prompt
from haive.agents.research.storm.outline_generator.models import Outline


def create_outline_refiner(llm):
    """Create an outline refiner chain.

    Args:
        llm: Language model to use.

    Returns:
        Chain that refines wiki outlines.
    """
    return refine_outline_prompt | llm.with_structured_output(Outline)
