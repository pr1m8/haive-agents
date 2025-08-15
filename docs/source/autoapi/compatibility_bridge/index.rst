compatibility_bridge
====================

.. py:module:: compatibility_bridge

.. autoapi-nested-parse::

   Compatibility Bridge for Dynamic Supervisor with Existing Multi-Agent Architecture.

   This module provides integration between the new dynamic supervisor system
   and the existing multi-agent base classes, ensuring seamless interoperability.


   .. autolink-examples:: compatibility_bridge
      :collapse:


Attributes
----------

.. autoapisummary::

   compatibility_bridge.logger


Classes
-------

.. autoapisummary::

   compatibility_bridge.DynamicMultiAgentSupervisor
   compatibility_bridge.ReactMultiAgentSupervisor


Functions
---------

.. autoapisummary::

   compatibility_bridge.create_compatible_supervisor
   compatibility_bridge.migrate_from_multi_agent


Module Contents
---------------

.. py:class:: DynamicMultiAgentSupervisor

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Multi-agent system with dynamic supervisor capabilities.

   This class bridges the gap between the existing MultiAgent architecture
   and the new dynamic supervisor system, providing:

   - Compatibility with existing MultiAgent patterns
   - Dynamic agent addition/removal during runtime
   - Integration with AgentSchemaComposer
   - Support for all existing execution modes + dynamic supervision


   .. autolink-examples:: DynamicMultiAgentSupervisor
      :collapse:

   .. py:method:: _build_dynamic_supervisor_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with integrated dynamic supervisor.


      .. autolink-examples:: _build_dynamic_supervisor_graph
         :collapse:


   .. py:method:: _create_dynamic_management_node() -> Any

      Create node for dynamic agent management operations.


      .. autolink-examples:: _create_dynamic_management_node
         :collapse:


   .. py:method:: _create_dynamic_supervisor_node() -> Any

      Create supervisor node that integrates with multi-agent state.


      .. autolink-examples:: _create_dynamic_supervisor_node
         :collapse:


   .. py:method:: _create_managed_agent_node(agent: haive.agents.base.agent.Agent) -> Any

      Create node for an agent managed by dynamic supervisor.


      .. autolink-examples:: _create_managed_agent_node
         :collapse:


   .. py:method:: _setup_hybrid_schema() -> None

      Set up hybrid schema combining AgentSchemaComposer and dynamic state.


      .. autolink-examples:: _setup_hybrid_schema
         :collapse:


   .. py:method:: _setup_schemas() -> None

      Enhanced schema setup that integrates dynamic supervisor state.


      .. autolink-examples:: _setup_schemas
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with dynamic supervisor integration.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_dynamic_status() -> dict[str, Any]

      Get status of dynamic supervisor capabilities.


      .. autolink-examples:: get_dynamic_status
         :collapse:


   .. py:method:: register_agent_dynamically(agent: haive.agents.base.agent.Agent, capability: str | None = None) -> bool
      :async:


      Register an agent dynamically at runtime.


      .. autolink-examples:: register_agent_dynamically
         :collapse:


   .. py:method:: setup_agent() -> None

      Enhanced setup with dynamic supervisor integration.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: setup_dynamic_supervisor() -> DynamicMultiAgentSupervisor

      Set up the dynamic supervisor if needed.


      .. autolink-examples:: setup_dynamic_supervisor
         :collapse:


   .. py:method:: unregister_agent_dynamically(agent_name: str) -> bool
      :async:


      Unregister an agent dynamically at runtime.


      .. autolink-examples:: unregister_agent_dynamically
         :collapse:


   .. py:attribute:: _dynamic_supervisor
      :type:  haive.agents.supervisor.integrated_supervisor.IntegratedDynamicSupervisor | None
      :value: None



   .. py:attribute:: enable_dynamic_management
      :type:  bool
      :value: None



   .. py:attribute:: supervisor_engine
      :type:  Any | None
      :value: None



   .. py:attribute:: use_choice_model
      :type:  bool
      :value: None



.. py:class:: ReactMultiAgentSupervisor

   Bases: :py:obj:`DynamicMultiAgentSupervisor`


   Multi-agent supervisor with ReactAgent-style capabilities.

   Combines ReactAgent looping behavior with multi-agent coordination
   and dynamic supervisor capabilities.


   .. autolink-examples:: ReactMultiAgentSupervisor
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with React-style looping and multi-agent coordination.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: execution_mode
      :type:  str
      :value: None



.. py:function:: create_compatible_supervisor(agents: collections.abc.Sequence[haive.agents.base.agent.Agent], name: str = 'Compatible Supervisor', enable_dynamic: bool = True, supervisor_engine: Any = None) -> DynamicMultiAgentSupervisor | haive.agents.multi.base.MultiAgent

   Factory function to create compatible supervisor based on requirements.

   :param agents: List of agents to manage
   :param name: Name of the supervisor system
   :param enable_dynamic: Whether to enable dynamic capabilities
   :param supervisor_engine: Engine for supervisor decisions

   :returns: Either DynamicMultiAgentSupervisor or standard MultiAgent


   .. autolink-examples:: create_compatible_supervisor
      :collapse:

.. py:function:: migrate_from_multi_agent(multi_agent: haive.agents.multi.base.MultiAgent) -> DynamicMultiAgentSupervisor

   Migrate existing MultiAgent to dynamic supervisor version.

   :param multi_agent: Existing MultiAgent instance

   :returns: DynamicMultiAgentSupervisor with same configuration


   .. autolink-examples:: migrate_from_multi_agent
      :collapse:

.. py:data:: logger

