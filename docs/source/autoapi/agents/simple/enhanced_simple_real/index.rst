agents.simple.enhanced_simple_real
==================================

.. py:module:: agents.simple.enhanced_simple_real

.. autoapi-nested-parse::

   Enhanced SimpleAgent - Real implementation using Agent[AugLLMConfig].

   This is the real SimpleAgent implementation showing it as Agent[AugLLMConfig].
   It carefully imports only what's needed to avoid circular imports.


   .. autolink-examples:: agents.simple.enhanced_simple_real
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.enhanced_simple_real.agent
   agents.simple.enhanced_simple_real.logger


Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_real.EnhancedAgentBase
   agents.simple.enhanced_simple_real.SimpleAgent


Module Contents
---------------

.. py:class:: EnhancedAgentBase

   Minimal base for enhanced agents to avoid circular imports.


   .. autolink-examples:: EnhancedAgentBase
      :collapse:

   .. py:method:: arun(input_data: Any) -> Any
      :async:


      Async run method.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: build_graph() -> Any
      :abstractmethod:


      Build the agent's graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: run(input_data: Any) -> Any

      Sync run method.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_agent() -> None

      Hook for subclass setup.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: engine
      :type:  Any
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: SimpleAgent

   Bases: :py:obj:`EnhancedAgentBase`


   Enhanced SimpleAgent that is essentially Agent[AugLLMConfig].

   This demonstrates the key insight: SimpleAgent IS Agent[AugLLMConfig].
   All the complexity is handled by the base Agent class and the engine type.

   In the full implementation with working imports, this would inherit from:
   Agent[AugLLMConfig] where Agent is from enhanced_agent.py

   Key points:
   - Engine is always AugLLMConfig
   - Minimal implementation needed
   - Type safety for engine-specific features
   - Clean separation of concerns


   .. autolink-examples:: SimpleAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation showing engine type.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build minimal graph for SimpleAgent.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: ensure_aug_llm_config(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Ensure we have an AugLLMConfig engine.


      .. autolink-examples:: ensure_aug_llm_config
         :collapse:


   .. py:method:: setup_agent() -> None

      Sync convenience fields to the AugLLMConfig engine.


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



.. py:data:: agent

.. py:data:: logger

