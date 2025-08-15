agents.reasoning_and_critique.self_discover.aug_llms
====================================================

.. py:module:: agents.reasoning_and_critique.self_discover.aug_llms


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.aug_llms.adapt_chain
   agents.reasoning_and_critique.self_discover.aug_llms.adapt_prompt_template
   agents.reasoning_and_critique.self_discover.aug_llms.adapt_template
   agents.reasoning_and_critique.self_discover.aug_llms.reasoning_modules_instance
   agents.reasoning_and_critique.self_discover.aug_llms.reasoning_prompt
   agents.reasoning_and_critique.self_discover.aug_llms.select_chain
   agents.reasoning_and_critique.self_discover.aug_llms.select_prompt_template
   agents.reasoning_and_critique.self_discover.aug_llms.select_prompt_template
   agents.reasoning_and_critique.self_discover.aug_llms.step_reasoning_chain
   agents.reasoning_and_critique.self_discover.aug_llms.step_reasoning_prompt_template
   agents.reasoning_and_critique.self_discover.aug_llms.structured_chain
   agents.reasoning_and_critique.self_discover.aug_llms.structured_template
   agents.reasoning_and_critique.self_discover.aug_llms.structured_template_prompt


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.aug_llms.ReasoningModules


Module Contents
---------------

.. py:class:: ReasoningModules(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for ReasoningModules - needs proper implementation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningModules
      :collapse:

   .. py:attribute:: modules
      :type:  list[str]
      :value: None



.. py:data:: adapt_chain

.. py:data:: adapt_prompt_template

.. py:data:: adapt_template
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      Rephrase and specify each reasoning module so that it better helps solving the task:
      
      SELECTED module descriptions:
      {selected_modules}
      
      Task: {task_description}
      
      Adapt each reasoning module description to better solve the task:
      """

   .. raw:: html

      </details>



.. py:data:: reasoning_modules_instance

.. py:data:: reasoning_prompt
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      Step {step_id}: {step_description}
      
      Task Context: {task_description}
      
      Relevant Reasoning Modules:
      {reasoning_modules}
      
      Perform step {step_id} based on the provided reasoning structure. Ensure clarity and logical deduction.
      """

   .. raw:: html

      </details>



.. py:data:: select_chain

.. py:data:: select_prompt_template

.. py:data:: select_prompt_template

.. py:data:: step_reasoning_chain

.. py:data:: step_reasoning_prompt_template

.. py:data:: structured_chain

.. py:data:: structured_template

.. py:data:: structured_template_prompt
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      Operationalize the reasoning modules into a step-by-step reasoning plan in JSON format:
      
      Here's an example:
      
      Example Plan:
      {{
          "id": 1,
          "name": "Example Plan",
          "status": "not_started",
          "tasks": [
              {{
                  "id": 1,
                  "description": "Analyze the problem thoroughly.",
                  "status": "in_progress",
                  "reasoning_modules": [
                      {{
                          "name": "Critical Thinking",
                          "description": "Analyze the problem from different perspectives, questioning assumptions, and evaluating evidence or information."
                      }},
                      {{
                          "name": "Systems Thinking",
                          "description": "Consider the problem as part of a larger system and understand interconnected elements."
                      }}
                  ],
                  "subtasks": [
                      {{
                          "id": 2,
                          "description": "Break down the problem into smaller parts.",
                          "status": "not_started",
                          "reasoning_modules": [
                              {{
                                  "name": "Problem Decomposition",
                                  "description": "How can I break down this problem into smaller, more manageable parts?"
                              }}
                          ],
                          "subtasks": []
                      }}
                  ]
              }}
          ]
      }}
      
      Adapted module description:
      {adapted_modules}
      
      Task: {task_description}
      
      Implement a reasoning structure for solvers to follow step-by-step and arrive at the correct answer.
      
      Note: do NOT actually arrive at a conclusion in this pass. Your job is to generate a PLAN so that in the future you can fill it out and arrive at the correct conclusion for tasks like this.
      """

   .. raw:: html

      </details>



