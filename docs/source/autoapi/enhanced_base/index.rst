
:py:mod:`enhanced_base`
=======================

.. py:module:: enhanced_base

Enhanced Multi-Agent Base for flexible agent orchestration.

from typing import Any, Dict
This module provides an improved multi-agent base that leverages the advanced
conditional edges functionality from base_graph2.py while keeping the API simple
and similar to how it works in simple agents.

The MultiAgentBase class enables sophisticated agent orchestration patterns including:

- **Sequential Execution**: Simple chain of agents in order
- **Conditional Branching**: Dynamic routing based on state conditions
- **Plan-Execute-Replan**: Complex workflows with feedback loops
- **Parallel Schema Composition**: Isolated namespaces for agent fields

The system uses Pydantic fields for configuration and supports both simple
edge definitions and complex conditional routing with proper error handling
and state management.

.. rubric:: Example

Sequential multi-agent system::

    agents = [planner, executor, validator]
    multi_agent = MultiAgentBase(
        agents=agents,
        name="sequential_pipeline"
    )

Conditional branching system::

    def route_condition(state) -> str:
        return "success" if state.validation_passed else "retry"

    multi_agent = MultiAgentBase(
        agents=[processor, validator, retrier],
        branches=[
            (validator, route_condition, {
                "success": "END",
                "retry": retrier
            })
        ]
    )

.. seealso::

   :class:`haive.agents.planning.plan_and_execute.PlanAndExecuteAgent`: Complete Plan and Execute implementation
   :class:`haive.core.graph.state_graph.base_graph2.BaseGraph`: Underlying graph implementation


.. autolink-examples:: enhanced_base
   :collapse:

Classes
-------

.. autoapisummary::

   enhanced_base.AgentList
   enhanced_base.MultiAgentBase


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentList:

   .. graphviz::
      :align: center

      digraph inheritance_AgentList {
        node [shape=record];
        "AgentList" [label="AgentList"];
        "list" -> "AgentList";
      }

.. autoclass:: enhanced_base.AgentList
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgentBase:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentBase {
        node [shape=record];
        "MultiAgentBase" [label="MultiAgentBase"];
        "haive.agents.base.agent.Agent" -> "MultiAgentBase";
      }

.. autoclass:: enhanced_base.MultiAgentBase
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   enhanced_base.create_branching_multi_agent
   enhanced_base.create_plan_execute_multi_agent
   enhanced_base.create_sequential_multi_agent

.. py:function:: create_branching_multi_agent(agents: list[haive.agents.base.agent.Agent], branches: list[tuple], name: str = 'Branching Multi-Agent', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> MultiAgentBase

   Create a multi-agent system with conditional branching.

   This convenience function creates a MultiAgentBase configured for conditional
   execution with branching logic. The system uses SEQUENCE schema build mode
   by default for unified state management.

   :param agents: List of agents involved in the branching system
   :param branches: List of branch tuples defining conditional routing
   :param name: Name for the multi-agent system
   :param state_schema: Optional state schema override
   :param \*\*kwargs: Additional configuration options for MultiAgentBase

   :returns: Configured branching multi-agent system
   :rtype: MultiAgentBase

   .. rubric:: Example

   Create a system with conditional routing::

       def route_condition(state):
           return "success" if state.is_valid else "retry"

       branches = [
           (validator, route_condition, {
               "success": "END",
               "retry": processor
           })
       ]

       system = create_branching_multi_agent(
           agents=[processor, validator],
           branches=branches,
           name="validation_system"
       )


   .. autolink-examples:: create_branching_multi_agent
      :collapse:

.. py:function:: create_plan_execute_multi_agent(planner_agent: haive.agents.base.agent.Agent, executor_agent: haive.agents.base.agent.Agent, replanner_agent: haive.agents.base.agent.Agent, name: str = 'Plan and Execute System', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, schema_build_mode: haive.core.schema.agent_schema_composer.BuildMode = BuildMode.PARALLEL, **kwargs) -> MultiAgentBase

   Create a Plan and Execute multi-agent system with proper routing.


   .. autolink-examples:: create_plan_execute_multi_agent
      :collapse:

.. py:function:: create_sequential_multi_agent(agents: list[haive.agents.base.agent.Agent], name: str = 'Sequential Multi-Agent', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> MultiAgentBase

   Create a simple sequential multi-agent system.

   This convenience function creates a MultiAgentBase configured for sequential
   execution where agents run in the order provided. The system uses SEQUENCE
   schema build mode for unified state management.

   :param agents: List of agents to execute in sequence
   :param name: Name for the multi-agent system
   :param state_schema: Optional state schema override
   :param \*\*kwargs: Additional configuration options for MultiAgentBase

   :returns: Configured sequential multi-agent system
   :rtype: MultiAgentBase

   .. rubric:: Example

   Create a simple pipeline::

       agents = [preprocessor, analyzer, summarizer]
       pipeline = create_sequential_multi_agent(
           agents=agents,
           name="analysis_pipeline"
       )


   .. autolink-examples:: create_sequential_multi_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: enhanced_base
   :collapse:
   
.. autolink-skip:: next
