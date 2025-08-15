agents.routing_agent
====================

.. py:module:: agents.routing_agent


Attributes
----------

.. autoapisummary::

   agents.routing_agent.logger
   agents.routing_agent.main_engine


Classes
-------

.. autoapisummary::

   agents.routing_agent.RoutingAgent
   agents.routing_agent.RoutingAgentConfig
   agents.routing_agent.RoutingAgentSchema


Functions
---------

.. autoapisummary::

   agents.routing_agent.create_routing_agent


Module Contents
---------------

.. py:class:: RoutingAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Simple agent with conditional routing capabilities.


   .. autolink-examples:: RoutingAgent
      :collapse:

   .. py:method:: setup_workflow() -> None

      Set up the workflow with routing.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:class:: RoutingAgentConfig

   Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`


   Configuration for a routing agent.


   .. autolink-examples:: RoutingAgentConfig
      :collapse:

   .. py:attribute:: conditions
      :type:  dict[str, list[collections.abc.Callable]]
      :value: None



   .. py:attribute:: default_routes
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: handlers
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig | collections.abc.Callable]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:class:: RoutingAgentSchema

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgentSchema`


   Schema for routing agents.


   .. autolink-examples:: RoutingAgentSchema
      :collapse:

   .. py:attribute:: current_node
      :type:  str
      :value: None



   .. py:attribute:: route_history
      :type:  list[str]
      :value: None



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

.. py:data:: logger

.. py:data:: main_engine

