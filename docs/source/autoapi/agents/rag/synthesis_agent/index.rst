agents.rag.synthesis_agent
==========================

.. py:module:: agents.rag.synthesis_agent

.. autoapi-nested-parse::

   Synthesis Agent for RAG - SimpleAgentV3 that synthesizes multiple RAG results.


   .. autolink-examples:: agents.rag.synthesis_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.synthesis_agent.SynthesisAgent


Module Contents
---------------

.. py:class:: SynthesisAgent

   Bases: :py:obj:`SimpleAgentV3`


   SimpleAgentV3 configured for synthesizing results from multiple RAG sources.


   .. autolink-examples:: SynthesisAgent
      :collapse:

   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



