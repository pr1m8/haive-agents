
:py:mod:`agents.dynamic_supervisor.prompts`
===========================================

.. py:module:: agents.dynamic_supervisor.prompts

Prompt templates for dynamic supervisor agent.

This module contains prompt templates and system messages used by the
dynamic supervisor for task routing and agent management.

Constants:
    SUPERVISOR_SYSTEM_PROMPT: Main system prompt for supervisor
    CAPABILITY_ANALYSIS_PROMPT: Prompt for analyzing required capabilities
    ROUTING_DECISION_PROMPT: Prompt for making routing decisions

Functions:
    format_supervisor_prompt: Format the main supervisor prompt with agents
    format_agent_list: Format agent list for inclusion in prompts


.. autolink-examples:: agents.dynamic_supervisor.prompts
   :collapse:


Functions
---------

.. autoapisummary::

   agents.dynamic_supervisor.prompts.format_agent_list
   agents.dynamic_supervisor.prompts.format_missing_capability
   agents.dynamic_supervisor.prompts.format_supervisor_prompt

.. py:function:: format_agent_list(agents: dict[str, haive.agents.dynamic_supervisor.models.AgentInfo]) -> str

   Format agent list for inclusion in prompts.

   Creates a formatted list showing agent names, descriptions,
   capabilities, and status.

   :param agents: Dictionary of agent name to AgentInfo

   :returns: Formatted agent list string

   .. rubric:: Example

   Agent list format::

       - search_agent: Web search specialist
         Capabilities: search, research, web
         Status: Active

       - math_agent: Mathematics expert
         Capabilities: math, calculation, statistics
         Status: Inactive


   .. autolink-examples:: format_agent_list
      :collapse:

.. py:function:: format_missing_capability(task: str, capability: str, reason: str, requirements: list[str]) -> str

   Format a missing capability message.

   :param task: The task that needs the capability
   :param capability: The missing capability
   :param reason: Why this capability is needed
   :param requirements: What the ideal agent would need to do

   :returns: Formatted message about missing capability


   .. autolink-examples:: format_missing_capability
      :collapse:

.. py:function:: format_supervisor_prompt(agents: dict[str, haive.agents.dynamic_supervisor.models.AgentInfo]) -> str

   Format the supervisor system prompt with current agents.

   :param agents: Dictionary of agent name to AgentInfo

   :returns: Formatted system prompt

   .. rubric:: Example

   Formatting prompt with agents::

       prompt = format_supervisor_prompt(state.agents)
       # Use in supervisor engine configuration


   .. autolink-examples:: format_supervisor_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.dynamic_supervisor.prompts
   :collapse:
   
.. autolink-skip:: next
