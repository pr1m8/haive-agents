agents.rag.flare.agent
======================

.. py:module:: agents.rag.flare.agent

.. autoapi-nested-parse::

   FLARE (Forward-Looking Active REtrieval) RAG Agents.

   from typing import Any
   Implementation of FLARE RAG with forward-looking retrieval and iterative generation.
   Uses structured output models for planning and managing active retrieval decisions.


   .. autolink-examples:: agents.rag.flare.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.flare.agent.FLARE_GENERATION_PROMPT
   agents.rag.flare.agent.FLARE_PLANNING_PROMPT
   agents.rag.flare.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.flare.agent.ActiveRetrievalAgent
   agents.rag.flare.agent.ConfidenceLevel
   agents.rag.flare.agent.FLAREPlan
   agents.rag.flare.agent.FLAREPlannerAgent
   agents.rag.flare.agent.FLARERAGAgent
   agents.rag.flare.agent.FLAREResult
   agents.rag.flare.agent.RetrievalDecision


Functions
---------

.. autoapisummary::

   agents.rag.flare.agent.create_active_retrieval_callable
   agents.rag.flare.agent.create_flare_planner_callable
   agents.rag.flare.agent.create_flare_rag_agent
   agents.rag.flare.agent.get_flare_rag_io_schema


Module Contents
---------------

.. py:class:: ActiveRetrievalAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that performs active retrieval based on FLARE plans.


   .. autolink-examples:: ActiveRetrievalAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build active retrieval graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: embedding_model
      :type:  str | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Active Retrieval'



.. py:class:: ConfidenceLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Confidence levels for generation.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConfidenceLevel
      :collapse:

   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: VERY_HIGH
      :value: 'very_high'



.. py:class:: FLAREPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Forward-looking plan for active retrieval.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FLAREPlan
      :collapse:

   .. py:attribute:: completion_criteria
      :type:  str
      :value: None



   .. py:attribute:: confidence_in_current
      :type:  ConfidenceLevel
      :value: None



   .. py:attribute:: current_query
      :type:  str
      :value: None



   .. py:attribute:: evidence_sufficiency
      :type:  float
      :value: None



   .. py:attribute:: expected_length
      :type:  int
      :value: None



   .. py:attribute:: generation_so_far
      :type:  str
      :value: None



   .. py:attribute:: hallucination_risk
      :type:  float
      :value: None



   .. py:attribute:: next_generation_focus
      :type:  str
      :value: None



   .. py:attribute:: next_sentences_needed
      :type:  int
      :value: None



   .. py:attribute:: planning_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: retrieval_decision
      :type:  RetrievalDecision
      :value: None



   .. py:attribute:: retrieval_justification
      :type:  str
      :value: None



   .. py:attribute:: retrieval_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: uncertainty_tokens
      :type:  list[str]
      :value: None



.. py:class:: FLAREPlannerAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that creates FLARE plans for iterative generation and active retrieval.


   .. autolink-examples:: FLAREPlannerAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build FLARE planning graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'FLARE Planner'



.. py:class:: FLARERAGAgent

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Complete FLARE RAG agent with forward-looking active retrieval.


   .. autolink-examples:: FLARERAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, max_iterations: int = 5, confidence_threshold: float = 0.7, **kwargs)
      :classmethod:


      Create FLARE RAG agent from documents.

      :param documents: Documents to index
      :param llm_config: LLM configuration
      :param max_iterations: Maximum FLARE iterations
      :param confidence_threshold: Confidence threshold for retrieval
      :param \*\*kwargs: Additional arguments

      :returns: FLARERAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: FLAREResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Results from FLARE processing.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FLAREResult
      :collapse:

   .. py:attribute:: documents_retrieved
      :type:  int
      :value: None



   .. py:attribute:: evidence_coverage
      :type:  float
      :value: None



   .. py:attribute:: factual_grounding
      :type:  float
      :value: None



   .. py:attribute:: final_response
      :type:  str
      :value: None



   .. py:attribute:: generation_confidence
      :type:  float
      :value: None



   .. py:attribute:: iteration_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: processing_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: retrieval_decisions
      :type:  list[str]
      :value: None



   .. py:attribute:: retrieval_efficiency
      :type:  float
      :value: None



   .. py:attribute:: retrieval_queries_used
      :type:  list[str]
      :value: None



   .. py:attribute:: retrieval_rounds
      :type:  int
      :value: None



   .. py:attribute:: total_iterations
      :type:  int
      :value: None



   .. py:attribute:: uncertainty_reduction
      :type:  float
      :value: None



.. py:class:: RetrievalDecision

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Decisions for active retrieval.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RetrievalDecision
      :collapse:

   .. py:attribute:: COMPLETE
      :value: 'complete'



   .. py:attribute:: CONTINUE
      :value: 'continue'



   .. py:attribute:: RETRIEVE
      :value: 'retrieve'



.. py:function:: create_active_retrieval_callable(documents: list[langchain_core.documents.Document], embedding_model: str | None = None)

   Create callable function for active retrieval.


   .. autolink-examples:: create_active_retrieval_callable
      :collapse:

.. py:function:: create_flare_planner_callable(llm_config: haive.core.models.llm.base.LLMConfig)

   Create callable function for FLARE planning.


   .. autolink-examples:: create_flare_planner_callable
      :collapse:

.. py:function:: create_flare_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, flare_mode: str = 'adaptive', **kwargs) -> FLARERAGAgent

   Create a FLARE RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param flare_mode: FLARE mode ("conservative", "adaptive", "aggressive")
   :param \*\*kwargs: Additional arguments

   :returns: Configured FLARE RAG agent


   .. autolink-examples:: create_flare_rag_agent
      :collapse:

.. py:function:: get_flare_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for FLARE RAG agents.


   .. autolink-examples:: get_flare_rag_io_schema
      :collapse:

.. py:data:: FLARE_GENERATION_PROMPT

.. py:data:: FLARE_PLANNING_PROMPT

.. py:data:: logger

