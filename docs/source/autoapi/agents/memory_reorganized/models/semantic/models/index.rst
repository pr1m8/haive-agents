agents.memory_reorganized.models.semantic.models
================================================

.. py:module:: agents.memory_reorganized.models.semantic.models

.. autoapi-nested-parse::

   Models model module.

   This module provides models functionality for the Haive framework.

   Classes:
       SemanticMemory: SemanticMemory implementation.

   Functions:
       validate_user_id: Validate User Id functionality.
       validate_concept_graph: Validate Concept Graph functionality.
       validate_semantic_consistency: Validate Semantic Consistency functionality.


   .. autolink-examples:: agents.memory_reorganized.models.semantic.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.models.semantic.models.SemanticMemory


Module Contents
---------------

.. py:class:: SemanticMemory

   Bases: :py:obj:`haive.agents.memory.models.base.BaseMemoryModel`, :py:obj:`haive.agents.memory.models.semantic.mixins.UserContextMixin`, :py:obj:`haive.agents.memory.models.semantic.mixins.TemporalMixin`


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
      :classmethod:


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



