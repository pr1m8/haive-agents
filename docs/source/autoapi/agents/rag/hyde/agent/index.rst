agents.rag.hyde.agent
=====================

.. py:module:: agents.rag.hyde.agent

.. autoapi-nested-parse::

   HyDE (Hypothetical Document Embeddings) RAG Agent.

   from typing import Any
   Bridges query-document semantic gap by generating hypothetical documents.
   Implements architecture from rag-architectures-flows.md:
   Query -> Generate Hypothetical Doc -> Embed -> Retrieve Real Docs -> Generate


   .. autolink-examples:: agents.rag.hyde.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.hyde.agent.HYDE_ANSWER_PROMPT
   agents.rag.hyde.agent.HYDE_GENERATION_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.hyde.agent.HyDERAGAgent


Module Contents
---------------

.. py:class:: HyDERAGAgent

   Bases: :py:obj:`haive.agents.multi.MultiAgent`


   HyDE RAG using hypothetical document generation for better retrieval.


   .. autolink-examples:: HyDERAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs)
      :classmethod:


      Create HyDE RAG from documents.

      :param documents: Documents to index
      :param llm_config: Optional LLM configuration
      :param \*\*kwargs: Additional arguments

      :returns: HyDERAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:data:: HYDE_ANSWER_PROMPT

.. py:data:: HYDE_GENERATION_PROMPT

