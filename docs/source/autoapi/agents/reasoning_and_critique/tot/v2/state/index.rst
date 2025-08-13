
:py:mod:`agents.reasoning_and_critique.tot.v2.state`
====================================================

.. py:module:: agents.reasoning_and_critique.tot.v2.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.state.ExpansionState
   agents.reasoning_and_critique.tot.v2.state.ToTState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExpansionState:

   .. graphviz::
      :align: center

      digraph inheritance_ExpansionState {
        node [shape=record];
        "ExpansionState" [label="ExpansionState"];
        "ToTState" -> "ExpansionState";
      }

.. autoclass:: agents.reasoning_and_critique.tot.v2.state.ExpansionState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToTState:

   .. graphviz::
      :align: center

      digraph inheritance_ToTState {
        node [shape=record];
        "ToTState" [label="ToTState"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "ToTState";
      }

.. autoclass:: agents.reasoning_and_critique.tot.v2.state.ToTState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.state.update_candidates

.. py:function:: update_candidates(existing: list | None = None, updates: list | Literal['clear'] | None = None) -> list

   Custom reducer for candidates.


   .. autolink-examples:: update_candidates
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.v2.state
   :collapse:
   
.. autolink-skip:: next
