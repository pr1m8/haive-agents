agents.memory.models_dir.semantic.models
========================================

.. py:module:: agents.memory.models_dir.semantic.models


Classes
-------

.. autoapisummary::

   agents.memory.models_dir.semantic.models.SemanticMemory


Functions
---------

.. autoapisummary::

   agents.memory.models_dir.semantic.models.get_context_summary
   agents.memory.models_dir.semantic.models.update_context
   agents.memory.models_dir.semantic.models.validate_concept_graph
   agents.memory.models_dir.semantic.models.validate_semantic_consistency
   agents.memory.models_dir.semantic.models.validate_user_id


Module Contents
---------------

.. py:class:: SemanticMemory

   Bases: :py:obj:`haive.agents.memory.models_dir.base.BaseMemoryModel`, :py:obj:`haive.agents.memory.models_dir.semantic.mixins.UserContextMixin`, :py:obj:`haive.agents.memory.models_dir.semantic.mixins.TemporalMixin`


   Advanced semantic memory with comprehensive user modeling.


   .. autolink-examples:: SemanticMemory
      :collapse:

   .. py:method:: _extract_keywords(data: dict[str, Any]) -> list[str]

      Extract semantic keywords from factual knowledge.


      .. autolink-examples:: _extract_keywords
         :collapse:


   .. py:method:: get_context_summary() -> str

      Generate comprehensive context summary.


      .. autolink-examples:: get_context_summary
         :collapse:


   .. py:method:: update_context(new_data: dict[str, Any]) -> None

      Intelligently update contextual information.


      .. autolink-examples:: update_context
         :collapse:


   .. py:method:: validate_concept_graph(v: dict[str, list[str]]) -> dict[str, list[str]]
      :classmethod:


      Validate concept graph structure.


      .. autolink-examples:: validate_concept_graph
         :collapse:


   .. py:method:: validate_semantic_consistency() -> SemanticMemory

      Advanced semantic consistency validation.


      .. autolink-examples:: validate_semantic_consistency
         :collapse:


   .. py:method:: validate_user_id(v: str) -> str
      :classmethod:


      Enhanced user ID validation.


      .. autolink-examples:: validate_user_id
         :collapse:


   .. py:attribute:: __memory_type__
      :value: 'semantic'



   .. py:attribute:: __validation_level__
      :value: 'enterprise'



   .. py:attribute:: belief_system
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: concept_graph
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: embedding_vector
      :type:  list[float] | None
      :value: None



   .. py:attribute:: factual_knowledge
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: personality_profile
      :type:  PersonalityTraits
      :value: None



   .. py:attribute:: preferences
      :type:  UserPreferences
      :value: None



   .. py:attribute:: semantic_keywords
      :type:  list[str]
      :value: None



   .. py:attribute:: temporal_weight
      :type:  float
      :value: None



   .. py:attribute:: user_id
      :type:  str
      :value: None



.. py:function:: get_context_summary(memory: SemanticMemory) -> str

   Generate comprehensive context summary.


   .. autolink-examples:: get_context_summary
      :collapse:

.. py:function:: update_context(memory: SemanticMemory, new_data: dict[str, Any]) -> None

   Intelligently update contextual information.


   .. autolink-examples:: update_context
      :collapse:

.. py:function:: validate_concept_graph(graph: dict[str, list[str]]) -> dict[str, list[str]]

   Validate conceptual relationship graph.


   .. autolink-examples:: validate_concept_graph
      :collapse:

.. py:function:: validate_semantic_consistency(memory: SemanticMemory) -> SemanticMemory

   Validate semantic memory consistency.


   .. autolink-examples:: validate_semantic_consistency
      :collapse:

.. py:function:: validate_user_id(user_id: str) -> str

   Validate user ID format.


   .. autolink-examples:: validate_user_id
      :collapse:

