agents.simple.clean_enhanced_simple.v2
======================================

.. py:module:: agents.simple.clean_enhanced_simple.v2

.. autoapi-nested-parse::

   Clean_Enhanced_Simple core module.

   This module provides clean enhanced simple functionality for the Haive framework.

   Classes:
       SimpleAgent: SimpleAgent implementation.

   Functions:
       setup_agent: Setup Agent functionality.
       build_graph: Build Graph functionality.


   .. autolink-examples:: agents.simple.clean_enhanced_simple.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.clean_enhanced_simple.v2.logger


Classes
-------

.. autoapisummary::

   agents.simple.clean_enhanced_simple.v2.SimpleAgent


Module Contents
---------------

.. py:class:: SimpleAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`\ [\ :py:obj:`haive.core.engine.aug_llm.AugLLMConfig`\ ]


   SimpleAgent is just Agent[AugLLMConfig].

   This is the entire implementation - SimpleAgent is nothing more than
   an Agent with its engine type locked to AugLLMConfig. Everything else
   comes from the enhanced base Agent class.

   This demonstrates the power of engine-focused generics:
   - SimpleAgent = Agent[AugLLMConfig]
   - ReactAgent = Agent[AugLLMConfig] + looping
   - RAGAgent = Agent[RetrieverEngine]
   - etc.


   .. autolink-examples:: SimpleAgent
      :collapse:

   .. py:method:: _has_tool_calls(state: dict[str, Any]) -> bool

      Check if last message has tool calls.


      .. autolink-examples:: _has_tool_calls
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build simple graph: START -> agent -> (tools?) -> END.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup by ensuring we have AugLLMConfig and syncing fields.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: max_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



   .. py:attribute:: tools
      :type:  list[Any]
      :value: None



.. py:data:: logger

