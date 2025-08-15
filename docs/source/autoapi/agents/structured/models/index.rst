agents.structured.models
========================

.. py:module:: agents.structured.models

.. autoapi-nested-parse::

   Pydantic models for structured output agents.

   This module defines the common output models used by structured agents
   for converting unstructured text into organized data.


   .. autolink-examples:: agents.structured.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.structured.models.AnalysisOutput
   agents.structured.models.DecisionOutput
   agents.structured.models.GenericStructuredOutput
   agents.structured.models.TaskOutput


Module Contents
---------------

.. py:class:: AnalysisOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for analysis tasks.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AnalysisOutput
      :collapse:

   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: evidence
      :type:  list[str]
      :value: None



   .. py:attribute:: findings
      :type:  list[str]
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: recommendations
      :type:  list[str]
      :value: None



   .. py:attribute:: summary
      :type:  str
      :value: None



.. py:class:: DecisionOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for decision-making content.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DecisionOutput
      :collapse:

   .. py:attribute:: alternatives
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: cons
      :type:  list[str]
      :value: None



   .. py:attribute:: decision
      :type:  str
      :value: None



   .. py:attribute:: next_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: pros
      :type:  list[str]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: GenericStructuredOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Generic structured output model for any content.

   This model provides a flexible structure that can capture
   the essence of most text outputs in an organized way.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GenericStructuredOutput
      :collapse:

   .. py:attribute:: action_items
      :type:  list[str]
      :value: None



   .. py:attribute:: categories
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: key_points
      :type:  list[str]
      :value: None



   .. py:attribute:: main_content
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



.. py:class:: TaskOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for task-related content.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskOutput
      :collapse:

   .. py:attribute:: complexity
      :type:  int
      :value: None



   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: estimated_time
      :type:  str | None
      :value: None



   .. py:attribute:: requirements
      :type:  list[str]
      :value: None



   .. py:attribute:: steps
      :type:  list[str]
      :value: None



   .. py:attribute:: task_description
      :type:  str
      :value: None



