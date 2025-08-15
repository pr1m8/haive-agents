agents.planning.plan_and_execute.engines
========================================

.. py:module:: agents.planning.plan_and_execute.engines


Attributes
----------

.. autoapisummary::

   agents.planning.plan_and_execute.engines.EXECUTOR_PROMPT
   agents.planning.plan_and_execute.engines.EXECUTOR_PROMPT_TEMPLATE
   agents.planning.plan_and_execute.engines.PLANNER_PROMPT
   agents.planning.plan_and_execute.engines.PLANNER_PROMPT_TEMPLATE
   agents.planning.plan_and_execute.engines.REPLANNER_PROMPT
   agents.planning.plan_and_execute.engines.REPLANNER_PROMPT_TEMPLATE
   agents.planning.plan_and_execute.engines.planner_aug_llm_config
   agents.planning.plan_and_execute.engines.replanner_aug_llm_config


Module Contents
---------------

.. py:data:: EXECUTOR_PROMPT
   :value: 'You are a helpful assistant'


.. py:data:: EXECUTOR_PROMPT_TEMPLATE

.. py:data:: PLANNER_PROMPT
   :value: 'For the given objective, come up with a simple step by step plan. This plan should involve...


.. py:data:: PLANNER_PROMPT_TEMPLATE

.. py:data:: REPLANNER_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """For the given objective, come up with a simple step by step plan. This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.
      
      Your objective was this:
      {input}
      
      Your original plan was this:
      {plan}
      
      You have currently done the follow steps:
      {past_steps}
      
      Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan.
      """

   .. raw:: html

      </details>



.. py:data:: REPLANNER_PROMPT_TEMPLATE

.. py:data:: planner_aug_llm_config

.. py:data:: replanner_aug_llm_config

