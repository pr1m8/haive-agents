"""Haive Agents Module - Main exports.

This module provides various agent implementations for the Haive framework.
"""

import os
import sys
from typing import TYPE_CHECKING

# Lazy loading for performance - defer all agent imports until needed
_AGENT_IMPORTS = {
    "Agent": ("haive.agents.base", "Agent"),
    "MultiAgent": ("haive.agents.multi", "MultiAgent"),
    "ReactAgent": ("haive.agents.react", "ReactAgent"),
    "SimpleAgent": ("haive.agents.simple", "SimpleAgent"),
}

# Check if we're in documentation mode (Sphinx is running)
_DOCUMENTATION_MODE = (
    "sphinx" in sys.modules
    or "SPHINX_BUILD" in os.environ
    or "HAIVE_DOCS_MODE" in os.environ
    or any("sphinx" in arg for arg in sys.argv)
)

# Type checking imports (for linters and IDE support)
if TYPE_CHECKING:
    from haive.agents.base import Agent
    from haive.agents.multi import MultiAgent
    from haive.agents.react import ReactAgent
    from haive.agents.simple import SimpleAgent
else:
    # Forward declarations for linters when not type checking
    Agent = None  # type: ignore
    SimpleAgent = None  # type: ignore
    ReactAgent = None  # type: ignore
    MultiAgent = None  # type: ignore

# For documentation generation, import all classes immediately
# This ensures Sphinx/autoapi can find them during static analysis
if _DOCUMENTATION_MODE:
    try:
        import importlib

        for name, (module_path, class_name) in _AGENT_IMPORTS.items():
            module = importlib.import_module(module_path)
            agent_class = getattr(module, class_name)
            globals()[name] = agent_class
    except ImportError:
        # If imports fail during docs build, just log and continue
        pass


def __getattr__(name: str):
    """Lazy load agent classes to avoid import-time overhead."""
    if name in _AGENT_IMPORTS:
        module_path, class_name = _AGENT_IMPORTS[name]

        # Import module and get class
        import importlib

        module = importlib.import_module(module_path)
        agent_class = getattr(module, class_name)

        # Cache in globals for subsequent access
        globals()[name] = agent_class
        return agent_class

    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# RAG agents
# from haive.agents.rag import (
#     BaseRAGAgent,
#     ConversationRAGAgent,
#     DocumentRAGAgent,
#     MultiDocumentRAGAgent,
#     StreamingRAGAgent,
#     StructuredRAGAgent,
# )

# Memory agents
# from haive.agents.memory import (
#     BaseMemoryAgent,
#     EpisodicMemoryAgent,
#     SemanticMemoryAgent,
#     HybridMemoryAgent,
# )

# Import submodules for documentation
try:
    # These imports allow sphinx to find the submodules
    from haive.agents import conversation, planning, research, sequential, supervisor
except ImportError as e:
    # Log but don't fail if submodules aren't available
    import warnings

    warnings.warn(f"Failed to import agent submodules: {e}")

# Planning agents
# from haive.agents.planning import (
#     PlannerAgent,
#     TreeOfThoughtsAgent,
#     GoalDecomposerAgent,
# )

# Research agents
# from haive.agents.research import (
#     ResearchAgent,
#     WebSearchAgent,
#     ScholarAgent,
# )

# Reasoning agents
# from haive.agents.reasoning_and_critique import (
#     LLMCompilerAgent,
#     LLMDebuggerAgent,
#     LLMReasonerAgent,
#     SelfDiscoverAgent,
#     SelfRefineAgent,
# )

# Workflow agents
# from haive.agents.workflow import (
#     SequentialAgent,
#     ParallelAgent,
#     ConditionalAgent,
# )

__all__ = [
    # Base
    "Agent",
    # Multi-agent
    "MultiAgent",
    # React
    "ReactAgent",
    # Simple
    "SimpleAgent",
    # # RAG
    # "BaseRAGAgent",
    # "ConversationRAGAgent",
    # "DocumentRAGAgent",
    # "MultiDocumentRAGAgent",
    # "StreamingRAGAgent",
    # "StructuredRAGAgent",
    # # Memory
    # "BaseMemoryAgent",
    # "EpisodicMemoryAgent",
    # "SemanticMemoryAgent",
    # "HybridMemoryAgent",
    # # Planning
    # "PlannerAgent",
    # "TreeOfThoughtsAgent",
    # "GoalDecomposerAgent",
    # # Research
    # "ResearchAgent",
    # "WebSearchAgent",
    # "ScholarAgent",
    # # Reasoning
    # "LLMCompilerAgent",
    # "LLMDebuggerAgent",
    # "LLMReasonerAgent",
    # "SelfDiscoverAgent",
    # "SelfRefineAgent",
    # # Workflow
    # "SequentialAgent",
    # "ParallelAgent",
    # "ConditionalAgent",
]
