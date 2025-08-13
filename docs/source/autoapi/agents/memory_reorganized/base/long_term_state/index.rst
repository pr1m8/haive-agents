
:py:mod:`agents.memory_reorganized.base.long_term_state`
========================================================

.. py:module:: agents.memory_reorganized.base.long_term_state

State core module.

This module provides state functionality for the Haive framework.

Classes:
    LongTermMemoryState: LongTermMemoryState implementation.


.. autolink-examples:: agents.memory_reorganized.base.long_term_state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.long_term_state.KnowledgeTriple
   agents.memory_reorganized.base.long_term_state.LongTermMemoryState


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KnowledgeTriple:

   .. graphviz::
      :align: center

      digraph inheritance_KnowledgeTriple {
        node [shape=record];
        "KnowledgeTriple" [label="KnowledgeTriple"];
        "pydantic.BaseModel" -> "KnowledgeTriple";
      }

.. autopydantic_model:: agents.memory_reorganized.base.long_term_state.KnowledgeTriple
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

   Inheritance diagram for LongTermMemoryState:

   .. graphviz::
      :align: center

      digraph inheritance_LongTermMemoryState {
        node [shape=record];
        "LongTermMemoryState" [label="LongTermMemoryState"];
        "agents.react_agent.state.AgentState" -> "LongTermMemoryState";
      }

.. autoclass:: agents.memory_reorganized.base.long_term_state.LongTermMemoryState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.base.long_term_state
   :collapse:
   
.. autolink-skip:: next
