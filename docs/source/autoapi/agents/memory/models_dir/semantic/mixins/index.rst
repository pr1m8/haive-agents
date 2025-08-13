
:py:mod:`agents.memory.models_dir.semantic.mixins`
==================================================

.. py:module:: agents.memory.models_dir.semantic.mixins


Classes
-------

.. autoapisummary::

   agents.memory.models_dir.semantic.mixins.PersonalityTraits
   agents.memory.models_dir.semantic.mixins.TemporalMixin
   agents.memory.models_dir.semantic.mixins.UserContextMixin
   agents.memory.models_dir.semantic.mixins.UserPreferences


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PersonalityTraits:

   .. graphviz::
      :align: center

      digraph inheritance_PersonalityTraits {
        node [shape=record];
        "PersonalityTraits" [label="PersonalityTraits"];
        "pydantic.BaseModel" -> "PersonalityTraits";
      }

.. autopydantic_model:: agents.memory.models_dir.semantic.mixins.PersonalityTraits
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TemporalMixin:

   .. graphviz::
      :align: center

      digraph inheritance_TemporalMixin {
        node [shape=record];
        "TemporalMixin" [label="TemporalMixin"];
      }

.. autoclass:: agents.memory.models_dir.semantic.mixins.TemporalMixin
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for UserContextMixin:

   .. graphviz::
      :align: center

      digraph inheritance_UserContextMixin {
        node [shape=record];
        "UserContextMixin" [label="UserContextMixin"];
      }

.. autoclass:: agents.memory.models_dir.semantic.mixins.UserContextMixin
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for UserPreferences:

   .. graphviz::
      :align: center

      digraph inheritance_UserPreferences {
        node [shape=record];
        "UserPreferences" [label="UserPreferences"];
        "pydantic.BaseModel" -> "UserPreferences";
      }

.. autopydantic_model:: agents.memory.models_dir.semantic.mixins.UserPreferences
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.memory.models_dir.semantic.mixins.calculate_temporal_relevance
   agents.memory.models_dir.semantic.mixins.validate_expertise
   agents.memory.models_dir.semantic.mixins.validate_personality_consistency
   agents.memory.models_dir.semantic.mixins.validate_temporal_weight
   agents.memory.models_dir.semantic.mixins.validate_topic_consistency

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



.. rubric:: Related Links

.. autolink-examples:: agents.memory.models_dir.semantic.mixins
   :collapse:
   
.. autolink-skip:: next
