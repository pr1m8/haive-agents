
:py:mod:`agents.planning.smart_parsing_example`
===============================================

.. py:module:: agents.planning.smart_parsing_example

Smart Output Parsing Integration Example for Planning Agents.

This example demonstrates how to use smart output parsing with post-hooks
to handle different types of agent outputs intelligently.


.. autolink-examples:: agents.planning.smart_parsing_example
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.smart_parsing_example.DecisionPoint
   agents.planning.smart_parsing_example.ProgressReport
   agents.planning.smart_parsing_example.SmartExecutorAgent
   agents.planning.smart_parsing_example.SmartPlannerAgent
   agents.planning.smart_parsing_example.SmartSimpleAgent
   agents.planning.smart_parsing_example.TaskAnalysis


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DecisionPoint:

   .. graphviz::
      :align: center

      digraph inheritance_DecisionPoint {
        node [shape=record];
        "DecisionPoint" [label="DecisionPoint"];
        "pydantic.BaseModel" -> "DecisionPoint";
      }

.. autopydantic_model:: agents.planning.smart_parsing_example.DecisionPoint
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ProgressReport:

   .. graphviz::
      :align: center

      digraph inheritance_ProgressReport {
        node [shape=record];
        "ProgressReport" [label="ProgressReport"];
        "pydantic.BaseModel" -> "ProgressReport";
      }

.. autopydantic_model:: agents.planning.smart_parsing_example.ProgressReport
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SmartExecutorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SmartExecutorAgent {
        node [shape=record];
        "SmartExecutorAgent" [label="SmartExecutorAgent"];
        "haive.agents.base.smart_output_parsing.SmartOutputParsingMixin" -> "SmartExecutorAgent";
        "haive.agents.planning.base.agents.executor.BaseExecutorAgent" -> "SmartExecutorAgent";
      }

.. autoclass:: agents.planning.smart_parsing_example.SmartExecutorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SmartPlannerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SmartPlannerAgent {
        node [shape=record];
        "SmartPlannerAgent" [label="SmartPlannerAgent"];
        "haive.agents.base.smart_output_parsing.SmartOutputParsingMixin" -> "SmartPlannerAgent";
        "haive.agents.planning.base.agents.planner.BasePlannerAgent" -> "SmartPlannerAgent";
      }

.. autoclass:: agents.planning.smart_parsing_example.SmartPlannerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SmartSimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SmartSimpleAgent {
        node [shape=record];
        "SmartSimpleAgent" [label="SmartSimpleAgent"];
        "haive.agents.base.smart_output_parsing.SmartOutputParsingMixin" -> "SmartSimpleAgent";
        "SimpleAgentV3" -> "SmartSimpleAgent";
      }

.. autoclass:: agents.planning.smart_parsing_example.SmartSimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_TaskAnalysis {
        node [shape=record];
        "TaskAnalysis" [label="TaskAnalysis"];
        "pydantic.BaseModel" -> "TaskAnalysis";
      }

.. autopydantic_model:: agents.planning.smart_parsing_example.TaskAnalysis
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



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



.. rubric:: Related Links

.. autolink-examples:: agents.planning.smart_parsing_example
   :collapse:
   
.. autolink-skip:: next
