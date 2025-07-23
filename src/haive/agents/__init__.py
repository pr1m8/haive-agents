"""Haive Agents Module - Main exports.

This module provides various agent implementations for the Haive framework.
"""

# Lazy loading for performance - defer all agent imports until needed
_AGENT_IMPORTS = {
    "Agent": ("haive.agents.base", "Agent"),
    "MultiAgent": ("haive.agents.multi.clean", "MultiAgent"),
    "ReactAgent": ("haive.agents.react.agent", "ReactAgent"),
    "SimpleAgent": ("haive.agents.simple", "SimpleAgent"),
}


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
    # Simple
    "SimpleAgent",
    # React
    "ReactAgent",
    # Multi-agent
    "MultiAgent",
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
