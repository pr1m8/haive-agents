agents.dynamic_supervisor.agent
===============================

.. py:module:: agents.dynamic_supervisor.agent

.. autoapi-nested-parse::

   Dynamic Supervisor Agent implementation.

   This module contains the main DynamicSupervisorAgent class that extends
   SimpleAgent to provide dynamic agent management capabilities.

   Classes:
       DynamicSupervisorAgent: Main supervisor implementation

   Functions:
       create_dynamic_supervisor: Factory function for creating supervisors

   .. rubric:: Example

   Creating a dynamic supervisor::

       from haive.agents.dynamic_supervisor import DynamicSupervisorAgent
       from haive.core.engine import AugLLMConfig

       supervisor = DynamicSupervisorAgent(
           name="task_router",
           engine=supervisor_engine,
           enable_agent_builder=True
       )

       # Run with initial agents
       state = supervisor.create_initial_state()
       state.add_agent("search", search_agent, "Search expert")

       result = await supervisor.arun(
           "Find information about Paris and translate to French",
           state=state
       )


   .. autolink-examples:: agents.dynamic_supervisor.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.dynamic_supervisor.agent.logger


Classes
-------

.. autoapisummary::

   agents.dynamic_supervisor.agent.DynamicSupervisorAgent


Functions
---------

.. autoapisummary::

   agents.dynamic_supervisor.agent.create_dynamic_supervisor


Module Contents
---------------

.. py:class:: DynamicSupervisorAgent

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Dynamic supervisor agent that manages other agents at runtime.

   Extends ReactAgent to get the looping behavior needed for continuous
   agent selection and execution. The supervisor can add, remove, activate,
   and deactivate agents while running, and generates handoff tools dynamically.

   Architecture:
       - Inherits ReactAgent's reasoning + acting loop
       - Tools execute agents directly (no separate node)
       - Uses SupervisorStateWithTools for dynamic tool generation
       - Handoff tools execute agents and return to supervisor loop

   .. attribute:: enable_agent_builder

      Whether to include agent request capability

   .. attribute:: state_schema_override

      Force use of supervisor state schema

   .. attribute:: auto_sync_tools

      Whether to sync tools automatically

   .. rubric:: Example

   Basic supervisor setup::

       supervisor = DynamicSupervisorAgent(
           name="coordinator",
           engine=AugLLMConfig(
               model="gpt-4",
               force_tool_use=True,
               system_message="Route tasks to appropriate agents"
           )
       )

       # Add agents
       state = supervisor.create_initial_state()
       state.add_agent("coder", code_agent, "Python expert")

       # Run task
       result = await supervisor.arun("Write a Python function", state=state)


   .. autolink-examples:: DynamicSupervisorAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: add_default_agent(name: str, agent: Any, description: str) -> None

      Add a default agent that's always available.

      Default agents are automatically added to new states.

      :param name: Agent identifier
      :param agent: Agent instance
      :param description: Agent description


      .. autolink-examples:: add_default_agent
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any] | list[langchain_core.messages.BaseMessage], state: haive.agents.dynamic_supervisor.state.SupervisorStateWithTools | None = None, **kwargs) -> Any
      :async:


      Run the supervisor asynchronously.

      Extends SimpleAgent.arun to handle supervisor state and
      dynamic tool synchronization.

      :param input_data: Input message(s) or task
      :param state: Optional supervisor state with agents
      :param \*\*kwargs: Additional arguments for execution

      :returns: Execution result with updated state

      .. rubric:: Example

      Running with state::

          state = supervisor.create_initial_state()
          state.add_agent("math", math_agent, "Math expert")

          result = await supervisor.arun(
              "Calculate the square root of 144",
              state=state
          )


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with direct agent execution via tools.

      Uses the base ReactAgent graph where handoff tools execute
      agents directly and the ReAct loop handles multi-step coordination.
      No separate agent_execution node needed.

      :returns: Configured supervisor graph with ReAct loop


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_initial_state() -> haive.agents.dynamic_supervisor.state.SupervisorStateWithTools

      Create initial supervisor state.

      Convenience method to create a properly initialized state
      with the supervisor's configuration.

      :returns: Initialized supervisor state

      .. rubric:: Example

      Creating initial state::

          state = supervisor.create_initial_state()
          state.add_agent("search", agent, "Search expert")


      .. autolink-examples:: create_initial_state
         :collapse:


   .. py:method:: run(input_data: str | dict[str, Any] | list[langchain_core.messages.BaseMessage], state: haive.agents.dynamic_supervisor.state.SupervisorStateWithTools | None = None, **kwargs) -> Any

      Run the supervisor synchronously.

      Synchronous version of arun.

      :param input_data: Input message(s) or task
      :param state: Optional supervisor state with agents
      :param \*\*kwargs: Additional arguments for execution

      :returns: Execution result with updated state


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the supervisor with custom state schema.

      Overrides SimpleAgent setup to use SupervisorStateWithTools
      and configure the supervisor-specific settings.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: auto_sync_tools
      :type:  bool
      :value: None



   .. py:attribute:: enable_agent_builder
      :type:  bool
      :value: None



   .. py:attribute:: state_schema_override
      :type:  type
      :value: None



.. py:function:: create_dynamic_supervisor(name: str = 'supervisor', model: str = 'gpt-4', temperature: float = 0.0, force_tool_use: bool = True, enable_agent_builder: bool = False, **kwargs) -> DynamicSupervisorAgent

   Factory function to create a configured dynamic supervisor.

   :param name: Supervisor name
   :param model: LLM model to use
   :param temperature: LLM temperature (0.0 for deterministic)
   :param force_tool_use: Whether to force tool usage
   :param enable_agent_builder: Enable agent request capability
   :param \*\*kwargs: Additional arguments for supervisor

   :returns: Configured DynamicSupervisorAgent instance

   .. rubric:: Example

   Quick supervisor creation::

       supervisor = create_dynamic_supervisor(
           name="task_coordinator",
           model="gpt-4",
           enable_agent_builder=True
       )


   .. autolink-examples:: create_dynamic_supervisor
      :collapse:

.. py:data:: logger

