agents.rag.multi_agent_rag.compatibility
========================================

.. py:module:: agents.rag.multi_agent_rag.compatibility

.. autoapi-nested-parse::

   Safe Agent Compatibility Testing.

   This module provides comprehensive compatibility testing for RAG agents using the
   compatibility module without modifying or breaking existing agents.


   .. autolink-examples:: agents.rag.multi_agent_rag.compatibility
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.multi_agent_rag.compatibility.logger


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.compatibility.AgentCompatibilityReport
   agents.rag.multi_agent_rag.compatibility.CompatibilityLevel
   agents.rag.multi_agent_rag.compatibility.MultiAgentCompatibilityReport
   agents.rag.multi_agent_rag.compatibility.SafeCompatibilityTester


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.compatibility.quick_agent_compatibility_check
   agents.rag.multi_agent_rag.compatibility.safe_test_rag_compatibility
   agents.rag.multi_agent_rag.compatibility.test_custom_agent_workflow


Module Contents
---------------

.. py:class:: AgentCompatibilityReport

   Comprehensive compatibility report for agent pairs.


   .. autolink-examples:: AgentCompatibilityReport
      :collapse:

   .. py:attribute:: compatibility_level
      :type:  CompatibilityLevel


   .. py:attribute:: compatibility_score
      :type:  float


   .. py:attribute:: conflicting_fields
      :type:  list[str]


   .. py:attribute:: detailed_analysis
      :type:  dict[str, Any]


   .. py:attribute:: issues
      :type:  list[str]


   .. py:attribute:: missing_fields
      :type:  list[str]


   .. py:attribute:: quality_assessment
      :type:  str


   .. py:attribute:: recommended_adapters
      :type:  list[str]


   .. py:attribute:: safe_to_chain
      :type:  bool


   .. py:attribute:: source_agent
      :type:  str


   .. py:attribute:: suggested_mappings
      :type:  dict[str, str]


   .. py:attribute:: target_agent
      :type:  str


.. py:class:: CompatibilityLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Levels of compatibility between agents.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompatibilityLevel
      :collapse:

   .. py:attribute:: ADAPTABLE
      :value: 'adaptable'



   .. py:attribute:: COMPATIBLE
      :value: 'compatible'



   .. py:attribute:: INCOMPATIBLE
      :value: 'incompatible'



   .. py:attribute:: PERFECT
      :value: 'perfect'



   .. py:attribute:: PROBLEMATIC
      :value: 'problematic'



.. py:class:: MultiAgentCompatibilityReport

   Compatibility report for multiple agents in a workflow.


   .. autolink-examples:: MultiAgentCompatibilityReport
      :collapse:

   .. py:attribute:: compatibility_matrix
      :type:  dict[tuple[str, str], AgentCompatibilityReport]


   .. py:attribute:: compatible_pairs
      :type:  int


   .. py:attribute:: overall_compatible
      :type:  bool


   .. py:attribute:: required_adapters
      :type:  list[dict[str, Any]]


   .. py:attribute:: risk_assessment
      :type:  str


   .. py:attribute:: total_agents
      :type:  int


   .. py:attribute:: total_pairs
      :type:  int


   .. py:attribute:: workflow_name
      :type:  str


   .. py:attribute:: workflow_recommendations
      :type:  list[str]


.. py:class:: SafeCompatibilityTester

   Safe compatibility testing that doesn't modify original agents.

   This class provides comprehensive compatibility analysis between agents
   without risking damage to existing systems.


   .. autolink-examples:: SafeCompatibilityTester
      :collapse:

   .. py:method:: _assess_compatibility_level(compat_result, detailed_report) -> CompatibilityLevel

      Assess the compatibility level based on results.


      .. autolink-examples:: _assess_compatibility_level
         :collapse:


   .. py:method:: _assess_quality(compat_result) -> str

      Assess the quality of the compatibility.


      .. autolink-examples:: _assess_quality
         :collapse:


   .. py:method:: _assess_workflow_risk(compatibility_matrix) -> str

      Assess the risk level of the workflow.


      .. autolink-examples:: _assess_workflow_risk
         :collapse:


   .. py:method:: _basic_schema_compatibility_check(source_schema, target_schema)

      Basic schema compatibility check without CompatibilityChecker.


      .. autolink-examples:: _basic_schema_compatibility_check
         :collapse:


   .. py:method:: _calculate_compatibility_score(compat_result) -> float

      Calculate a numeric compatibility score.


      .. autolink-examples:: _calculate_compatibility_score
         :collapse:


   .. py:method:: _create_error_report(source_name: str, target_name: str, error_msg: str) -> AgentCompatibilityReport

      Create an error report for failed compatibility tests.


      .. autolink-examples:: _create_error_report
         :collapse:


   .. py:method:: _extract_issues(compat_result, detailed_report) -> list[str]

      Extract compatibility issues from results.


      .. autolink-examples:: _extract_issues
         :collapse:


   .. py:method:: _fields_similar(field1: str, field2: str) -> bool

      Check if two field names are similar enough to suggest mapping.


      .. autolink-examples:: _fields_similar
         :collapse:


   .. py:method:: _find_conflicting_fields(source_analysis, target_analysis) -> list[str]

      Find fields that exist in both schemas but with different types.


      .. autolink-examples:: _find_conflicting_fields
         :collapse:


   .. py:method:: _find_conversion_paths(source_schema, target_schema) -> list[str]

      Find possible conversion paths between schemas.


      .. autolink-examples:: _find_conversion_paths
         :collapse:


   .. py:method:: _generate_field_mappings(source_analysis, target_analysis) -> dict[str, str]

      Generate suggested field mappings between schemas.


      .. autolink-examples:: _generate_field_mappings
         :collapse:


   .. py:method:: _generate_workflow_recommendations(compatibility_matrix, agents) -> list[str]

      Generate recommendations for improving workflow compatibility.


      .. autolink-examples:: _generate_workflow_recommendations
         :collapse:


   .. py:method:: _get_timestamp() -> str

      Get current timestamp for reports.


      .. autolink-examples:: _get_timestamp
         :collapse:


   .. py:method:: _identify_required_adapters(compatibility_matrix) -> list[dict[str, Any]]

      Identify specific adapters needed for workflow compatibility.


      .. autolink-examples:: _identify_required_adapters
         :collapse:


   .. py:method:: _recommend_adapters(compat_result) -> list[str]

      Recommend adapter strategies for compatibility issues.


      .. autolink-examples:: _recommend_adapters
         :collapse:


   .. py:method:: _safe_extract_input_schema(agent: haive.agents.base.agent.Agent) -> type | None

      Safely extract input schema without modifying agent.


      .. autolink-examples:: _safe_extract_input_schema
         :collapse:


   .. py:method:: _safe_extract_output_schema(agent: haive.agents.base.agent.Agent) -> type | None

      Safely extract output schema without modifying agent.


      .. autolink-examples:: _safe_extract_output_schema
         :collapse:


   .. py:method:: _test_state_compatibility() -> dict[str, Any]

      Test compatibility with the RAG state schema.


      .. autolink-examples:: _test_state_compatibility
         :collapse:


   .. py:method:: test_agent_pair_compatibility(source_agent: haive.agents.base.agent.Agent, target_agent: haive.agents.base.agent.Agent, safe_mode: bool = True) -> AgentCompatibilityReport

      Safely test compatibility between two agents.

      :param source_agent: The source agent in the workflow
      :param target_agent: The target agent in the workflow
      :param safe_mode: If True, uses read-only testing without modifications

      :returns: Detailed compatibility report


      .. autolink-examples:: test_agent_pair_compatibility
         :collapse:


   .. py:method:: test_rag_agents_safely() -> dict[str, Any]

      Safely test compatibility of common RAG agent combinations.

      :returns: Comprehensive test results for common RAG patterns


      .. autolink-examples:: test_rag_agents_safely
         :collapse:


   .. py:method:: test_workflow_compatibility(agents: list[haive.agents.base.agent.Agent], workflow_name: str = 'RAG Workflow') -> MultiAgentCompatibilityReport

      Test compatibility across an entire workflow of agents.

      :param agents: List of agents in workflow order
      :param workflow_name: Name of the workflow being tested

      :returns: Comprehensive workflow compatibility report


      .. autolink-examples:: test_workflow_compatibility
         :collapse:


   .. py:attribute:: _test_cache


   .. py:attribute:: analyzer


   .. py:attribute:: converter_registry


.. py:function:: quick_agent_compatibility_check(agent1: haive.agents.base.agent.Agent, agent2: haive.agents.base.agent.Agent) -> bool

   Quick compatibility check between two agents.

   :returns: True if agents are safe to chain, False otherwise


   .. autolink-examples:: quick_agent_compatibility_check
      :collapse:

.. py:function:: safe_test_rag_compatibility() -> dict[str, Any]

   Safely test RAG agent compatibility without breaking anything.

   This is the main function to use for testing RAG agent compatibility.


   .. autolink-examples:: safe_test_rag_compatibility
      :collapse:

.. py:function:: test_custom_agent_workflow(agents: list[haive.agents.base.agent.Agent], workflow_name: str) -> MultiAgentCompatibilityReport

   Test compatibility of a custom agent workflow.

   :param agents: List of agents to test
   :param workflow_name: Name for the workflow

   :returns: Comprehensive compatibility report


   .. autolink-examples:: test_custom_agent_workflow
      :collapse:

.. py:data:: logger

