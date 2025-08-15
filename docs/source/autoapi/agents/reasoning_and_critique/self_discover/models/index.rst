agents.reasoning_and_critique.self_discover.models
==================================================

.. py:module:: agents.reasoning_and_critique.self_discover.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.models.AdaptedModule
   agents.reasoning_and_critique.self_discover.models.ModuleAdaptationResult
   agents.reasoning_and_critique.self_discover.models.ModuleSelectionResult
   agents.reasoning_and_critique.self_discover.models.ReasoningOutput
   agents.reasoning_and_critique.self_discover.models.ReasoningOutputStep
   agents.reasoning_and_critique.self_discover.models.ReasoningStep
   agents.reasoning_and_critique.self_discover.models.ReasoningStructure
   agents.reasoning_and_critique.self_discover.models.SelectedModule


Module Contents
---------------

.. py:class:: AdaptedModule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An adapted version of a reasoning module for a specific task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModule
      :collapse:

   .. py:attribute:: adapted_description
      :type:  str
      :value: None



   .. py:attribute:: application_strategy
      :type:  str
      :value: None



   .. py:attribute:: original_module_id
      :type:  str
      :value: None



.. py:class:: ModuleAdaptationResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of the module adaptation stage.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleAdaptationResult
      :collapse:

   .. py:method:: format_for_next_stage() -> str

      Format the adapted modules for the structure stage.


      .. autolink-examples:: format_for_next_stage
         :collapse:


   .. py:attribute:: adapted_modules
      :type:  list[AdaptedModule]
      :value: None



.. py:class:: ModuleSelectionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of the module selection stage.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleSelectionResult
      :collapse:

   .. py:method:: format_for_next_stage() -> str

      Format the selected modules for the adaptation stage.


      .. autolink-examples:: format_for_next_stage
         :collapse:


   .. py:method:: validate_modules(modules) -> Any
      :classmethod:


      Ensure we have a reasonable number of modules.


      .. autolink-examples:: validate_modules
         :collapse:


   .. py:attribute:: selected_modules
      :type:  list[SelectedModule]
      :value: None



.. py:class:: ReasoningOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete reasoning output with all steps and final answer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningOutput
      :collapse:

   .. py:method:: format_complete_reasoning() -> str

      Format the complete reasoning process.


      .. autolink-examples:: format_complete_reasoning
         :collapse:


   .. py:attribute:: completed_steps
      :type:  list[ReasoningOutputStep]
      :value: None



   .. py:attribute:: confidence
      :type:  float | None
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



.. py:class:: ReasoningOutputStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A completed step in the reasoning process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningOutputStep
      :collapse:

   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  Any | None
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



.. py:class:: ReasoningStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A step in the reasoning plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStep
      :collapse:

   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: related_module_ids
      :type:  list[str] | None
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



.. py:class:: ReasoningStructure(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A structured reasoning plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStructure
      :collapse:

   .. py:method:: format_for_next_stage() -> str

      Format the reasoning structure as JSON for the reasoning stage.


      .. autolink-examples:: format_for_next_stage
         :collapse:


   .. py:method:: validate_steps(steps) -> Any
      :classmethod:


      Ensure we have a reasonable number of steps.


      .. autolink-examples:: validate_steps
         :collapse:


   .. py:attribute:: steps
      :type:  list[ReasoningStep]
      :value: None



.. py:class:: SelectedModule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A reasoning module selected for a specific problem.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelectedModule
      :collapse:

   .. py:attribute:: module_id
      :type:  str
      :value: None



   .. py:attribute:: module_name
      :type:  str
      :value: None



   .. py:attribute:: rationale
      :type:  str
      :value: None



