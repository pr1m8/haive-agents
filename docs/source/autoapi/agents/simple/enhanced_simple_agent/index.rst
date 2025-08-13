
:py:mod:`agents.simple.enhanced_simple_agent`
=============================================

.. py:module:: agents.simple.enhanced_simple_agent

Enhanced SimpleAgent with engine-focused generics.

This implements SimpleAgent using the enhanced agent pattern with engine generics.
SimpleAgent becomes essentially Agent[AugLLMConfig] as requested.


.. autolink-examples:: agents.simple.enhanced_simple_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_agent.EnhancedSimpleAgent


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

.. autoclass:: agents.simple.enhanced_simple_agent.EnhancedSimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.simple.enhanced_simple_agent.create_simple_agent

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

.. autolink-examples:: agents.simple.enhanced_simple_agent
   :collapse:
   
.. autolink-skip:: next
