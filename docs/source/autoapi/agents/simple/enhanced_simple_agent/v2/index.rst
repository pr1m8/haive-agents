
:py:mod:`agents.simple.enhanced_simple_agent.v2`
================================================

.. py:module:: agents.simple.enhanced_simple_agent.v2

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

Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_agent.v2.EnhancedSimpleAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedSimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedSimpleAgent {
        node [shape=record];
        "EnhancedSimpleAgent" [label="EnhancedSimpleAgent"];
        "haive.agents.base.agent.Agent[haive.core.engine.aug_llm.AugLLMConfig]" -> "EnhancedSimpleAgent";
      }

.. autoclass:: agents.simple.enhanced_simple_agent.v2.EnhancedSimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.simple.enhanced_simple_agent.v2.create_simple_agent

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



.. rubric:: Related Links

.. autolink-examples:: agents.simple.enhanced_simple_agent.v2
   :collapse:
   
.. autolink-skip:: next
