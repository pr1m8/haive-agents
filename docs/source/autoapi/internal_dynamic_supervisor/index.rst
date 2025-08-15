internal_dynamic_supervisor
===========================

.. py:module:: internal_dynamic_supervisor

.. autoapi-nested-parse::

   Internal Dynamic Supervisor - Agents Added by Supervisor Decisions.

   The supervisor itself decides when to add/remove agents based on requests,
   not external management calls.


   .. autolink-examples:: internal_dynamic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   internal_dynamic_supervisor.logger


Classes
-------

.. autoapisummary::

   internal_dynamic_supervisor.InternalDynamicSupervisor


Functions
---------

.. autoapisummary::

   internal_dynamic_supervisor.test_internal_dynamic


Module Contents
---------------

.. py:class:: InternalDynamicSupervisor

   Bases: :py:obj:`haive.agents.multi.base.agent.MultiAgent`


   Supervisor that internally decides when to add/remove agents.

   The supervisor analyzes requests and:
   1. Checks if existing agents can handle the task
   2. If not, creates/adds appropriate agents
   3. Routes to the best available agent
   4. Can remove agents when no longer needed


   .. autolink-examples:: InternalDynamicSupervisor
      :collapse:

   .. py:method:: _create_agent_creator_node()

      Create node that actually creates new agents.


      .. autolink-examples:: _create_agent_creator_node
         :collapse:


   .. py:method:: _create_agent_from_template(agent_type: str, request: str) -> bool
      :async:


      Actually create an agent from a template.


      .. autolink-examples:: _create_agent_from_template
         :collapse:


   .. py:method:: _create_dynamic_executor_node()

      Create executor that runs the selected agent.


      .. autolink-examples:: _create_dynamic_executor_node
         :collapse:


   .. py:method:: _create_internal_supervisor_node()

      Create supervisor that makes internal decisions about agent management.


      .. autolink-examples:: _create_internal_supervisor_node
         :collapse:


   .. py:method:: _determine_needed_agent_type(content: str) -> str | None

      Determine what type of agent is needed for this request.


      .. autolink-examples:: _determine_needed_agent_type
         :collapse:


   .. py:method:: _extract_state_dict(state: Any) -> dict[str, Any]

      Extract state dict preserving messages.


      .. autolink-examples:: _extract_state_dict
         :collapse:


   .. py:method:: _find_suitable_existing_agent(content: str) -> str | None

      Find if we have an existing agent that can handle the request.


      .. autolink-examples:: _find_suitable_existing_agent
         :collapse:


   .. py:method:: _route_from_supervisor(state: Any) -> str

      Route from supervisor based on action decided.


      .. autolink-examples:: _route_from_supervisor
         :collapse:


   .. py:method:: _setup_agent_templates()

      Set up templates for agents the supervisor can create.


      .. autolink-examples:: _setup_agent_templates
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with internal decision making.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_available_templates() -> dict[str, dict[str, Any]]

      Get available agent templates.


      .. autolink-examples:: get_available_templates
         :collapse:


   .. py:method:: get_creation_history() -> list[dict[str, Any]]

      Get history of agents created by supervisor.


      .. autolink-examples:: get_creation_history
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up with agent creation templates.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _agent_templates
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: _creation_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: coordination_mode
      :type:  Literal['internal_dynamic']
      :value: None



   .. py:attribute:: enable_internal_agent_creation
      :type:  bool
      :value: None



   .. py:attribute:: max_agents
      :type:  int
      :value: None



.. py:function:: test_internal_dynamic()
   :async:


   Test the internal dynamic supervisor.


   .. autolink-examples:: test_internal_dynamic
      :collapse:

.. py:data:: logger

