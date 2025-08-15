agents.simple.enhanced_simple_agent_v2.v2
=========================================

.. py:module:: agents.simple.enhanced_simple_agent_v2.v2

.. autoapi-nested-parse::

   Enhanced_Simple_Agent_V2 core module.

   This module provides enhanced simple agent v2 functionality for the Haive framework.

   Classes:
       directly: directly implementation.
       SimpleAgentV2: SimpleAgentV2 implementation.

   Functions:
       ensure_engine: Ensure Engine functionality.
       setup_agent: Setup Agent functionality.
       build_graph: Build Graph functionality.


   .. autolink-examples:: agents.simple.enhanced_simple_agent_v2.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.enhanced_simple_agent_v2.v2.logger


Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_agent_v2.v2.SimpleAgentV2


Module Contents
---------------

.. py:class:: SimpleAgentV2

   Bases: :py:obj:`base.enhanced_agent.Agent`\ [\ :py:obj:`haive.core.engine.aug_llm.AugLLMConfig`\ ]


   SimpleAgent V2 using the enhanced Agent pattern.

   This demonstrates SimpleAgent as Agent[AugLLMConfig] - the cleanest
   possible implementation using engine-focused generics.

   Key points:
   - Inherits from enhanced Agent with AugLLMConfig as engine type
   - Engine is guaranteed to be AugLLMConfig
   - All complex logic handled by base enhanced Agent
   - SimpleAgent is just configuration and graph building


   .. autolink-examples:: SimpleAgentV2
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build minimal graph for SimpleAgent.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: ensure_engine(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Ensure we have an AugLLMConfig engine.


      .. autolink-examples:: ensure_engine
         :collapse:


   .. py:method:: setup_agent() -> None

      Sync fields to engine.


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

