
:py:mod:`agents.chain_agent`
============================

.. py:module:: agents.chain_agent


Classes
-------

.. autoapisummary::

   agents.chain_agent.ChainAgent
   agents.chain_agent.ChainAgentConfig
   agents.chain_agent.ChainAgentSchema


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ChainAgent {
        node [shape=record];
        "ChainAgent" [label="ChainAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "ChainAgent";
      }

.. autoclass:: agents.chain_agent.ChainAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ChainAgentConfig {
        node [shape=record];
        "ChainAgentConfig" [label="ChainAgentConfig"];
        "haive.agents.simple.config.SimpleAgentConfig" -> "ChainAgentConfig";
      }

.. autoclass:: agents.chain_agent.ChainAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainAgentSchema:

   .. graphviz::
      :align: center

      digraph inheritance_ChainAgentSchema {
        node [shape=record];
        "ChainAgentSchema" [label="ChainAgentSchema"];
        "haive.agents.simple.state.SimpleAgentState" -> "ChainAgentSchema";
      }

.. autoclass:: agents.chain_agent.ChainAgentSchema
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.chain_agent.create_chain_agent

.. py:function:: create_chain_agent(engines: list[haive.core.engine.aug_llm.AugLLMConfig], name: str | None = None, system_prompt: str | None = None, step_names: list[str] | None = None, visualize: bool = True, **kwargs) -> ChainAgent

   Create a chain agent from a list of engines.

   :param engines: List of AugLLMConfig engines to chain together
   :param name: Optional name for the agent
   :param system_prompt: Optional system prompt
   :param step_names: Optional names for each step
   :param visualize: Whether to generate a visualization
   :param \*\*kwargs: Additional configuration parameters

   :returns: ChainAgent instance


   .. autolink-examples:: create_chain_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.chain_agent
   :collapse:
   
.. autolink-skip:: next
