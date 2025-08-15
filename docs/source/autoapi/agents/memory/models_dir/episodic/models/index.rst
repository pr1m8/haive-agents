agents.memory.models_dir.episodic.models
========================================

.. py:module:: agents.memory.models_dir.episodic.models


Classes
-------

.. autoapisummary::

   agents.memory.models_dir.episodic.models.EpisodicMemory


Functions
---------

.. autoapisummary::

   agents.memory.models_dir.episodic.models.calculate_learning_value
   agents.memory.models_dir.episodic.models.validate_content_safety
   agents.memory.models_dir.episodic.models.validate_episodic_consistency


Module Contents
---------------

.. py:class:: EpisodicMemory

   Bases: :py:obj:`haive.agents.memory.models_dir.base.BaseMemoryModel`, :py:obj:`haive.agents.memory.models_dir.semantic.mixins.TemporalMixin`


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
      :type:  haive.agents.memory.models_dir.episodic.mixins.PerformanceMetrics
      :value: None



   .. py:attribute:: session_id
      :type:  str
      :value: None



   .. py:attribute:: similarity_cluster
      :type:  str | None
      :value: None



   .. py:attribute:: task_execution
      :type:  haive.agents.memory.models_dir.episodic.mixins.TaskExecution
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



.. py:function:: calculate_learning_value(memory: EpisodicMemory) -> float

   Calculate learning value of an episodic memory.


   .. autolink-examples:: calculate_learning_value
      :collapse:

.. py:function:: validate_content_safety(content: str) -> str

   Validate content safety for episodic memory.


   .. autolink-examples:: validate_content_safety
      :collapse:

.. py:function:: validate_episodic_consistency(memory: EpisodicMemory) -> EpisodicMemory

   Validate episodic memory consistency.


   .. autolink-examples:: validate_episodic_consistency
      :collapse:

