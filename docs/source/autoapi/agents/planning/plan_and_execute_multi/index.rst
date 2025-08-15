agents.planning.plan_and_execute_multi
======================================

.. py:module:: agents.planning.plan_and_execute_multi

.. autoapi-nested-parse::

   Plan and Execute Agent Implementation.

   from typing import Any, Dict
   Simple Plan and Execute agent using MultiAgentBase with proper configuration.


   .. autolink-examples:: agents.planning.plan_and_execute_multi
      :collapse:


Functions
---------

.. autoapisummary::

   agents.planning.plan_and_execute_multi.should_continue
   agents.planning.plan_and_execute_multi.should_end


Module Contents
---------------

.. py:function:: should_continue(state: dict[str, Any]) -> str

   Determine if execution should continue or replan.


   .. autolink-examples:: should_continue
      :collapse:

.. py:function:: should_end(state: dict[str, Any]) -> str

   Determine if execution should end.


   .. autolink-examples:: should_end
      :collapse:

