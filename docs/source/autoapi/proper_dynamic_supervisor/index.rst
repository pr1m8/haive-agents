proper_dynamic_supervisor
=========================

.. py:module:: proper_dynamic_supervisor

.. autoapi-nested-parse::

   Proper Dynamic Supervisor using correct state extraction patterns.

   This implementation follows the EngineNode/AgentNode patterns for proper
   state handling and dynamic agent execution without graph rebuilding.


   .. autolink-examples:: proper_dynamic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   proper_dynamic_supervisor.logger


Classes
-------

.. autoapisummary::

   proper_dynamic_supervisor.MockAgent
   proper_dynamic_supervisor.ProperDynamicSupervisor


Module Contents
---------------

.. py:class:: MockAgent(name: str, response_prefix: str | None = None)

   Simple mock agent for testing.


   .. autolink-examples:: MockAgent
      :collapse:

   .. py:method:: ainvoke(state: dict[str, Any], config=None) -> dict[str, Any]
      :async:



   .. py:attribute:: name


   .. py:attribute:: response_prefix
      :value: 'Uninferable response'



.. py:class:: ProperDynamicSupervisor(**kwargs)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Dynamic supervisor that executes agents without graph rebuilding.

   Key design:
   1. Fixed graph structure: supervisor -> executor -> supervisor
   2. Dynamic agent execution in executor node
   3. Proper state extraction following EngineNode patterns
   4. No graph rebuilding needed - agents are executed dynamically


   .. autolink-examples:: ProperDynamicSupervisor
      :collapse:

   .. py:method:: _create_supervisor_node()

      Create the supervisor decision node.


      .. autolink-examples:: _create_supervisor_node
         :collapse:


   .. py:method:: _route_supervisor(state: dict[str, Any] | Any) -> str

      Route from supervisor node.


      .. autolink-examples:: _route_supervisor
         :collapse:


   .. py:method:: _select_agent(content: str, available_agents: list[str]) -> str | None

      Select the best agent for the given content.

      This is a simple implementation - can be enhanced with:
      - LLM-based routing
      - Capability matching
      - Performance metrics
      - Load balancing


      .. autolink-examples:: _select_agent
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the fixed supervisor graph structure.

      The graph structure is:
      1. supervisor: Decides which agent to execute
      2. executor: Dynamically executes the chosen agent
      3. Loop back to supervisor or END

      No rebuilding needed when agents are added/removed!


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_registered_agents() -> list[str]

      Get list of registered agent names.


      .. autolink-examples:: get_registered_agents
         :collapse:


   .. py:method:: getagent_capabilities() -> dict[str, str]

      Get agent capabilities descriptions.


      .. autolink-examples:: getagent_capabilities
         :collapse:


   .. py:method:: register_agent(agent: Any, capability: str | None = None, agent_name: str | None = None) -> bool

      Register an agent for dynamic execution.

      :param agent: The agent instance to register
      :param capability: Description of agent's capabilities
      :param agent_name: Optional name override (uses agent.name by default)

      :returns: Success status
      :rtype: bool


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: unregister_agent(agent_name: str) -> bool

      Unregister an agent.

      :param agent_name: Name of agent to remove

      :returns: Success status
      :rtype: bool


      .. autolink-examples:: unregister_agent
         :collapse:


   .. py:attribute:: agent_capabilities
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: agent_registry
      :type:  dict[str, Any]
      :value: None



.. py:data:: logger

