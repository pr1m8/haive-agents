basic_supervisor
================

.. py:module:: basic_supervisor

.. autoapi-nested-parse::

   Haive Supervisor Agent - ReactAgent with Dynamic Routing and Agent Registry.

   ReactAgent-based supervisor with:
   1. Agent registry with add_agent tool
   2. Dynamic routing tool that creates base model with agents in state
   3. Prompt template showing available agents
   4. Generic agent execution node for running selected agents


   .. autolink-examples:: basic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   basic_supervisor.console
   basic_supervisor.logger


Classes
-------

.. autoapisummary::

   basic_supervisor.SupervisorAgent
   basic_supervisor.SupervisorState


Module Contents
---------------

.. py:class:: SupervisorAgent(name: str = 'supervisor', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   ReactAgent-based supervisor with dynamic routing and agent registry.

   Architecture:
   1. ReactAgent with add_agent tool for dynamic agent registration
   2. Dynamic routing tool creates base model with agents in state
   3. Prompt template shows available agents and gets routing decision
   4. Generic agent execution node runs the selected agent

   Initialize supervisor agent.

   :param name: Supervisor name
   :param engine: LLM engine for routing decisions
   :param \*\*kwargs: Additional ReactAgent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SupervisorAgent
      :collapse:

   .. py:method:: _create_supervisor_prompt() -> str

      Create supervisor prompt template.


      .. autolink-examples:: _create_supervisor_prompt
         :collapse:


   .. py:method:: _create_supervisor_tools()

      Create tools for supervisor agent.


      .. autolink-examples:: _create_supervisor_tools
         :collapse:


   .. py:method:: _prepare_agent_state(supervisor_state, agent: haive.agents.base.agent.Agent)

      Prepare state for agent execution.


      .. autolink-examples:: _prepare_agent_state
         :collapse:


   .. py:method:: add_worker_agent(agent: haive.agents.base.agent.Agent, capability_description: str | None = None) -> bool

      Add a worker agent to the supervisor registry.

      :param agent: Worker agent to add
      :param capability_description: Description of agent capabilities

      :returns: True if added successfully
      :rtype: bool


      .. autolink-examples:: add_worker_agent
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with proper nodes for dynamic routing.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_generic_agent_execution_node() -> Any

      Create generic agent execution node that takes routing output and runs selected agent.


      .. autolink-examples:: create_generic_agent_execution_node
         :collapse:


   .. py:method:: get_worker_agents() -> list[str]

      Get list of worker agent names.


      .. autolink-examples:: get_worker_agents
         :collapse:


   .. py:method:: print_supervisor_status() -> None

      Print supervisor status.


      .. autolink-examples:: print_supervisor_status
         :collapse:


   .. py:method:: remove_worker_agent(agent_name: str) -> bool

      Remove a worker agent.

      :param agent_name: Name of agent to remove

      :returns: True if removed successfully
      :rtype: bool


      .. autolink-examples:: remove_worker_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Register engine in state engines dict for proper node lookup.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _agent_registry
      :type:  dict[str, haive.agents.base.agent.Agent]


.. py:class:: SupervisorState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State schema extending MessagesState with supervisor-specific fields.


   .. autolink-examples:: SupervisorState
      :collapse:

   .. py:attribute:: agents
      :type:  dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.base.base.Engine]
      :value: None



   .. py:attribute:: last_agent
      :type:  str | None
      :value: None



   .. py:attribute:: next_agent
      :type:  str | None
      :value: None



   .. py:attribute:: routing_decision
      :type:  str | None
      :value: None



   .. py:attribute:: routing_timestamp
      :type:  float | None
      :value: None



.. py:data:: console

.. py:data:: logger

