
:py:mod:`agents.reasoning_and_critique.lats.agent`
==================================================

.. py:module:: agents.reasoning_and_critique.lats.agent


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.agent.LATSAgent
   agents.reasoning_and_critique.lats.agent.LATSAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LATSAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LATSAgent {
        node [shape=record];
        "LATSAgent" [label="LATSAgent"];
        "haive.core.engine.agent.agent.Agent[LATSAgentConfig]" -> "LATSAgent";
      }

.. autoclass:: agents.reasoning_and_critique.lats.agent.LATSAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LATSAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_LATSAgentConfig {
        node [shape=record];
        "LATSAgentConfig" [label="LATSAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "LATSAgentConfig";
      }

.. autoclass:: agents.reasoning_and_critique.lats.agent.LATSAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.lats.agent.create_lats_agent

.. py:function:: create_lats_agent(system_prompt: str | None = None, tools: list[Any] | None = None, model: str = 'gpt-4o', temperature: float = 0.7, candidates_per_expansion: int = 5, max_tree_height: int = 5, name: str | None = None, **kwargs) -> LATSAgent

   Create a LATS agent with the specified configuration.

   :param system_prompt: Optional system prompt for generation
   :param tools: Optional tools to use
   :param model: Model to use
   :param temperature: Temperature for generation
   :param candidates_per_expansion: Number of candidates per expansion
   :param max_tree_height: Maximum tree height
   :param name: Optional agent name
   :param \*\*kwargs: Additional configuration parameters

   :returns: LATSAgent instance


   .. autolink-examples:: create_lats_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.lats.agent
   :collapse:
   
.. autolink-skip:: next
