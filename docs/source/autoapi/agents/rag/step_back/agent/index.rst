agents.rag.step_back.agent
==========================

.. py:module:: agents.rag.step_back.agent

.. autoapi-nested-parse::

   Step-Back Prompting RAG Agents.

   from typing import Any
   Implementation of step-back prompting for abstract reasoning.
   Generates broader conceptual queries for enhanced context retrieval.


   .. autolink-examples:: agents.rag.step_back.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.step_back.agent.STEP_BACK_GENERATOR_PROMPT
   agents.rag.step_back.agent.STEP_BACK_SYNTHESIS_PROMPT
   agents.rag.step_back.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.step_back.agent.DualRetrievalAgent
   agents.rag.step_back.agent.StepBackQuery
   agents.rag.step_back.agent.StepBackQueryGeneratorAgent
   agents.rag.step_back.agent.StepBackRAGAgent
   agents.rag.step_back.agent.StepBackResult


Functions
---------

.. autoapisummary::

   agents.rag.step_back.agent.create_step_back_rag_agent
   agents.rag.step_back.agent.get_step_back_rag_io_schema


Module Contents
---------------

.. py:class:: DualRetrievalAgent(documents: list[langchain_core.documents.Document], embedding_model: str | None = None, max_docs_each: int = 5, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that performs both original and step-back retrieval.

   Initialize dual retrieval agent.

   :param documents: Documents for retrieval
   :param embedding_model: Embedding model
   :param max_docs_each: Max docs to retrieve for each query
   :param \*\*kwargs: Additional arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DualRetrievalAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build dual retrieval graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: base_retriever


   .. py:attribute:: documents


   .. py:attribute:: embedding_model
      :value: None



   .. py:attribute:: max_docs_each
      :value: 5



   .. py:attribute:: name
      :type:  str
      :value: 'Dual Retrieval'



.. py:class:: StepBackQuery(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Step-back query generation result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepBackQuery
      :collapse:

   .. py:attribute:: abstraction_level
      :type:  str
      :value: None



   .. py:attribute:: broader_context
      :type:  str
      :value: None



   .. py:attribute:: conceptual_focus
      :type:  str
      :value: None



   .. py:attribute:: expected_benefit
      :type:  str
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: step_back_query
      :type:  str
      :value: None



.. py:class:: StepBackQueryGeneratorAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, abstraction_level: str = 'moderate', **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that generates step-back queries for abstract reasoning.

   Initialize step-back query generator.

   :param llm_config: LLM configuration
   :param abstraction_level: Level of abstraction ("low", "moderate", "high")
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepBackQueryGeneratorAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build step-back query generation graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: abstraction_level
      :value: 'moderate'



   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Step-Back Query Generator'



.. py:class:: StepBackRAGAgent

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Complete Step-Back RAG agent with abstract reasoning.


   .. autolink-examples:: StepBackRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, embedding_model: str | None = None, abstraction_level: str = 'moderate', max_docs_each: int = 5, **kwargs)
      :classmethod:


      Create Step-Back RAG agent from documents.

      :param documents: Documents to index
      :param llm_config: LLM configuration
      :param embedding_model: Embedding model for retrieval
      :param abstraction_level: Level of abstraction for step-back queries
      :param max_docs_each: Max docs to retrieve for each query type
      :param \*\*kwargs: Additional arguments

      :returns: StepBackRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: StepBackResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Combined results from step-back retrieval.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepBackResult
      :collapse:

   .. py:attribute:: conceptual_coverage
      :type:  float
      :value: None



   .. py:attribute:: context_enhancement
      :type:  float
      :value: None



   .. py:attribute:: integration_strategy
      :type:  str
      :value: None



   .. py:attribute:: original_documents
      :type:  list[str]
      :value: None



   .. py:attribute:: step_back_documents
      :type:  list[str]
      :value: None



   .. py:attribute:: synthesis_approach
      :type:  str
      :value: None



.. py:function:: create_step_back_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, reasoning_depth: str = 'moderate', **kwargs) -> StepBackRAGAgent

   Create a Step-Back RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param reasoning_depth: Depth of reasoning ("shallow", "moderate", "deep")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Step-Back RAG agent


   .. autolink-examples:: create_step_back_rag_agent
      :collapse:

.. py:function:: get_step_back_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Step-Back RAG agents.


   .. autolink-examples:: get_step_back_rag_io_schema
      :collapse:

.. py:data:: STEP_BACK_GENERATOR_PROMPT

.. py:data:: STEP_BACK_SYNTHESIS_PROMPT

.. py:data:: logger

