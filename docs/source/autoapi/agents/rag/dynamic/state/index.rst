agents.rag.dynamic.state
========================

.. py:module:: agents.rag.dynamic.state


Classes
-------

.. autoapisummary::

   agents.rag.dynamic.state.DynamicRAGState


Module Contents
---------------

.. py:class:: DynamicRAGState

   Bases: :py:obj:`haive.agents.rag.base.state.BaseRAGState`


   State for Dynamic RAG.


   .. autolink-examples:: DynamicRAGState
      :collapse:

   .. py:attribute:: routing_explanation
      :type:  str | None
      :value: None



   .. py:attribute:: selected_sources
      :type:  list[str]
      :value: None



   .. py:attribute:: source_documents
      :type:  dict[str, list[langchain.schema.Document]]
      :value: None



   .. py:attribute:: source_metrics
      :type:  dict[str, dict[str, Any]]
      :value: None



