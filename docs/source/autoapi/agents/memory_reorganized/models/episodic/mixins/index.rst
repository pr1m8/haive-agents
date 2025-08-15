agents.memory_reorganized.models.episodic.mixins
================================================

.. py:module:: agents.memory_reorganized.models.episodic.mixins

.. autoapi-nested-parse::

   Mixins model module.

   This module provides mixins functionality for the Haive framework.

   Classes:
       PerformanceMetrics: PerformanceMetrics implementation.
       TaskExecution: TaskExecution implementation.

   Functions:
       validate_performance_logic: Validate Performance Logic functionality.
       validate_execution_steps: Validate Execution Steps functionality.


   .. autolink-examples:: agents.memory_reorganized.models.episodic.mixins
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.models.episodic.mixins.PerformanceMetrics
   agents.memory_reorganized.models.episodic.mixins.TaskExecution


Module Contents
---------------

.. py:class:: PerformanceMetrics(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Detailed performance tracking for episodic memories.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PerformanceMetrics
      :collapse:

   .. py:method:: validate_performance_logic() -> PerformanceMetrics

      Validate performance metric consistency.


      .. autolink-examples:: validate_performance_logic
         :collapse:


   .. py:attribute:: completion_time
      :type:  float
      :value: None



   .. py:attribute:: complexity_score
      :type:  int
      :value: None



   .. py:attribute:: error_frequency
      :type:  float
      :value: None



   .. py:attribute:: success_rate
      :type:  float
      :value: None



   .. py:attribute:: user_satisfaction
      :type:  float | None
      :value: None



.. py:class:: TaskExecution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Detailed task execution context.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskExecution
      :collapse:

   .. py:method:: validate_execution_steps(v: list[str]) -> list[str]
      :classmethod:


      Validate execution step format.


      .. autolink-examples:: validate_execution_steps
         :collapse:


   .. py:attribute:: decision_points
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: execution_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: input_parameters
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: task_type
      :type:  str
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



