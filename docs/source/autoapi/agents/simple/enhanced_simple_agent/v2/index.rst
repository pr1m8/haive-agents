agents.simple.enhanced_simple_agent.v2
======================================

.. py:module:: agents.simple.enhanced_simple_agent.v2

.. autoapi-nested-parse::

   Enhanced_Simple_Agent core module.

   This module provides enhanced simple agent functionality for the Haive framework.

   Classes:
       EnhancedSimpleAgent: EnhancedSimpleAgent implementation.

   Functions:
       calculator: Calculator functionality.
       create_default_engine: Create Default Engine functionality.
       setup_agent: Setup Agent functionality.


   .. autolink-examples:: agents.simple.enhanced_simple_agent.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.enhanced_simple_agent.v2.SimpleAgent
   agents.simple.enhanced_simple_agent.v2.logger


Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_agent.v2.EnhancedSimpleAgent


Functions
---------

.. autoapisummary::

   agents.simple.enhanced_simple_agent.v2.create_simple_agent


Module Contents
---------------

.. py:class:: EnhancedSimpleAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`\ [\ :py:obj:`haive.core.engine.aug_llm.AugLLMConfig`\ ]


   Enhanced SimpleAgent that is essentially Agent[AugLLMConfig].

   This is the cleanest implementation - SimpleAgent is just an Agent
   specialized for AugLLMConfig as its engine type. All the complex
   functionality comes from the base enhanced Agent class.

   The engine-focused generic pattern provides:
   - Type safety: engine is always AugLLMConfig
   - Clean design: SimpleAgent = Agent[AugLLMConfig]
   - Flexibility: Can still use tools, structured output, etc.

   .. attribute:: temperature

      LLM temperature (0.0-2.0), synced to engine.

   .. attribute:: max_tokens

      Maximum tokens for responses, synced to engine.

   .. attribute:: system_message

      System prompt, synced to engine.

   .. attribute:: tools

      List of tools available to the agent.

   .. rubric:: Examples

   Basic usage::

       agent = EnhancedSimpleAgent(
           name="assistant",
           temperature=0.7,
           system_message="You are a helpful assistant"
       )
       response = await agent.arun("Hello!")

   With tools::

       from langchain_core.tools import tool

       @tool
       def calculator(expression: str) -> str:
           return str(eval(expression))

       agent = EnhancedSimpleAgent(
           name="math_helper",
           tools=[calculator]
       )
       result = await agent.arun("What is 15 * 23?")


   .. autolink-examples:: EnhancedSimpleAgent
      :collapse:

   .. py:method:: add_tool(tool: Any) -> None

      Add a tool to the agent.

      :param tool: Tool to add.

      .. note:: Graph rebuild may be needed after adding tools.


      .. autolink-examples:: add_tool
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the simple agent graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_default_engine(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Create AugLLMConfig engine if not provided.


      .. autolink-examples:: create_default_engine
         :collapse:


   .. py:method:: get_aug_llm_config() -> haive.core.engine.aug_llm.AugLLMConfig

      Get the AugLLMConfig engine with proper typing.

      This is a type-safe accessor that leverages the generic pattern.

      :returns: The AugLLMConfig engine.

      :raises ValueError: If engine is not set.


      .. autolink-examples:: get_aug_llm_config
         :collapse:


   .. py:method:: setup_agent() -> None

      Sync convenience fields to the AugLLMConfig engine.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: update_system_message(message: str) -> None

      Update system message on both agent and engine.

      :param message: New system message.


      .. autolink-examples:: update_system_message
         :collapse:


   .. py:method:: update_temperature(temperature: float) -> None

      Update temperature on both agent and engine.

      :param temperature: New temperature value (0.0-2.0).


      .. autolink-examples:: update_temperature
         :collapse:


   .. py:attribute:: max_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



   .. py:attribute:: tools
      :type:  list[Any]
      :value: None



.. py:function:: create_simple_agent(name: str = 'simple_agent', temperature: float = 0.7, max_tokens: int | None = None, system_message: str | None = None, tools: list[Any] | None = None, **kwargs) -> EnhancedSimpleAgent

   Create an enhanced SimpleAgent with common defaults.

   This factory function provides a convenient way to create SimpleAgents
   with sensible defaults.

   :param name: Agent name.
   :param temperature: LLM temperature (0.0-2.0).
   :param max_tokens: Maximum response tokens.
   :param system_message: System prompt.
   :param tools: List of tools.
   :param \*\*kwargs: Additional arguments passed to agent.

   :returns: Configured EnhancedSimpleAgent instance.

   .. rubric:: Example

   agent = create_simple_agent(
       name="helper",
       temperature=0.5,
       system_message="You are a helpful coding assistant"
   )


   .. autolink-examples:: create_simple_agent
      :collapse:

.. py:data:: SimpleAgent

.. py:data:: logger

