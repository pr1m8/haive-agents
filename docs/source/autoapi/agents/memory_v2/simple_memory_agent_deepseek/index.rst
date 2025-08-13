
:py:mod:`agents.memory_v2.simple_memory_agent_deepseek`
=======================================================

.. py:module:: agents.memory_v2.simple_memory_agent_deepseek

SimpleMemoryAgent that works with DeepSeek - avoiding broken imports.

This is a working version of SimpleMemoryAgent that:
1. Uses DeepSeek LLM configuration
2. Avoids the broken kg_map_merge imports
3. Implements core memory functionality


.. autolink-examples:: agents.memory_v2.simple_memory_agent_deepseek
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.simple_memory_agent_deepseek.EnhancedMemoryItem
   agents.memory_v2.simple_memory_agent_deepseek.ImportanceLevel
   agents.memory_v2.simple_memory_agent_deepseek.MemoryState
   agents.memory_v2.simple_memory_agent_deepseek.MemoryStateWithTokens
   agents.memory_v2.simple_memory_agent_deepseek.MemoryType
   agents.memory_v2.simple_memory_agent_deepseek.SimpleMemoryAgentDeepSeek
   agents.memory_v2.simple_memory_agent_deepseek.UnifiedMemoryEntry


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMemoryItem:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMemoryItem {
        node [shape=record];
        "EnhancedMemoryItem" [label="EnhancedMemoryItem"];
        "MemoryItem" -> "EnhancedMemoryItem";
      }

.. autoclass:: agents.memory_v2.simple_memory_agent_deepseek.EnhancedMemoryItem
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ImportanceLevel:

   .. graphviz::
      :align: center

      digraph inheritance_ImportanceLevel {
        node [shape=record];
        "ImportanceLevel" [label="ImportanceLevel"];
        "str" -> "ImportanceLevel";
        "enum.Enum" -> "ImportanceLevel";
      }

.. autoclass:: agents.memory_v2.simple_memory_agent_deepseek.ImportanceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ImportanceLevel** is an Enum defined in ``agents.memory_v2.simple_memory_agent_deepseek``.


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryState:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryState {
        node [shape=record];
        "MemoryState" [label="MemoryState"];
        "pydantic.BaseModel" -> "MemoryState";
      }

.. autopydantic_model:: agents.memory_v2.simple_memory_agent_deepseek.MemoryState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryStateWithTokens:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStateWithTokens {
        node [shape=record];
        "MemoryStateWithTokens" [label="MemoryStateWithTokens"];
        "haive.core.schema.prebuilt.messages.messages_with_token_usage.MessagesStateWithTokenUsage" -> "MemoryStateWithTokens";
      }

.. autoclass:: agents.memory_v2.simple_memory_agent_deepseek.MemoryStateWithTokens
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryType:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryType {
        node [shape=record];
        "MemoryType" [label="MemoryType"];
        "str" -> "MemoryType";
        "enum.Enum" -> "MemoryType";
      }

.. autoclass:: agents.memory_v2.simple_memory_agent_deepseek.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.memory_v2.simple_memory_agent_deepseek``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleMemoryAgentDeepSeek:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleMemoryAgentDeepSeek {
        node [shape=record];
        "SimpleMemoryAgentDeepSeek" [label="SimpleMemoryAgentDeepSeek"];
        "haive.agents.simple.agent.SimpleAgent" -> "SimpleMemoryAgentDeepSeek";
      }

.. autoclass:: agents.memory_v2.simple_memory_agent_deepseek.SimpleMemoryAgentDeepSeek
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for UnifiedMemoryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_UnifiedMemoryEntry {
        node [shape=record];
        "UnifiedMemoryEntry" [label="UnifiedMemoryEntry"];
        "pydantic.BaseModel" -> "UnifiedMemoryEntry";
      }

.. autopydantic_model:: agents.memory_v2.simple_memory_agent_deepseek.UnifiedMemoryEntry
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.memory_v2.simple_memory_agent_deepseek.test_with_deepseek

.. py:function:: test_with_deepseek()
   :async:


   Test the agent with DeepSeek configuration.


   .. autolink-examples:: test_with_deepseek
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.simple_memory_agent_deepseek
   :collapse:
   
.. autolink-skip:: next
