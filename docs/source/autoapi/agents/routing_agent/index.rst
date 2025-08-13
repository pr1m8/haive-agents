
:py:mod:`agents.routing_agent`
==============================

.. py:module:: agents.routing_agent


Classes
-------

.. autoapisummary::

   agents.routing_agent.RoutingAgent
   agents.routing_agent.RoutingAgentConfig
   agents.routing_agent.RoutingAgentSchema


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoutingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingAgent {
        node [shape=record];
        "RoutingAgent" [label="RoutingAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "RoutingAgent";
      }

.. autoclass:: agents.routing_agent.RoutingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoutingAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingAgentConfig {
        node [shape=record];
        "RoutingAgentConfig" [label="RoutingAgentConfig"];
        "haive.agents.simple.config.SimpleAgentConfig" -> "RoutingAgentConfig";
      }

.. autoclass:: agents.routing_agent.RoutingAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoutingAgentSchema:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingAgentSchema {
        node [shape=record];
        "RoutingAgentSchema" [label="RoutingAgentSchema"];
        "haive.agents.simple.agent.SimpleAgentSchema" -> "RoutingAgentSchema";
      }

.. autoclass:: agents.routing_agent.RoutingAgentSchema
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.routing_agent.create_routing_agent

.. py:function:: create_routing_agent(main_engine: haive.core.engine.aug_llm.AugLLMConfig, handlers: dict[str, haive.core.engine.aug_llm.AugLLMConfig | collections.abc.Callable], conditions: dict[str, list[collections.abc.Callable]], default_routes: dict[str, str], system_prompt: str = 'You are a helpful assistant.', name: str | None = None) -> RoutingAgent

   Create a routing agent with the specified components.

   :param main_engine: Main LLM engine
   :param handlers: Dictionary of handler nodes
   :param conditions: Routing conditions by source node
   :param default_routes: Default routes by source node
   :param system_prompt: System prompt for the agent
   :param name: Optional name for the agent

   :returns: RoutingAgent instance


   .. autolink-examples:: create_routing_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.routing_agent
   :collapse:
   
.. autolink-skip:: next
