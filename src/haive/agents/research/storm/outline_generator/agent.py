"""Outline generator for STORM research pipeline.

Generates initial outlines for wiki articles.
"""

from haive.agents.research.storm.outline_generator.prompt import direct_gen_outline_prompt
from haive.agents.research.storm.outline_generator.models import Outline


def create_outline_generator(llm):
    """Create an outline generator chain.

    Args:
        llm: Language model to use.

    Returns:
        Chain that generates wiki outlines.
    """
    return direct_gen_outline_prompt | llm.with_structured_output(Outline)
