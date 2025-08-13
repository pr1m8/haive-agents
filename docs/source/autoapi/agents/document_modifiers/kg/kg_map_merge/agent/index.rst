
:py:mod:`agents.document_modifiers.kg.kg_map_merge.agent`
=========================================================

.. py:module:: agents.document_modifiers.kg.kg_map_merge.agent


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.agent.ParallelKGTransformer
   agents.document_modifiers.kg.kg_map_merge.agent.ParallelKGTransformerConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelKGTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelKGTransformer {
        node [shape=record];
        "ParallelKGTransformer" [label="ParallelKGTransformer"];
        "haive.core.engine.agent.agent.Agent[ParallelKGTransformerConfig]" -> "ParallelKGTransformer";
      }

.. autoclass:: agents.document_modifiers.kg.kg_map_merge.agent.ParallelKGTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelKGTransformerConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelKGTransformerConfig {
        node [shape=record];
        "ParallelKGTransformerConfig" [label="ParallelKGTransformerConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "ParallelKGTransformerConfig";
      }

.. autoclass:: agents.document_modifiers.kg.kg_map_merge.agent.ParallelKGTransformerConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.agent.build_agent
   agents.document_modifiers.kg.kg_map_merge.agent.main

.. py:function:: build_agent(documents: list[langchain_core.documents.Document]) -> ParallelKGTransformer

   Build a Parallel Knowledge Graph Transformer agent.

   :param documents: Documents to process
   :type documents: List[Document]

   :returns: Configured agent
   :rtype: ParallelKGTransformer


   .. autolink-examples:: build_agent
      :collapse:

.. py:function:: main()
   :async:




.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.kg.kg_map_merge.agent
   :collapse:
   
.. autolink-skip:: next
