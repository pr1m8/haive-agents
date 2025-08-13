
:py:mod:`agents.memory_v2.simple_memory_agent`
==============================================

.. py:module:: agents.memory_v2.simple_memory_agent

SimpleMemoryAgent with token-aware memory management and summarization.

This agent follows V3 enhanced patterns with automatic summarization
when approaching token limits, similar to LangMem's approach.


.. autolink-examples:: agents.memory_v2.simple_memory_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.simple_memory_agent.EnhancedMemoryItem
   agents.memory_v2.simple_memory_agent.ImportanceLevel
   agents.memory_v2.simple_memory_agent.MemoryConfig
   agents.memory_v2.simple_memory_agent.MemoryState
   agents.memory_v2.simple_memory_agent.MemoryStateWithTokens
   agents.memory_v2.simple_memory_agent.MemoryType
   agents.memory_v2.simple_memory_agent.SimpleMemoryAgent
   agents.memory_v2.simple_memory_agent.TokenAwareMemoryConfig
   agents.memory_v2.simple_memory_agent.TokenThresholds
   agents.memory_v2.simple_memory_agent.TokenTracker


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

.. autoclass:: agents.memory_v2.simple_memory_agent.EnhancedMemoryItem
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

.. autoclass:: agents.memory_v2.simple_memory_agent.ImportanceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ImportanceLevel** is an Enum defined in ``agents.memory_v2.simple_memory_agent``.


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryConfig {
        node [shape=record];
        "MemoryConfig" [label="MemoryConfig"];
        "pydantic.BaseModel" -> "MemoryConfig";
      }

.. autopydantic_model:: agents.memory_v2.simple_memory_agent.MemoryConfig
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

   Inheritance diagram for MemoryState:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryState {
        node [shape=record];
        "MemoryState" [label="MemoryState"];
        "pydantic.BaseModel" -> "MemoryState";
      }

.. autopydantic_model:: agents.memory_v2.simple_memory_agent.MemoryState
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

.. autoclass:: agents.memory_v2.simple_memory_agent.MemoryStateWithTokens
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

.. autoclass:: agents.memory_v2.simple_memory_agent.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.memory_v2.simple_memory_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleMemoryAgent {
        node [shape=record];
        "SimpleMemoryAgent" [label="SimpleMemoryAgent"];
        "haive.agents.simple.enhanced_agent_v3.EnhancedSimpleAgent" -> "SimpleMemoryAgent";
      }

.. autoclass:: agents.memory_v2.simple_memory_agent.SimpleMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TokenAwareMemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_TokenAwareMemoryConfig {
        node [shape=record];
        "TokenAwareMemoryConfig" [label="TokenAwareMemoryConfig"];
        "agents.memory_v2.memory_tools.MemoryConfig" -> "TokenAwareMemoryConfig";
      }

.. autoclass:: agents.memory_v2.simple_memory_agent.TokenAwareMemoryConfig
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TokenThresholds:

   .. graphviz::
      :align: center

      digraph inheritance_TokenThresholds {
        node [shape=record];
        "TokenThresholds" [label="TokenThresholds"];
        "pydantic.BaseModel" -> "TokenThresholds";
      }

.. autopydantic_model:: agents.memory_v2.simple_memory_agent.TokenThresholds
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

   Inheritance diagram for TokenTracker:

   .. graphviz::
      :align: center

      digraph inheritance_TokenTracker {
        node [shape=record];
        "TokenTracker" [label="TokenTracker"];
        "pydantic.BaseModel" -> "TokenTracker";
      }

.. autopydantic_model:: agents.memory_v2.simple_memory_agent.TokenTracker
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

   agents.memory_v2.simple_memory_agent.classify_memory
   agents.memory_v2.simple_memory_agent.get_memory_stats
   agents.memory_v2.simple_memory_agent.retrieve_memory
   agents.memory_v2.simple_memory_agent.search_memory
   agents.memory_v2.simple_memory_agent.store_memory








.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.simple_memory_agent
   :collapse:
   
.. autolink-skip:: next
