enhanced_clean_multi_agent
==========================

.. py:module:: enhanced_clean_multi_agent

.. autoapi-nested-parse::

   Enhanced Clean Multi-Agent Implementation using Agent[AugLLMConfig].

   MultiAgent = Agent[AugLLMConfig] + agent coordination + state management.

   This combines the enhanced agent pattern with the clean multi-agent approach:
   - Uses Agent[AugLLMConfig] as the base
   - Supports AgentNodeV3 for state projection
   - Maintains the engines dict pattern
   - Provides multiple state management strategies


   .. autolink-examples:: enhanced_clean_multi_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   enhanced_clean_multi_agent.logger
   enhanced_clean_multi_agent.planner


Classes
-------

.. autoapisummary::

   enhanced_clean_multi_agent.ContainerMultiAgentState
   enhanced_clean_multi_agent.EnhancedMultiAgent
   enhanced_clean_multi_agent.MinimalMultiAgentState


Module Contents
---------------

.. py:class:: ContainerMultiAgentState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   Container pattern with isolated agent states and MetaStateSchema support.


   .. autolink-examples:: ContainerMultiAgentState
      :collapse:

   .. py:attribute:: agent_states
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: agents
      :type:  dict[str, haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]
      :value: None



   .. py:attribute:: completed_agents
      :type:  list[str]
      :value: None



   .. py:attribute:: current_agent
      :type:  str | None
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_count
      :type:  int
      :value: None



   .. py:attribute:: final_result
      :type:  Any | None
      :value: None



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



   .. py:attribute:: needs_recompile
      :type:  bool
      :value: None



   .. py:attribute:: shared_context
      :type:  dict[str, Any]
      :value: None



.. py:class:: EnhancedMultiAgent

   Bases: :py:obj:`haive.agents.simple.enhanced_simple_real.EnhancedAgentBase`


   Enhanced Multi-Agent coordinator with flexible state management.

   MultiAgent = Agent[AugLLMConfig] + agent coordination + state projection.

   Key features:
   1. Uses AgentNodeV3 for proper state projection
   2. Supports multiple execution modes (sequential, parallel, conditional)
   3. Flexible state management strategies
   4. Compatible with MetaStateSchema for meta-capabilities

   .. attribute:: agents

      List or dict of agents to coordinate

   .. attribute:: mode

      Execution mode (sequential, parallel, conditional)

   .. attribute:: state_strategy

      State management approach

   .. attribute:: shared_fields

      Fields shared between agents

   .. attribute:: state_transfer_map

      Rules for transferring state between agents

   .. rubric:: Examples

   Sequential with state transfer::

       multi = EnhancedMultiAgent(
           name="pipeline",
           agents=[planner, executor, reviewer],
           mode="sequential",
           state_transfer_map={
               ("planner", "executor"): {"plan": "task_plan"},
               ("executor", "reviewer"): {"result": "execution_result"}
           }
       )

   Parallel with aggregation::

       multi = EnhancedMultiAgent(
           name="ensemble",
           agents={"expert1": agent1, "expert2": agent2},
           mode="parallel",
           state_strategy="container"
       )

   With MetaStateSchema::

       from haive.core.schema.prebuilt.meta_state import MetaStateSchema

       meta_multi = MetaStateSchema.from_agent(
           agent=multi,
           initial_state={"shared_context": {"project": "AI"}}
       )


   .. autolink-examples:: EnhancedMultiAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _build_conditional_pattern(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, agent_names: list[str]) -> None

      Build conditional execution pattern.


      .. autolink-examples:: _build_conditional_pattern
         :collapse:


   .. py:method:: _build_parallel_pattern(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, agent_names: list[str]) -> None

      Build parallel execution pattern.


      .. autolink-examples:: _build_parallel_pattern
         :collapse:


   .. py:method:: _build_sequential_pattern(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, agent_names: list[str]) -> None

      Build sequential execution pattern.


      .. autolink-examples:: _build_sequential_pattern
         :collapse:


   .. py:method:: _get_default_coordinator_prompt() -> str

      Get default coordinator prompt.


      .. autolink-examples:: _get_default_coordinator_prompt
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build multi-agent execution graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_agent(name: str) -> haive.agents.simple.enhanced_simple_real.EnhancedAgentBase | None

      Get agent by name.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: get_agent_names() -> list[str]

      Get list of agent names.


      .. autolink-examples:: get_agent_names
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup multi-agent coordinator.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: setup_state_schema() -> EnhancedMultiAgent

      Setup appropriate state schema based on strategy.


      .. autolink-examples:: setup_state_schema
         :collapse:


   .. py:method:: validate_agents(v: list[haive.agents.simple.enhanced_simple_real.EnhancedAgentBase] | dict[str, haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]) -> list[haive.agents.simple.enhanced_simple_real.EnhancedAgentBase] | dict[str, haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]
      :classmethod:


      Validate and normalize agents.


      .. autolink-examples:: validate_agents
         :collapse:


   .. py:attribute:: agents
      :type:  list[haive.agents.simple.enhanced_simple_real.EnhancedAgentBase] | dict[str, haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]
      :value: None



   .. py:attribute:: coordinator_prompt
      :type:  str | None
      :value: None



   .. py:attribute:: mode
      :type:  Literal['sequential', 'parallel', 'conditional']
      :value: None



   .. py:attribute:: shared_fields
      :type:  list[str]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.state_schema.StateSchema] | None
      :value: None



   .. py:attribute:: state_strategy
      :type:  Literal['minimal', 'container', 'custom']
      :value: None



   .. py:attribute:: state_transfer_map
      :type:  dict[tuple[str, str], dict[str, str]]
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



.. py:class:: MinimalMultiAgentState

   Bases: :py:obj:`typing_extensions.TypedDict`


   Minimal state for multi-agent coordination.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MinimalMultiAgentState
      :collapse:

   .. py:attribute:: completed_agents
      :type:  list[str]


   .. py:attribute:: current_agent
      :type:  str | None


   .. py:attribute:: error
      :type:  str | None


   .. py:attribute:: final_result
      :type:  Any | None


   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]


.. py:data:: logger

.. py:data:: planner

