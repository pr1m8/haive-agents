"""Unified Memory Module for Haive Agents.

This module provides comprehensive memory functionality including:
- Simple and React memory agents with token tracking
- Multi-agent coordination and routing
- Search and retrieval capabilities
- Knowledge graph integration
- External system integrations (LangMem, DeepSeek)

The memory system is organized into logical submodules:
- agents: Specialized memory agents (Simple, React, Multi, LTM)
- search: Search-specific functionality
- retrieval: Advanced retrieval patterns (RAG, Graph)
- coordination: Multi-agent coordination
- knowledge: Knowledge graph management
- integrations: External system integrations
- api: Unified public interface

Examples:
    Basic usage::

        from haive.agents.memory_reorganized import SimpleMemoryAgent
        agent = SimpleMemoryAgent(name="memory_agent")

    Advanced usage::

        from haive.agents.memory_reorganized.api import UnifiedMemoryAPI
        memory = UnifiedMemoryAPI()

    Specialized agents::

        from haive.agents.memory_reorganized.search import SemanticSearchAgent
        from haive.agents.memory_reorganized.coordination import MultiAgentCoordinator
"""

# Core memory agents
try:
    from .agents.ltm import LongTermMemoryAgent
    from .agents.multi import MultiMemoryAgent, MultiMemoryConfig
    from .agents.react import ReactMemoryAgent
    from .agents.simple import SimpleMemoryAgent, TokenAwareMemoryConfig
except ImportError:
    # Graceful fallback if agents have import issues
    SimpleMemoryAgent = None
    ReactMemoryAgent = None
    MultiMemoryAgent = None
    LongTermMemoryAgent = None

# Unified API
try:
    from .api.unified_memory_api import UnifiedMemoryAPI
except ImportError:
    UnifiedMemoryAPI = None

# Base classes and states
try:
    from .base.state import MemoryState
    from .base.token_state import MemoryStateWithTokens
    from .core.types import MemoryType
except ImportError:
    MemoryState = None
    MemoryStateWithTokens = None
    MemoryType = None

# Search functionality
try:
    from .search.pro_search.agent import ProSearchAgent
    from .search.quick_search.agent import QuickSearchAgent
except ImportError:
    QuickSearchAgent = None
    ProSearchAgent = None

# Coordination
try:
    from .coordination.agentic_rag_coordinator import AgenticRAGCoordinator
    from .coordination.multi_agent_coordinator import MultiAgentCoordinator
except ImportError:
    MultiAgentCoordinator = None
    AgenticRAGCoordinator = None

# Integration support
try:
    from .integrations.langmem_agent import LTMAgent as LangMemAgent
except ImportError:
    LangMemAgent = None

__all__ = [
    # Core agents
    "SimpleMemoryAgent",
    "ReactMemoryAgent",
    "MultiMemoryAgent",
    "LongTermMemoryAgent",
    # API
    "UnifiedMemoryAPI",
    # Base classes
    "MemoryState",
    "MemoryStateWithTokens",
    "MemoryType",
    # Configuration
    "TokenAwareMemoryConfig",
    "MultiMemoryConfig",
    # Search
    "QuickSearchAgent",
    "ProSearchAgent",
    # Coordination
    "MultiAgentCoordinator",
    "AgenticRAGCoordinator",
    # Integrations
    "LangMemAgent",
]

# Filter out None values from failed imports
__all__ = [name for name in __all__ if globals().get(name) is not None]
