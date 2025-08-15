agents.planning_v2.base.planner.prompts_advanced
================================================

.. py:module:: agents.planning_v2.base.planner.prompts_advanced

.. autoapi-nested-parse::

   Advanced prompt patterns for the planner using MessagesPlaceholder.


   .. autolink-examples:: agents.planning_v2.base.planner.prompts_advanced
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning_v2.base.planner.prompts_advanced.planner_prompt_dynamic
   agents.planning_v2.base.planner.prompts_advanced.planner_prompt_with_placeholder


Functions
---------

.. autoapisummary::

   agents.planning_v2.base.planner.prompts_advanced.get_environment_context
   agents.planning_v2.base.planner.prompts_advanced.plan_with_context_messages


Module Contents
---------------

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

.. py:data:: planner_prompt_dynamic

.. py:data:: planner_prompt_with_placeholder

