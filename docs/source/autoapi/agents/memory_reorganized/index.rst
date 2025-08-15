agents.memory_reorganized
=========================

.. py:module:: agents.memory_reorganized

.. autoapi-nested-parse::

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


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/memory_reorganized/agents/index
   /autoapi/agents/memory_reorganized/api/index
   /autoapi/agents/memory_reorganized/base/index
   /autoapi/agents/memory_reorganized/coordination/index
   /autoapi/agents/memory_reorganized/core/index
   /autoapi/agents/memory_reorganized/integrations/index
   /autoapi/agents/memory_reorganized/knowledge/index
   /autoapi/agents/memory_reorganized/models/index
   /autoapi/agents/memory_reorganized/retrieval/index
   /autoapi/agents/memory_reorganized/search/index


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.LangMemAgent
   agents.memory_reorganized.MemoryState
   agents.memory_reorganized.MultiAgentCoordinator
   agents.memory_reorganized.QuickSearchAgent
   agents.memory_reorganized.SimpleMemoryAgent
   agents.memory_reorganized.UnifiedMemoryAPI


Package Contents
----------------

.. py:data:: LangMemAgent
   :value: None


.. py:data:: MemoryState
   :value: None


.. py:data:: MultiAgentCoordinator
   :value: None


.. py:data:: QuickSearchAgent
   :value: None


.. py:data:: SimpleMemoryAgent
   :value: None


.. py:data:: UnifiedMemoryAPI
   :value: None


