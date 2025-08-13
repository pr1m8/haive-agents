
:py:mod:`agents.memory_v2.graph_memory_agent`
=============================================

.. py:module:: agents.memory_v2.graph_memory_agent

Graph Memory Agent with LLMGraphTransformer, TNT, and Graph RAG.

This implementation combines:
1. Graph transformation for structured knowledge extraction
2. Text-to-Neo4j (TNT) capabilities for direct graph database storage
3. Graph RAG for intelligent querying of the knowledge graph


.. autolink-examples:: agents.memory_v2.graph_memory_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.graph_memory_agent.GraphMemoryAgent
   agents.memory_v2.graph_memory_agent.GraphMemoryConfig
   agents.memory_v2.graph_memory_agent.GraphMemoryMode


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GraphMemoryAgent {
        node [shape=record];
        "GraphMemoryAgent" [label="GraphMemoryAgent"];
      }

.. autoclass:: agents.memory_v2.graph_memory_agent.GraphMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphMemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GraphMemoryConfig {
        node [shape=record];
        "GraphMemoryConfig" [label="GraphMemoryConfig"];
      }

.. autoclass:: agents.memory_v2.graph_memory_agent.GraphMemoryConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphMemoryMode:

   .. graphviz::
      :align: center

      digraph inheritance_GraphMemoryMode {
        node [shape=record];
        "GraphMemoryMode" [label="GraphMemoryMode"];
        "str" -> "GraphMemoryMode";
        "enum.Enum" -> "GraphMemoryMode";
      }

.. autoclass:: agents.memory_v2.graph_memory_agent.GraphMemoryMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GraphMemoryMode** is an Enum defined in ``agents.memory_v2.graph_memory_agent``.



Functions
---------

.. autoapisummary::

   agents.memory_v2.graph_memory_agent.example_graph_memory

.. py:function:: example_graph_memory()
   :async:


   Example of using GraphMemoryAgent.


   .. autolink-examples:: example_graph_memory
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.graph_memory_agent
   :collapse:
   
.. autolink-skip:: next
