agents.rag.multi_query.agent
============================

.. py:module:: agents.rag.multi_query.agent

.. autoapi-nested-parse::

   Multi-Query RAG Agent.

   Improves recall through query diversification.
   Generates multiple query variations and retrieves from all.


   .. autolink-examples:: agents.rag.multi_query.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.multi_query.agent.QUERY_EXPANSION_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.multi_query.agent.MultiQueryRAGAgent
   agents.rag.multi_query.agent.MultiRetrievalAgent
   agents.rag.multi_query.agent.QueryVariations


Module Contents
---------------

.. py:class:: MultiQueryRAGAgent

   Bases: :py:obj:`haive.agents.multi.enhanced_sequential_agent.SequentialAgent`


   Multi-Query RAG with query expansion for improved recall.


   .. autolink-examples:: MultiQueryRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, embedding_model: str | None = None, **kwargs)
      :classmethod:


      Create Multi-Query RAG from documents.

      :param documents: Documents to index
      :param llm_config: Optional LLM configuration
      :param embedding_model: Optional embedding model for vector store
      :param \*\*kwargs: Additional arguments

      :returns: MultiQueryRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: MultiRetrievalAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that performs parallel retrieval with multiple queries.


   .. autolink-examples:: MultiRetrievalAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph that retrieves with multiple queries in parallel.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: base_retriever
      :type:  haive.agents.rag.base.agent.BaseRAGAgent
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Multi-Query Retriever'



.. py:class:: QueryVariations(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for query variations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryVariations
      :collapse:

   .. py:attribute:: alternative_query
      :type:  str
      :value: None



   .. py:attribute:: broader_query
      :type:  str
      :value: None



   .. py:attribute:: specific_query
      :type:  str
      :value: None



.. py:data:: QUERY_EXPANSION_PROMPT

