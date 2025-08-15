agents.supervisor.agent
=======================

.. py:module:: agents.supervisor.agent

.. autoapi-nested-parse::

   Dynamic Supervisor V2 - Main agent implementation.

   This module contains the core DynamicSupervisor class that orchestrates
   runtime agent discovery, creation, and task routing.


   .. autolink-examples:: agents.supervisor.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.supervisor.agent.logger


Classes
-------

.. autoapisummary::

   agents.supervisor.agent.DynamicSupervisor


Functions
---------

.. autoapisummary::

   agents.supervisor.agent.create_dynamic_supervisor


Module Contents
---------------

.. py:class:: DynamicSupervisor(**data)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Advanced supervisor that discovers and creates agents at runtime.

   The DynamicSupervisor extends ReactAgent to provide intelligent task routing
   with the ability to discover, create, and manage specialized agents dynamically
   based on task requirements.

   Key capabilities:
       - Dynamic agent discovery from specifications
       - Runtime agent creation and lifecycle management
       - Intelligent task-to-agent matching
       - Performance tracking and optimization
       - Extensible discovery mechanisms

   .. attribute:: name

      Supervisor identifier

   .. attribute:: engine

      LLM configuration for supervisor reasoning

   .. attribute:: agent_specs

      Initial specifications for creatable agents

   .. attribute:: discovery_config

      Configuration for agent discovery

   .. attribute:: max_agents

      Maximum number of active agents to maintain

   .. attribute:: auto_discover

      Whether to automatically discover new agents

   .. attribute:: include_management_tools

      Whether to include agent management tools

   .. rubric:: Example

   Basic usage with predefined agent specs::

       supervisor = DynamicSupervisor(
           name="task_router",
           agent_specs=[
               AgentSpec(
                   name="researcher",
                   agent_type="ReactAgent",
                   description="Research and analysis expert",
                   specialties=["research", "analysis"],
                   tools=[web_search_tool]
               ),
               AgentSpec(
                   name="writer",
                   agent_type="SimpleAgentV3",
                   description="Content creation expert",
                   specialties=["writing", "editing"]
               )
           ]
       )

       result = await supervisor.arun(
           "Research quantum computing and write a summary"
       )

   Initialize the dynamic supervisor.

   :param \*\*data: Configuration parameters


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DynamicSupervisor
      :collapse:

   .. py:method:: _add_management_tools() -> None

      Add agent management tools to the supervisor.


      .. autolink-examples:: _add_management_tools
         :collapse:


   .. py:method:: _agent_execution_node(state: haive.agents.supervisor.state.DynamicSupervisorState) -> dict[str, Any]
      :async:


      Execute task with selected agent.


      .. autolink-examples:: _agent_execution_node
         :collapse:


   .. py:method:: _build_graph() -> None

      Build the supervisor execution graph.


      .. autolink-examples:: _build_graph
         :collapse:


   .. py:method:: _cleanup_inactive_agents(state: haive.agents.supervisor.state.DynamicSupervisorState) -> None

      Remove least recently used agents when at capacity.


      .. autolink-examples:: _cleanup_inactive_agents
         :collapse:


   .. py:method:: _discovery_node(state: haive.agents.supervisor.state.DynamicSupervisorState) -> dict[str, Any]
      :async:


      Agent discovery and creation node.


      .. autolink-examples:: _discovery_node
         :collapse:


   .. py:method:: _route_supervisor(state: haive.agents.supervisor.state.DynamicSupervisorState) -> str

      Determine next node based on workflow state.


      .. autolink-examples:: _route_supervisor
         :collapse:


   .. py:method:: _supervisor_node(state: haive.agents.supervisor.state.DynamicSupervisorState) -> dict[str, Any]
      :async:


      Supervisor reasoning node.

      Analyzes tasks and determines routing strategy.


      .. autolink-examples:: _supervisor_node
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any] | list[langchain_core.messages.BaseMessage]) -> Any
      :async:


      Run the supervisor asynchronously.

      :param input_data: Task input (string, dict, or messages)

      :returns: Agent execution result


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: get_metrics() -> dict[str, Any]

      Get supervisor performance metrics.

      :returns: Dictionary of metrics including agent stats


      .. autolink-examples:: get_metrics
         :collapse:


   .. py:method:: run(input_data: str | dict[str, Any] | list[langchain_core.messages.BaseMessage]) -> Any

      Run the supervisor synchronously.

      :param input_data: Task input

      :returns: Agent execution result


      .. autolink-examples:: run
         :collapse:


   .. py:method:: validate_agent_specs(v: list[haive.agents.supervisor.models.AgentSpec]) -> list[haive.agents.supervisor.models.AgentSpec]
      :classmethod:


      Validate agent specifications have unique names.


      .. autolink-examples:: validate_agent_specs
         :collapse:


   .. py:attribute:: _graph
      :type:  langgraph.graph.StateGraph | None


   .. py:attribute:: _state
      :type:  haive.agents.supervisor.state.DynamicSupervisorState


   .. py:attribute:: agent_specs
      :type:  list[haive.agents.supervisor.models.AgentSpec]
      :value: None



   .. py:attribute:: auto_discover
      :type:  bool
      :value: None



   .. py:attribute:: discovery_config
      :type:  haive.agents.supervisor.models.DiscoveryConfig
      :value: None



   .. py:attribute:: include_management_tools
      :type:  bool
      :value: None



   .. py:attribute:: max_agents
      :type:  int
      :value: None



.. py:function:: create_dynamic_supervisor(name: str = 'dynamic_supervisor', agent_specs: list[haive.agents.supervisor.models.AgentSpec] | None = None, discovery_mode: haive.agents.supervisor.models.AgentDiscoveryMode = AgentDiscoveryMode.MANUAL, **kwargs) -> DynamicSupervisor

   Factory function to create a configured dynamic supervisor.

   :param name: Supervisor name
   :param agent_specs: Initial agent specifications
   :param discovery_mode: How to discover new agents
   :param \*\*kwargs: Additional configuration

   :returns: Configured DynamicSupervisor instance

   .. rubric:: Example

   >>> supervisor = create_dynamic_supervisor(
   ...     name="task_router",
   ...     agent_specs=[math_spec, research_spec],
   ...     discovery_mode="manual",
   ...     max_agents=20
   ... )


   .. autolink-examples:: create_dynamic_supervisor
      :collapse:

.. py:data:: logger

