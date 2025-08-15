agents.document_modifiers.summarizer.map_branch.prompts
=======================================================

.. py:module:: agents.document_modifiers.summarizer.map_branch.prompts

.. autoapi-nested-parse::

   Prompts for the summarizer agent - The mapping and reducing prompts.


   .. autolink-examples:: agents.document_modifiers.summarizer.map_branch.prompts
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.document_modifiers.summarizer.map_branch.prompts.MAP_PROMPT
   agents.document_modifiers.summarizer.map_branch.prompts.REDUCE_PROMPT
   agents.document_modifiers.summarizer.map_branch.prompts.reduce_prompt_str


Module Contents
---------------

.. py:data:: MAP_PROMPT

.. py:data:: REDUCE_PROMPT

.. py:data:: reduce_prompt_str
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      The following is a set of summaries:
      {docs}
      Take these and distill it into a final, consolidated summary
      of the main themes.
      """

   .. raw:: html

      </details>



