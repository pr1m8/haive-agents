agents.reasoning_and_critique.self_discover.selector.models
===========================================================

.. py:module:: agents.reasoning_and_critique.self_discover.selector.models

.. autoapi-nested-parse::

   Models for the Self-Discover Selector Agent.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.selector.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.selector.models.ModuleSelection
   agents.reasoning_and_critique.self_discover.selector.models.SelectedModule


Module Contents
---------------

.. py:class:: ModuleSelection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The complete module selection for a task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleSelection
      :collapse:

   .. py:attribute:: selected_modules
      :type:  list[SelectedModule]
      :value: None



   .. py:attribute:: selection_rationale
      :type:  str
      :value: None



   .. py:attribute:: task_summary
      :type:  str
      :value: None



.. py:class:: SelectedModule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A reasoning module selected for the task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelectedModule
      :collapse:

   .. py:attribute:: contribution
      :type:  str
      :value: None



   .. py:attribute:: module_name
      :type:  str
      :value: None



   .. py:attribute:: module_number
      :type:  int
      :value: None



   .. py:attribute:: relevance_explanation
      :type:  str
      :value: None



