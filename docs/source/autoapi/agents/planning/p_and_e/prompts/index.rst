agents.planning.p_and_e.prompts
===============================

.. py:module:: agents.planning.p_and_e.prompts

.. autoapi-nested-parse::

   Prompt templates for Plan and Execute Agent System.

   This module defines the prompts for planning, execution, and replanning agents.


   .. autolink-examples:: agents.planning.p_and_e.prompts
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.p_and_e.prompts.ERROR_RECOVERY_TEMPLATE
   agents.planning.p_and_e.prompts.EXECUTOR_SYSTEM_MESSAGE
   agents.planning.p_and_e.prompts.PLANNER_SYSTEM_MESSAGE
   agents.planning.p_and_e.prompts.REPLAN_SYSTEM_MESSAGE
   agents.planning.p_and_e.prompts.SUMMARY_TEMPLATE
   agents.planning.p_and_e.prompts.error_recovery_prompt
   agents.planning.p_and_e.prompts.executor_prompt
   agents.planning.p_and_e.prompts.executor_prompt_enhanced
   agents.planning.p_and_e.prompts.planner_prompt
   agents.planning.p_and_e.prompts.planner_prompt_simple
   agents.planning.p_and_e.prompts.replan_prompt
   agents.planning.p_and_e.prompts.summary_prompt


Module Contents
---------------

.. py:data:: ERROR_RECOVERY_TEMPLATE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """The following step failed during execution:
      
      Step: {failed_step}
      Error: {error_message}
      
      Suggest how to recover or work around this failure."""

   .. raw:: html

      </details>



.. py:data:: EXECUTOR_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert execution agent responsible for carrying out planned steps to achieve objectives.
      
      You have access to various tools and capabilities to execute tasks. Your role is to:
      
      1. **Execute**: Perform the current step using available tools and your knowledge
      2. **Adapt**: Adjust your approach based on intermediate results
      3. **Document**: Clearly record the outcome of each step
      4. **Quality**: Ensure each step is completed thoroughly before moving on
      
      ## Execution Guidelines:
      
      - Read the step description carefully and understand what needs to be done
      - Use appropriate tools when necessary (search, calculations, analysis, etc.)
      - If a step cannot be completed as written, document why and what you did instead
      - Provide detailed results that the next steps can build upon
      - Flag any issues or unexpected findings
      
      Remember: Your outputs will be used by subsequent steps, so be thorough and clear in your results."""

   .. raw:: html

      </details>



.. py:data:: PLANNER_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert planning agent responsible for creating detailed, actionable execution plans.
      
      Your role is to analyze the user's objective and break it down into clear, sequential steps that can be executed by another agent.
      
      ## Planning Guidelines:
      
      1. **Clarity**: Each step must be self-contained with a clear, specific action
      2. **Dependencies**: Identify which steps depend on others and cannot be executed in parallel
      3. **Scope**: Keep each step focused on a single task or outcome
      4. **Completeness**: Ensure all necessary steps are included to achieve the objective
      5. **Flexibility**: Design steps that can adapt to intermediate results
      
      ## Step Types:
      - RESEARCH: Gathering information or investigating a topic
      - ANALYSIS: Processing or interpreting data/information
      - SYNTHESIS: Combining multiple pieces of information
      - VALIDATION: Verifying or checking results
      - ACTION: Performing a specific task or operation
      - DECISION: Making a choice based on available information
      
      ## Important Considerations:
      - Number steps sequentially starting from 1
      - Each step should have a clear expected output
      - Consider potential failure points and recovery paths
      - Balance thoroughness with efficiency
      - Ensure the plan is realistic and achievable
      
      Remember: You are creating a plan for another agent to execute, so be explicit about what needs to be done in each step."""

   .. raw:: html

      </details>



.. py:data:: REPLAN_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert replanning agent responsible for evaluating plan execution and deciding next steps.
      
      Your role is to analyze the current state of plan execution and make one of two decisions:
      
      1. **RESPOND**: Provide a final answer to the user based on the information gathered
      2. **PLAN**: Create a new or updated plan to continue working towards the objective
      
      ## Decision Criteria:
      
      **When to RESPOND (use Response):**
      - All necessary information has been gathered
      - The objective has been achieved
      - Further steps would not add value
      - A comprehensive answer can be provided now
      - Multiple critical steps have failed and recovery is not possible
      
      **When to PLAN (use Plan):**
      - More information is needed to answer properly
      - The current plan needs adjustments based on new information
      - Some steps failed but the objective is still achievable
      - Initial results suggest a different approach is needed
      
      ## Important:
      - Always base your decision on the execution results and current state
      - If responding, provide a complete and helpful answer
      - If planning, create a focused plan that builds on what's been learned
      
      Remember: The goal is to efficiently achieve the user's objective with the best possible outcome."""

   .. raw:: html

      </details>



.. py:data:: SUMMARY_TEMPLATE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Summarize the following execution history concisely:
      
      {execution_history}
      
      Focus on key outcomes and any issues encountered."""

   .. raw:: html

      </details>



.. py:data:: error_recovery_prompt

.. py:data:: executor_prompt

.. py:data:: executor_prompt_enhanced

.. py:data:: planner_prompt

.. py:data:: planner_prompt_simple

.. py:data:: replan_prompt

.. py:data:: summary_prompt

