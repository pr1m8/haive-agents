
:py:mod:`agents.react_class.react_agent2.many_tools.nodes`
==========================================================

.. py:module:: agents.react_class.react_agent2.many_tools.nodes



Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.many_tools.nodes.select_tools
   agents.react_class.react_agent2.many_tools.nodes.select_tools_with_repeat

.. py:function:: select_tools(state: haive.core.models.state.State, vs_config: haive.core.models.vectorstore.base.VectorStoreConfig)

.. py:function:: select_tools_with_repeat(state: haive.core.models.state.State, vs_config: haive.core.models.vectorstore.base.VectorStoreConfig, aug_llm_config: haive.core.engine.aug_llm.AugLLMConfig = query_builder_aug_llm_config)

   Selects tools based on the last message in the conversation state.

   If the last message is from a human, directly uses the content of the message
   as the query. Otherwise, constructs a query using a system message and invokes
   the LLM to generate tool suggestions.


   .. autolink-examples:: select_tools_with_repeat
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.many_tools.nodes
   :collapse:
   
.. autolink-skip:: next
