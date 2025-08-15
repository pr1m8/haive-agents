routing_patterns
================

.. py:module:: routing_patterns

.. autoapi-nested-parse::

   Routing patterns for multi-agent systems.

   from typing import Any
   Experiments with conditional routing, branching, and dynamic paths.
   Uses BaseGraph's add_conditional_edges for sophisticated routing.


   .. autolink-examples:: routing_patterns
      :collapse:


Attributes
----------

.. autoapisummary::

   routing_patterns.logger


Classes
-------

.. autoapisummary::

   routing_patterns.BranchingMultiAgent
   routing_patterns.RoutingMultiAgent


Functions
---------

.. autoapisummary::

   routing_patterns.category_router
   routing_patterns.confidence_router
   routing_patterns.error_router
   routing_patterns.has_tool_calls_router


Module Contents
---------------

.. py:class:: BranchingMultiAgent

   Bases: :py:obj:`RoutingMultiAgent`


   Multi-agent with branching and merging capabilities.

   Supports parallel branches that merge back together.

   .. rubric:: Example

   .. code-block:: python

       multi = BranchingMultiAgent("branching")

       # Main path
       multi.append(InputProcessor())

       # Branch based on input type
       multi.branch_on(
       "InputProcessor",
       lambda s: s.get("input_type"),
       branches={
       "text": [TextAnalyzer(), TextSummarizer()],
       "image": [ImageAnalyzer(), ImageCaptioner()],
       "audio": [AudioTranscriber(), AudioAnalyzer()]
       },
       merge_to=OutputFormatter()
       )


   .. autolink-examples:: BranchingMultiAgent
      :collapse:

   .. py:method:: branch_on(source: str | haive.agents.base.agent.Agent, condition: collections.abc.Callable[[Any], str], branches: dict[str, list[haive.agents.base.agent.Agent]], merge_to: haive.agents.base.agent.Agent | None = None) -> BranchingMultiAgent

      Create branching paths that merge back.

      :param source: Agent to branch from
      :param condition: Function returning branch key
      :param branches: Map of keys to agent sequences
      :param merge_to: Agent where branches merge (optional)


      .. autolink-examples:: branch_on
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with branching support.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: branches
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: merge_points
      :type:  dict[str, str]
      :value: None



.. py:class:: RoutingMultiAgent

   Bases: :py:obj:`haive.agents.multi.experiments.list_multi_agent.ListMultiAgent`


   Multi-agent with conditional routing capabilities.

   Extends ListMultiAgent with routing rules that determine
   which agent executes next based on state conditions.

   .. rubric:: Example

   .. code-block:: python

       multi = RoutingMultiAgent("router")

       # Add agents
       multi.append(ClassifierAgent())
       multi.append(TechnicalAgent())
       multi.append(BusinessAgent())
       multi.append(GeneralAgent())

       # Add routing from classifier
       multi.add_route(
       source="ClassifierAgent",
       condition=lambda state: state.get("category", "general"),
       routes={
       "technical": "TechnicalAgent",
       "business": "BusinessAgent",
       "general": "GeneralAgent"
       }
       )


   .. autolink-examples:: RoutingMultiAgent
      :collapse:

   .. py:method:: add_boolean_route(source: str | haive.agents.base.agent.Agent, condition: collections.abc.Callable[[Any], bool], true_dest: str | haive.agents.base.agent.Agent, false_dest: str | haive.agents.base.agent.Agent = END) -> RoutingMultiAgent

      Add simple boolean routing.

      :param source: Source agent
      :param condition: Boolean condition function
      :param true_dest: Destination when condition is True
      :param false_dest: Destination when condition is False (default: END)


      .. autolink-examples:: add_boolean_route
         :collapse:


   .. py:method:: add_multi_route(source: str | haive.agents.base.agent.Agent, condition: collections.abc.Callable[[Any], str], **routes: str | haive.agents.base.agent.Agent) -> RoutingMultiAgent

      Add multi-way routing with keyword arguments.

      .. rubric:: Example

      multi.add_multi_route(
          "classifier",
          lambda s: s["category"],
          technical="tech_agent",
          business="biz_agent",
          creative="creative_agent"
      )


      .. autolink-examples:: add_multi_route
         :collapse:


   .. py:method:: add_route(source: str | haive.agents.base.agent.Agent, condition: collections.abc.Callable[[Any], str | bool], routes: dict[str | bool, str | haive.agents.base.agent.Agent], default: str | None = None) -> RoutingMultiAgent

      Add routing rule for an agent.

      :param source: Source agent (name or instance)
      :param condition: Function that returns route key based on state
      :param routes: Map of condition results to destination agents
      :param default: Default route if no match (uses self.default_route if None)


      .. autolink-examples:: add_route
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with conditional routing.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: default_route
      :type:  str
      :value: None



   .. py:attribute:: routing_rules
      :type:  dict[str, dict[str, Any]]
      :value: None



.. py:function:: category_router(state: dict[str, Any]) -> str

   Route based on category field.


   .. autolink-examples:: category_router
      :collapse:

.. py:function:: confidence_router(state: dict[str, Any]) -> str

   Route based on confidence level.


   .. autolink-examples:: confidence_router
      :collapse:

.. py:function:: error_router(state: dict[str, Any]) -> str

   Route based on error presence.


   .. autolink-examples:: error_router
      :collapse:

.. py:function:: has_tool_calls_router(state: dict[str, Any]) -> bool

   Check if there are tool calls in the last message.


   .. autolink-examples:: has_tool_calls_router
      :collapse:

.. py:data:: logger

