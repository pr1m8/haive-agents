agents.memory_reorganized.models.episodic.models
================================================

.. py:module:: agents.memory_reorganized.models.episodic.models

.. autoapi-nested-parse::

   Models model module.

   This module provides models functionality for the Haive framework.

   Classes:
       EpisodicMemory: EpisodicMemory implementation.

   Functions:
       validate_content_safety: Validate Content Safety functionality.
       validate_episodic_consistency: Validate Episodic Consistency functionality.


   .. autolink-examples:: agents.memory_reorganized.models.episodic.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.models.episodic.models.EpisodicMemory


Module Contents
---------------

.. py:class:: EpisodicMemory

   Bases: :py:obj:`haive.agents.memory_reorganized.models.base.BaseMemoryModel`


   Sophisticated episodic memory for learning from experiences.


   .. autolink-examples:: EpisodicMemory
      :collapse:

   .. py:method:: _extract_lessons_from_feedback() -> list[str]

      Extract actionable lessons from user feedback.


      .. autolink-examples:: _extract_lessons_from_feedback
         :collapse:


   .. py:method:: calculate_learning_value() -> float

      Calculate the learning value of this episodic memory.


      .. autolink-examples:: calculate_learning_value
         :collapse:


   .. py:method:: calculate_temporal_relevance() -> float

      Calculate temporal relevance based on age and importance.

      :returns: Temporal relevance factor (0.0 to 1.0)


      .. autolink-examples:: calculate_temporal_relevance
         :collapse:


   .. py:method:: validate_content_safety(v: str) -> str
      :classmethod:


      Basic content safety validation.


      .. autolink-examples:: validate_content_safety
         :collapse:


   .. py:method:: validate_episodic_consistency() -> EpisodicMemory

      Validate episodic memory consistency.


      .. autolink-examples:: validate_episodic_consistency
         :collapse:


   .. py:attribute:: __memory_type__
      :value: 'episodic'



   .. py:attribute:: __validation_level__
      :value: 'enterprise'



   .. py:attribute:: agent_response
      :type:  str
      :value: None



   .. py:attribute:: environmental_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: feedback_received
      :type:  str | None
      :value: None



   .. py:attribute:: lessons_learned
      :type:  list[str]
      :value: None



   .. py:attribute:: outcome_classification
      :type:  Literal['success', 'partial_success', 'failure', 'error']
      :value: None



   .. py:attribute:: performance_metrics
      :type:  haive.agents.memory_reorganized.models.episodic.mixins.PerformanceMetrics
      :value: None



   .. py:attribute:: session_id
      :type:  str
      :value: None



   .. py:attribute:: similarity_cluster
      :type:  str | None
      :value: None



   .. py:attribute:: task_execution
      :type:  haive.agents.memory_reorganized.models.episodic.mixins.TaskExecution
      :value: None



   .. py:attribute:: temporal_weight
      :type:  float
      :value: None



   .. py:attribute:: user_id
      :type:  str
      :value: None



   .. py:attribute:: user_input
      :type:  str
      :value: None



