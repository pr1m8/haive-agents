agents.rag.multi_strategy.state
===============================

.. py:module:: agents.rag.multi_strategy.state


Classes
-------

.. autoapisummary::

   agents.rag.multi_strategy.state.MultiStrategyRAGState


Module Contents
---------------

.. py:class:: MultiStrategyRAGState

   Bases: :py:obj:`haive.agents.rag.self_corr.state.SelfCorrectiveRAGState`


   State for multi-strategy RAG agents.


   .. autolink-examples:: MultiStrategyRAGState
      :collapse:

   .. py:attribute:: query_type
      :type:  str | None
      :value: None



   .. py:attribute:: query_variations
      :type:  list[str]
      :value: None



   .. py:attribute:: rewritten_query
      :type:  str | None
      :value: None



   .. py:attribute:: strategy_metrics
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: strategy_name
      :type:  str | None
      :value: None



