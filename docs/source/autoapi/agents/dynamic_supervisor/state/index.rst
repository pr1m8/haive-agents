agents.dynamic_supervisor.state
===============================

.. py:module:: agents.dynamic_supervisor.state

.. autoapi-nested-parse::

   State schemas for dynamic supervisor agent.

   from typing import Any
   This module defines the state management for the dynamic supervisor, including
   agent registry, routing control, and tool generation. Two versions are provided:
   - SupervisorState: Uses exclude=True for agent serialization (v1)
   - SupervisorStateV2: Attempts full agent serialization (experimental)

   Classes:
       SupervisorState: Base supervisor state with agent registry
       SupervisorStateWithTools: Extends base with dynamic tool generation
       SupervisorStateV2: Experimental version with full serialization

   .. rubric:: Example

   Creating and managing supervisor state::

       state = SupervisorState()
       state.add_agent("search", search_agent, "Search specialist")
       state.activate_agent("search")

       # List active agents
       active = state.list_active_agents()


   .. autolink-examples:: agents.dynamic_supervisor.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.dynamic_supervisor.state.SupervisorState
   agents.dynamic_supervisor.state.SupervisorStateV2
   agents.dynamic_supervisor.state.SupervisorStateWithTools


Module Contents
---------------

.. py:class:: SupervisorState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages.messages_with_token_usage.MessagesStateWithTokenUsage`


   Base state for dynamic supervisor with agent registry.

   Inherits from MessagesState for message handling and adds agent management
   capabilities. Agents are stored in a registry with metadata for routing.

   .. attribute:: agents

      Registry of available agents by name

   .. attribute:: active_agents

      List of currently active agent names (unique)

   .. attribute:: next_agent

      Name of agent to execute next (routing control)

   .. attribute:: agent_task

      Task to pass to the selected agent

   .. attribute:: agent_response

      Response from the last executed agent

   .. rubric:: Example

   Basic agent management::

       state = SupervisorState()
       state.add_agent("math", math_agent, "Math specialist")
       state.set_routing("math", "Calculate 2+2")


   .. autolink-examples:: SupervisorState
      :collapse:

   .. py:method:: activate_agent(name: str) -> bool

      Activate an inactive agent.

      :param name: Agent name to activate

      :returns: True if agent was activated, False if not found


      .. autolink-examples:: activate_agent
         :collapse:


   .. py:method:: add_agent(name: str, agent: Any, description: str, active: bool = True) -> None

      Add an agent to the registry.

      :param name: Unique identifier for the agent
      :param agent: The agent instance
      :param description: Human-readable description of agent capabilities
      :param active: Whether agent should be immediately active

      .. rubric:: Example

      state.add_agent("search", search_agent, "Web search expert", active=True)


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: clear_execution_state() -> None

      Clear execution state after completion.


      .. autolink-examples:: clear_execution_state
         :collapse:


   .. py:method:: deactivate_agent(name: str) -> bool

      Deactivate an active agent.

      :param name: Agent name to deactivate

      :returns: True if agent was deactivated, False if not found


      .. autolink-examples:: deactivate_agent
         :collapse:


   .. py:method:: ensure_unique_agents(v: list[str]) -> list[str]
      :classmethod:


      Ensure active agents list contains unique values.

      :param v: List of agent names

      :returns: List with duplicates removed


      .. autolink-examples:: ensure_unique_agents
         :collapse:


   .. py:method:: get_agent(name: str) -> Any | None

      Get agent instance by name.

      :param name: Agent name

      :returns: Agent instance or None if not found


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: list_active_agents() -> dict[str, str]

      List all active agents with descriptions.

      :returns: Dict mapping agent names to descriptions


      .. autolink-examples:: list_active_agents
         :collapse:


   .. py:method:: list_all_agents() -> dict[str, str]

      List all agents (active and inactive) with descriptions.

      :returns: Dict mapping agent names to descriptions


      .. autolink-examples:: list_all_agents
         :collapse:


   .. py:method:: remove_agent(name: str) -> bool

      Remove an agent from the registry completely.

      :param name: Agent name to remove

      :returns: True if agent was removed, False if not found


      .. autolink-examples:: remove_agent
         :collapse:


   .. py:attribute:: active_agents
      :type:  list[str]
      :value: None



   .. py:attribute:: agent_response
      :type:  str | None
      :value: None



   .. py:attribute:: agents
      :type:  dict[str, haive.agents.dynamic_supervisor.models.AgentInfo]
      :value: None



   .. py:attribute:: execution_success
      :type:  bool
      :value: None



   .. py:attribute:: last_executed_agent
      :type:  str | None
      :value: None



   .. py:attribute:: model_config


.. py:class:: SupervisorStateV2

   Bases: :py:obj:`haive.core.schema.prebuilt.messages.messages_with_token_usage.MessagesStateWithTokenUsage`


   Experimental supervisor state with full agent serialization.

   This version attempts to serialize agents fully rather than excluding them.
   May require custom serialization logic or agent reconstruction.

   .. warning::

      This is experimental and may not work with all agent types or
      checkpointing systems. Use SupervisorState for production.


   .. autolink-examples:: SupervisorStateV2
      :collapse:

   .. py:attribute:: agents
      :type:  dict[str, haive.agents.dynamic_supervisor.models.AgentInfoV2]
      :value: None



   .. py:attribute:: model_config


.. py:class:: SupervisorStateWithTools

   Bases: :py:obj:`SupervisorState`


   Supervisor state with dynamic tool generation.

   Extends SupervisorState with automatic tool generation from registered agents.
   Creates handoff tools for each agent and manages a dynamic choice model.

   .. attribute:: agent_choice_model

      Dynamic model for validated agent selection

   .. attribute:: generated_tools

      List of tool names generated from agents

   .. rubric:: Example

   Using dynamic tools::

       state = SupervisorStateWithTools()
       state.add_agent("search", agent, "Search expert")
       state.sync_agents()  # Generates handoff_to_search tool

       tools = state.get_all_tools()  # Get tool instances


   .. autolink-examples:: SupervisorStateWithTools
      :collapse:

   .. py:method:: _generate_tools_from_agents() -> None

      Generate tools from current agents.


      .. autolink-examples:: _generate_tools_from_agents
         :collapse:


   .. py:method:: _sync_internal() -> None

      Internal sync method.


      .. autolink-examples:: _sync_internal
         :collapse:


   .. py:method:: _update_choice_model() -> None

      Update choice model with current agents.


      .. autolink-examples:: _update_choice_model
         :collapse:


   .. py:method:: activate_agent(name: str) -> bool

      Override to trigger tool regeneration.


      .. autolink-examples:: activate_agent
         :collapse:


   .. py:method:: add_agent(name: str, agent: Any, description: str, active: bool = True) -> None

      Override to trigger tool regeneration.


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: deactivate_agent(name: str) -> bool

      Override to trigger tool regeneration.


      .. autolink-examples:: deactivate_agent
         :collapse:


   .. py:method:: get_all_tools() -> list[Any]

      Get all generated tools as callable instances.

      :returns: List of tool instances ready for use


      .. autolink-examples:: get_all_tools
         :collapse:


   .. py:method:: remove_agent(name: str) -> bool

      Override to trigger tool regeneration.


      .. autolink-examples:: remove_agent
         :collapse:


   .. py:method:: sync_agents() -> None

      Public method to sync agents with tools and choice model.

      Call this after adding/removing agents to regenerate tools.


      .. autolink-examples:: sync_agents
         :collapse:


   .. py:method:: sync_on_init() -> SupervisorStateWithTools

      Sync tools and choice model after initialization.


      .. autolink-examples:: sync_on_init
         :collapse:


   .. py:attribute:: agent_choice_model
      :type:  haive.core.common.models.dynamic_choice_model.DynamicChoiceModel
      :value: None



   .. py:attribute:: generated_tools
      :type:  list[str]
      :value: None



