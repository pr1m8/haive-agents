
:py:mod:`agent_v4`
==================

.. py:module:: agent_v4

ReactAgent V4 - Simple loop pattern with proper inheritance.

Minimal ReactAgent that:
1. Inherits properly from SimpleAgentV3
2. Implements tool_node back to agent_node loop
3. No fancy features, just the core pattern


.. autolink-examples:: agent_v4
   :collapse:

Classes
-------

.. autoapisummary::

   agent_v4.ReactAgentV4


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgentV4:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgentV4 {
        node [shape=record];
        "ReactAgentV4" [label="ReactAgentV4"];
        "SimpleAgentV3" -> "ReactAgentV4";
      }

.. autoclass:: agent_v4.ReactAgentV4
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agent_v4
   :collapse:
   
.. autolink-skip:: next
