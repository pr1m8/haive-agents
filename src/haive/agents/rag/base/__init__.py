"""
Base RAG agent module.

This module provides the foundation for building 
Retrieval Augmented Generation agents.

IMPORTANT: The order of imports here is critical to ensure proper registration.
"""

# First import state and models
from haive.agents.rag.base.state import BaseRAGState, BaseRAGInputState, BaseRAGOutputState
from haive.agents.rag.base.models import *

# Then import config
from haive.agents.rag.base.config import BaseRAGConfig

# Import utilities and branches
#from haive.agents.rag.base.utils import *
#from haive.agents.rag.base.branches import *

# Import prompts if needed by the agent
#from haive.agents.rag.base.prompts import *

# Then import agent to trigger registration
# The agent.py file should contain the BaseRAGAgent class with proper decorators
from haive.agents.rag.base.agent import BaseRAGAgent

# Make key components available at module level
__all__ = [
    'BaseRAGState',
    'BaseRAGInputState',
    'BaseRAGOutputState',
    'BaseRAGConfig',
    'BaseRAGAgent'
]