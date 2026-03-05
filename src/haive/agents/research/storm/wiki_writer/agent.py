"""Wiki writer for STORM research pipeline.

Combines section drafts into a complete wiki article.
"""

from langchain_core.output_parsers import StrOutputParser

from haive.agents.research.storm.wiki_writer.prompt import writer_prompt


def create_wiki_writer(llm):
    """Create a wiki writer chain.

    Args:
        llm: Language model to use for writing.

    Returns:
        Chain that writes complete wiki articles.
    """
    return writer_prompt | llm | StrOutputParser()
