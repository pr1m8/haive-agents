
:py:mod:`configurable_base`
===========================

.. py:module:: configurable_base

Configurable Multi-Agent Base for flexible agent orchestration.

This module provides a general multi-agent base where you can:
- Pass agents
- Define branches/routing between agents
- Override state schema
- Configure schema composition methods


.. autolink-examples:: configurable_base
   :collapse:

Classes
-------

.. autoapisummary::

   configurable_base.AgentBranch
   configurable_base.ConfigurableMultiAgent
   configurable_base.WorkflowStep


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentBranch:

   .. graphviz::
      :align: center

      digraph inheritance_AgentBranch {
        node [shape=record];
        "AgentBranch" [label="AgentBranch"];
      }

.. autoclass:: configurable_base.AgentBranch
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableMultiAgent {
        node [shape=record];
        "ConfigurableMultiAgent" [label="ConfigurableMultiAgent"];
        "haive.agents.base.agent.Agent" -> "ConfigurableMultiAgent";
      }

.. autoclass:: configurable_base.ConfigurableMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WorkflowStep:

   .. graphviz::
      :align: center

      digraph inheritance_WorkflowStep {
        node [shape=record];
        "WorkflowStep" [label="WorkflowStep"];
      }

.. autoclass:: configurable_base.WorkflowStep
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   configurable_base.create_branching_multi_agent
   configurable_base.create_sequential_multi_agent
   configurable_base.create_workflow_multi_agent

.. py:function:: create_branching_multi_agent(agents: list[haive.agents.base.agent.Agent], branches: list[AgentBranch], name: str = 'BranchingMultiAgent', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> ConfigurableMultiAgent

   Create a multi-agent system with conditional branches.


   .. autolink-examples:: create_branching_multi_agent
      :collapse:

.. py:function:: create_sequential_multi_agent(agents: list[haive.agents.base.agent.Agent], name: str = 'SequentialMultiAgent', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> ConfigurableMultiAgent

   Create a sequential multi-agent system.


   .. autolink-examples:: create_sequential_multi_agent
      :collapse:

.. py:function:: create_workflow_multi_agent(agents: list[haive.agents.base.agent.Agent], workflow_steps: list[WorkflowStep], name: str = 'WorkflowMultiAgent', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> ConfigurableMultiAgent

   Create a multi-agent system with workflow steps.


   .. autolink-examples:: create_workflow_multi_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: configurable_base
   :collapse:
   
.. autolink-skip:: next
