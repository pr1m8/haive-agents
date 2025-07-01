# src/haive/agents/sequence/storm/__init__.py

"""STORM Agent - a research assistant that generates comprehensive
Wikipedia-style articles on a user-provided topic.

The STORM agent consists of three main components:
1. Research Agent: Generates initial outline and identifies perspectives
2. Interview Agent: Conducts expert interviews for diverse insights
3. Writing Agent: Refines outline, writes sections, and assembles final article

Each component is implemented as a separate agent, and the main STORM agent
orchestrates the flow between them.
"""

# Main STORM components
from haive.agents.research.storm.agent import STORMAgent
from haive.agents.research.storm.config import STORMAgentConfig

# Interview components
from haive.agents.research.storm.interview.agent import InterviewAgent
from haive.agents.research.storm.interview.config import InterviewAgentConfig
from haive.agents.research.storm.interview.state import InterviewState

# Research components
from haive.agents.research.storm.research.agent import ResearchAgent
from haive.agents.research.storm.research.config import ResearchAgentConfig
from haive.agents.research.storm.research.state import ResearchState
from haive.agents.research.storm.state import (
    Editor,
    Interview,
    Outline,
    Perspectives,
    RelatedSubjects,
    Section,
    STORMAgentState,
    Subsection,
    WikiSection,
)

# Writing components
from haive.agents.research.storm.writing.agent import WritingAgent
from haive.agents.research.storm.writing.config import WritingAgentConfig
from haive.agents.research.storm.writing.state import WritingState

__all__ = [
    # Main STORM components
    "STORMAgent",
    "STORMAgentConfig",
    "STORMAgentState",
    # State models
    "Outline",
    "Section",
    "Subsection",
    "RelatedSubjects",
    "Perspectives",
    "Editor",
    "Interview",
    "WikiSection",
    # Research components
    "ResearchAgent",
    "ResearchAgentConfig",
    "ResearchState",
    # Interview components
    "InterviewAgent",
    "InterviewAgentConfig",
    "InterviewState",
    # Writing components
    "WritingAgent",
    "WritingAgentConfig",
    "WritingState",
]
