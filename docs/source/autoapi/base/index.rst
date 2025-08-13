
:py:mod:`base`
==============

.. py:module:: base

Base multi-agent implementation with branching and conditional routing support.

This module provides an abstract base class for multi-agent systems that can:
- Execute agents in sequence, parallel, or with conditional branching
- Maintain private agent state schemas while sharing a global state
- Support complex routing patterns including loops and conditional paths


.. autolink-examples:: base
   :collapse:

Classes
-------

.. autoapisummary::

   base.ConditionalAgent
   base.ExecutionMode
   base.MultiAgent
   base.ParallelAgent
   base.SequentialAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConditionalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalAgent {
        node [shape=record];
        "ConditionalAgent" [label="ConditionalAgent"];
        "MultiAgent" -> "ConditionalAgent";
      }

.. autoclass:: base.ConditionalAgent
   :members:
   :undoc-members:
   :show-inheritance:




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

.. autoclass:: base.ExecutionMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ExecutionMode** is an Enum defined in ``base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgent {
        node [shape=record];
        "MultiAgent" [label="MultiAgent"];
        "haive.agents.base.agent.Agent" -> "MultiAgent";
      }

.. autoclass:: base.MultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelAgent {
        node [shape=record];
        "ParallelAgent" [label="ParallelAgent"];
        "MultiAgent" -> "ParallelAgent";
      }

.. autoclass:: base.ParallelAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialAgent {
        node [shape=record];
        "SequentialAgent" [label="SequentialAgent"];
        "MultiAgent" -> "SequentialAgent";
      }

.. autoclass:: base.SequentialAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: base
   :collapse:
   
.. autolink-skip:: next
