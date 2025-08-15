dynamic_activation_supervisor
=============================

.. py:module:: dynamic_activation_supervisor

.. autoapi-nested-parse::

   Dynamic Activation Supervisor for Component Management.

   This module provides DynamicActivationSupervisor, a supervisor agent that can
   dynamically activate components based on task requirements using the Dynamic
   Activation Pattern with MetaStateSchema integration.

   Based on:
   - @project_docs/active/patterns/dynamic_activation_pattern.md
   - @packages/haive-agents/examples/supervisor/advanced/dynamic_activation_example.py

   Implementation Notes:
   - Uses factory methods for complex initialization (no __init__ override)
   - Private attributes for internal state (_discovery_agent)
   - MetaStateSchema for component wrapping
   - DynamicActivationState as state schema
   - Proper Pydantic patterns throughout


   .. autolink-examples:: dynamic_activation_supervisor
      :collapse:


Classes
-------

.. autoapisummary::

   dynamic_activation_supervisor.DynamicActivationSupervisor


Module Contents
---------------

.. py:class:: DynamicActivationSupervisor

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Supervisor agent that can dynamically activate components.

   This supervisor extends the basic Agent class with dynamic activation
   capabilities. It can discover, activate, and manage components based on
   task requirements using MetaStateSchema for component wrapping.

   Key Features:
       - Dynamic component discovery using ComponentDiscoveryAgent
       - Automatic component activation based on task analysis
       - MetaStateSchema integration for component tracking
       - Factory methods for complex initialization
       - Graph-based workflow with conditional routing
       - Capability gap detection and filling

   :param name: Supervisor name
   :param engine: AugLLMConfig for LLM-based decision making
   :param state_schema: DynamicActivationState (set automatically)

   Private Attributes:
       _discovery_agent: ComponentDiscoveryAgent for finding components
       _meta_self: MetaStateSchema wrapper for self-tracking

   .. rubric:: Examples

   Basic usage::

       from haive.agents.supervisor.dynamic_activation_supervisor import DynamicActivationSupervisor
       from haive.core.engine.aug_llm import AugLLMConfig

       # Create supervisor
       supervisor = DynamicActivationSupervisor(
           name="dynamic_supervisor",
           engine=AugLLMConfig()
       )

       # Run task - supervisor will discover and activate components as needed
       result = await supervisor.arun("Calculate compound interest and create a chart")

   With discovery agent::

       supervisor = DynamicActivationSupervisor.create_with_discovery(
           name="discovery_supervisor",
           document_path="@haive-tools/docs",
           engine=AugLLMConfig()
       )

       # Supervisor will use discovery agent to find needed components
       result = await supervisor.arun("Process CSV data and generate insights")

   Manual component registration::

       supervisor = DynamicActivationSupervisor(
           name="manual_supervisor",
           engine=AugLLMConfig()
       )

       # Register components manually
       item = RegistryItem(
           id="calc_tool",
           name="Calculator",
           description="Mathematical calculations",
           component=calculator_tool
       )
       supervisor.state.registry.register(item)

       # Use registered components
       result = await supervisor.arun("Calculate 15 * 23")


   .. autolink-examples:: DynamicActivationSupervisor
      :collapse:

   .. py:method:: _activate_components_node(state: haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState) -> dict[str, Any]
      :async:


      Activate components to satisfy missing capabilities.


      .. autolink-examples:: _activate_components_node
         :collapse:


   .. py:method:: _analyze_task_node(state: haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState) -> dict[str, Any]
      :async:


      Analyze task requirements and update state.


      .. autolink-examples:: _analyze_task_node
         :collapse:


   .. py:method:: _discover_components_node(state: haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState) -> dict[str, Any]
      :async:


      Discover components for missing capabilities.


      .. autolink-examples:: _discover_components_node
         :collapse:


   .. py:method:: _execute_task_node(state: haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState) -> dict[str, Any]
      :async:


      Execute the task using active components.


      .. autolink-examples:: _execute_task_node
         :collapse:


   .. py:method:: _parse_capabilities(output: str) -> list[str]

      Parse capabilities from LLM output.


      .. autolink-examples:: _parse_capabilities
         :collapse:


   .. py:method:: _route_supervisor(state: haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState) -> str

      Route supervisor based on state.


      .. autolink-examples:: _route_supervisor
         :collapse:


   .. py:method:: _setup_supervisor_tools() -> None

      Set up default tools for the supervisor.

      This method adds core supervisor tools to the engine for
      component management and task routing.


      .. autolink-examples:: _setup_supervisor_tools
         :collapse:


   .. py:method:: _supervisor_node(state: haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState) -> dict[str, Any]
      :async:


      Main supervisor logic node.


      .. autolink-examples:: _supervisor_node
         :collapse:


   .. py:method:: activate_component_by_name(name: str) -> bool
      :async:


      Activate a component by name.

      :param name: Name of component to activate

      :returns: True if activation succeeded

      .. rubric:: Examples

      Activate specific component::

          success = await supervisor.activate_component_by_name("calculator")
          if success:
              print("Calculator activated successfully")


      .. autolink-examples:: activate_component_by_name
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.BaseGraph

      Build the dynamic activation supervisor graph.

      :returns: Compiled BaseGraph with supervisor workflow


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_with_components(name: str, components: list[dict[str, Any]], engine: haive.core.engine.aug_llm.AugLLMConfig, **kwargs) -> DynamicActivationSupervisor
      :classmethod:


      Factory method to create supervisor with pre-registered components.

      :param name: Supervisor name
      :param components: List of component dictionaries to register
      :param engine: AugLLMConfig for supervisor
      :param \*\*kwargs: Additional arguments for supervisor

      :returns: DynamicActivationSupervisor with pre-registered components

      .. rubric:: Examples

      Create with tools::

          components = [
              {
                  "id": "calc",
                  "name": "Calculator",
                  "description": "Math operations",
                  "component": calculator_tool
              },
              {
                  "id": "search",
                  "name": "Web Search",
                  "description": "Web searching",
                  "component": search_tool
              }
          ]

          supervisor = DynamicActivationSupervisor.create_with_components(
              name="tool_supervisor",
              components=components,
              engine=AugLLMConfig()
          )


      .. autolink-examples:: create_with_components
         :collapse:


   .. py:method:: create_with_discovery(name: str, document_path: str, engine: haive.core.engine.aug_llm.AugLLMConfig, **kwargs) -> DynamicActivationSupervisor
      :classmethod:


      Factory method to create supervisor with discovery agent.

      :param name: Supervisor name
      :param document_path: Path to documentation for component discovery
      :param engine: AugLLMConfig for supervisor
      :param \*\*kwargs: Additional arguments for supervisor

      :returns: DynamicActivationSupervisor with discovery capabilities

      .. rubric:: Examples

      Create with Haive tools discovery::

          supervisor = DynamicActivationSupervisor.create_with_discovery(
              name="haive_supervisor",
              document_path="@haive-tools",
              engine=AugLLMConfig()
          )

      Create with custom documentation::

          supervisor = DynamicActivationSupervisor.create_with_discovery(
              name="custom_supervisor",
              document_path="/path/to/docs",
              engine=AugLLMConfig(temperature=0.3)
          )


      .. autolink-examples:: create_with_discovery
         :collapse:


   .. py:method:: get_active_component_names() -> list[str]

      Get names of all active components.

      :returns: List of active component names

      .. rubric:: Examples

      List active components::

          active_names = supervisor.get_active_component_names()
          print(f"Active components: {', '.join(active_names)}")


      .. autolink-examples:: get_active_component_names
         :collapse:


   .. py:method:: get_registry_stats() -> dict[str, Any]

      Get statistics about the component registry.

      :returns: Dictionary with registry statistics

      .. rubric:: Examples

      Check registry status::

          stats = supervisor.get_registry_stats()
          print(f"Total components: {stats['total_components']}")
          print(f"Active components: {stats['active_components']}")


      .. autolink-examples:: get_registry_stats
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the dynamic activation supervisor.

      This method is called during agent initialization to set up
      the supervisor's internal state and components.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _discovery_agent
      :type:  haive.agents.discovery.component_discovery_agent.ComponentDiscoveryAgent | None
      :value: None



   .. py:attribute:: _meta_self
      :type:  haive.core.schema.prebuilt.meta_state.MetaStateSchema | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState]


