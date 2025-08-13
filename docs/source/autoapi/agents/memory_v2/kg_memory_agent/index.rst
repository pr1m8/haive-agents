
:py:mod:`agents.memory_v2.kg_memory_agent`
==========================================

.. py:module:: agents.memory_v2.kg_memory_agent

Knowledge Graph Memory Agent with Graph Database Integration.

This agent extends the existing KG transformer capabilities with:
1. Graph database upload and storage (Neo4j, Neptune, etc.)
2. Memory-specific knowledge graph construction
3. Time-weighted graph retrieval
4. Configurable storage backends

Based on existing ParallelKGTransformer but optimized for memory workflows.


.. autolink-examples:: agents.memory_v2.kg_memory_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.kg_memory_agent.EnhancedMemoryItem
   agents.memory_v2.kg_memory_agent.GraphDatabaseConnector
   agents.memory_v2.kg_memory_agent.GraphStorageBackend
   agents.memory_v2.kg_memory_agent.KGMemoryAgent
   agents.memory_v2.kg_memory_agent.KGMemoryConfig
   agents.memory_v2.kg_memory_agent.MessageDocumentConverter


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

.. autoclass:: agents.memory_v2.kg_memory_agent.EnhancedMemoryItem
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphDatabaseConnector:

   .. graphviz::
      :align: center

      digraph inheritance_GraphDatabaseConnector {
        node [shape=record];
        "GraphDatabaseConnector" [label="GraphDatabaseConnector"];
      }

.. autoclass:: agents.memory_v2.kg_memory_agent.GraphDatabaseConnector
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphStorageBackend:

   .. graphviz::
      :align: center

      digraph inheritance_GraphStorageBackend {
        node [shape=record];
        "GraphStorageBackend" [label="GraphStorageBackend"];
        "str" -> "GraphStorageBackend";
        "enum.Enum" -> "GraphStorageBackend";
      }

.. autoclass:: agents.memory_v2.kg_memory_agent.GraphStorageBackend
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GraphStorageBackend** is an Enum defined in ``agents.memory_v2.kg_memory_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KGMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_KGMemoryAgent {
        node [shape=record];
        "KGMemoryAgent" [label="KGMemoryAgent"];
      }

.. autoclass:: agents.memory_v2.kg_memory_agent.KGMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KGMemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_KGMemoryConfig {
        node [shape=record];
        "KGMemoryConfig" [label="KGMemoryConfig"];
        "pydantic.BaseModel" -> "KGMemoryConfig";
      }

.. autopydantic_model:: agents.memory_v2.kg_memory_agent.KGMemoryConfig
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

   Inheritance diagram for MessageDocumentConverter:

   .. graphviz::
      :align: center

      digraph inheritance_MessageDocumentConverter {
        node [shape=record];
        "MessageDocumentConverter" [label="MessageDocumentConverter"];
      }

.. autoclass:: agents.memory_v2.kg_memory_agent.MessageDocumentConverter
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.kg_memory_agent.create_memory_kg_agent
   agents.memory_v2.kg_memory_agent.create_neo4j_memory_agent

.. py:function:: create_memory_kg_agent(storage_backend: str = 'memory', llm_config: haive.core.engine.aug_llm.AugLLMConfig = None, **storage_kwargs) -> KGMemoryAgent

   Factory function to create KG Memory Agent.

   :param storage_backend: "memory", "neo4j", "file"
   :param llm_config: LLM configuration
   :param \*\*storage_kwargs: Backend-specific settings

   :returns: Configured KGMemoryAgent


   .. autolink-examples:: create_memory_kg_agent
      :collapse:

.. py:function:: create_neo4j_memory_agent(uri: str, username: str, password: str, database: str = 'neo4j', llm_config: haive.core.engine.aug_llm.AugLLMConfig = None) -> KGMemoryAgent

   Create KG Memory Agent with Neo4j backend.

   :param uri: Neo4j connection URI
   :param username: Database username
   :param password: Database password
   :param database: Database name
   :param llm_config: LLM configuration

   :returns: KGMemoryAgent configured for Neo4j


   .. autolink-examples:: create_neo4j_memory_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.kg_memory_agent
   :collapse:
   
.. autolink-skip:: next
