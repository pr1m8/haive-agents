agents.rag.agentic_router.agent_v2
==================================

.. py:module:: agents.rag.agentic_router.agent_v2

.. autoapi-nested-parse::

   Agentic RAG Router with Proper Conditional Routing.

   Implementation using conditional edges for routing between strategies.


   .. autolink-examples:: agents.rag.agentic_router.agent_v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.agentic_router.agent_v2.STRATEGY_SELECTION_PROMPT
   agents.rag.agentic_router.agent_v2.logger


Classes
-------

.. autoapisummary::

   agents.rag.agentic_router.agent_v2.AgenticRAGRouterV2
   agents.rag.agentic_router.agent_v2.RAGStrategy
   agents.rag.agentic_router.agent_v2.StrategyDecision


Module Contents
---------------

.. py:class:: AgenticRAGRouterV2

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agentic RAG Router using proper conditional routing.


   .. autolink-examples:: AgenticRAGRouterV2
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with conditional routing between strategies.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Agentic RAG Router V2'



.. py:class:: RAGStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available RAG strategies for routing.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGStrategy
      :collapse:

   .. py:attribute:: FLARE
      :value: 'flare'



   .. py:attribute:: FUSION
      :value: 'fusion'



   .. py:attribute:: HYDE
      :value: 'hyde'



   .. py:attribute:: MULTI_QUERY
      :value: 'multi_query'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: StrategyDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategy selection decision.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StrategyDecision
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: strategy
      :type:  RAGStrategy
      :value: None



.. py:data:: STRATEGY_SELECTION_PROMPT

.. py:data:: logger

