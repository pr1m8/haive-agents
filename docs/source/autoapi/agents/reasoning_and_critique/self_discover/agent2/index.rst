
:py:mod:`agents.reasoning_and_critique.self_discover.agent2`
============================================================

.. py:module:: agents.reasoning_and_critique.self_discover.agent2


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.agent2.SelfDiscoverAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfDiscoverAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelfDiscoverAgent {
        node [shape=record];
        "SelfDiscoverAgent" [label="SelfDiscoverAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.reasoning_and_critique.self_discover.config.SelfDiscoverAgentConfig]" -> "SelfDiscoverAgent";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.agent2.SelfDiscoverAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.agent2.create_self_discover_agent

.. py:function:: create_self_discover_agent(model: str = 'gpt-4o', temperature: float = 0.0, name: str | None = None, reasoning_modules: list[str] | None = None, select_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, adapt_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, structure_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, reasoning_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, visualize: bool = True, **kwargs) -> SelfDiscoverAgent

   Create a SelfDiscover agent with customizable parameters.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param name: Optional name for the agent
   :param reasoning_modules: List of reasoning modules to use
   :param select_prompt: Custom prompt for the selection stage
   :param adapt_prompt: Custom prompt for the adaptation stage
   :param structure_prompt: Custom prompt for the structure stage
   :param reasoning_prompt: Custom prompt for the reasoning stage
   :param visualize: Whether to visualize the graph
   :param \*\*kwargs: Additional configuration parameters

   :returns: SelfDiscoverAgent instance


   .. autolink-examples:: create_self_discover_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.agent2
   :collapse:
   
.. autolink-skip:: next
