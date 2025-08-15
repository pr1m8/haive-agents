agents.reasoning_and_critique.reflexion.aug_llms
================================================

.. py:module:: agents.reasoning_and_critique.reflexion.aug_llms


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.reflexion.aug_llms.initial_answer_chain_config
   agents.reasoning_and_critique.reflexion.aug_llms.initial_answer_prompt
   agents.reasoning_and_critique.reflexion.aug_llms.revise_instructions
   agents.reasoning_and_critique.reflexion.aug_llms.revision_chain_config
   agents.reasoning_and_critique.reflexion.aug_llms.revision_prompt


Module Contents
---------------

.. py:data:: initial_answer_chain_config

.. py:data:: initial_answer_prompt

.. py:data:: revise_instructions
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Revise your previous answer using the new information.
          - You should use the previous critique to add important information to your answer.
              - You MUST include numerical citations in your revised answer to ensure it can be verified.
              - Add a "References" section to the bottom of your answer (which does not count towards the word limit). In form of:
                  - [1] https://example.com
                  - [2] https://example.com
          - You should use the previous critique to remove superfluous information from your answer and make SURE it is not more than 250 words.
      """

   .. raw:: html

      </details>



.. py:data:: revision_chain_config

.. py:data:: revision_prompt

