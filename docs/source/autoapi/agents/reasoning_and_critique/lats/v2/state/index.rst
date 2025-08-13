
:py:mod:`agents.reasoning_and_critique.lats.v2.state`
=====================================================

.. py:module:: agents.reasoning_and_critique.lats.v2.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.v2.state.LATSState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LATSState:

   .. graphviz::
      :align: center

      digraph inheritance_LATSState {
        node [shape=record];
        "LATSState" [label="LATSState"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "LATSState";
      }

.. autoclass:: agents.reasoning_and_critique.lats.v2.state.LATSState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.lats.v2.state.update_nodes

.. py:function:: update_nodes(existing: dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode] | None = None, updates: dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode] | None = None) -> dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode]

   Custom reducer for tree nodes.


   .. autolink-examples:: update_nodes
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.lats.v2.state
   :collapse:
   
.. autolink-skip:: next
