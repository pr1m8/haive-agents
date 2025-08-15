agents.planning.p_and_e.enhanced_multi_agent
============================================

.. py:module:: agents.planning.p_and_e.enhanced_multi_agent

.. autoapi-nested-parse::

   Enhanced Multi-Agent Base for Plan and Execute patterns.

   This module provides an enhanced version of MultiAgent that allows for cleaner
   configuration with agents, state schema, and branches passed directly.


   .. autolink-examples:: agents.planning.p_and_e.enhanced_multi_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.p_and_e.enhanced_multi_agent.logger


Classes
-------

.. autoapisummary::

   agents.planning.p_and_e.enhanced_multi_agent.EnhancedMultiAgent
   agents.planning.p_and_e.enhanced_multi_agent.PlanAndExecuteMultiAgent


Module Contents
---------------

.. py:class:: EnhancedMultiAgent(agents: list[Any], state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, branches: dict[str, dict[str, Any]] | None = None, schema_composition_method: str = 'smart', execution_mode: str = 'conditional', **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Enhanced MultiAgent that accepts agents, state schema, and branches directly.

   Initialize enhanced multi-agent with direct configuration.

   :param agents: List of agents to orchestrate
   :param state_schema: Optional state schema override
   :param branches: Branch configuration for conditional routing
   :param schema_composition_method: How to compose schemas ("smart", "shared", "namespaced")
   :param execution_mode: Execution pattern
   :param \*\*kwargs: Additional MultiAgent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedMultiAgent
      :collapse:

   .. py:method:: setup_multi_agent() -> EnhancedMultiAgent

      Override to use state schema override if provided.


      .. autolink-examples:: setup_multi_agent
         :collapse:


   .. py:attribute:: _state_schema_override
      :value: None



.. py:class:: PlanAndExecuteMultiAgent(agents: list[Any], state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs)

   Bases: :py:obj:`EnhancedMultiAgent`


   Plan and Execute multi-agent using enhanced base.

   Initialize Plan and Execute multi-agent.

   :param agents: List of [planner, executor, replanner] agents
   :param state_schema: Optional state schema (defaults to PlanExecuteState)
   :param \*\*kwargs: Additional arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanAndExecuteMultiAgent
      :collapse:

   .. py:method:: _prepare_execution_step(state: Any)

      Prepare the next execution step.


      .. autolink-examples:: _prepare_execution_step
         :collapse:


   .. py:method:: _prepare_replan_step(state: Any)

      Prepare for replanning.


      .. autolink-examples:: _prepare_replan_step
         :collapse:


   .. py:method:: _process_execution_result(state: Any)

      Process the execution result and update the plan.


      .. autolink-examples:: _process_execution_result
         :collapse:


   .. py:method:: _process_replan_decision(state: Any)

      Process the replanning decision.


      .. autolink-examples:: _process_replan_decision
         :collapse:


   .. py:method:: _route_after_execution(state: Any) -> str

      Route after execution based on plan status.


      .. autolink-examples:: _route_after_execution
         :collapse:


   .. py:method:: _route_after_replan(state: Any) -> str

      Route after replanning decision.


      .. autolink-examples:: _route_after_replan
         :collapse:


   .. py:method:: build_custom_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the Plan and Execute workflow graph.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:data:: logger

