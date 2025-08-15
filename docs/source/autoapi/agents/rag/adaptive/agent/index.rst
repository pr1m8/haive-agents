agents.rag.adaptive.agent
=========================

.. py:module:: agents.rag.adaptive.agent

.. autoapi-nested-parse::

   Adaptive RAG Agent.

   Dynamic strategy selection based on query complexity.
   Routes queries to appropriate RAG strategies.


   .. autolink-examples:: agents.rag.adaptive.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.adaptive.agent.DIRECT_ANSWER_PROMPT
   agents.rag.adaptive.agent.QUERY_ANALYZER_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.adaptive.agent.AdaptiveRAGAgent
   agents.rag.adaptive.agent.QueryAnalysis


Module Contents
---------------

.. py:class:: AdaptiveRAGAgent

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Adaptive RAG that routes queries based on complexity.


   .. autolink-examples:: AdaptiveRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, embedding_model: str | None = None, **kwargs)
      :classmethod:


      Create Adaptive RAG from documents.

      :param documents: Documents to index
      :param llm_config: Optional LLM configuration
      :param embedding_model: Optional embedding model
      :param \*\*kwargs: Additional arguments

      :returns: AdaptiveRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: QueryAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis of query characteristics.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryAnalysis
      :collapse:

   .. py:attribute:: complexity
      :type:  Literal['simple', 'medium', 'complex', 'known']
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: domain_specific
      :type:  bool
      :value: None



   .. py:attribute:: requires_multi_hop
      :type:  bool
      :value: None



   .. py:attribute:: temporal_sensitivity
      :type:  bool
      :value: None



   .. py:attribute:: topics
      :type:  list[str]
      :value: None



.. py:data:: DIRECT_ANSWER_PROMPT

.. py:data:: QUERY_ANALYZER_PROMPT

