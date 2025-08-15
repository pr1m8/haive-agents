agents.rag.hyde.agent_v2
========================

.. py:module:: agents.rag.hyde.agent_v2

.. autoapi-nested-parse::

   HyDE (Hypothetical Document Embeddings) RAG Agent V2.

   Bridges query-document semantic gap by generating hypothetical documents.
   This version properly embeds the hypothetical document for retrieval.


   .. autolink-examples:: agents.rag.hyde.agent_v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.hyde.agent_v2.HYDE_GENERATION_PROMPT
   agents.rag.hyde.agent_v2.HYDE_RETRIEVAL_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.hyde.agent_v2.HyDERAGAgentV2
   agents.rag.hyde.agent_v2.HyDERetrieverAgent


Functions
---------

.. autoapisummary::

   agents.rag.hyde.agent_v2.build_graph
   agents.rag.hyde.agent_v2.transform_to_query


Module Contents
---------------

.. py:class:: HyDERAGAgentV2

   Bases: :py:obj:`haive.agents.multi.enhanced_sequential_agent.SequentialAgent`


   HyDE RAG using hypothetical document generation for better retrieval.

   This version properly uses the hypothetical document as the basis for retrieval.


   .. autolink-examples:: HyDERAGAgentV2
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, embedding_model: str | None = None, **kwargs)
      :classmethod:


      Create HyDE RAG from documents.

      :param documents: Documents to index
      :param llm_config: Optional LLM configuration
      :param embedding_model: Optional embedding model for vector store
      :param \*\*kwargs: Additional arguments

      :returns: HyDERAGAgentV2 instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: HyDERetrieverAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Custom retriever that uses hypothetical document for enhanced retrieval.


   .. autolink-examples:: HyDERetrieverAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph that passes hypothetical doc as query.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: base_retriever
      :type:  haive.agents.rag.base.agent.BaseRAGAgent
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'HyDE Retriever'



.. py:function:: build_graph() -> Any

   Build custom graph for HyDE workflows.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_graph
      :collapse:

.. py:function:: transform_to_query(hypothesis: str) -> str

   Transform hypothesis to query format.

   :param hypothesis: Generated hypothesis text

   :returns: Formatted query string


   .. autolink-examples:: transform_to_query
      :collapse:

.. py:data:: HYDE_GENERATION_PROMPT

.. py:data:: HYDE_RETRIEVAL_PROMPT

