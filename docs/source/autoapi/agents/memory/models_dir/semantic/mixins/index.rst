agents.memory.models_dir.semantic.mixins
========================================

.. py:module:: agents.memory.models_dir.semantic.mixins


Classes
-------

.. autoapisummary::

   agents.memory.models_dir.semantic.mixins.PersonalityTraits
   agents.memory.models_dir.semantic.mixins.TemporalMixin
   agents.memory.models_dir.semantic.mixins.UserContextMixin
   agents.memory.models_dir.semantic.mixins.UserPreferences


Functions
---------

.. autoapisummary::

   agents.memory.models_dir.semantic.mixins.calculate_temporal_relevance
   agents.memory.models_dir.semantic.mixins.validate_expertise
   agents.memory.models_dir.semantic.mixins.validate_personality_consistency
   agents.memory.models_dir.semantic.mixins.validate_temporal_weight
   agents.memory.models_dir.semantic.mixins.validate_topic_consistency


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



.. py:function:: calculate_temporal_relevance(memory_item) -> float

   Calculate temporal relevance of memory item.


   .. autolink-examples:: calculate_temporal_relevance
      :collapse:

.. py:function:: validate_expertise(areas: list[str]) -> list[str]

   Validate expertise areas.


   .. autolink-examples:: validate_expertise
      :collapse:

.. py:function:: validate_personality_consistency(traits: list[str]) -> list[str]

   Validate personality trait consistency.


   .. autolink-examples:: validate_personality_consistency
      :collapse:

.. py:function:: validate_temporal_weight(weight: float) -> float

   Validate temporal weight value.


   .. autolink-examples:: validate_temporal_weight
      :collapse:

.. py:function:: validate_topic_consistency(interests: list[str], avoided: list[str]) -> tuple[list[str], list[str]]

   Validate topic consistency between interests and avoided topics.


   .. autolink-examples:: validate_topic_consistency
      :collapse:

