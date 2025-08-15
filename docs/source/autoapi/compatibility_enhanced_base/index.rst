compatibility_enhanced_base
===========================

.. py:module:: compatibility_enhanced_base

.. autoapi-nested-parse::

   Compatibility-Enhanced Multi-Agent Base.

   from typing import Any
   This module extends the multi-agent base with built-in compatibility checking,
   ensuring agents are compatible before building workflows and providing
   automatic adaptation when possible.


   .. autolink-examples:: compatibility_enhanced_base
      :collapse:


Attributes
----------

.. autoapisummary::

   compatibility_enhanced_base.logger


Classes
-------

.. autoapisummary::

   compatibility_enhanced_base.CompatibilityEnhancedConditionalAgent
   compatibility_enhanced_base.CompatibilityEnhancedMultiAgent
   compatibility_enhanced_base.CompatibilityEnhancedParallelAgent
   compatibility_enhanced_base.CompatibilityEnhancedSequentialAgent
   compatibility_enhanced_base.CompatibilityMode
   compatibility_enhanced_base.CompatibilityResult


Functions
---------

.. autoapisummary::

   compatibility_enhanced_base.create_compatible_multi_agent


Module Contents
---------------

.. py:class:: CompatibilityEnhancedConditionalAgent(**kwargs)

   Bases: :py:obj:`CompatibilityEnhancedMultiAgent`


   Conditional agent with built-in compatibility checking.


   .. autolink-examples:: CompatibilityEnhancedConditionalAgent
      :collapse:

.. py:class:: CompatibilityEnhancedMultiAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Multi-agent system with built-in compatibility checking and automatic adaptation.

   This class extends the base MultiAgent with comprehensive compatibility checking
   that runs automatically when agents are added, when graphs are built, and during
   runtime to ensure smooth agent interaction.

   Key Features:
   - Automatic compatibility checking when agents are added
   - Built-in adapter creation for incompatible agents
   - Runtime compatibility monitoring
   - Detailed compatibility reporting
   - Multiple compatibility modes (strict, adaptive, permissive, auto-fix)

   .. rubric:: Example

   >>> system = CompatibilityEnhancedMultiAgent(
   ...     agents=[retrieval_agent, grading_agent, answer_agent],
   ...     compatibility_mode=CompatibilityMode.ADAPTIVE
   ... )
   >>> # Compatibility is automatically checked and issues are resolved


   .. autolink-examples:: CompatibilityEnhancedMultiAgent
      :collapse:

   .. py:method:: _adapt_agent_for_compatibility(agent: haive.agents.base.agent.Agent, compatibility_result: CompatibilityResult) -> None

      Adapt an agent to improve compatibility.


      .. autolink-examples:: _adapt_agent_for_compatibility
         :collapse:


   .. py:method:: _apply_field_mapping_adapter(agent: haive.agents.base.agent.Agent, adapter_spec: dict[str, Any]) -> None

      Apply a field mapping adapter to an agent.


      .. autolink-examples:: _apply_field_mapping_adapter
         :collapse:


   .. py:method:: _auto_fix_compatibility(agent: haive.agents.base.agent.Agent, compatibility_result: CompatibilityResult) -> None

      Automatically fix compatibility issues where possible.


      .. autolink-examples:: _auto_fix_compatibility
         :collapse:


   .. py:method:: _check_agent_compatibility(new_agent: haive.agents.base.agent.Agent) -> CompatibilityResult

      Check compatibility of a new agent with existing agents.


      .. autolink-examples:: _check_agent_compatibility
         :collapse:


   .. py:method:: _check_agent_pair_compatibility(source_agent: haive.agents.base.agent.Agent, target_agent: haive.agents.base.agent.Agent) -> dict[str, Any]

      Check compatibility between two specific agents.


      .. autolink-examples:: _check_agent_pair_compatibility
         :collapse:


   .. py:method:: _check_state_schema_compatibility(agent: haive.agents.base.agent.Agent) -> dict[str, Any]

      Check if agent is compatible with the shared state schema.


      .. autolink-examples:: _check_state_schema_compatibility
         :collapse:


   .. py:method:: _extract_adapter_suggestions(compat_result) -> list[dict[str, Any]]

      Extract adapter suggestions from compatibility result.


      .. autolink-examples:: _extract_adapter_suggestions
         :collapse:


   .. py:method:: _generate_compatibility_recommendations() -> list[str]

      Generate recommendations for improving compatibility.


      .. autolink-examples:: _generate_compatibility_recommendations
         :collapse:


   .. py:method:: _get_agent_input_schema(agent: haive.agents.base.agent.Agent) -> type | None

      Safely extract agent input schema.


      .. autolink-examples:: _get_agent_input_schema
         :collapse:


   .. py:method:: _get_agent_output_schema(agent: haive.agents.base.agent.Agent) -> type | None

      Safely extract agent output schema.


      .. autolink-examples:: _get_agent_output_schema
         :collapse:


   .. py:method:: _get_agent_state_schema(agent: haive.agents.base.agent.Agent) -> type | None

      Safely extract agent state schema.


      .. autolink-examples:: _get_agent_state_schema
         :collapse:


   .. py:method:: _validate_workflow_compatibility() -> None

      Validate compatibility of the entire workflow before building.


      .. autolink-examples:: _validate_workflow_compatibility
         :collapse:


   .. py:method:: add_agent(agent: haive.agents.base.agent.Agent, check_compatibility: bool | None = None) -> None

      Add an agent to the multi-agent system with automatic compatibility checking.

      :param agent: The agent to add
      :param check_compatibility: Whether to check compatibility (defaults to auto_check_compatibility)


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: build_graph() -> Any

      Build graph with pre-build compatibility validation.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_compatibility_report(detailed: bool | None = None) -> dict[str, Any]

      Generate a comprehensive compatibility report.


      .. autolink-examples:: get_compatibility_report
         :collapse:


   .. py:method:: visualize_compatibility() -> None

      Visualize the compatibility status of the multi-agent system.


      .. autolink-examples:: visualize_compatibility
         :collapse:


   .. py:attribute:: _applied_adapters
      :value: []



   .. py:attribute:: _compatibility_cache


   .. py:attribute:: _compatibility_checker


   .. py:attribute:: _compatibility_results
      :value: []



   .. py:attribute:: _type_analyzer


   .. py:attribute:: auto_check_compatibility
      :type:  bool
      :value: True



   .. py:attribute:: compatibility_mode
      :type:  CompatibilityMode


   .. py:attribute:: compatibility_report_level
      :type:  str
      :value: 'summary'



   .. py:attribute:: compatibility_threshold
      :type:  float
      :value: 0.7



   .. py:attribute:: enable_auto_adapters
      :type:  bool
      :value: True



.. py:class:: CompatibilityEnhancedParallelAgent(**kwargs)

   Bases: :py:obj:`CompatibilityEnhancedMultiAgent`


   Parallel agent with built-in compatibility checking.


   .. autolink-examples:: CompatibilityEnhancedParallelAgent
      :collapse:

.. py:class:: CompatibilityEnhancedSequentialAgent(**kwargs)

   Bases: :py:obj:`CompatibilityEnhancedMultiAgent`


   Sequential agent with built-in compatibility checking.


   .. autolink-examples:: CompatibilityEnhancedSequentialAgent
      :collapse:

.. py:class:: CompatibilityMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Modes for handling compatibility issues.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompatibilityMode
      :collapse:

   .. py:attribute:: ADAPTIVE
      :value: 'adaptive'



   .. py:attribute:: AUTO_FIX
      :value: 'auto_fix'



   .. py:attribute:: PERMISSIVE
      :value: 'permissive'



   .. py:attribute:: STRICT
      :value: 'strict'



.. py:class:: CompatibilityResult

   Result of compatibility checking.


   .. autolink-examples:: CompatibilityResult
      :collapse:

   .. py:attribute:: auto_fixes_applied
      :type:  list[str]


   .. py:attribute:: compatibility_score
      :type:  float


   .. py:attribute:: is_compatible
      :type:  bool


   .. py:attribute:: issues
      :type:  list[str]


   .. py:attribute:: suggested_adapters
      :type:  list[dict[str, Any]]


   .. py:attribute:: warnings
      :type:  list[str]


.. py:function:: create_compatible_multi_agent(agents: list[haive.agents.base.agent.Agent], execution_mode: ExecutionMode = ExecutionMode.SEQUENCE, compatibility_mode: CompatibilityMode = CompatibilityMode.ADAPTIVE, **kwargs) -> CompatibilityEnhancedMultiAgent

   Create a multi-agent system with automatic compatibility checking.

   This function creates a multi-agent system and automatically checks and fixes
   compatibility issues based on the specified compatibility mode.


   .. autolink-examples:: create_compatible_multi_agent
      :collapse:

.. py:data:: logger

