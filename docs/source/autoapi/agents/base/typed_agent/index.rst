agents.base.typed_agent
=======================

.. py:module:: agents.base.typed_agent

.. autoapi-nested-parse::

   Typed agent base classes with clear separation of concerns.

   This module provides a cleaner agent hierarchy that matches the state schema
   hierarchy, with better separation between different types of agents.


   .. autolink-examples:: agents.base.typed_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.typed_agent.TState


Classes
-------

.. autoapisummary::

   agents.base.typed_agent.AdaptiveAgent
   agents.base.typed_agent.BaseAgent
   agents.base.typed_agent.BaseExecutor
   agents.base.typed_agent.DataProcessor
   agents.base.typed_agent.LLMAgent
   agents.base.typed_agent.MetaAgent
   agents.base.typed_agent.ReactiveAgent
   agents.base.typed_agent.ToolExecutor
   agents.base.typed_agent.WorkflowAgent


Functions
---------

.. autoapisummary::

   agents.base.typed_agent.create_agent
   agents.base.typed_agent.create_executor


Module Contents
---------------

.. py:class:: AdaptiveAgent(name: str, performance_metrics: list[str], adaptation_threshold: float = 0.7, **kwargs)

   Bases: :py:obj:`WorkflowAgent`


   Agent that adapts its behavior based on performance.

   Tracks its own performance and modifies strategy accordingly.


   .. autolink-examples:: AdaptiveAgent
      :collapse:

   .. py:method:: adapt_strategy(state: haive.core.schema.base_state_schemas.WorkflowState) -> None
      :async:


      Adapt the agent's strategy.


      .. autolink-examples:: adapt_strategy
         :collapse:


   .. py:method:: calculate_performance(state: haive.core.schema.base_state_schemas.WorkflowState) -> dict[str, float]

      Calculate performance metrics.


      .. autolink-examples:: calculate_performance
         :collapse:


   .. py:method:: execute(state: haive.core.schema.base_state_schemas.WorkflowState) -> haive.core.schema.base_state_schemas.WorkflowState
      :async:


      Execute with performance tracking.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: needs_adaptation(metrics: dict[str, float]) -> bool

      Check if adaptation is needed.


      .. autolink-examples:: needs_adaptation
         :collapse:


   .. py:attribute:: adaptation_threshold
      :value: 0.7



   .. py:attribute:: performance_history
      :type:  list[dict[str, float]]
      :value: []



   .. py:attribute:: performance_metrics


.. py:class:: BaseAgent(name: str, primary_engine: haive.core.engine.base.Engine | None = None, state_schema: type[haive.core.schema.base_state_schemas.AgentState] = AgentState, **kwargs)

   Bases: :py:obj:`BaseExecutor`\ [\ :py:obj:`haive.core.schema.base_state_schemas.AgentState`\ ]


   Base class for agents with primary decision-making engine.

   Agents are executors that have a primary engine (usually LLM)
   for making decisions.


   .. autolink-examples:: BaseAgent
      :collapse:

   .. py:method:: execute(state: haive.core.schema.base_state_schemas.AgentState) -> haive.core.schema.base_state_schemas.AgentState
      :async:


      Execute agent logic.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: run_engine(engine: haive.core.engine.base.Engine, state: haive.core.schema.base_state_schemas.AgentState) -> Any
      :abstractmethod:

      :async:


      Run the primary engine with state.


      .. autolink-examples:: run_engine
         :collapse:


   .. py:method:: update_state_with_result(state: haive.core.schema.base_state_schemas.AgentState, result: Any) -> haive.core.schema.base_state_schemas.AgentState

      Update state with engine result.


      .. autolink-examples:: update_state_with_result
         :collapse:


   .. py:attribute:: primary_engine
      :value: None



.. py:class:: BaseExecutor(name: str, state_schema: type[TState], **kwargs)

   Bases: :py:obj:`abc.ABC`, :py:obj:`Generic`\ [\ :py:obj:`TState`\ ]


   Base class for all executors (not necessarily agents).

   Executors are components that process state but don't necessarily
   have LLM capabilities. This includes tool executors, data processors,
   routers, validators, etc.


   .. autolink-examples:: BaseExecutor
      :collapse:

   .. py:method:: execute(state: TState) -> TState
      :abstractmethod:

      :async:


      Execute the processing logic.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: get_required_engines() -> list[str]

      Get list of required engine names.


      .. autolink-examples:: get_required_engines
         :collapse:


   .. py:method:: validate_state(state: TState) -> bool

      Validate that state has required components.


      .. autolink-examples:: validate_state
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: name


   .. py:attribute:: state_schema


.. py:class:: DataProcessor(name: str, required_engines: list[str], **kwargs)

   Bases: :py:obj:`BaseExecutor`\ [\ :py:obj:`haive.core.schema.base_state_schemas.DataProcessingState`\ ]


   Executor for data processing workflows.

   Processes data through various transformation engines.


   .. autolink-examples:: DataProcessor
      :collapse:

   .. py:method:: _process_with_engine(engine: haive.core.engine.base.Engine, data: Any) -> Any
      :async:


      Process data with a specific engine.


      .. autolink-examples:: _process_with_engine
         :collapse:


   .. py:method:: execute(state: haive.core.schema.base_state_schemas.DataProcessingState) -> haive.core.schema.base_state_schemas.DataProcessingState
      :async:


      Process data through stages.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: get_required_engines() -> list[str]

      Get list of required engine names.


      .. autolink-examples:: get_required_engines
         :collapse:


   .. py:attribute:: required_engines


.. py:class:: LLMAgent(name: str, primary_engine: haive.core.engine.base.Engine | None = None, state_schema: type[haive.core.schema.base_state_schemas.AgentState] = AgentState, **kwargs)

   Bases: :py:obj:`BaseAgent`


   Standard LLM-based agent.

   Uses an LLM engine for conversation and decision making.


   .. autolink-examples:: LLMAgent
      :collapse:

   .. py:method:: run_engine(engine: haive.core.engine.base.Engine, state: haive.core.schema.base_state_schemas.AgentState) -> Any
      :async:


      Run LLM engine.


      .. autolink-examples:: run_engine
         :collapse:


   .. py:method:: update_state_with_result(state: haive.core.schema.base_state_schemas.AgentState, result: Any) -> haive.core.schema.base_state_schemas.AgentState

      Update state with LLM result.


      .. autolink-examples:: update_state_with_result
         :collapse:


.. py:class:: MetaAgent(name: str, primary_engine: haive.core.engine.base.Engine | None = None, agent_factory: dict[str, type[BaseAgent]] | None = None, **kwargs)

   Bases: :py:obj:`WorkflowAgent`


   Agent that can spawn and manage other agents.

   This is for advanced scenarios where agents need to dynamically
   create and coordinate other agents.


   .. autolink-examples:: MetaAgent
      :collapse:

   .. py:method:: aggregate_results(state: haive.core.schema.base_state_schemas.MetaAgentState) -> None

      Aggregate sub-agent results.


      .. autolink-examples:: aggregate_results
         :collapse:


   .. py:method:: execute(state: haive.core.schema.base_state_schemas.MetaAgentState) -> haive.core.schema.base_state_schemas.MetaAgentState
      :async:


      Execute meta-agent logic.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: execute_sub_agents(state: haive.core.schema.base_state_schemas.MetaAgentState) -> None
      :async:


      Execute active sub-agents.


      .. autolink-examples:: execute_sub_agents
         :collapse:


   .. py:method:: should_aggregate(state: haive.core.schema.base_state_schemas.MetaAgentState) -> bool

      Determine if results should be aggregated.


      .. autolink-examples:: should_aggregate
         :collapse:


   .. py:method:: should_spawn_agents(state: haive.core.schema.base_state_schemas.MetaAgentState) -> bool

      Determine if new agents should be spawned.


      .. autolink-examples:: should_spawn_agents
         :collapse:


   .. py:method:: spawn_agents(state: haive.core.schema.base_state_schemas.MetaAgentState) -> None
      :async:


      Spawn new sub-agents.


      .. autolink-examples:: spawn_agents
         :collapse:


   .. py:attribute:: agent_factory


   .. py:attribute:: state_schema


.. py:class:: ReactiveAgent(name: str, triggers: list[dict[str, Any]], **kwargs)

   Bases: :py:obj:`LLMAgent`


   Agent that reacts to specific patterns or triggers.

   Useful for monitoring, alerting, or event-driven workflows.


   .. autolink-examples:: ReactiveAgent
      :collapse:

   .. py:method:: check_triggers(state: haive.core.schema.base_state_schemas.AgentState) -> list[str]

      Check which triggers are activated.


      .. autolink-examples:: check_triggers
         :collapse:


   .. py:method:: evaluate_trigger(trigger: dict[str, Any], state: haive.core.schema.base_state_schemas.AgentState) -> bool

      Evaluate a single trigger.


      .. autolink-examples:: evaluate_trigger
         :collapse:


   .. py:method:: execute(state: haive.core.schema.base_state_schemas.AgentState) -> haive.core.schema.base_state_schemas.AgentState
      :async:


      Check triggers before normal execution.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: triggers


.. py:class:: ToolExecutor(name: str, execution_strategy: str = 'sequential', **kwargs)

   Bases: :py:obj:`BaseExecutor`\ [\ :py:obj:`haive.core.schema.base_state_schemas.ToolExecutorState`\ ]


   Executor for tool-based workflows without LLM.

   Executes tools based on predefined plans or rules.


   .. autolink-examples:: ToolExecutor
      :collapse:

   .. py:method:: _execute_tool(tool: Any, inputs: dict[str, Any]) -> Any
      :async:


      Execute a single tool.


      .. autolink-examples:: _execute_tool
         :collapse:


   .. py:method:: _find_tool(state: haive.core.schema.base_state_schemas.ToolExecutorState, tool_name: str) -> Any | None

      Find a tool by name.


      .. autolink-examples:: _find_tool
         :collapse:


   .. py:method:: execute(state: haive.core.schema.base_state_schemas.ToolExecutorState) -> haive.core.schema.base_state_schemas.ToolExecutorState
      :async:


      Execute tools according to plan.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: execution_strategy
      :value: 'sequential'



.. py:class:: WorkflowAgent(name: str, primary_engine: haive.core.engine.base.Engine | None = None, initial_graph: dict[str, Any] | None = None, **kwargs)

   Bases: :py:obj:`BaseAgent`


   Agent that can modify its own workflow graph.

   This agent can inspect results and dynamically modify its
   execution graph.


   .. autolink-examples:: WorkflowAgent
      :collapse:

   .. py:method:: determine_graph_modifications(state: haive.core.schema.base_state_schemas.WorkflowState) -> dict[str, Any]
      :async:


      Determine what graph modifications to make.


      .. autolink-examples:: determine_graph_modifications
         :collapse:


   .. py:method:: execute(state: haive.core.schema.base_state_schemas.WorkflowState) -> haive.core.schema.base_state_schemas.WorkflowState
      :async:


      Execute with potential graph modification.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: should_modify_graph(state: haive.core.schema.base_state_schemas.WorkflowState) -> bool

      Determine if graph should be modified.


      .. autolink-examples:: should_modify_graph
         :collapse:


   .. py:attribute:: initial_graph
      :value: None



.. py:function:: create_agent(agent_type: str, name: str, engine: haive.core.engine.base.Engine | None = None, **kwargs) -> BaseAgent

   Factory to create appropriate agent.

   :param agent_type: Type of agent
   :param name: Name for the agent
   :param engine: Primary engine for the agent
   :param \*\*kwargs: Additional arguments

   :returns: Agent instance


   .. autolink-examples:: create_agent
      :collapse:

.. py:function:: create_executor(executor_type: str, name: str, **kwargs) -> BaseExecutor

   Factory to create appropriate executor.

   :param executor_type: Type of executor
   :param name: Name for the executor
   :param \*\*kwargs: Additional arguments

   :returns: Executor instance


   .. autolink-examples:: create_executor
      :collapse:

.. py:data:: TState

