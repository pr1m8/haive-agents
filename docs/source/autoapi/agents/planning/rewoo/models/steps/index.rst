agents.planning.rewoo.models.steps
==================================

.. py:module:: agents.planning.rewoo.models.steps

.. autoapi-nested-parse::

   Step Models for ReWOO Planning.

   Abstract step class and concrete implementations with computed fields and validators.


   .. autolink-examples:: agents.planning.rewoo.models.steps
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.rewoo.models.steps.AbstractStep
   agents.planning.rewoo.models.steps.BasicStep


Module Contents
---------------

.. py:class:: AbstractStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`abc.ABC`


   Abstract base step that other steps inherit from.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AbstractStep
      :collapse:

   .. py:method:: can_execute(completed_steps: set[str]) -> bool
      :abstractmethod:


      Check if this step can execute given completed steps.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(context: dict[str, Any]) -> Any
      :abstractmethod:


      Execute this step with given context.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: validate_dependencies(v: list[str]) -> list[str]
      :classmethod:


      Validate dependency IDs.


      .. autolink-examples:: validate_dependencies
         :collapse:


   .. py:method:: validate_id(v: str) -> str
      :classmethod:


      Validate step ID format.


      .. autolink-examples:: validate_id
         :collapse:


   .. py:property:: dependency_count
      :type: int


      Number of dependencies.

      .. autolink-examples:: dependency_count
         :collapse:


   .. py:attribute:: depends_on
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:property:: has_dependencies
      :type: bool


      Whether this step has dependencies.

      .. autolink-examples:: has_dependencies
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


.. py:class:: BasicStep(/, **data: Any)

   Bases: :py:obj:`AbstractStep`


   Basic concrete implementation for testing.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BasicStep
      :collapse:

   .. py:method:: can_execute(completed_steps: set[str]) -> bool

      Basic implementation - all dependencies must be completed.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(context: dict[str, Any]) -> Any

      Basic execution - just return the description.


      .. autolink-examples:: execute
         :collapse:


