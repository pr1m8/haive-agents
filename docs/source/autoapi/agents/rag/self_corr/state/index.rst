agents.rag.self_corr.state
==========================

.. py:module:: agents.rag.self_corr.state


Classes
-------

.. autoapisummary::

   agents.rag.self_corr.state.SelfCorrectiveRAGState


Module Contents
---------------

.. py:class:: SelfCorrectiveRAGState

   Bases: :py:obj:`haive.agents.rag.base.config.BaseRAGState`


   State schema for self-corrective RAG agents.

   Extends the base RAG state with fields for tracking answer quality,
   correction iterations, and assessment of hallucinations.


   .. autolink-examples:: SelfCorrectiveRAGState
      :collapse:

   .. py:attribute:: answer_score
      :type:  float
      :value: None



   .. py:attribute:: correction_iterations
      :type:  int
      :value: None



   .. py:attribute:: filtered_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: final_answer
      :type:  bool
      :value: None



   .. py:attribute:: final_confidence
      :type:  float | None
      :value: None



   .. py:attribute:: hallucination_assessment
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: relevance_scores
      :type:  dict[str, float]
      :value: None



