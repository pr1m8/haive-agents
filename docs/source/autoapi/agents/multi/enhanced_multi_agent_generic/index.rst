agents.multi.enhanced_multi_agent_generic
=========================================

.. py:module:: agents.multi.enhanced_multi_agent_generic

.. autoapi-nested-parse::

   Enhanced MultiAgent with proper generics for contained agents.

   MultiAgent[AgentsT] where AgentsT represents the agents it contains.


   .. autolink-examples:: agents.multi.enhanced_multi_agent_generic
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.multi.enhanced_multi_agent_generic.Agent
   agents.multi.enhanced_multi_agent_generic.AgentsT
   agents.multi.enhanced_multi_agent_generic.logger


Classes
-------

.. autoapisummary::

   agents.multi.enhanced_multi_agent_generic.AdaptiveBranchingMultiAgent
   agents.multi.enhanced_multi_agent_generic.BranchingMultiAgent
   agents.multi.enhanced_multi_agent_generic.ConditionalMultiAgent
   agents.multi.enhanced_multi_agent_generic.MultiAgent
   agents.multi.enhanced_multi_agent_generic.ReportTeamAgents


Module Contents
---------------

.. py:class:: AdaptiveBranchingMultiAgent

   Bases: :py:obj:`BranchingMultiAgent`


   Branching MultiAgent that adapts routing based on performance.

   Tracks agent performance and adjusts routing probabilities.


   .. autolink-examples:: AdaptiveBranchingMultiAgent
      :collapse:

   .. py:method:: get_best_agent_for_task(task_type: str) -> str

      Get best performing agent for task type.


      .. autolink-examples:: get_best_agent_for_task
         :collapse:


   .. py:method:: update_performance(agent_name: str, success: bool, duration: float) -> None

      Update agent performance metrics.


      .. autolink-examples:: update_performance
         :collapse:


   .. py:attribute:: adaptation_rate
      :type:  float
      :value: None



   .. py:attribute:: agent_performance
      :type:  dict[str, dict[str, float]]
      :value: None



.. py:class:: BranchingMultiAgent

   Bases: :py:obj:`MultiAgent`\ [\ :py:obj:`dict`\ [\ :py:obj:`str`\ , :py:obj:`Agent`\ ]\ ]


   MultiAgent specialized for branching execution.

   Routes to different agents based on conditions.


   .. autolink-examples:: BranchingMultiAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build branching execution graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: mode
      :type:  Literal['branch']
      :value: None



.. py:class:: ConditionalMultiAgent

   Bases: :py:obj:`MultiAgent`\ [\ :py:obj:`dict`\ [\ :py:obj:`str`\ , :py:obj:`Agent`\ ]\ ]


   MultiAgent with conditional execution based on previous results.

   Executes agents conditionally based on outputs.


   .. autolink-examples:: ConditionalMultiAgent
      :collapse:

   .. py:method:: _evaluate_condition(condition: str, state: dict[str, Any]) -> bool

      Evaluate a condition against state.


      .. autolink-examples:: _evaluate_condition
         :collapse:


   .. py:method:: should_continue(state: dict[str, Any], current_agent: str) -> str | None

      Determine next agent based on conditions.


      .. autolink-examples:: should_continue
         :collapse:


   .. py:attribute:: condition_rules
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: mode
      :type:  Literal['conditional']
      :value: None



.. py:class:: MultiAgent

   Bases: :py:obj:`Agent`, :py:obj:`Generic`\ [\ :py:obj:`AgentsT`\ ]


   Enhanced MultiAgent generic on the agents it contains.

   MultiAgent[AgentsT] = Agent[AugLLMConfig] + agents: AgentsT

   This properly represents that MultiAgent is:
   1. An agent itself (uses AugLLMConfig for coordination)
   2. Generic on the agents it contains

   .. rubric:: Examples

   With typed dict of agents::

       agents: Dict[str, Agent] = {
           "planner": PlannerAgent(...),
           "executor": ExecutorAgent(...)
       }
       multi: MultiAgent[Dict[str, Agent]] = MultiAgent(
           name="coordinator",
           agents=agents
       )

   With list of agents::

       agent_list: List[ReactAgent] = [agent1, agent2, agent3]
       multi: MultiAgent[List[ReactAgent]] = MultiAgent(
           name="ensemble",
           agents=agent_list
       )

   With specific agent types::

       from typing import TypedDict

       class MyAgents(TypedDict):
           researcher: RAGAgent
           analyzer: ReactAgent
           writer: SimpleAgent

       agents = MyAgents(
           researcher=rag_agent,
           analyzer=react_agent,
           writer=simple_agent
       )

       multi: MultiAgent[MyAgents] = MultiAgent(
           name="report_team",
           agents=agents
       )


   .. autolink-examples:: MultiAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: get_agent(name: str) -> Agent | None

      Get agent by name.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: get_agent_names() -> list[str]

      Get list of agent names.


      .. autolink-examples:: get_agent_names
         :collapse:


   .. py:method:: validate_agents(v: AgentsT) -> AgentsT
      :classmethod:


      Validate agents based on type.


      .. autolink-examples:: validate_agents
         :collapse:


   .. py:attribute:: agents
      :type:  AgentsT
      :value: None



   .. py:attribute:: branch_condition
      :type:  Any | None
      :value: None



   .. py:attribute:: branch_map
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: mode
      :type:  Literal['sequential', 'parallel', 'conditional', 'branch']
      :value: None



.. py:class:: ReportTeamAgents

   Bases: :py:obj:`TypedDict`


   Typed dict for report team agents.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReportTeamAgents
      :collapse:

   .. py:attribute:: analyst
      :type:  Agent


   .. py:attribute:: researcher
      :type:  Agent


   .. py:attribute:: writer
      :type:  Agent


.. py:data:: Agent

.. py:data:: AgentsT

.. py:data:: logger

