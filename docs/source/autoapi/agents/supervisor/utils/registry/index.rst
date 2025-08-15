agents.supervisor.utils.registry
================================

.. py:module:: agents.supervisor.utils.registry

.. autoapi-nested-parse::

   Agent Registry for Haive Supervisor System.

   Manages agent lifecycle and routing model synchronization using DynamicChoiceModel.
   Provides runtime agent registration/deregistration with automatic routing updates.


   .. autolink-examples:: agents.supervisor.utils.registry
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.supervisor.utils.registry.console
   agents.supervisor.utils.registry.logger


Classes
-------

.. autoapisummary::

   agents.supervisor.utils.registry.AgentRegistry


Module Contents
---------------

.. py:class:: AgentRegistry(routing_model: haive.core.common.models.dynamic_choice_model.DynamicChoiceModel[str])

   Manages agent lifecycle and routing model synchronization.

   This class provides a centralized registry for managing agents in a supervisor
   system, with automatic synchronization to a DynamicChoiceModel for routing.

   Features:
       - Runtime agent registration/deregistration
       - Automatic routing model updates
       - Agent capability tracking
       - Conflict detection and resolution
       - Rich visualization of registry state

   Initialize agent registry.

   :param routing_model: DynamicChoiceModel to synchronize with agent changes


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentRegistry
      :collapse:

   .. py:method:: _print_registration_details(agent_name: str, action: str) -> None

      Print detailed registration information.

      :param agent_name: Name of affected agent
      :param action: Action performed (REGISTER/UNREGISTER)


      .. autolink-examples:: _print_registration_details
         :collapse:


   .. py:method:: clear_all() -> None

      Remove all registered agents.

      Warning: This will clear the entire registry!


      .. autolink-examples:: clear_all
         :collapse:


   .. py:method:: get_agent(name: str) -> haive.agents.base.agent.Agent | None

      Get agent by name.

      :param name: Agent name

      :returns: Agent instance or None if not found


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: get_agent_capabilities() -> dict[str, str]

      Get mapping of agent names to their capabilities.

      :returns: Dict mapping agent names to capability descriptions


      .. autolink-examples:: get_agent_capabilities
         :collapse:


   .. py:method:: get_agent_capability(agent_name: str) -> str | None

      Get capability description for specific agent.

      :param agent_name: Name of agent

      :returns: Capability description or None if agent not found


      .. autolink-examples:: get_agent_capability
         :collapse:


   .. py:method:: get_agent_count() -> int

      Get number of registered agents.

      :returns: Number of currently registered agents


      .. autolink-examples:: get_agent_count
         :collapse:


   .. py:method:: get_available_agents() -> list[str]

      Get list of currently available agent names.

      :returns: List of agent names available for routing


      .. autolink-examples:: get_available_agents
         :collapse:


   .. py:method:: get_registry_stats() -> dict[str, Any]

      Get registry statistics.

      :returns: Dictionary with registry statistics


      .. autolink-examples:: get_registry_stats
         :collapse:


   .. py:method:: get_routing_options() -> list[str]

      Get all routing options including END.

      :returns: List of all valid routing choices


      .. autolink-examples:: get_routing_options
         :collapse:


   .. py:method:: is_agent_registered(agent_name: str) -> bool

      Check if agent is registered.

      :param agent_name: Agent name to check

      :returns: True if agent is registered, False otherwise


      .. autolink-examples:: is_agent_registered
         :collapse:


   .. py:method:: mark_rebuilt() -> None

      Mark that supervisor graph has been rebuilt.


      .. autolink-examples:: mark_rebuilt
         :collapse:


   .. py:method:: needs_rebuild() -> bool

      Check if supervisor graph needs rebuilding.

      :returns: True if agents have been added/removed since last check


      .. autolink-examples:: needs_rebuild
         :collapse:


   .. py:method:: print_registry_state() -> None

      Print comprehensive registry state information.


      .. autolink-examples:: print_registry_state
         :collapse:


   .. py:method:: register(agent: haive.agents.base.agent.Agent, capability_description: str | None = None) -> bool

      Register an agent and update routing model.

      :param agent: Agent instance to register
      :param capability_description: Optional description of agent capabilities

      :returns: True if registration successful, False if agent name conflict
      :rtype: bool

      :raises ValueError: If agent has no name or invalid configuration


      .. autolink-examples:: register
         :collapse:


   .. py:method:: unregister(agent_name: str) -> bool

      Remove an agent and update routing model.

      :param agent_name: Name of agent to remove

      :returns: True if removal successful, False if agent not found
      :rtype: bool


      .. autolink-examples:: unregister
         :collapse:


   .. py:method:: validate_routing_choice(choice: str) -> bool

      Validate if a routing choice is valid.

      :param choice: Routing choice to validate

      :returns: True if choice is valid, False otherwise


      .. autolink-examples:: validate_routing_choice
         :collapse:


   .. py:attribute:: _rebuild_needed
      :value: False



   .. py:attribute:: agent_capabilities
      :type:  dict[str, str]


   .. py:attribute:: agents
      :type:  dict[str, haive.agents.base.agent.Agent]


   .. py:attribute:: registration_timestamps
      :type:  dict[str, float]


   .. py:attribute:: routing_model


.. py:data:: console

.. py:data:: logger

