
:py:mod:`agents.reflection.state`
=================================

.. py:module:: agents.reflection.state

State schema for Reflection Agent.


.. autolink-examples:: agents.reflection.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reflection.state.ReflectionState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionState:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionState {
        node [shape=record];
        "ReflectionState" [label="ReflectionState"];
        "haive.core.schema.prebuilt.multi_agent_state.MultiAgentState" -> "ReflectionState";
      }

.. autoclass:: agents.reflection.state.ReflectionState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reflection.state.add_improvement
   agents.reflection.state.finalize
   agents.reflection.state.should_continue

.. py:function:: add_improvement(state: ReflectionState, improvement: haive.agents.reflection.models.Improvement) -> None

   Add improvement to reflection state (module-level function).


   .. autolink-examples:: add_improvement
      :collapse:

.. py:function:: finalize(state: ReflectionState) -> str

   Finalize the reflection process (module-level function).


   .. autolink-examples:: finalize
      :collapse:

.. py:function:: should_continue(state: ReflectionState) -> bool

   Check if reflection should continue (module-level function).


   .. autolink-examples:: should_continue
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.state
   :collapse:
   
.. autolink-skip:: next
