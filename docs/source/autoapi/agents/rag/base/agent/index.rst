agents.rag.base.agent
=====================

.. py:module:: agents.rag.base.agent


Classes
-------

.. autoapisummary::

   agents.rag.base.agent.BaseRAGAgent


Module Contents
---------------

.. py:class:: BaseRAGAgent

   Bases: :py:obj:`haive.core.engine.retriever.mixins.RetrieverMixin`, :py:obj:`haive.agents.base.agent.Agent`


   Base RAG agent that performs retrieval.

   This agent inherits from RetrieverMixin which provides:
   - Automatic conversion of VectorStoreConfig to VectorStoreRetrieverConfig
   - Class methods for creating agents from various sources

   .. rubric:: Examples

   .. code-block:: python

       # Create with default generic retriever
       agent = BaseRAGAgent(name="my_retriever")

       # Create from vector store config directly
       agent = BaseRAGAgent(name="my_retriever", engine=vector_store_config)

       # Create from documents
       agent = BaseRAGAgent.from_documents(
       documents=[Document(page_content="...")],
       embedding_model=embedding_config,
       name="my_rag_agent"
       )


   .. autolink-examples:: BaseRAGAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the RAG agent graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: engine
      :type:  haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.vectorstore.VectorStoreConfig
      :value: None



