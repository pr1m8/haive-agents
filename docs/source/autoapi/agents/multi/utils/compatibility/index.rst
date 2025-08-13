
:py:mod:`agents.multi.utils.compatibility`
==========================================

.. py:module:: agents.multi.utils.compatibility

Compatibility module for legacy multi-agent imports.

This module provides backward compatibility for code that imports from:
- haive.agents.multi.base
- haive.agents.multi.multi_agent
- haive.agents.multi.base_multi_agent

New code should use:
- haive.agents.multi.clean.MultiAgent (current default)
- haive.agents.multi.enhanced_multi_agent_v4.MultiAgent (recommended)


.. autolink-examples:: agents.multi.utils.compatibility
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.utils.compatibility.ExecutionMode


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

.. autoclass:: agents.multi.utils.compatibility.ExecutionMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ExecutionMode** is an Enum defined in ``agents.multi.utils.compatibility``.





.. rubric:: Related Links

.. autolink-examples:: agents.multi.utils.compatibility
   :collapse:
   
.. autolink-skip:: next
