agents.rag.multi_agent_rag.specialized_workflows_v2
===================================================

.. py:module:: agents.rag.multi_agent_rag.specialized_workflows_v2

.. autoapi-nested-parse::

   Specialized Workflows V2 - Using Enhanced State Schemas.

   Updated versions of FLARE, Dynamic RAG, Debate RAG, etc. using
   state schemas with built-in configuration support.


   .. autolink-examples:: agents.rag.multi_agent_rag.specialized_workflows_v2
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.specialized_workflows_v2.AdaptiveThresholdRAGAgentV2
   agents.rag.multi_agent_rag.specialized_workflows_v2.DebateRAGAgentV2
   agents.rag.multi_agent_rag.specialized_workflows_v2.DynamicRAGAgentV2
   agents.rag.multi_agent_rag.specialized_workflows_v2.FLAREAgentV2


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.specialized_workflows_v2.build_custom_graph


Module Contents
---------------

.. py:class:: AdaptiveThresholdRAGAgentV2(initial_threshold: float = 0.7, threshold_step: float = 0.1, min_threshold: float = 0.3, max_threshold: float = 0.95, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`, :py:obj:`haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin`


   Adaptive Threshold RAG V2 - Configuration in AdaptiveThresholdRAGState.


   .. autolink-examples:: AdaptiveThresholdRAGAgentV2
      :collapse:

   .. py:method:: ainvoke(inputs: dict[str, Any]) -> dict[str, Any]
      :async:


      Inject configuration.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _initial_config


.. py:class:: DebateRAGAgentV2(position_names: list[str] | None = None, max_debate_rounds: int = 3, require_consensus: bool = False, enable_judge: bool = True, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`, :py:obj:`haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin`


   Debate RAG V2 - Configuration in DebateRAGState.


   .. autolink-examples:: DebateRAGAgentV2
      :collapse:

   .. py:method:: ainvoke(inputs: dict[str, Any]) -> dict[str, Any]
      :async:


      Inject configuration and initialize debate positions.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _initial_config


.. py:class:: DynamicRAGAgentV2(min_retrievers: int = 1, max_retrievers: int = 5, performance_threshold: float = 0.6, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`, :py:obj:`haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin`


   Dynamic RAG V2 - Configuration in DynamicRAGState.


   .. autolink-examples:: DynamicRAGAgentV2
      :collapse:

   .. py:method:: ainvoke(inputs: dict[str, Any]) -> dict[str, Any]
      :async:


      Inject configuration.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _initial_config


.. py:class:: FLAREAgentV2(uncertainty_threshold: float = 0.3, max_retrieval_rounds: int = 3, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`, :py:obj:`haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin`


   FLARE V2 - Configuration stored in FLAREState.


   .. autolink-examples:: FLAREAgentV2
      :collapse:

   .. py:method:: ainvoke(inputs: dict[str, Any]) -> dict[str, Any]
      :async:


      Inject configuration into state.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _initial_config


.. py:function:: build_custom_graph() -> Any

   Build custom graph for specialized workflows v2.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:

