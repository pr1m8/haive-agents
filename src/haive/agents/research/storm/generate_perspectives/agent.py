"""Perspective generator for STORM research pipeline.

Generates diverse perspectives/experts for wiki research.
"""

from haive.agents.research.storm.generate_perspectives.prompt import gen_perspectives_prompt
from haive.agents.research.storm.generate_perspectives.models import Perspectives


def create_perspectives_generator(llm):
    """Create a perspectives generator chain.

    Args:
        llm: Language model to use.

    Returns:
        Chain that generates diverse perspectives.
    """
    return gen_perspectives_prompt | llm.with_structured_output(Perspectives)
