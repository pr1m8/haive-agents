
:py:mod:`agents.planning_v2.base.planner.prompts_advanced`
==========================================================

.. py:module:: agents.planning_v2.base.planner.prompts_advanced

Advanced prompt patterns for the planner using MessagesPlaceholder.


.. autolink-examples:: agents.planning_v2.base.planner.prompts_advanced
   :collapse:


Functions
---------

.. autoapisummary::

   agents.planning_v2.base.planner.prompts_advanced.get_environment_context
   agents.planning_v2.base.planner.prompts_advanced.plan_with_context_messages

.. py:function:: get_environment_context()

   Dynamically generate context based on environment.


   .. autolink-examples:: get_environment_context
      :collapse:

.. py:function:: plan_with_context_messages(objective: str, context_items: list[str] = None)
   :async:


   Create a plan with optional context messages.

   :param objective: The planning objective
   :param context_items: List of context strings to include as messages

   :returns: Plan result


   .. autolink-examples:: plan_with_context_messages
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning_v2.base.planner.prompts_advanced
   :collapse:
   
.. autolink-skip:: next
