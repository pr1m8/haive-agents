
:py:mod:`agents.memory_v2.multi_memory_agent`
=============================================

.. py:module:: agents.memory_v2.multi_memory_agent

MultiMemoryAgent - Coordinates different memory strategies.

This agent acts as a meta-coordinator that routes queries to different specialized
memory agents based on query type, context, and memory strategy optimization.


.. autolink-examples:: agents.memory_v2.multi_memory_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.multi_memory_agent.MemoryPriority
   agents.memory_v2.multi_memory_agent.MemoryRoutingRule
   agents.memory_v2.multi_memory_agent.MemoryStateWithTokens
   agents.memory_v2.multi_memory_agent.MemoryStrategy
   agents.memory_v2.multi_memory_agent.MultiMemoryAgent
   agents.memory_v2.multi_memory_agent.MultiMemoryConfig
   agents.memory_v2.multi_memory_agent.MultiMemoryState
   agents.memory_v2.multi_memory_agent.QueryClassifier
   agents.memory_v2.multi_memory_agent.QueryType
   agents.memory_v2.multi_memory_agent.ResponseSynthesizer
   agents.memory_v2.multi_memory_agent.SimpleMemoryAgent
   agents.memory_v2.multi_memory_agent.TokenAwareMemoryConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryPriority:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryPriority {
        node [shape=record];
        "MemoryPriority" [label="MemoryPriority"];
        "str" -> "MemoryPriority";
        "enum.Enum" -> "MemoryPriority";
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.MemoryPriority
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryPriority** is an Enum defined in ``agents.memory_v2.multi_memory_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryRoutingRule:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryRoutingRule {
        node [shape=record];
        "MemoryRoutingRule" [label="MemoryRoutingRule"];
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.MemoryRoutingRule
   :members:
   :undoc-members:
   :show-inheritance:

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

.. autoclass:: agents.memory_v2.multi_memory_agent.MemoryStateWithTokens
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStrategy {
        node [shape=record];
        "MemoryStrategy" [label="MemoryStrategy"];
        "str" -> "MemoryStrategy";
        "enum.Enum" -> "MemoryStrategy";
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.MemoryStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryStrategy** is an Enum defined in ``agents.memory_v2.multi_memory_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiMemoryAgent {
        node [shape=record];
        "MultiMemoryAgent" [label="MultiMemoryAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "MultiMemoryAgent";
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.MultiMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiMemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MultiMemoryConfig {
        node [shape=record];
        "MultiMemoryConfig" [label="MultiMemoryConfig"];
        "pydantic.BaseModel" -> "MultiMemoryConfig";
      }

.. autopydantic_model:: agents.memory_v2.multi_memory_agent.MultiMemoryConfig
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiMemoryState:

   .. graphviz::
      :align: center

      digraph inheritance_MultiMemoryState {
        node [shape=record];
        "MultiMemoryState" [label="MultiMemoryState"];
        "agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens" -> "MultiMemoryState";
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.MultiMemoryState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryClassifier:

   .. graphviz::
      :align: center

      digraph inheritance_QueryClassifier {
        node [shape=record];
        "QueryClassifier" [label="QueryClassifier"];
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.QueryClassifier
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryType:

   .. graphviz::
      :align: center

      digraph inheritance_QueryType {
        node [shape=record];
        "QueryType" [label="QueryType"];
        "str" -> "QueryType";
        "enum.Enum" -> "QueryType";
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.QueryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryType** is an Enum defined in ``agents.memory_v2.multi_memory_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResponseSynthesizer:

   .. graphviz::
      :align: center

      digraph inheritance_ResponseSynthesizer {
        node [shape=record];
        "ResponseSynthesizer" [label="ResponseSynthesizer"];
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.ResponseSynthesizer
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleMemoryAgent {
        node [shape=record];
        "SimpleMemoryAgent" [label="SimpleMemoryAgent"];
        "haive.agents.simple.enhanced_agent_v3.EnhancedSimpleAgent" -> "SimpleMemoryAgent";
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.SimpleMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TokenAwareMemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_TokenAwareMemoryConfig {
        node [shape=record];
        "TokenAwareMemoryConfig" [label="TokenAwareMemoryConfig"];
        "agents.memory_v2.memory_tools.MemoryConfig" -> "TokenAwareMemoryConfig";
      }

.. autoclass:: agents.memory_v2.multi_memory_agent.TokenAwareMemoryConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.multi_memory_agent.create_multi_memory_agent

.. py:function:: create_multi_memory_agent(name: str = 'multi_memory_coordinator', enable_graph: bool = HAS_GRAPH_MEMORY, enable_rag: bool = HAS_RAG_MEMORY, **kwargs) -> MultiMemoryAgent

   Factory function to create a MultiMemoryAgent with sensible defaults.


   .. autolink-examples:: create_multi_memory_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.multi_memory_agent
   :collapse:
   
.. autolink-skip:: next
