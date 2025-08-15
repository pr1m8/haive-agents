agents.document_modifiers.summarizer.iterative_refinement.engines
=================================================================

.. py:module:: agents.document_modifiers.summarizer.iterative_refinement.engines


Attributes
----------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.engines.initial_summary_aug_llm
   agents.document_modifiers.summarizer.iterative_refinement.engines.refine_prompt
   agents.document_modifiers.summarizer.iterative_refinement.engines.refine_summary_aug_llm
   agents.document_modifiers.summarizer.iterative_refinement.engines.refine_template
   agents.document_modifiers.summarizer.iterative_refinement.engines.summarize_prompt


Module Contents
---------------

.. py:data:: initial_summary_aug_llm

.. py:data:: refine_prompt

.. py:data:: refine_summary_aug_llm

.. py:data:: refine_template
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      Produce a final summary.
      
      Existing summary up to this point:
      {existing_answer}
      
      New context:
      ------------
      {context}
      ------------
      
      Given the new context, refine the original summary.
      """

   .. raw:: html

      </details>



.. py:data:: summarize_prompt

