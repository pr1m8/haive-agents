agents.reasoning_and_critique.self_discover.v2.models
=====================================================

.. py:module:: agents.reasoning_and_critique.self_discover.v2.models

.. autoapi-nested-parse::

   Structured output models for Self-Discovery reasoning system.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.v2.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.v2.models.AdaptedModules
   agents.reasoning_and_critique.self_discover.v2.models.Config
   agents.reasoning_and_critique.self_discover.v2.models.FinalAnswer
   agents.reasoning_and_critique.self_discover.v2.models.ReasoningStructure
   agents.reasoning_and_critique.self_discover.v2.models.SelectedModules


Module Contents
---------------

.. py:class:: AdaptedModules(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Adapted reasoning modules tailored to the specific task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModules
      :collapse:

   .. py:class:: Config

      .. py:attribute:: json_schema_extra



   .. py:attribute:: adapted_modules
      :type:  list[dict[str, str]]
      :value: None



.. py:class:: Config(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration model for Self-Discovery reasoning system.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Config
      :collapse:

   .. py:attribute:: confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: modules
      :type:  list[str]
      :value: None



.. py:class:: FinalAnswer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final answer with reasoning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FinalAnswer
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float | None
      :value: None



   .. py:attribute:: reasoning_steps
      :type:  dict[str, str]
      :value: None



.. py:class:: ReasoningStructure(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Step-by-step reasoning structure for solving the task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStructure
      :collapse:

   .. py:attribute:: reasoning_structure
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: steps
      :type:  list[str]
      :value: None



.. py:class:: SelectedModules(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Selected reasoning modules for the task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelectedModules
      :collapse:

   .. py:attribute:: rationale
      :type:  str | None
      :value: None



   .. py:attribute:: selected_modules
      :type:  list[str]
      :value: None



