agents.planning.rewoo_v3.models
===============================

.. py:module:: agents.planning.rewoo_v3.models

.. autoapi-nested-parse::

   Pydantic models for ReWOO V3 Agent.

   This module defines structured output models for the ReWOO (Reasoning without Observation)
   methodology using Enhanced MultiAgent V3.

   Key Models:
   - ReWOOPlan: Planner agent structured output with evidence placeholders
   - EvidenceItem: Individual evidence collected by worker
   - EvidenceCollection: Worker agent structured output with all evidence
   - ReWOOSolution: Solver agent final answer with reasoning


   .. autolink-examples:: agents.planning.rewoo_v3.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.rewoo_v3.models.EvidenceCollection
   agents.planning.rewoo_v3.models.EvidenceItem
   agents.planning.rewoo_v3.models.EvidenceStatus
   agents.planning.rewoo_v3.models.PlanStep
   agents.planning.rewoo_v3.models.ReWOOPlan
   agents.planning.rewoo_v3.models.ReWOOSolution
   agents.planning.rewoo_v3.models.ReWOOV3Input
   agents.planning.rewoo_v3.models.ReWOOV3Output


Module Contents
---------------

.. py:class:: EvidenceCollection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Worker agent structured output with all collected evidence.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EvidenceCollection
      :collapse:

   .. py:attribute:: collection_id
      :type:  str
      :value: None



   .. py:attribute:: completed_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: evidence_items
      :type:  list[EvidenceItem]
      :value: None



   .. py:attribute:: execution_notes
      :type:  list[str]
      :value: None



   .. py:attribute:: failure_count
      :type:  int
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: success_count
      :type:  int
      :value: None



   .. py:attribute:: summary
      :type:  str
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



.. py:class:: EvidenceItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual piece of evidence collected by Worker.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EvidenceItem
      :collapse:

   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: evidence_id
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: status
      :type:  EvidenceStatus
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



.. py:class:: EvidenceStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of evidence collection.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EvidenceStatus
      :collapse:

   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: PARTIAL
      :value: 'partial'



   .. py:attribute:: PENDING
      :value: 'pending'



   .. py:attribute:: SUCCESS
      :value: 'success'



.. py:class:: PlanStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual step in the ReWOO plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanStep
      :collapse:

   .. py:attribute:: depends_on
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: evidence_id
      :type:  str
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: tool_call
      :type:  str | None
      :value: None



.. py:class:: ReWOOPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured planning output from Planner agent.

   The plan contains all steps upfront without seeing any tool results.
   Each step has an evidence placeholder that will be filled by the Worker.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOPlan
      :collapse:

   .. py:attribute:: approach
      :type:  str
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: expected_evidence
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: steps
      :type:  list[PlanStep]
      :value: None



   .. py:attribute:: total_steps
      :type:  int
      :value: None



.. py:class:: ReWOOSolution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final synthesized solution from Solver agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOSolution
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: evidence_used
      :type:  list[str]
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: solution_id
      :type:  str
      :value: None



   .. py:attribute:: synthesis_process
      :type:  str
      :value: None



.. py:class:: ReWOOV3Input(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input model for ReWOO V3 agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOV3Input
      :collapse:

   .. py:attribute:: context
      :type:  str | None
      :value: None



   .. py:attribute:: max_steps
      :type:  int | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: tools_preference
      :type:  list[str] | None
      :value: None



.. py:class:: ReWOOV3Output(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output model for ReWOO V3 agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOV3Output
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: evidence_collected
      :type:  int
      :value: None



   .. py:attribute:: evidence_summary
      :type:  str
      :value: None



   .. py:attribute:: execution_time
      :type:  float
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: planning_time
      :type:  float
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: reasoning_process
      :type:  str
      :value: None



   .. py:attribute:: solution_id
      :type:  str
      :value: None



   .. py:attribute:: solving_time
      :type:  float
      :value: None



   .. py:attribute:: steps_planned
      :type:  int
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



   .. py:attribute:: total_execution_time
      :type:  float
      :value: None



