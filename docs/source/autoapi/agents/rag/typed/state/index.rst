agents.rag.typed.state
======================

.. py:module:: agents.rag.typed.state


Classes
-------

.. autoapisummary::

   agents.rag.typed.state.TypedRAGState


Module Contents
---------------

.. py:class:: TypedRAGState

   Bases: :py:obj:`haive.agents.rag.base.state.BaseRAGState`


   State for Typed-RAG.


   .. autolink-examples:: TypedRAGState
      :collapse:

   .. py:attribute:: aggregated_answer
      :type:  str | None
      :value: None



   .. py:attribute:: query_category
      :type:  str | None
      :value: None



   .. py:attribute:: query_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: subqueries
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: subquery_results
      :type:  dict[str, list[langchain.schema.Document]]
      :value: None



