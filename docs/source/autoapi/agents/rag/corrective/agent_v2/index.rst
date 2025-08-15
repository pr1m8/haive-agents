agents.rag.corrective.agent_v2
==============================

.. py:module:: agents.rag.corrective.agent_v2

.. autoapi-nested-parse::

   Corrective RAG (CRAG) Agent V2.

   from typing import Any
   Self-correcting retrieval with proper quality assessment.
   Implements architecture from rag-architectures-flows.md:
   Retrieval → Relevance Check → Knowledge Refinement/Web Search/Combine


   .. autolink-examples:: agents.rag.corrective.agent_v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.corrective.agent_v2.REFINE_DOCS_PROMPT
   agents.rag.corrective.agent_v2.WEB_SEARCH_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.corrective.agent_v2.CorrectiveRAGAgentV2


Module Contents
---------------

.. py:class:: CorrectiveRAGAgentV2

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Corrective RAG with proper self-correcting retrieval.


   .. autolink-examples:: CorrectiveRAGAgentV2
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, relevance_threshold: float = 0.7, **kwargs)
      :classmethod:


      Create Corrective RAG from documents.

      :param documents: Documents to index
      :param llm_config: Optional LLM configuration
      :param relevance_threshold: Threshold for document relevance (0-1)
      :param \*\*kwargs: Additional arguments

      :returns: CorrectiveRAGAgentV2 instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:data:: REFINE_DOCS_PROMPT

.. py:data:: WEB_SEARCH_PROMPT

