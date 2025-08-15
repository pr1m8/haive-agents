agents.planning.smart_parsing_example
=====================================

.. py:module:: agents.planning.smart_parsing_example

.. autoapi-nested-parse::

   Smart Output Parsing Integration Example for Planning Agents.

   This example demonstrates how to use smart output parsing with post-hooks
   to handle different types of agent outputs intelligently.


   .. autolink-examples:: agents.planning.smart_parsing_example
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.smart_parsing_example.logger


Classes
-------

.. autoapisummary::

   agents.planning.smart_parsing_example.DecisionPoint
   agents.planning.smart_parsing_example.ProgressReport
   agents.planning.smart_parsing_example.SmartExecutorAgent
   agents.planning.smart_parsing_example.SmartPlannerAgent
   agents.planning.smart_parsing_example.SmartSimpleAgent
   agents.planning.smart_parsing_example.TaskAnalysis


Functions
---------

.. autoapisummary::

   agents.planning.smart_parsing_example._enhanced_content_detection
   agents.planning.smart_parsing_example._parse_progress
   agents.planning.smart_parsing_example._parse_progress_callable
   agents.planning.smart_parsing_example._parse_task_analysis
   agents.planning.smart_parsing_example._parse_task_analysis_callable
   agents.planning.smart_parsing_example.create_adaptive_parsing_workflow
   agents.planning.smart_parsing_example.create_smart_planning_workflow
   agents.planning.smart_parsing_example.test_smart_parsing_workflow


Module Contents
---------------

.. py:class:: DecisionPoint(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for decision points in workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DecisionPoint
      :collapse:

   .. py:attribute:: decision_type
      :type:  str
      :value: None



   .. py:attribute:: options
      :type:  list[str]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: recommendation
      :type:  str
      :value: None



.. py:class:: ProgressReport(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for progress reporting.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ProgressReport
      :collapse:

   .. py:attribute:: completed_steps
      :type:  int
      :value: None



   .. py:attribute:: current_status
      :type:  str
      :value: None



   .. py:attribute:: next_actions
      :type:  list[str]
      :value: None



   .. py:attribute:: total_steps
      :type:  int
      :value: None



.. py:class:: SmartExecutorAgent(**kwargs)

   Bases: :py:obj:`haive.agents.base.smart_output_parsing.SmartOutputParsingMixin`, :py:obj:`haive.agents.planning.base.agents.executor.BaseExecutorAgent`


   BaseExecutorAgent enhanced with smart output parsing.


   .. autolink-examples:: SmartExecutorAgent
      :collapse:

.. py:class:: SmartPlannerAgent(**kwargs)

   Bases: :py:obj:`haive.agents.base.smart_output_parsing.SmartOutputParsingMixin`, :py:obj:`haive.agents.planning.base.agents.planner.BasePlannerAgent`


   BasePlannerAgent enhanced with smart output parsing.


   .. autolink-examples:: SmartPlannerAgent
      :collapse:

.. py:class:: SmartSimpleAgent(**kwargs)

   Bases: :py:obj:`haive.agents.base.smart_output_parsing.SmartOutputParsingMixin`, :py:obj:`SimpleAgentV3`


   SimpleAgentV3 enhanced with smart output parsing.


   .. autolink-examples:: SmartSimpleAgent
      :collapse:

.. py:class:: TaskAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for task analysis output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskAnalysis
      :collapse:

   .. py:attribute:: complexity
      :type:  str
      :value: None



   .. py:attribute:: estimated_time
      :type:  str
      :value: None



   .. py:attribute:: required_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: risk_factors
      :type:  list[str]
      :value: None



.. py:function:: _enhanced_content_detection(state) -> str

   Enhanced content detection for different parsing strategies.


   .. autolink-examples:: _enhanced_content_detection
      :collapse:

.. py:function:: _parse_progress(context) -> ProgressReport | None

   Custom parser for progress report output.


   .. autolink-examples:: _parse_progress
      :collapse:

.. py:function:: _parse_progress_callable(state) -> dict[str, Any]

   Callable version of progress parser.


   .. autolink-examples:: _parse_progress_callable
      :collapse:

.. py:function:: _parse_task_analysis(context) -> TaskAnalysis | None

   Custom parser for task analysis output.


   .. autolink-examples:: _parse_task_analysis
      :collapse:

.. py:function:: _parse_task_analysis_callable(state) -> dict[str, Any]

   Callable version of task analysis parser.


   .. autolink-examples:: _parse_task_analysis_callable
      :collapse:

.. py:function:: create_adaptive_parsing_workflow()

   Create workflow with adaptive parsing based on content detection.


   .. autolink-examples:: create_adaptive_parsing_workflow
      :collapse:

.. py:function:: create_smart_planning_workflow()
   :async:


   Create a planning workflow with smart output parsing.


   .. autolink-examples:: create_smart_planning_workflow
      :collapse:

.. py:function:: test_smart_parsing_workflow()
   :async:


   Test the smart parsing workflow with different input types.


   .. autolink-examples:: test_smart_parsing_workflow
      :collapse:

.. py:data:: logger

