agents.rag.llm_rag.state
========================

.. py:module:: agents.rag.llm_rag.state


Classes
-------

.. autoapisummary::

   agents.rag.llm_rag.state.LLMRAGInputState
   agents.rag.llm_rag.state.LLMRAGOutputState
   agents.rag.llm_rag.state.LLMRAGState


Module Contents
---------------

.. py:class:: LLMRAGInputState

   Bases: :py:obj:`haive.agents.rag.base.state.BaseRAGInputState`


   Input state for LLM RAG agents.


   .. autolink-examples:: LLMRAGInputState
      :collapse:

.. py:class:: LLMRAGOutputState

   Bases: :py:obj:`haive.agents.rag.base.state.BaseRAGOutputState`


   Output state for LLM RAG agents.


   .. autolink-examples:: LLMRAGOutputState
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: is_relevant
      :type:  bool
      :value: None



.. py:class:: LLMRAGState

   Bases: :py:obj:`haive.agents.rag.base.state.BaseRAGState`, :py:obj:`LLMRAGOutputState`


   State for LLM RAG agents.


   .. autolink-examples:: LLMRAGState
      :collapse:

