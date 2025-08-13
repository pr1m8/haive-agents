
:py:mod:`agents.memory.models_dir.semantic.models`
==================================================

.. py:module:: agents.memory.models_dir.semantic.models


Classes
-------

.. autoapisummary::

   agents.memory.models_dir.semantic.models.SemanticMemory


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SemanticMemory:

   .. graphviz::
      :align: center

      digraph inheritance_SemanticMemory {
        node [shape=record];
        "SemanticMemory" [label="SemanticMemory"];
        "haive.agents.memory.models_dir.base.BaseMemoryModel" -> "SemanticMemory";
        "haive.agents.memory.models_dir.semantic.mixins.UserContextMixin" -> "SemanticMemory";
        "haive.agents.memory.models_dir.semantic.mixins.TemporalMixin" -> "SemanticMemory";
      }

.. autoclass:: agents.memory.models_dir.semantic.models.SemanticMemory
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory.models_dir.semantic.models.get_context_summary
   agents.memory.models_dir.semantic.models.update_context
   agents.memory.models_dir.semantic.models.validate_concept_graph
   agents.memory.models_dir.semantic.models.validate_semantic_consistency
   agents.memory.models_dir.semantic.models.validate_user_id

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



.. rubric:: Related Links

.. autolink-examples:: agents.memory.models_dir.semantic.models
   :collapse:
   
.. autolink-skip:: next
