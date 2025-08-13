
:py:mod:`multi_agent_v2`
========================

.. py:module:: multi_agent_v2

Multi-agent V2 with proper state management and rebuilding support.

This module provides a rebuilt MultiAgent that uses MultiAgentState without
schema flattening, maintaining type safety and hierarchical access.


.. autolink-examples:: multi_agent_v2
   :collapse:

Classes
-------

.. autoapisummary::

   multi_agent_v2.ExecutionMode
   multi_agent_v2.MultiAgentV2


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionMode:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionMode {
        node [shape=record];
        "ExecutionMode" [label="ExecutionMode"];
        "str" -> "ExecutionMode";
        "enum.Enum" -> "ExecutionMode";
      }

.. autoclass:: multi_agent_v2.ExecutionMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ExecutionMode** is an Enum defined in ``multi_agent_v2``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentV2 {
        node [shape=record];
        "MultiAgentV2" [label="MultiAgentV2"];
        "haive.agents.base.agent.Agent" -> "MultiAgentV2";
      }

.. autoclass:: multi_agent_v2.MultiAgentV2
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: multi_agent_v2
   :collapse:
   
.. autolink-skip:: next
