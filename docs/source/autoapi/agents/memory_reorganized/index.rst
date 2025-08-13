
:py:mod:`agents.memory_reorganized`
===================================

.. py:module:: agents.memory_reorganized

Unified Memory Module for Haive Agents.

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

.. rubric:: Examples

Basic usage::

    from haive.agents.memory_reorganized import SimpleMemoryAgent
    agent = SimpleMemoryAgent(name="memory_agent")

Advanced usage::

    from haive.agents.memory_reorganized.api import UnifiedMemoryAPI
    memory = UnifiedMemoryAPI()

Specialized agents::

    from haive.agents.memory_reorganized.search import SemanticSearchAgent
    from haive.agents.memory_reorganized.coordination import MultiAgentCoordinator


.. autolink-examples:: agents.memory_reorganized
   :collapse:




