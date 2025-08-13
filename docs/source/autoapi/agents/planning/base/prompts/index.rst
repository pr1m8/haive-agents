
:py:mod:`agents.planning.base.prompts`
======================================

.. py:module:: agents.planning.base.prompts

Base Planning Prompts - Core prompt templates for strategic planning.

This module provides the foundational prompt templates used by base planning agents
for creating comprehensive, actionable plans.


.. autolink-examples:: agents.planning.base.prompts
   :collapse:


Functions
---------

.. autoapisummary::

   agents.planning.base.prompts.create_conversation_context
   agents.planning.base.prompts.create_planning_context

.. py:function:: create_conversation_context(objective: str, participants: str = '', topic: str = '', scope: str = '', analysis_goals: str = '') -> dict

   Create context dictionary for conversation analysis prompts.

   :param objective: The analysis objective
   :param participants: Who was involved in the conversation
   :param topic: Main topic or purpose of conversation
   :param scope: Length, format, or scope of conversation
   :param analysis_goals: What insights are needed from analysis

   :returns: Complete context for conversation analysis prompts
   :rtype: dict


   .. autolink-examples:: create_conversation_context
      :collapse:

.. py:function:: create_planning_context(objective: str, available_tools: str = '', time_constraints: str = '', complexity_level: str = 'moderate', domain_focus: str = '', additional_context: str = '') -> dict

   Create context dictionary for planning prompts.

   :param objective: The main planning objective
   :param available_tools: Tools and resources available
   :param time_constraints: Time limitations or deadlines
   :param complexity_level: Desired complexity (simple, moderate, detailed, comprehensive)
   :param domain_focus: Specific domain or area of focus
   :param additional_context: Any additional context information

   :returns: Complete context for planning prompts
   :rtype: dict


   .. autolink-examples:: create_planning_context
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.base.prompts
   :collapse:
   
.. autolink-skip:: next
