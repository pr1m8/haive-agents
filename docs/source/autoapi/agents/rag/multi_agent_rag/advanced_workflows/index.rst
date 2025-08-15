agents.rag.multi_agent_rag.advanced_workflows
=============================================

.. py:module:: agents.rag.multi_agent_rag.advanced_workflows

.. autoapi-nested-parse::

   Advanced RAG Workflows - Graph RAG and Agentic RAG Patterns.

   This module implements the most sophisticated RAG architectures including
   Graph RAG, Agentic routing, speculative execution, and self-routing patterns.


   .. autolink-examples:: agents.rag.multi_agent_rag.advanced_workflows
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.advanced_workflows.AgenticGraphRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.AgenticRAGRouterAgent
   agents.rag.multi_agent_rag.advanced_workflows.AgenticRAGState
   agents.rag.multi_agent_rag.advanced_workflows.GraphRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.GraphRAGState
   agents.rag.multi_agent_rag.advanced_workflows.QueryPlanningAgenticRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.SelfReflectiveAgenticRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.SelfRouteRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.SpeculativeRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.advanced_workflows.build_custom_graph


Module Contents
---------------

.. py:class:: AgenticGraphRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Agentic Graph RAG - combines graph reasoning with agentic routing.
   and dynamic planning for complex multi-step reasoning.


   .. autolink-examples:: AgenticGraphRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: AgenticRAGRouterAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Agentic RAG Router - intelligently routes queries to different RAG strategies.
   based on query type, complexity, and domain.


   .. autolink-examples:: AgenticRAGRouterAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: AgenticRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   RAG state for agentic routing and planning.


   .. autolink-examples:: AgenticRAGState
      :collapse:

   .. py:attribute:: agent_plan
      :type:  list[dict[str, Any]]
      :value: []



   .. py:attribute:: dynamic_routing
      :type:  bool
      :value: True



   .. py:attribute:: execution_trace
      :type:  list[str]
      :value: []



   .. py:attribute:: routing_strategy
      :type:  str
      :value: ''



.. py:class:: GraphRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Graph RAG - uses knowledge graph construction and traversal.
   for contextually rich retrieval and reasoning.


   .. autolink-examples:: GraphRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: GraphRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   RAG state for graph-based approaches.


   .. autolink-examples:: GraphRAGState
      :collapse:

   .. py:attribute:: entity_relationships
      :type:  dict[str, dict[str, str]]


   .. py:attribute:: graph_entities
      :type:  list[str]
      :value: []



   .. py:attribute:: graph_paths
      :type:  list[list[str]]
      :value: []



   .. py:attribute:: knowledge_graph
      :type:  dict[str, list[str]]


.. py:class:: QueryPlanningAgenticRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Query Planning Agentic RAG - creates detailed execution plans.
   for complex queries requiring multiple reasoning steps.


   .. autolink-examples:: QueryPlanningAgenticRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: SelfReflectiveAgenticRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Self-Reflective Agentic RAG - continuously reflects on and improves.
   its own reasoning and retrieval processes.


   .. autolink-examples:: SelfReflectiveAgenticRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: SelfRouteRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Self-Route RAG - dynamically routes itself to different reasoning.
   strategies based on intermediate results and confidence levels.


   .. autolink-examples:: SelfRouteRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: SpeculativeRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Speculative RAG - generates multiple possible answer hypotheses.
   in parallel and validates them against retrieved evidence.


   .. autolink-examples:: SpeculativeRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:function:: build_custom_graph() -> Any

   Build custom graph for advanced workflows.

   This is a utility function for creating custom graphs for
   advanced RAG workflows in this module.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:

