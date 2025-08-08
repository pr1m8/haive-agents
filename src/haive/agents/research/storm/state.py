"""State management for STORM research workflow.

This module provides Pydantic models for managing state throughout the STORM
(Synthesis of Topic Outline through Retrieval and Multi-perspective questioning)
research process, including topic definition, article generation, and research coordination.

Classes:
    TopicState: Simple state container for research topic
    ArticleState: State container for final article content
    ResearchState: Complete research workflow state management

Example:
    Basic research state management::

        from haive.agents.research.storm.state import ResearchState

        state = ResearchState(
            topic=TopicState(topic="AI Safety"),
            outline=outline_instance,
            editors=editor_list,
            interview_results=interview_list,
            sections=section_list
        )

        draft = state.draft  # Get compiled article draft
"""

from pydantic import BaseModel, Field, computed_field

from haive.agents.research.storm.generate_perspectives.models import Editor
from haive.agents.research.storm.interview.models import InterviewState
from haive.agents.research.storm.outline_generator.models import Outline
from haive.agents.research.storm.section_writer.models import WikiSection


class TopicState(BaseModel):
    """Simple state container for research topic.

    Attributes:
        topic: The research topic as a string.

    Example:
        >>> state = TopicState(topic="Machine Learning Ethics")
        >>> print(state.topic)
        Machine Learning Ethics
    """

    topic: str = Field(..., description="The topic of the research")


class ArticleState(BaseModel):
    """State container for final article content.

    Attributes:
        article: The complete final article text.

    Example:
        >>> state = ArticleState(article="This is the final article...")
        >>> print(len(state.article))
        25
    """

    article: str = Field(..., description="The final article of the research")


class ResearchState(TopicState, ArticleState):
    """Complete research workflow state management.

    This class manages the entire STORM research process state, including
    topic definition, outline generation, editor perspectives, interview
    results, and final section compilation.

    Attributes:
        topic: The research topic state container.
        outline: Generated outline for the research article.
        editors: List of editor perspectives for multi-angle research.
        interview_results: Results from perspective-based interviews.
        sections: Final compiled sections for the article.

    Properties:
        draft: Compiled draft article from all sections.

    Example:
        Complete research workflow::

            from haive.agents.research.storm.state import ResearchState

            state = ResearchState(
                topic=TopicState(topic="Climate Change"),
                outline=generated_outline,
                editors=editor_perspectives,
                interview_results=interview_data,
                sections=compiled_sections
            )

            # Get the complete draft
            article_draft = state.draft
            print(f"Draft length: {len(article_draft)} characters")
    """

    topic: TopicState = Field(..., description="The topic of the research")
    outline: Outline = Field(..., description="The outline of the research")
    editors: list[Editor] = Field(..., description="The editors of the research")
    interview_results: list[InterviewState] = Field(
        ..., description="The interview results of the research"
    )
    # The final sections output
    sections: list[WikiSection] = Field(
        ..., description="The final sections of the research"
    )

    @computed_field
    @property
    def draft(self) -> str:
        """Compile all sections into a single draft article.

        Returns:
            str: Complete article draft with all sections joined by double newlines.

        Example:
            >>> draft_text = research_state.draft
            >>> print(draft_text[:100])
            # Introduction

            Climate change refers to...
        """
        return "\n\n".join([section.as_str for section in self.sections])
