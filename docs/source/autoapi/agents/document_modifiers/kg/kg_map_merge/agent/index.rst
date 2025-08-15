agents.document_modifiers.kg.kg_map_merge.agent
===============================================

.. py:module:: agents.document_modifiers.kg.kg_map_merge.agent


Attributes
----------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.agent.logger


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.agent.ParallelKGTransformer
   agents.document_modifiers.kg.kg_map_merge.agent.ParallelKGTransformerConfig


Functions
---------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.agent.build_agent
   agents.document_modifiers.kg.kg_map_merge.agent.main


Module Contents
---------------

.. py:class:: ParallelKGTransformer(config: ParallelKGTransformerConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`ParallelKGTransformerConfig`\ ]


   An agent that builds a knowledge graph by extracting.
   nodes and relationships in parallel across multiple documents.


   .. autolink-examples:: ParallelKGTransformer
      :collapse:

   .. py:method:: collect_graph_documents(state: haive.agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState | dict[str, Any], **kwargs)
      :async:



   .. py:method:: collect_nodes(state: haive.agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState, content: langchain_core.documents.Document | dict | pydantic.BaseModel | None = None, index: int | None = None)
      :async:



   .. py:method:: collect_relationships(state: haive.agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState, content: langchain_core.documents.Document | dict | pydantic.BaseModel | None = None, nodes: list[haive.agents.document_modifiers.kg.kg_map_merge.models.EntityNode] | None = None, index: int | None = None, context_type: str = 'document')
      :async:



   .. py:method:: map_graph_documents(state: haive.agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState)


   .. py:method:: map_nodes(state: haive.agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState)

      Map node extraction across documents.


      .. autolink-examples:: map_nodes
         :collapse:


   .. py:method:: map_relationships(state: haive.agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState)

      Map relationship extraction across documents and nodes.


      .. autolink-examples:: map_relationships
         :collapse:


   .. py:method:: merge_graphs(state: haive.agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState)

      Merge extracted graph documents, nodes, and relationships.


      .. autolink-examples:: merge_graphs
         :collapse:


   .. py:method:: setup_workflow() -> None


   .. py:attribute:: graph_merger


   .. py:attribute:: llm_graph_transformer


   .. py:attribute:: node_extractor


   .. py:attribute:: relationship_extractor


.. py:class:: ParallelKGTransformerConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the Parallel Knowledge Graph Transformer.


   .. autolink-examples:: ParallelKGTransformerConfig
      :collapse:

   .. py:attribute:: checkpoint_mode
      :type:  str
      :value: None



   .. py:attribute:: contents
      :type:  list[langchain_core.documents.Document]


   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'ParallelKGTransformer'



   .. py:attribute:: state_schema
      :type:  haive.agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState
      :value: None



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


.. py:data:: logger

