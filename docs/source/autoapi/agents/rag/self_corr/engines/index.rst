agents.rag.self_corr.engines
============================

.. py:module:: agents.rag.self_corr.engines


Attributes
----------

.. autoapisummary::

   agents.rag.self_corr.engines.GENERATE_PROMPT
   agents.rag.self_corr.engines.GENERATE_PROMPT_TEMPLATE
   agents.rag.self_corr.engines.GRADE_PROMPT
   agents.rag.self_corr.engines.GRADE_PROMPT_TEMPLATE
   agents.rag.self_corr.engines.REWRITER_PROMPT
   agents.rag.self_corr.engines.REWRITER_PROMPT_TEMPLATE


Module Contents
---------------

.. py:data:: GENERATE_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
      Question: {question} 
      Context: {context}"""

   .. raw:: html

      </details>



.. py:data:: GENERATE_PROMPT_TEMPLATE

.. py:data:: GRADE_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a grader assessing relevance of a retrieved document to a user question. 
       Here is the retrieved document: 
      
       {context} 
      
      Here is the user question: {question} 
      If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. 
      Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""

   .. raw:: html

      </details>



.. py:data:: GRADE_PROMPT_TEMPLATE

.. py:data:: REWRITER_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      Look at the input and try to reason about the underlying semantic intent / meaning.
      
      Here is the initial question:
      
      ------- 
      
      {question}
      
      ------- 
      
      Formulate an improved question:
      """

   .. raw:: html

      </details>



.. py:data:: REWRITER_PROMPT_TEMPLATE

