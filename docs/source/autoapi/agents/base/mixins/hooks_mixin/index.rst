agents.base.mixins.hooks_mixin
==============================

.. py:module:: agents.base.mixins.hooks_mixin

.. autoapi-nested-parse::

   Enhanced hooks mixin for the Haive framework.

   from typing import Any
   Provides a flexible hooks system that can be used by both single and multi agents,
   with support for different hook points and graph-aware modifications.


   .. autolink-examples:: agents.base.mixins.hooks_mixin
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.mixins.hooks_mixin.T
   agents.base.mixins.hooks_mixin.logger


Classes
-------

.. autoapisummary::

   agents.base.mixins.hooks_mixin.HooksMixin


Functions
---------

.. autoapisummary::

   agents.base.mixins.hooks_mixin.hook


Module Contents
---------------

.. py:class:: HooksMixin(**kwargs)

   Bases: :py:obj:`Generic`\ [\ :py:obj:`haive.agents.base.types.TState`\ ]


   Mixin that provides comprehensive hooks functionality.

   This mixin is generic over the state type, allowing hooks to be
   type-safe with respect to the agent's state schema.

   Initialize hooks storage.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HooksMixin
      :collapse:

   .. py:method:: _auto_register_hooks()

      Automatically register methods decorated with @hook.


      .. autolink-examples:: _auto_register_hooks
         :collapse:


   .. py:method:: clear_hook_results() -> None

      Clear all stored hook results.


      .. autolink-examples:: clear_hook_results
         :collapse:


   .. py:method:: disable_hooks() -> None

      Disable hook execution.


      .. autolink-examples:: disable_hooks
         :collapse:


   .. py:method:: enable_hooks() -> None

      Enable hook execution.


      .. autolink-examples:: enable_hooks
         :collapse:


   .. py:method:: get_hook_result(point: haive.agents.base.types.HookPoint, hook_name: str) -> Any

      Get stored result from a previous hook execution.


      .. autolink-examples:: get_hook_result
         :collapse:


   .. py:method:: list_hooks() -> dict[str, list[dict[str, Any]]]

      List all registered hooks with metadata.


      .. autolink-examples:: list_hooks
         :collapse:


   .. py:method:: register_hook(point: haive.agents.base.types.HookPoint, hook: collections.abc.Callable, priority: int = 0, name: str | None = None, graph_aware: bool = False, condition: collections.abc.Callable[[HooksMixin, haive.agents.base.types.HookContext[haive.agents.base.types.TState]], bool] | None = None) -> None

      Register a hook with enhanced capabilities.

      :param point: Hook point to register at
      :param hook: Hook function to call
      :param priority: Execution priority (higher = earlier)
      :param name: Optional hook name
      :param graph_aware: Whether hook needs graph context
      :param condition: Optional condition function


      .. autolink-examples:: register_hook
         :collapse:


   .. py:method:: run_hooks(point: haive.agents.base.types.HookPoint, *args, context: haive.agents.base.types.HookContext[haive.agents.base.types.TState] | None = None, **kwargs) -> Any

      Run hooks for a specific point with enhanced context.

      :returns: Last non-None result from hooks, or None


      .. autolink-examples:: run_hooks
         :collapse:


   .. py:method:: unregister_hook(point: haive.agents.base.types.HookPoint, hook: collections.abc.Callable | str | None = None) -> None

      Unregister one or all hooks at a point.


      .. autolink-examples:: unregister_hook
         :collapse:


   .. py:attribute:: _hook_enabled
      :type:  bool
      :value: None



   .. py:attribute:: _hook_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: _hooks
      :type:  dict[haive.agents.base.types.HookPoint, list[dict[str, Any]]]
      :value: None



.. py:function:: hook(point: haive.agents.base.types.HookPoint, priority: int = 0, name: str | None = None, graph_aware: bool = False, condition: collections.abc.Callable | None = None)

   Decorator for marking methods as hooks.

   Usage:
       @hook(HookPoint.AFTER_GRAPH_BUILD, priority=10)
       def add_output_parser(self, graph, context):
           # Modify graph
           return graph


   .. autolink-examples:: hook
      :collapse:

.. py:data:: T

.. py:data:: logger

