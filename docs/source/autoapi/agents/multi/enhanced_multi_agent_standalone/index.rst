agents.multi.enhanced_multi_agent_standalone
============================================

.. py:module:: agents.multi.enhanced_multi_agent_standalone

.. autoapi-nested-parse::

   Standalone Enhanced MultiAgent Implementation - Fully Working.

   This is a complete, working implementation of the enhanced multi-agent pattern
   that avoids import issues and demonstrates all the core concepts:

   - MultiAgent[AgentsT] - Generic on the agents it contains
   - Sequential, Parallel, Branching, Conditional, Adaptive patterns
   - Real async execution with debug output
   - Type safety through generics
   - No problematic imports

   Key Insight: MultiAgent is generic on its agents, not just engine!
   MultiAgent[AgentsT] = Agent[AugLLMConfig] + agents: AgentsT


   .. autolink-examples:: agents.multi.enhanced_multi_agent_standalone
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.multi.enhanced_multi_agent_standalone.AgentsT
   agents.multi.enhanced_multi_agent_standalone.logger


Classes
-------

.. autoapisummary::

   agents.multi.enhanced_multi_agent_standalone.AdaptiveBranchingMultiAgent
   agents.multi.enhanced_multi_agent_standalone.Agent
   agents.multi.enhanced_multi_agent_standalone.BranchingMultiAgent
   agents.multi.enhanced_multi_agent_standalone.MinimalEngine
   agents.multi.enhanced_multi_agent_standalone.MultiAgent
   agents.multi.enhanced_multi_agent_standalone.SimpleAgent


Functions
---------

.. autoapisummary::

   agents.multi.enhanced_multi_agent_standalone.demo_enhanced_multi_agent


Module Contents
---------------

.. py:class:: AdaptiveBranchingMultiAgent(name: str, agents: dict[str, Agent], **kwargs)

   Bases: :py:obj:`BranchingMultiAgent`


   Branching MultiAgent that adapts routing based on performance.


   .. autolink-examples:: AdaptiveBranchingMultiAgent
      :collapse:

   .. py:method:: _execute_branching(input_data: str, debug: bool = False) -> str
      :async:


      Execute with adaptive agent selection.


      .. autolink-examples:: _execute_branching
         :collapse:


   .. py:method:: get_best_agent_for_task(task_type: str = 'general') -> str

      Get best performing agent.


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



.. py:class:: Agent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`abc.ABC`


   Enhanced Agent base class - Agent[EngineT] pattern.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Agent
      :collapse:

   .. py:method:: arun(input_data: str, debug: bool = False) -> str
      :abstractmethod:

      :async:


      Async execution method.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: run(input_data: str, debug: bool = False) -> str

      Sync execution method.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: engine
      :type:  Any
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: BranchingMultiAgent(name: str, agents: dict[str, Agent], **kwargs)

   Bases: :py:obj:`MultiAgent`\ [\ :py:obj:`dict`\ [\ :py:obj:`str`\ , :py:obj:`Agent`\ ]\ ]


   MultiAgent specialized for branching execution.


   .. autolink-examples:: BranchingMultiAgent
      :collapse:

   .. py:attribute:: mode
      :type:  Literal['branch']
      :value: None



.. py:class:: MinimalEngine(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Minimal engine for demonstration.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MinimalEngine
      :collapse:

   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



.. py:class:: MultiAgent(/, **data: Any)

   Bases: :py:obj:`Agent`, :py:obj:`Generic`\ [\ :py:obj:`AgentsT`\ ]


   Enhanced MultiAgent generic on the agents it contains.

   MultiAgent[AgentsT] = Agent[AugLLMConfig] + agents: AgentsT

   This properly represents that MultiAgent is:
   1. An agent itself (uses engine for coordination)
   2. Generic on the agents it contains

   .. rubric:: Examples

   Sequential pipeline::

       agents = [planner, executor, reviewer]
       multi: MultiAgent[List[SimpleAgent]] = MultiAgent(
           name="pipeline",
           agents=agents,
           mode="sequential"
       )

   Branching router::

       agents = {"technical": tech_agent, "business": biz_agent}
       multi: MultiAgent[Dict[str, SimpleAgent]] = MultiAgent(
           name="router",
           agents=agents,
           mode="branch"
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MultiAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _execute_branching(input_data: str, debug: bool = False) -> str
      :async:


      Execute with intelligent routing.


      .. autolink-examples:: _execute_branching
         :collapse:


   .. py:method:: _execute_conditional(input_data: str, debug: bool = False) -> str
      :async:


      Execute with conditional flow.


      .. autolink-examples:: _execute_conditional
         :collapse:


   .. py:method:: _execute_parallel(input_data: str, debug: bool = False) -> str
      :async:


      Execute all agents in parallel.


      .. autolink-examples:: _execute_parallel
         :collapse:


   .. py:method:: _execute_sequential(input_data: str, debug: bool = False) -> str
      :async:


      Execute agents in sequence.


      .. autolink-examples:: _execute_sequential
         :collapse:


   .. py:method:: _route_request(input_data: str) -> str

      Route request to appropriate agent based on content.


      .. autolink-examples:: _route_request
         :collapse:


   .. py:method:: arun(input_data: str, debug: bool = False) -> str
      :async:


      Execute based on mode.


      .. autolink-examples:: arun
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



   .. py:attribute:: branch_map
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: mode
      :type:  Literal['sequential', 'parallel', 'conditional', 'branch']
      :value: None



.. py:class:: SimpleAgent(/, **data: Any)

   Bases: :py:obj:`Agent`


   SimpleAgent = Agent[AugLLMConfig] - minimal working implementation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SimpleAgent
      :collapse:

   .. py:method:: arun(input_data: str, debug: bool = False) -> str
      :async:


      Async run with realistic simulation.


      .. autolink-examples:: arun
         :collapse:


.. py:function:: demo_enhanced_multi_agent()
   :async:


   Demonstrate all enhanced multi-agent patterns.


   .. autolink-examples:: demo_enhanced_multi_agent
      :collapse:

.. py:data:: AgentsT

.. py:data:: logger

