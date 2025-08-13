
:py:mod:`agents.memory.kg_generator_agent`
==========================================

.. py:module:: agents.memory.kg_generator_agent

Knowledge Graph Generator Agent for Memory System.

This agent specializes in extracting and maintaining knowledge graphs from memories,
building entity relationships and semantic connections across the memory system.


.. autolink-examples:: agents.memory.kg_generator_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.kg_generator_agent.KGGeneratorAgent
   agents.memory.kg_generator_agent.KGGeneratorAgentConfig
   agents.memory.kg_generator_agent.KnowledgeGraphNode
   agents.memory.kg_generator_agent.KnowledgeGraphRelationship
   agents.memory.kg_generator_agent.MemoryKnowledgeGraph


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KGGeneratorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_KGGeneratorAgent {
        node [shape=record];
        "KGGeneratorAgent" [label="KGGeneratorAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "KGGeneratorAgent";
      }

.. autoclass:: agents.memory.kg_generator_agent.KGGeneratorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KGGeneratorAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_KGGeneratorAgentConfig {
        node [shape=record];
        "KGGeneratorAgentConfig" [label="KGGeneratorAgentConfig"];
        "pydantic.BaseModel" -> "KGGeneratorAgentConfig";
      }

.. autopydantic_model:: agents.memory.kg_generator_agent.KGGeneratorAgentConfig
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

   Inheritance diagram for KnowledgeGraphNode:

   .. graphviz::
      :align: center

      digraph inheritance_KnowledgeGraphNode {
        node [shape=record];
        "KnowledgeGraphNode" [label="KnowledgeGraphNode"];
        "pydantic.BaseModel" -> "KnowledgeGraphNode";
      }

.. autopydantic_model:: agents.memory.kg_generator_agent.KnowledgeGraphNode
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

   Inheritance diagram for KnowledgeGraphRelationship:

   .. graphviz::
      :align: center

      digraph inheritance_KnowledgeGraphRelationship {
        node [shape=record];
        "KnowledgeGraphRelationship" [label="KnowledgeGraphRelationship"];
        "pydantic.BaseModel" -> "KnowledgeGraphRelationship";
      }

.. autopydantic_model:: agents.memory.kg_generator_agent.KnowledgeGraphRelationship
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

   Inheritance diagram for MemoryKnowledgeGraph:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryKnowledgeGraph {
        node [shape=record];
        "MemoryKnowledgeGraph" [label="MemoryKnowledgeGraph"];
        "pydantic.BaseModel" -> "MemoryKnowledgeGraph";
      }

.. autopydantic_model:: agents.memory.kg_generator_agent.MemoryKnowledgeGraph
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





.. rubric:: Related Links

.. autolink-examples:: agents.memory.kg_generator_agent
   :collapse:
   
.. autolink-skip:: next
