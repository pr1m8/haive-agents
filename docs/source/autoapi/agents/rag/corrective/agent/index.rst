agents.rag.corrective.agent
===========================

.. py:module:: agents.rag.corrective.agent

.. autoapi-nested-parse::

   Corrective RAG (CRAG) Agent.

   from typing import Any, Dict
   Self-correcting retrieval with quality assessment.
   Implements architecture from rag-architectures-flows.md:
   Retrieval → Relevance Check → Knowledge Refinement/Web Search/Combine


   .. autolink-examples:: agents.rag.corrective.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.corrective.agent.ANSWER_PROMPT
   agents.rag.corrective.agent.DOCUMENT_GRADER_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.corrective.agent.CorrectiveRAGAgent


Module Contents
---------------

.. py:class:: CorrectiveRAGAgent

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Corrective RAG with self-correcting retrieval.


   .. autolink-examples:: CorrectiveRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, relevance_threshold: float = 0.7, **kwargs)
      :classmethod:


      Create Corrective RAG from documents.

      :param documents: Documents to index
      :param llm_config: Optional LLM configuration
      :param relevance_threshold: Threshold for document relevance
      :param \*\*kwargs: Additional arguments

      :returns: CorrectiveRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:data:: ANSWER_PROMPT

.. py:data:: DOCUMENT_GRADER_PROMPT

