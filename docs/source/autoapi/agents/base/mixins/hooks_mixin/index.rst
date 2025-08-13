
:py:mod:`agents.base.mixins.hooks_mixin`
========================================

.. py:module:: agents.base.mixins.hooks_mixin

Enhanced hooks mixin for the Haive framework.

from typing import Any
Provides a flexible hooks system that can be used by both single and multi agents,
with support for different hook points and graph-aware modifications.


.. autolink-examples:: agents.base.mixins.hooks_mixin
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.mixins.hooks_mixin.HooksMixin


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HooksMixin:

   .. graphviz::
      :align: center

      digraph inheritance_HooksMixin {
        node [shape=record];
        "HooksMixin" [label="HooksMixin"];
        "Generic[haive.agents.base.types.TState]" -> "HooksMixin";
      }

.. autoclass:: agents.base.mixins.hooks_mixin.HooksMixin
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.base.mixins.hooks_mixin.hook

.. py:function:: hook(point: haive.agents.base.types.HookPoint, priority: int = 0, name: str | None = None, graph_aware: bool = False, condition: collections.abc.Callable | None = None)

   Decorator for marking methods as hooks.

   Usage:
       @hook(HookPoint.AFTER_GRAPH_BUILD, priority=10)
       def add_output_parser(self, graph, context):
           # Modify graph
           return graph


   .. autolink-examples:: hook
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.base.mixins.hooks_mixin
   :collapse:
   
.. autolink-skip:: next
