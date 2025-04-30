# src/haive/agents/sequence/storm/__init__.py

"""
STORM Agent - a research assistant that generates comprehensive
Wikipedia-style articles on a user-provided topic.

The STORM agent consists of three main components:
1. Research Agent: Generates initial outline and identifies perspectives
2. Interview Agent: Conducts expert interviews for diverse insights  
3. Writing Agent: Refines outline, writes sections, and assembles final article

Each component is implemented as a separate agent, and the main STORM agent
orchestrates the flow between them.
"""

# Main STORM components
from .agent import STORMAgent
from .config import STORMAgentConfig
from .state import (
    STORMAgentState, 
    Outline, 
    Section,
    Subsection,
    RelatedSubjects,
    Perspectives,
    Editor,
    Interview, 
    WikiSection
)

# Research components
from .research.agent import ResearchAgent
from .research.config import ResearchAgentConfig
from .research.state import ResearchState

# Interview components
from .interview.agent import InterviewAgent
from .interview.config import InterviewAgentConfig
from .interview.state import InterviewState

# Writing components
from .writing.agent import WritingAgent
from .writing.config import WritingAgentConfig
from .writing.state import WritingState

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
    "WritingState"
]