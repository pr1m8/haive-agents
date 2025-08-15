agents.memory_reorganized.models.semantic.mixins
================================================

.. py:module:: agents.memory_reorganized.models.semantic.mixins

.. autoapi-nested-parse::

   Mixins model module.

   This module provides mixins functionality for the Haive framework.

   Classes:
       UserContextMixin: UserContextMixin implementation.
       TemporalMixin: TemporalMixin implementation.
       PersonalityTraits: PersonalityTraits implementation.

   Functions:
       get_context_summary: Get Context Summary functionality.
       update_context: Update Context functionality.
       validate_temporal_weight: Validate Temporal Weight functionality.


   .. autolink-examples:: agents.memory_reorganized.models.semantic.mixins
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.models.semantic.mixins.PersonalityTraits
   agents.memory_reorganized.models.semantic.mixins.TemporalMixin
   agents.memory_reorganized.models.semantic.mixins.UserContextMixin
   agents.memory_reorganized.models.semantic.mixins.UserPreferences


Module Contents
---------------

.. py:class:: PersonalityTraits(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Sophisticated personality modeling.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PersonalityTraits
      :collapse:

   .. py:method:: validate_expertise(v: list[str]) -> list[str]
      :classmethod:


      Validate and normalize expertise areas.


      .. autolink-examples:: validate_expertise
         :collapse:


   .. py:method:: validate_personality_consistency() -> PersonalityTraits
      :classmethod:


      Ensure personality traits are consistent.


      .. autolink-examples:: validate_personality_consistency
         :collapse:


   .. py:attribute:: communication_style
      :type:  Literal['formal', 'casual', 'technical', 'friendly', 'direct']
      :value: None



   .. py:attribute:: cultural_context
      :type:  str | None
      :value: None



   .. py:attribute:: expertise_areas
      :type:  list[str]
      :value: None



   .. py:attribute:: interaction_preferences
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: language_preferences
      :type:  list[str]
      :value: None



.. py:class:: TemporalMixin

   Mixin for temporal memory management.


   .. autolink-examples:: TemporalMixin
      :collapse:

   .. py:method:: calculate_temporal_relevance() -> float

      Calculate temporal relevance based on age and access patterns.


      .. autolink-examples:: calculate_temporal_relevance
         :collapse:


   .. py:method:: validate_temporal_weight(v: float) -> float
      :classmethod:


      Validate temporal decay weight.


      .. autolink-examples:: validate_temporal_weight
         :collapse:


.. py:class:: UserContextMixin

   Mixin for user-specific context management.


   .. autolink-examples:: UserContextMixin
      :collapse:

   .. py:method:: get_context_summary() -> str
      :abstractmethod:


      Generate contextual summary.


      .. autolink-examples:: get_context_summary
         :collapse:


   .. py:method:: update_context(new_data: dict[str, Any]) -> None
      :abstractmethod:


      Update contextual information.


      .. autolink-examples:: update_context
         :collapse:


.. py:class:: UserPreferences(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Enhanced user preferences with validation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: UserPreferences
      :collapse:

   .. py:method:: validate_topic_consistency() -> UserPreferences
      :classmethod:


      Ensure no overlap between interested and avoided topics.


      .. autolink-examples:: validate_topic_consistency
         :collapse:


   .. py:attribute:: avoided_topics
      :type:  list[str]
      :value: None



   .. py:attribute:: data_retention_days
      :type:  int
      :value: None



   .. py:attribute:: notification_settings
      :type:  dict[str, bool]
      :value: None



   .. py:attribute:: preferred_response_length
      :type:  Literal['brief', 'moderate', 'detailed']
      :value: None



   .. py:attribute:: privacy_level
      :type:  Literal['public', 'private', 'restricted']
      :value: None



   .. py:attribute:: topics_of_interest
      :type:  list[str]
      :value: None



