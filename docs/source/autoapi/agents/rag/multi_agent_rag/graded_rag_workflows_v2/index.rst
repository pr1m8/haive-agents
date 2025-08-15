agents.rag.multi_agent_rag.graded_rag_workflows_v2
==================================================

.. py:module:: agents.rag.multi_agent_rag.graded_rag_workflows_v2

.. autoapi-nested-parse::

   Graded RAG Workflows V2 - Using Enhanced State Schemas.

   This version uses state schemas with built-in configuration support,
   providing a cleaner approach to managing agent-specific parameters.


   .. autolink-examples:: agents.rag.multi_agent_rag.graded_rag_workflows_v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows_v2.agent


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows_v2.FLAREAgentV2Example
   agents.rag.multi_agent_rag.graded_rag_workflows_v2.FullyGradedRAGAgentV2
   agents.rag.multi_agent_rag.graded_rag_workflows_v2.MultiCriteriaGradedRAGAgentV2


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows_v2.build_custom_graph
   agents.rag.multi_agent_rag.graded_rag_workflows_v2.create_graded_rag_agent


Module Contents
---------------

.. py:class:: FLAREAgentV2Example(uncertainty_threshold: float = 0.3, max_retrieval_rounds: int = 3, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`, :py:obj:`haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin`


   FLARE Agent V2 example using enhanced state schema.


   .. autolink-examples:: FLAREAgentV2Example
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build custom graph.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _initial_config


.. py:class:: FullyGradedRAGAgentV2(relevance_threshold: float = 0.5, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`, :py:obj:`haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin`


   Fully Graded RAG V2 - Uses enhanced state schema with configuration support.


   .. autolink-examples:: FullyGradedRAGAgentV2
      :collapse:

   .. py:method:: ainvoke(inputs: dict[str, Any]) -> dict[str, Any]
      :async:


      Override to inject configuration into state.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: build_custom_graph() -> Any

      Build the custom graph with state initialization.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _initial_config


.. py:class:: MultiCriteriaGradedRAGAgentV2(grading_criteria: list[str] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`, :py:obj:`haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin`


   Multi-Criteria Graded RAG V2 - Configuration stored in state schema.


   .. autolink-examples:: MultiCriteriaGradedRAGAgentV2
      :collapse:

   .. py:method:: ainvoke(inputs: dict[str, Any]) -> dict[str, Any]
      :async:


      Override to inject configuration.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:attribute:: _initial_config


.. py:function:: build_custom_graph() -> Any

   Build custom graph for graded RAG workflows v2.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:

.. py:function:: create_graded_rag_agent(workflow_type: str = 'fully_graded', relevance_threshold: float = 0.5, grading_criteria: list[str] | None = None, **kwargs) -> haive.agents.multi.base.MultiAgent

   Factory function to create graded RAG agents with proper configuration.


   .. autolink-examples:: create_graded_rag_agent
      :collapse:

.. py:data:: agent

