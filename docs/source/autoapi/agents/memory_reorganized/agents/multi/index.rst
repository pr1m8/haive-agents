
:py:mod:`agents.memory_reorganized.agents.multi`
================================================

.. py:module:: agents.memory_reorganized.agents.multi

MultiMemoryAgent - Coordinates different memory strategies.

This agent acts as a meta-coordinator that routes queries to different specialized
memory agents based on query type, context, and memory strategy optimization.


.. autolink-examples:: agents.memory_reorganized.agents.multi
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.agents.multi.MemoryPriority
   agents.memory_reorganized.agents.multi.MemoryRoutingRule
   agents.memory_reorganized.agents.multi.MemoryStrategy
   agents.memory_reorganized.agents.multi.MultiMemoryAgent
   agents.memory_reorganized.agents.multi.MultiMemoryConfig
   agents.memory_reorganized.agents.multi.MultiMemoryState
   agents.memory_reorganized.agents.multi.QueryClassifier
   agents.memory_reorganized.agents.multi.QueryType
   agents.memory_reorganized.agents.multi.ResponseSynthesizer


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

.. autoclass:: agents.memory_reorganized.agents.multi.MemoryPriority
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryPriority** is an Enum defined in ``agents.memory_reorganized.agents.multi``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryRoutingRule:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryRoutingRule {
        node [shape=record];
        "MemoryRoutingRule" [label="MemoryRoutingRule"];
      }

.. autoclass:: agents.memory_reorganized.agents.multi.MemoryRoutingRule
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

.. autoclass:: agents.memory_reorganized.agents.multi.MemoryStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryStrategy** is an Enum defined in ``agents.memory_reorganized.agents.multi``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiMemoryAgent {
        node [shape=record];
        "MultiMemoryAgent" [label="MultiMemoryAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "MultiMemoryAgent";
      }

.. autoclass:: agents.memory_reorganized.agents.multi.MultiMemoryAgent
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

.. autopydantic_model:: agents.memory_reorganized.agents.multi.MultiMemoryConfig
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
        "haive.agents.memory_reorganized.base.token_state.MemoryStateWithTokens" -> "MultiMemoryState";
      }

.. autoclass:: agents.memory_reorganized.agents.multi.MultiMemoryState
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

.. autoclass:: agents.memory_reorganized.agents.multi.QueryClassifier
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

.. autoclass:: agents.memory_reorganized.agents.multi.QueryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryType** is an Enum defined in ``agents.memory_reorganized.agents.multi``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResponseSynthesizer:

   .. graphviz::
      :align: center

      digraph inheritance_ResponseSynthesizer {
        node [shape=record];
        "ResponseSynthesizer" [label="ResponseSynthesizer"];
      }

.. autoclass:: agents.memory_reorganized.agents.multi.ResponseSynthesizer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_reorganized.agents.multi.create_multi_memory_agent

.. py:function:: create_multi_memory_agent(name: str = 'multi_memory_coordinator', enable_graph: bool = HAS_GRAPH_MEMORY, enable_rag: bool = HAS_RAG_MEMORY, **kwargs) -> MultiMemoryAgent

   Factory function to create a MultiMemoryAgent with sensible defaults.


   .. autolink-examples:: create_multi_memory_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.agents.multi
   :collapse:
   
.. autolink-skip:: next
