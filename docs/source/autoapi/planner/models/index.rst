planner.models
==============

.. py:module:: planner.models

.. autoapi-nested-parse::

   Planner Models - Custom Pydantic models for strategic planning.

   This module defines the structured output models used by the planner agent
   for creating comprehensive, actionable task plans.


   .. autolink-examples:: planner.models
      :collapse:


Classes
-------

.. autoapisummary::

   planner.models.PlanningContext
   planner.models.TaskPlan
   planner.models.TaskStep


Module Contents
---------------

.. py:class:: PlanningContext(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Context information for the planner agent.

   Provides additional context that helps the planner create better,
   more targeted plans based on available resources and constraints.

   .. attribute:: available_tools

      Tools that can be used during execution

   .. attribute:: time_constraints

      Any time limitations to consider

   .. attribute:: complexity_level

      Desired complexity level for the plan

   .. attribute:: domain_focus

      Specific domain or area of focus

   .. attribute:: previous_attempts

      Information about previous planning attempts

   .. rubric:: Examples

   Research context::

       context = PlanningContext(
           available_tools=["web_search", "calculator", "document_reader"],
           time_constraints="Complete within 1 hour",
           complexity_level="detailed",
           domain_focus="financial_analysis"
       )

   Simple task context::

       context = PlanningContext(
           available_tools=["calculator"],
           complexity_level="simple",
           domain_focus="mathematics"
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanningContext
      :collapse:

   .. py:attribute:: available_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: complexity_level
      :type:  Literal['simple', 'moderate', 'detailed', 'comprehensive']
      :value: None



   .. py:attribute:: domain_focus
      :type:  str | None
      :value: None



   .. py:attribute:: previous_attempts
      :type:  list[str]
      :value: None



   .. py:attribute:: time_constraints
      :type:  str | None
      :value: None



.. py:class:: TaskPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive task plan with metadata and execution strategy.

   Represents a complete strategic plan for accomplishing a complex objective,
   including all steps, reasoning, and success criteria.

   .. attribute:: objective

      The main goal we're trying to achieve

   .. attribute:: steps

      Ordered list of steps to execute

   .. attribute:: reasoning

      Explanation of the planning approach

   .. attribute:: success_criteria

      How we'll know the objective is achieved

   .. attribute:: estimated_total_time

      Total estimated time for all steps

   .. attribute:: plan_type

      Type of planning strategy used

   .. attribute:: risk_factors

      Potential risks and mitigation strategies

   .. rubric:: Examples

   Research plan::

       plan = TaskPlan(
           objective="Research Tesla's Q4 2024 financial performance",
           steps=[search_step, analysis_step, summary_step],
           reasoning="Sequential approach: gather data, analyze, summarize",
           success_criteria="Complete financial overview with key metrics",
           plan_type="sequential_research"
       )

   Complex analysis plan::

       plan = TaskPlan(
           objective="Compare renewable energy adoption across countries",
           steps=[data_steps, comparison_steps, visualization_step],
           reasoning="Parallel data gathering followed by comparative analysis",
           success_criteria="Comprehensive comparison with visual insights",
           plan_type="comparative_analysis",
           risk_factors=["Data availability", "Currency conversion accuracy"]
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskPlan
      :collapse:

   .. py:attribute:: estimated_total_time
      :type:  str | None
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: plan_type
      :type:  Literal['sequential', 'parallel', 'sequential_research', 'comparative_analysis', 'creative', 'analytical']
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: risk_factors
      :type:  list[str]
      :value: None



   .. py:attribute:: steps
      :type:  list[TaskStep]
      :value: None



   .. py:attribute:: success_criteria
      :type:  str
      :value: None



.. py:class:: TaskStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual step in a task plan with rich metadata.

   Represents a single actionable step within a larger plan, including
   all the information needed for successful execution.

   .. attribute:: step_id

      Unique identifier for tracking this step

   .. attribute:: description

      Clear, actionable description of what to do

   .. attribute:: expected_outcome

      What result this step should produce

   .. attribute:: tools_needed

      Tools required for execution

   .. attribute:: priority

      Execution priority level

   .. attribute:: estimated_time

      Estimated completion time

   .. attribute:: dependencies

      Steps that must complete before this one

   .. rubric:: Examples

   Basic step::

       step = TaskStep(
           step_id="step_1",
           description="Search for current stock price of AAPL",
           expected_outcome="Current AAPL stock price in USD",
           tools_needed=["web_search"],
           priority="high"
       )

   Step with dependencies::

       step = TaskStep(
           step_id="step_2",
           description="Calculate percentage change from yesterday",
           expected_outcome="Percentage change calculation",
           tools_needed=["calculator"],
           dependencies=["step_1"],
           priority="medium"
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskStep
      :collapse:

   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: estimated_time
      :type:  str | None
      :value: None



   .. py:attribute:: expected_outcome
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  Literal['high', 'medium', 'low']
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: tools_needed
      :type:  list[str]
      :value: None



