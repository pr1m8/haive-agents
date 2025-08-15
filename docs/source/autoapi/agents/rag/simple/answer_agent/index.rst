agents.rag.simple.answer_agent
==============================

.. py:module:: agents.rag.simple.answer_agent

.. autoapi-nested-parse::

   Answer Agent for RAG - SimpleAgent with document context prompt.


   .. autolink-examples:: agents.rag.simple.answer_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.simple.answer_agent.AnswerAgent


Module Contents
---------------

.. py:class:: AnswerAgent

   Bases: :py:obj:`SimpleAgentV3`


   SimpleAgent configured for answering questions based on retrieved documents.


   .. autolink-examples:: AnswerAgent
      :collapse:

   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



   .. py:attribute:: system_message
      :type:  str
      :value: None



