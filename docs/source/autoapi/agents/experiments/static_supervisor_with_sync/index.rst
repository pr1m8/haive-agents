agents.experiments.static_supervisor_with_sync
==============================================

.. py:module:: agents.experiments.static_supervisor_with_sync

.. autoapi-nested-parse::

   Static supervisor inheriting from ReactAgent with tool node modifications.

   This supervisor uses ReactAgent's looping behavior but modifies the tool node
   to execute agent handoffs stored in state.


   .. autolink-examples:: agents.experiments.static_supervisor_with_sync
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.experiments.static_supervisor_with_sync.logger


Classes
-------

.. autoapisummary::

   agents.experiments.static_supervisor_with_sync.AgentEntry
   agents.experiments.static_supervisor_with_sync.StaticSupervisor
   agents.experiments.static_supervisor_with_sync.SupervisorReactState


Module Contents
---------------

.. py:class:: AgentEntry(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a registered agent in the supervisor state.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentEntry
      :collapse:

   .. py:method:: from_agent(name: str, description: str, agent: haive.agents.base.agent.Agent) -> AgentEntry
      :classmethod:


      Create an AgentEntry from an agent instance.


      .. autolink-examples:: from_agent
         :collapse:


   .. py:method:: get_agent() -> haive.agents.base.agent.Agent

      Deserialize and return the agent instance.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:attribute:: agent_class
      :type:  str


   .. py:attribute:: agent_instance
      :type:  bytes


   .. py:attribute:: description
      :type:  str


   .. py:attribute:: name
      :type:  str


.. py:class:: StaticSupervisor(**kwargs)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Supervisor that inherits ReactAgent behavior with modified tool node.

   This supervisor uses ReactAgent's looping behavior but overrides the tool
   node to execute agent handoffs from state instead of regular tools.

   Initialize supervisor with custom state schema.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StaticSupervisor
      :collapse:

   .. py:method:: _create_list_agents_tool() -> langchain_core.tools.BaseTool

      Create tool for listing available agents.


      .. autolink-examples:: _create_list_agents_tool
         :collapse:


   .. py:method:: _execute_agent_handoff(state: SupervisorReactState, agent_name: str, tool_call: dict) -> str

      Execute handoff to a specific agent from state.


      .. autolink-examples:: _execute_agent_handoff
         :collapse:


   .. py:method:: _execute_regular_tool(state: SupervisorReactState, tool_name: str, tool_call: dict) -> str

      Execute regular supervisor tools.


      .. autolink-examples:: _execute_regular_tool
         :collapse:


   .. py:method:: _execute_tool_or_agent(state: SupervisorReactState) -> dict[str, Any]

      Execute tools or agent handoffs based on the tool call.

      This replaces the standard tool node behavior to handle agent handoffs
      from state instead of just executing tools.


      .. autolink-examples:: _execute_tool_or_agent
         :collapse:


   .. py:method:: _update_engine_tools() -> None

      Update the engine's tools based on registered agents.


      .. autolink-examples:: _update_engine_tools
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph using ReactAgent pattern with custom tool execution.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: register_agent(name: str, description: str, agent: haive.agents.base.agent.Agent) -> None

      Register an agent with the supervisor.

      This updates the state and triggers tool synchronization.


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the supervisor with dynamic tools.


      .. autolink-examples:: setup_agent
         :collapse:


.. py:class:: SupervisorReactState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   State schema for ReactAgent-based supervisor with agent registry.


   .. autolink-examples:: SupervisorReactState
      :collapse:

   .. py:method:: sync_tools_with_agents() -> SupervisorReactState

      Ensure handoff tools are synchronized with registered agents.

      This validator runs after field assignment to ensure tools
      always match the registered agents.


      .. autolink-examples:: sync_tools_with_agents
         :collapse:


   .. py:attribute:: current_agent
      :type:  str | None
      :value: None



   .. py:attribute:: handoff_tools
      :type:  dict[str, langchain_core.tools.BaseTool]
      :value: None



   .. py:attribute:: last_handoff_result
      :type:  Any | None
      :value: None



   .. py:attribute:: messages
      :type:  list[Any]
      :value: None



   .. py:attribute:: registered_agents
      :type:  dict[str, AgentEntry]
      :value: None



.. py:data:: logger

