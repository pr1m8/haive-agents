
:py:mod:`agents.planning.plan_and_execute_multi`
================================================

.. py:module:: agents.planning.plan_and_execute_multi

Plan and Execute Agent Implementation.

from typing import Any, Dict
Simple Plan and Execute agent using MultiAgentBase with proper configuration.


.. autolink-examples:: agents.planning.plan_and_execute_multi
   :collapse:


Functions
---------

.. autoapisummary::

   agents.planning.plan_and_execute_multi.PlanAndExecuteAgent
   agents.planning.plan_and_execute_multi.create_plan_execute_branches
   agents.planning.plan_and_execute_multi.should_continue
   agents.planning.plan_and_execute_multi.should_end



.. py:function:: should_continue(state: dict[str, Any]) -> str

   Determine if execution should continue or replan.


   .. autolink-examples:: should_continue
      :collapse:

.. py:function:: should_end(state: dict[str, Any]) -> str

   Determine if execution should end.


   .. autolink-examples:: should_end
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.plan_and_execute_multi
   :collapse:
   
.. autolink-skip:: next
