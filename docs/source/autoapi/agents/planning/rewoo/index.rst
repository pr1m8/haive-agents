agents.planning.rewoo
=====================

.. py:module:: agents.planning.rewoo

.. autoapi-nested-parse::

   ReWOO Planning System.

   A comprehensive planning system based on ReWOO (Reasoning without Observation) methodology.


   .. autolink-examples:: agents.planning.rewoo
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/planning/rewoo/agents/index
   /autoapi/agents/planning/rewoo/models/index


Classes
-------

.. autoapisummary::

   agents.planning.rewoo.AbstractStep
   agents.planning.rewoo.BasicStep
   agents.planning.rewoo.ExecutionPlan


Package Contents
----------------

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


.. py:class:: ExecutionPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   !!! abstract "Usage Documentation"
       [Models](../concepts/models.md)

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of the class variables defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The core schema of the model.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

   .. attribute:: __pydantic_serializer__

      The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The `pydantic-core` `SchemaValidator` used to validate instances of the model.

   .. attribute:: __pydantic_fields__

      A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.

   .. attribute:: __pydantic_computed_fields__

      A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

   .. attribute:: __pydantic_extra__

      A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
      is set to `'allow'`.

   .. attribute:: __pydantic_fields_set__

      The names of fields explicitly set during instantiation.

   .. attribute:: __pydantic_private__

      Values of private attributes set on the model instance.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionPlan
      :collapse:

   .. py:method:: add_step(step: agents.planning.rewoo.models.steps.AbstractStep)

      Add a step to the plan.


      .. autolink-examples:: add_step
         :collapse:


   .. py:method:: get_ready_steps(completed_steps: set[str]) -> list[agents.planning.rewoo.models.steps.AbstractStep]

      Get steps that are ready to execute.


      .. autolink-examples:: get_ready_steps
         :collapse:


   .. py:method:: get_step_by_id(step_id: str) -> agents.planning.rewoo.models.steps.AbstractStep | None

      Get step by ID.


      .. autolink-examples:: get_step_by_id
         :collapse:


   .. py:method:: validate_no_circular_dependencies() -> ExecutionPlan

      Validate no circular dependencies exist.


      .. autolink-examples:: validate_no_circular_dependencies
         :collapse:


   .. py:method:: validate_steps(v: list[agents.planning.rewoo.models.steps.AbstractStep]) -> list[agents.planning.rewoo.models.steps.AbstractStep]
      :classmethod:


      Validate steps and check for duplicate IDs.


      .. autolink-examples:: validate_steps
         :collapse:


   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:property:: execution_levels
      :type: list[list[str]]


      Steps organized by execution level for parallelization.

      .. autolink-examples:: execution_levels
         :collapse:


   .. py:property:: has_dependencies
      :type: bool


      Whether any step has dependencies.

      .. autolink-examples:: has_dependencies
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:property:: max_parallelism
      :type: int


      Maximum number of steps that can run in parallel.

      .. autolink-examples:: max_parallelism
         :collapse:


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:property:: step_count
      :type: int


      Total number of steps.

      .. autolink-examples:: step_count
         :collapse:


   .. py:property:: step_ids
      :type: list[str]


      List of all step IDs.

      .. autolink-examples:: step_ids
         :collapse:


   .. py:attribute:: steps
      :type:  list[agents.planning.rewoo.models.steps.AbstractStep]
      :value: None



