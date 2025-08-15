agents.rag.answer_agent
=======================

.. py:module:: agents.rag.answer_agent

.. autoapi-nested-parse::

   Answer Agent for RAG - SimpleAgentV3 with document context prompt.


   .. autolink-examples:: agents.rag.answer_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.answer_agent.AnswerAgent


Module Contents
---------------

.. py:class:: AnswerAgent

   Bases: :py:obj:`SimpleAgentV3`


   SimpleAgentV3 configured for answering questions based on retrieved documents.


   .. autolink-examples:: AnswerAgent
      :collapse:

   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



