agents.rag.filtered.state
=========================

.. py:module:: agents.rag.filtered.state


Classes
-------

.. autoapisummary::

   agents.rag.filtered.state.FilteredRAGState


Module Contents
---------------

.. py:class:: FilteredRAGState

   Bases: :py:obj:`haive.agents.rag.base.state.BaseRAGState`


   State for filtered RAG agents.

   This state extends the base RAG state with:
   1. Filtered documents - a subset of retrieved documents that passed relevance filtering
   2. Relevance scores - numerical scores indicating how relevant each document is to the query
   3. Error tracking - any errors encountered during the filtering process

   The filtering process helps to:
   - Improve answer quality by focusing on the most relevant information
   - Reduce noise and hallucinations from irrelevant content
   - Provide transparency through relevance scoring


   .. autolink-examples:: FilteredRAGState
      :collapse:

   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: filtered_documents
      :type:  list[langchain_core.documents.Document] | list[str] | None
      :value: None



   .. py:attribute:: relevance_scores
      :type:  dict[str, float]
      :value: None



