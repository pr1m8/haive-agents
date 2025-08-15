configurable_base
=================

.. py:module:: configurable_base

.. autoapi-nested-parse::

   Configurable Multi-Agent Base for flexible agent orchestration.

   This module provides a general multi-agent base where you can:
   - Pass agents
   - Define branches/routing between agents
   - Override state schema
   - Configure schema composition methods


   .. autolink-examples:: configurable_base
      :collapse:


Attributes
----------

.. autoapisummary::

   configurable_base.logger


Classes
-------

.. autoapisummary::

   configurable_base.AgentBranch
   configurable_base.ConfigurableMultiAgent
   configurable_base.WorkflowStep


Functions
---------

.. autoapisummary::

   configurable_base.create_branching_multi_agent
   configurable_base.create_sequential_multi_agent
   configurable_base.create_workflow_multi_agent


Module Contents
---------------

.. py:class:: AgentBranch(from_agent: str | haive.agents.base.agent.Agent, condition: collections.abc.Callable[[Any], str], destinations: dict[str, str | haive.agents.base.agent.Agent], default: str | haive.agents.base.agent.Agent | None = None)

   Represents a branch/routing between agents.

   Initialize agent branch.

   :param from_agent: Source agent (name or Agent object)
   :param condition: Function that returns routing key based on state
   :param destinations: Mapping of condition results to target agents
   :param default: Default destination if condition doesn't match


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentBranch
      :collapse:

   .. py:attribute:: condition


   .. py:attribute:: default
      :value: None



   .. py:attribute:: destinations


   .. py:attribute:: from_agent


.. py:class:: ConfigurableMultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Configurable multi-agent base that accepts agents and routing configuration.

   This base class allows you to:
   - Pass a list of agents
   - Define branches/routing between agents
   - Add workflow steps between agents
   - Override state schema or use composition
   - Configure schema composition methods


   .. autolink-examples:: ConfigurableMultiAgent
      :collapse:

   .. py:method:: _add_default_sequential_flow(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add default sequential flow if no branches/steps defined.


      .. autolink-examples:: _add_default_sequential_flow
         :collapse:


   .. py:method:: _get_agent_node_name(agent: str | haive.agents.base.agent.Agent) -> str

      Get the node name for an agent.


      .. autolink-examples:: _get_agent_node_name
         :collapse:


   .. py:method:: _get_unique_node_name(base_name: str) -> str

      Ensure unique node names.


      .. autolink-examples:: _get_unique_node_name
         :collapse:


   .. py:method:: _normalize_destination(dest: str | haive.agents.base.agent.Agent) -> str

      Normalize destination to node name.


      .. autolink-examples:: _normalize_destination
         :collapse:


   .. py:method:: add_branch(from_agent: str | haive.agents.base.agent.Agent, condition: collections.abc.Callable[[Any], str], destinations: dict[str, str | haive.agents.base.agent.Agent], default: str | haive.agents.base.agent.Agent | None = None) -> None

      Add a branch/routing between agents.


      .. autolink-examples:: add_branch
         :collapse:


   .. py:method:: add_workflow_step(name: str, function: collections.abc.Callable, inputs: list[str | haive.agents.base.agent.Agent] | None = None, outputs: list[str | haive.agents.base.agent.Agent] | None = None) -> None

      Add a workflow step between agents.


      .. autolink-examples:: add_workflow_step
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the graph from agents, branches, and workflow steps.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up the agent - called by parent Agent class.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: setup_configurable_multi_agent() -> ConfigurableMultiAgent

      Set up the configurable multi-agent system.


      .. autolink-examples:: setup_configurable_multi_agent
         :collapse:


   .. py:attribute:: _agent_node_mapping
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: _workflow_node_mapping
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: branches
      :type:  list[AgentBranch]
      :value: None



   .. py:attribute:: end_condition
      :type:  collections.abc.Callable[[Any], bool] | None
      :value: None



   .. py:attribute:: include_meta
      :type:  bool
      :value: None



   .. py:attribute:: schema_composition_method
      :type:  str
      :value: None



   .. py:attribute:: start_agent
      :type:  str | haive.agents.base.agent.Agent | None
      :value: None



   .. py:attribute:: state_schema_override
      :type:  type[haive.core.schema.state_schema.StateSchema] | None
      :value: None



   .. py:attribute:: workflow_steps
      :type:  list[WorkflowStep]
      :value: None



.. py:class:: WorkflowStep(name: str, function: collections.abc.Callable, inputs: list[str | haive.agents.base.agent.Agent] | None = None, outputs: list[str | haive.agents.base.agent.Agent] | None = None)

   Represents a workflow step between agents.

   Initialize workflow step.

   :param name: Name of the workflow step
   :param function: Function to execute
   :param inputs: Agents/nodes that feed into this step
   :param outputs: Agents/nodes this step feeds into


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WorkflowStep
      :collapse:

   .. py:attribute:: function


   .. py:attribute:: inputs
      :value: []



   .. py:attribute:: name


   .. py:attribute:: outputs
      :value: []



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

.. py:data:: logger

