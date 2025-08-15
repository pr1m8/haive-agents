agents.base.agent_with_token_tracking
=====================================

.. py:module:: agents.base.agent_with_token_tracking

.. autoapi-nested-parse::

   Agent base class with integrated token usage tracking.

   This module provides an enhanced Agent base class that automatically tracks
   token usage for all LLM interactions, providing cost analysis and capacity
   monitoring capabilities.


   .. autolink-examples:: agents.base.agent_with_token_tracking
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.agent_with_token_tracking.logger


Classes
-------

.. autoapisummary::

   agents.base.agent_with_token_tracking.TokenTrackingAgent


Module Contents
---------------

.. py:class:: TokenTrackingAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent base class with automatic token usage tracking.

   This enhanced agent automatically tracks token usage for all LLM interactions,
   providing detailed metrics on token consumption, costs, and capacity usage.
   It uses MessagesStateWithTokenUsage as the default state schema.

   Additional features:
   - Automatic token extraction from LLM responses
   - Cost calculation based on provider pricing
   - Capacity percentage monitoring
   - Token usage history tracking
   - Conversation cost analysis

   .. rubric:: Example

   .. code-block:: python

       class MyAgent(TokenTrackingAgent):
       def build_graph(self):
       # Your graph logic
       pass

       agent = MyAgent(
       name="cost_aware_agent",
       engine=llm_engine,
       track_costs=True,
       input_cost_per_1k=0.003,
       output_cost_per_1k=0.015
       )

       # After running
       result = agent.invoke({"query": "Hello"})
       usage = agent.get_token_usage_summary()
       print(f"Total tokens: {usage['total_tokens']}")
       print(f"Total cost: ${usage['total_cost']:.4f}")


   .. autolink-examples:: TokenTrackingAgent
      :collapse:

   .. py:method:: _setup_schemas() -> None

      Generate schemas with token tracking support.


      .. autolink-examples:: _setup_schemas
         :collapse:


   .. py:method:: calculate_conversation_costs() -> None

      Calculate costs for the current conversation.


      .. autolink-examples:: calculate_conversation_costs
         :collapse:


   .. py:method:: get_token_usage_summary() -> dict[str, Any]

      Get token usage summary from the current state.

      :returns: Dictionary with token usage statistics


      .. autolink-examples:: get_token_usage_summary
         :collapse:


   .. py:attribute:: cached_input_cost_per_1k
      :type:  float | None
      :value: None



   .. py:attribute:: input_cost_per_1k
      :type:  float
      :value: None



   .. py:attribute:: output_cost_per_1k
      :type:  float
      :value: None



   .. py:attribute:: track_costs
      :type:  bool
      :value: None



.. py:data:: logger

