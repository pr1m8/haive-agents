registry_supervisor
===================

.. py:module:: registry_supervisor

.. autoapi-nested-parse::

   Registry-Based Dynamic Supervisor using DynamicChoiceModel.

   The supervisor gets agents from an agent registry instead of creating them.
   Uses DynamicChoiceModel for selection and all agents are ReactAgents.


   .. autolink-examples:: registry_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   registry_supervisor.logger


Classes
-------

.. autoapisummary::

   registry_supervisor.AgentRegistry
   registry_supervisor.AgentRetrievalTool
   registry_supervisor.AgentSelectionTool
   registry_supervisor.RegistrySupervisor


Functions
---------

.. autoapisummary::

   registry_supervisor.test_registry_supervisor


Module Contents
---------------

.. py:class:: AgentRegistry

   Registry of available agents that can be added to supervisor.


   .. autolink-examples:: AgentRegistry
      :collapse:

   .. py:method:: get_agent(agent_name: str) -> haive.agents.react.agent.ReactAgent | None

      Get an agent from registry.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: get_available_agents() -> dict[str, str]

      Get available agents with capabilities.


      .. autolink-examples:: get_available_agents
         :collapse:


   .. py:method:: register_agent(agent: haive.agents.react.agent.ReactAgent, capability: str | None = None)

      Register an agent as available.


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: search_agents_by_capability(task_description: str) -> list[str]

      Search for agents that might handle the task.


      .. autolink-examples:: search_agents_by_capability
         :collapse:


   .. py:attribute:: agent_capabilities
      :type:  dict[str, str]


   .. py:attribute:: available_agents
      :type:  dict[str, haive.agents.react.agent.ReactAgent]


.. py:class:: AgentRetrievalTool(registry: AgentRegistry, supervisor, **kwargs)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool to retrieve agents from registry based on task needs.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentRetrievalTool
      :collapse:

   .. py:method:: _run(task_description: str, agent_type_needed: str = '') -> str

      Retrieve agent from registry.


      .. autolink-examples:: _run
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """Get a suitable agent from the agent registry for the current task.
             Use this when no currently active agent can handle the request."""

      .. raw:: html

         </details>



      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'get_agent_from_registry'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


   .. py:attribute:: registry


   .. py:attribute:: supervisor


.. py:class:: AgentSelectionTool(choice_model: haive.core.common.models.dynamic_choice_model.DynamicChoiceModel, **kwargs)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool that uses DynamicChoiceModel to select from active agents.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentSelectionTool
      :collapse:

   .. py:method:: _run(task_description: str) -> str

      Select from currently active agents.


      .. autolink-examples:: _run
         :collapse:


   .. py:attribute:: choice_model


   .. py:attribute:: description
      :type:  str
      :value: 'Select the best active agent for the current task using the choice model.'


      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'select_active_agent'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


.. py:class:: RegistrySupervisor

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Supervisor that gets agents from a registry using DynamicChoiceModel.

   This supervisor:
   1. Maintains a registry of available agents
   2. Uses DynamicChoiceModel to track active agents
   3. Uses tools to select from active agents or get new ones from registry
   4. All execution agents are ReactAgents


   .. autolink-examples:: RegistrySupervisor
      :collapse:

   .. py:method:: _add_agent_to_active(agent: haive.agents.react.agent.ReactAgent)

      Add agent to active roster and update choice model.


      .. autolink-examples:: _add_agent_to_active
         :collapse:


   .. py:method:: _create_executor_node()

      Create executor that runs selected ReactAgent.


      .. autolink-examples:: _create_executor_node
         :collapse:


   .. py:method:: _create_supervisor_node()

      Create supervisor node that uses tools for agent management.


      .. autolink-examples:: _create_supervisor_node
         :collapse:


   .. py:method:: _extract_state_dict(state: Any) -> dict[str, Any]

      Extract state dict preserving messages.


      .. autolink-examples:: _extract_state_dict
         :collapse:


   .. py:method:: _parse_decision_result(result: dict[str, Any]) -> str | None

      Parse the supervisor's decision result.


      .. autolink-examples:: _parse_decision_result
         :collapse:


   .. py:method:: _route_from_supervisor(state: Any) -> str

      Route from supervisor.


      .. autolink-examples:: _route_from_supervisor
         :collapse:


   .. py:method:: _update_choice_model()

      Update choice model with current active agents.


      .. autolink-examples:: _update_choice_model
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with registry integration.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_active_agents() -> list[str]

      Get currently active agents.


      .. autolink-examples:: get_active_agents
         :collapse:


   .. py:method:: get_choice_model_status() -> dict[str, Any]

      Get choice model status.


      .. autolink-examples:: get_choice_model_status
         :collapse:


   .. py:method:: get_registry_agents() -> dict[str, str]

      Get available agents in registry.


      .. autolink-examples:: get_registry_agents
         :collapse:


   .. py:method:: populate_registry(agents: list[haive.agents.react.agent.ReactAgent], capabilities: list[str] | None = None)

      Populate the agent registry with available agents.


      .. autolink-examples:: populate_registry
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up supervisor with registry and choice model.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _active_agents
      :type:  dict[str, haive.agents.react.agent.ReactAgent]
      :value: None



   .. py:attribute:: _choice_model
      :type:  haive.core.common.models.dynamic_choice_model.DynamicChoiceModel | None
      :value: None



   .. py:attribute:: _registry
      :type:  AgentRegistry
      :value: None



   .. py:attribute:: max_active_agents
      :type:  int
      :value: None



.. py:function:: test_registry_supervisor()
   :async:


   Test the registry supervisor.


   .. autolink-examples:: test_registry_supervisor
      :collapse:

.. py:data:: logger

