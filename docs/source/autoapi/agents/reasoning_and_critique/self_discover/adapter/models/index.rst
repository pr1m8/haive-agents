agents.reasoning_and_critique.self_discover.adapter.models
==========================================================

.. py:module:: agents.reasoning_and_critique.self_discover.adapter.models

.. autoapi-nested-parse::

   Models for the Self-Discover Adapter Agent.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.adapter.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.adapter.models.AdaptedModule
   agents.reasoning_and_critique.self_discover.adapter.models.AdaptedModules


Module Contents
---------------

.. py:class:: AdaptedModule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A reasoning module adapted for the specific task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModule
      :collapse:

   .. py:attribute:: concrete_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: expected_insights
      :type:  str
      :value: None



   .. py:attribute:: original_module
      :type:  str
      :value: None



   .. py:attribute:: task_specific_adaptation
      :type:  str
      :value: None



.. py:class:: AdaptedModules(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Collection of task-adapted reasoning modules.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModules
      :collapse:

   .. py:attribute:: adapted_modules
      :type:  list[AdaptedModule]
      :value: None



   .. py:attribute:: integration_strategy
      :type:  str
      :value: None



   .. py:attribute:: task_context
      :type:  str
      :value: None



