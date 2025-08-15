agents.task_analysis.context.models
===================================

.. py:module:: agents.task_analysis.context.models


Classes
-------

.. autoapisummary::

   agents.task_analysis.context.models.ContextAnalysis
   agents.task_analysis.context.models.ContextDomain
   agents.task_analysis.context.models.ContextFlow
   agents.task_analysis.context.models.ContextFreshness
   agents.task_analysis.context.models.ContextRequirement
   agents.task_analysis.context.models.ContextSize


Module Contents
---------------

.. py:class:: ContextAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete context analysis for a task plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextAnalysis
      :collapse:

   .. py:attribute:: caching_strategy
      :type:  Literal['none', 'lru', 'full']
      :value: 'lru'



   .. py:attribute:: context_flows
      :type:  list[ContextFlow]
      :value: None



   .. py:attribute:: context_risks
      :type:  list[str]
      :value: None



   .. py:attribute:: loading_strategy
      :type:  Literal['eager', 'lazy', 'streaming']
      :value: 'lazy'



   .. py:attribute:: mitigation_strategies
      :type:  list[str]
      :value: None



   .. py:attribute:: task_contexts
      :type:  dict[str, ContextRequirement]
      :value: None



   .. py:attribute:: total_context_requirement
      :type:  ContextRequirement


   .. py:attribute:: total_estimated_tokens
      :type:  int
      :value: None



   .. py:attribute:: unique_domains
      :type:  list[str]
      :value: None



.. py:class:: ContextDomain(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A domain of knowledge required.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextDomain
      :collapse:

   .. py:attribute:: domain_name
      :type:  str
      :value: None



   .. py:attribute:: expertise_level
      :type:  Literal['basic', 'intermediate', 'advanced', 'expert']
      :value: 'basic'



   .. py:attribute:: preferred_sources
      :type:  list[str]
      :value: None



   .. py:attribute:: required_sources
      :type:  list[str]
      :value: None



   .. py:attribute:: specific_topics
      :type:  list[str]
      :value: None



.. py:class:: ContextFlow(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   How context flows between tasks.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextFlow
      :collapse:

   .. py:attribute:: data_keys
      :type:  list[str]
      :value: None



   .. py:attribute:: flow_type
      :type:  Literal['direct', 'transformed', 'aggregated', 'filtered']
      :value: 'direct'



   .. py:attribute:: is_required
      :type:  bool
      :value: None



   .. py:attribute:: source_task_id
      :type:  str


   .. py:attribute:: target_task_id
      :type:  str


   .. py:attribute:: transformations
      :type:  list[str]
      :value: None



.. py:class:: ContextFreshness

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   How recent context needs to be.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextFreshness
      :collapse:

   .. py:attribute:: CURRENT
      :value: 'current'



   .. py:attribute:: HISTORICAL
      :value: 'historical'



   .. py:attribute:: REALTIME
      :value: 'realtime'



   .. py:attribute:: RECENT
      :value: 'recent'



.. py:class:: ContextRequirement(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete context requirements for a task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextRequirement
      :collapse:

   .. py:method:: merge_with(other: ContextRequirement) -> ContextRequirement

      Merge two context requirements.


      .. autolink-examples:: merge_with
         :collapse:


   .. py:attribute:: domains
      :type:  list[ContextDomain]
      :value: None



   .. py:attribute:: estimated_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: freshness
      :type:  ContextFreshness
      :value: None



   .. py:attribute:: integration_points
      :type:  list[str]
      :value: None



   .. py:attribute:: must_exclude
      :type:  list[str]
      :value: None



   .. py:attribute:: optional_information
      :type:  list[str]
      :value: None



   .. py:attribute:: postprocessing_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: preprocessing_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: quality_requirements
      :type:  list[str]
      :value: None



   .. py:attribute:: required_information
      :type:  list[str]
      :value: None



   .. py:attribute:: size
      :type:  ContextSize
      :value: None



.. py:class:: ContextSize

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Size categories for context.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextSize
      :collapse:

   .. py:attribute:: LARGE
      :value: 'large'



   .. py:attribute:: MASSIVE
      :value: 'massive'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: MINIMAL
      :value: 'minimal'



   .. py:attribute:: SMALL
      :value: 'small'



