"""Section writer for STORM research pipeline.

Creates wiki sections from outlines and retrieved documents.
"""

from haive.agents.research.storm.section_writer.models import WikiSection
from haive.agents.research.storm.section_writer.prompt import section_writer_prompt


def create_section_writer(llm):
    """Create a section writer chain.

    Args:
        llm: Language model to use for writing.

    Returns:
        Chain that writes wiki sections.
    """
    return section_writer_prompt | llm.with_structured_output(WikiSection)
