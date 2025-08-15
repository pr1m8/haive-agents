agents.rag.base.prompts
=======================

.. py:module:: agents.rag.base.prompts


Attributes
----------

.. autoapisummary::

   agents.rag.base.prompts.hallucination_prompt
   agents.rag.base.prompts.rag_base_prompt
   agents.rag.base.prompts.re_write_prompt
   agents.rag.base.prompts.system
   agents.rag.base.prompts.system_rewrite


Module Contents
---------------

.. py:data:: hallucination_prompt

.. py:data:: rag_base_prompt
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an assistant for question-answering tasks.
      Use the following pieces of retrieved context to answer the question.
      If you don't know the answer, just say that you don't know. Use three sentences
      maximum and keep the answer concise.
      Question: {query}
      Context: {context}
      Answer:
      """

   .. raw:: html

      </details>



.. py:data:: re_write_prompt

.. py:data:: system
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. 
      
           Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""

   .. raw:: html

      </details>



.. py:data:: system_rewrite
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You a question re-writer that converts an input question to a better version that is optimized 
      
           for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""

   .. raw:: html

      </details>



