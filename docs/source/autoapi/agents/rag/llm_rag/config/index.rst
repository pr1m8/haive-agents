agents.rag.llm_rag.config
=========================

.. py:module:: agents.rag.llm_rag.config


Attributes
----------

.. autoapisummary::

   agents.rag.llm_rag.config.RAG_BASE_PROMPT
   agents.rag.llm_rag.config.RELEVANCE_CHECKER_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.llm_rag.config.LLMRAGConfig


Module Contents
---------------

.. py:class:: LLMRAGConfig

   Bases: :py:obj:`haive.agents.rag.base.config.BaseRAGConfig`


   Configuration for an LLM-enhanced RAG agent.


   .. autolink-examples:: LLMRAGConfig
      :collapse:

   .. py:method:: setup_engines() -> LLMRAGConfig

      After validation, register all engines needed by the agent.
      This ensures the agent workflow can access all the necessary components.


      .. autolink-examples:: setup_engines
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel]


   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel]


   .. py:attribute:: relevance_checker_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]


.. py:data:: RAG_BASE_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an assistant for question-answering tasks.
      Use the following pieces of retrieved context to answer the question.
      
      First, determine if the context is relevant to the question. If the context is not relevant to
      the question, respond with "The retrieved documents are not relevant to the question."
      
      If the context is relevant:
      - Use the provided context to answer the question
      - If you don't know the answer even with the context, just say that you don't know
      - Use three sentences maximum and keep the answer concise
      - Base your answer solely on the provided context
      
      Question: {query}
      Context: {context}
      Answer:
      """

   .. raw:: html

      </details>



.. py:data:: RELEVANCE_CHECKER_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an assistant that determines if retrieved documents are relevant to a user query.
      Your task is to analyze the query and retrieved documents to determine if they contain information
      that would help answer the query.
      
      Query: {query}
      Retrieved Documents:
      {documents}
      
      Are these documents relevant to the query? Reply with just "Yes" or "No".
      """

   .. raw:: html

      </details>



