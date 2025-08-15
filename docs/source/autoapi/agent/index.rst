agent
=====

.. py:module:: agent

.. autoapi-nested-parse::

   Core Multi-Agent implementation.

   This module provides the main MultiAgent class that serves as the foundation
   for all multi-agent systems in Haive. It combines multiple agents and coordinates
   their execution with various modes and strategies.


   .. autolink-examples:: agent
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agent/v2/index


Classes
-------

.. autoapisummary::

   agent.ExecutionMode
   agent.MultiAgent
   agent.MultiAgentConfig
   agent.MultiAgentState


Functions
---------

.. autoapisummary::

   agent.create_hierarchical_multi_agent
   agent.create_parallel_multi_agent
   agent.create_sequential_multi_agent


Module Contents
---------------

.. py:class:: ExecutionMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Execution modes for multi-agent systems.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionMode
      :collapse:

   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: HIERARCHICAL
      :value: 'hierarchical'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: ROUND_ROBIN
      :value: 'round_robin'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



.. py:class:: MultiAgent(config: MultiAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.Agent`


   Multi-agent system that coordinates execution of multiple agents.

   This class provides a flexible framework for combining multiple agents
   with different execution modes, coordination strategies, and error handling.

   .. rubric:: Examples

   Basic sequential execution::

       agents = {
           "planner": PlannerAgent(config=planner_config),
           "executor": ExecutorAgent(config=executor_config)
       }

       multi_config = MultiAgentConfig(
           name="workflow",
           agents=agents,
           execution_mode=ExecutionMode.SEQUENTIAL
       )

       multi_agent = MultiAgent(multi_config)
       result = multi_agent.run("Create and execute a plan")

   Parallel execution::

       multi_config = MultiAgentConfig(
           name="parallel_workflow",
           agents=agents,
           execution_mode=ExecutionMode.PARALLEL
       )


   .. autolink-examples:: MultiAgent
      :collapse:

   .. py:method:: _execute_conditional(input_data: Any, state: MultiAgentState, **kwargs) -> Any

      Execute agents based on conditions.


      .. autolink-examples:: _execute_conditional
         :collapse:


   .. py:method:: _execute_hierarchical(input_data: Any, state: MultiAgentState, **kwargs) -> Any

      Execute agents in hierarchical fashion.


      .. autolink-examples:: _execute_hierarchical
         :collapse:


   .. py:method:: _execute_parallel(input_data: Any, state: MultiAgentState, **kwargs) -> Any

      Execute agents in parallel.


      .. autolink-examples:: _execute_parallel
         :collapse:


   .. py:method:: _execute_round_robin(input_data: Any, state: MultiAgentState, **kwargs) -> Any

      Execute agents in round-robin fashion.


      .. autolink-examples:: _execute_round_robin
         :collapse:


   .. py:method:: _execute_sequential(input_data: Any, state: MultiAgentState, **kwargs) -> Any

      Execute agents sequentially.


      .. autolink-examples:: _execute_sequential
         :collapse:


   .. py:method:: _setup_conditional_workflow() -> None

      Set up conditional execution workflow.


      .. autolink-examples:: _setup_conditional_workflow
         :collapse:


   .. py:method:: _setup_hierarchical_workflow() -> None

      Set up hierarchical execution workflow.


      .. autolink-examples:: _setup_hierarchical_workflow
         :collapse:


   .. py:method:: _setup_parallel_workflow() -> None

      Set up parallel execution workflow.


      .. autolink-examples:: _setup_parallel_workflow
         :collapse:


   .. py:method:: _setup_round_robin_workflow() -> None

      Set up round-robin execution workflow.


      .. autolink-examples:: _setup_round_robin_workflow
         :collapse:


   .. py:method:: _setup_sequential_workflow() -> None

      Set up sequential execution workflow.


      .. autolink-examples:: _setup_sequential_workflow
         :collapse:


   .. py:method:: _should_execute_agent(agent: haive.core.engine.agent.Agent, input_data: Any) -> bool

      Determine if an agent should be executed based on conditions.


      .. autolink-examples:: _should_execute_agent
         :collapse:


   .. py:method:: _should_stop_round_robin(result: Any, iteration: int) -> bool

      Determine if round-robin execution should stop.


      .. autolink-examples:: _should_stop_round_robin
         :collapse:


   .. py:method:: add_agent(name: str, agent: haive.core.engine.agent.Agent) -> None

      Add an agent to the multi-agent system.


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: get_agent(name: str) -> haive.core.engine.agent.Agent | None

      Get an agent by name.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: list_agents() -> list[str]

      List all agent names.


      .. autolink-examples:: list_agents
         :collapse:


   .. py:method:: remove_agent(name: str) -> haive.core.engine.agent.Agent | None

      Remove an agent from the multi-agent system.


      .. autolink-examples:: remove_agent
         :collapse:


   .. py:method:: run(input_data: Any, **kwargs) -> Any

      Run the multi-agent system.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the multi-agent workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: agents


   .. py:attribute:: coordination_strategy


   .. py:attribute:: error_handling


   .. py:attribute:: execution_mode


   .. py:attribute:: max_iterations


   .. py:attribute:: state_schema


   .. py:attribute:: timeout


.. py:class:: MultiAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.AgentConfig`


   Configuration for MultiAgent systems.


   .. autolink-examples:: MultiAgentConfig
      :collapse:

   .. py:method:: validate_agents(v: dict[str, haive.core.engine.agent.Agent]) -> dict[str, haive.core.engine.agent.Agent]
      :classmethod:


      Validate that all agents have proper names.


      .. autolink-examples:: validate_agents
         :collapse:


   .. py:attribute:: agents
      :type:  dict[str, haive.core.engine.agent.Agent]
      :value: None



   .. py:attribute:: coordination_strategy
      :type:  str | None
      :value: None



   .. py:attribute:: error_handling
      :type:  str
      :value: None



   .. py:attribute:: execution_mode
      :type:  ExecutionMode
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: timeout
      :type:  float | None
      :value: None



.. py:class:: MultiAgentState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   State schema for multi-agent execution.


   .. autolink-examples:: MultiAgentState
      :collapse:

   .. py:attribute:: agent_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: completed_agents
      :type:  list[str]
      :value: None



   .. py:attribute:: current_agent
      :type:  str | None
      :value: None



   .. py:attribute:: execution_complete
      :type:  bool
      :value: None



   .. py:attribute:: execution_order
      :type:  list[str]
      :value: None



   .. py:attribute:: failed_agents
      :type:  list[str]
      :value: None



   .. py:attribute:: iteration_count
      :type:  int
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



.. py:function:: create_hierarchical_multi_agent(supervisor: haive.core.engine.agent.Agent, subordinates: list[haive.core.engine.agent.Agent], name: str = 'hierarchical_multi_agent') -> MultiAgent

   Create a hierarchical multi-agent system.


   .. autolink-examples:: create_hierarchical_multi_agent
      :collapse:

.. py:function:: create_parallel_multi_agent(agents: list[haive.core.engine.agent.Agent], name: str = 'parallel_multi_agent') -> MultiAgent

   Create a parallel multi-agent system.


   .. autolink-examples:: create_parallel_multi_agent
      :collapse:

.. py:function:: create_sequential_multi_agent(agents: list[haive.core.engine.agent.Agent], name: str = 'sequential_multi_agent') -> MultiAgent

   Create a sequential multi-agent system.


   .. autolink-examples:: create_sequential_multi_agent
      :collapse:

