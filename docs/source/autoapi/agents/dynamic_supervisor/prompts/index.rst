agents.dynamic_supervisor.prompts
=================================

.. py:module:: agents.dynamic_supervisor.prompts

.. autoapi-nested-parse::

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


Attributes
----------

.. autoapisummary::

   agents.dynamic_supervisor.prompts.CAPABILITY_ANALYSIS_PROMPT
   agents.dynamic_supervisor.prompts.MISSING_CAPABILITY_PROMPT
   agents.dynamic_supervisor.prompts.MULTI_AGENT_COORDINATION_TEMPLATE
   agents.dynamic_supervisor.prompts.ROUTING_DECISION_PROMPT
   agents.dynamic_supervisor.prompts.ROUTING_EXPLANATION_TEMPLATE
   agents.dynamic_supervisor.prompts.SUPERVISOR_SYSTEM_PROMPT


Functions
---------

.. autoapisummary::

   agents.dynamic_supervisor.prompts.format_agent_list
   agents.dynamic_supervisor.prompts.format_missing_capability
   agents.dynamic_supervisor.prompts.format_supervisor_prompt


Module Contents
---------------

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

.. py:data:: CAPABILITY_ANALYSIS_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Analyze the following task and identify required capabilities:
      
      Task: {task}
      
      Consider:
      1. What type of expertise is needed?
      2. What tools or resources are required?
      3. Are there multiple steps requiring different capabilities?
      4. What would be the ideal agent profile for this task?
      
      Required capabilities:"""

   .. raw:: html

      </details>



.. py:data:: MISSING_CAPABILITY_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """I've identified that this task requires capabilities we don't currently have.
      
      Task: {task}
      Missing capability: {capability}
      
      The task requires {capability} because {reason}. We would need an agent that can:
      {requirements}
      
      For now, I'm unable to complete this task without the {capability} capability."""

   .. raw:: html

      </details>



.. py:data:: MULTI_AGENT_COORDINATION_TEMPLATE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """This task requires coordination between multiple agents:
      
      Task: {task}
      
      Step-by-step plan:
      {plan}
      
      I'll coordinate the execution:
      1. First, I'll route to {first_agent} for {first_step}
      2. Then use the results with {second_agent} for {second_step}
      3. Finally, {final_step}
      
      Starting with step 1..."""

   .. raw:: html

      </details>



.. py:data:: ROUTING_DECISION_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Based on the task analysis and available agents, make a routing decision:
      
      Task: {task}
      Required capabilities: {capabilities}
      
      Available agents:
      {agent_list}
      
      Decision criteria:
      - Match required capabilities to agent descriptions
      - Consider agent availability (active/inactive)
      - Identify if multiple agents are needed
      - Determine if any capabilities are missing
      
      Your routing decision:"""

   .. raw:: html

      </details>



.. py:data:: ROUTING_EXPLANATION_TEMPLATE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """I'm routing this task to {agent_name} because:
      
      - The task requires: {required_capabilities}
      - {agent_name} provides: {agent_capabilities}
      - Match confidence: {confidence}%
      
      Task for {agent_name}: {task_description}"""

   .. raw:: html

      </details>



.. py:data:: SUPERVISOR_SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an intelligent task supervisor that routes tasks to specialized agents.
      
      Your role is to:
      1. Analyze incoming tasks to understand what capabilities are needed
      2. Route tasks to the most appropriate available agent
      3. Identify when required capabilities are missing
      4. Coordinate multi-step tasks that require multiple agents
      
      Available agents:
      {agent_list}
      
      When routing tasks:
      - Use handoff tools (handoff_to_[agent_name]) to delegate work to specific agents
      - Provide clear, detailed task descriptions when handing off
      - Consider agent capabilities and current availability (active/inactive)
      - If no suitable agent exists, use choose_agent("END") and explain what's missing
      
      For multi-step tasks:
      - Break down the task into logical steps
      - Identify which agent should handle each step
      - Route to agents sequentially as needed
      
      Always:
      - Explain your routing decisions
      - Provide context when handing off tasks
      - Be specific about what you need from each agent"""

   .. raw:: html

      </details>



