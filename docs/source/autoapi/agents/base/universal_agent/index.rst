agents.base.universal_agent
===========================

.. py:module:: agents.base.universal_agent

.. autoapi-nested-parse::

   Universal Agent - Simplified base class for all agent types.

   This module provides a simplified Agent base class that maintains familiar
   naming while providing clear type-based capabilities and proper separation
   of concerns through agent types rather than complex inheritance hierarchies.


   .. autolink-examples:: agents.base.universal_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.universal_agent.logger


Classes
-------

.. autoapisummary::

   agents.base.universal_agent.Agent


Functions
---------

.. autoapisummary::

   agents.base.universal_agent.get_agent_capabilities
   agents.base.universal_agent.is_orchestration_agent
   agents.base.universal_agent.is_processing_agent
   agents.base.universal_agent.is_reasoning_agent


Module Contents
---------------

.. py:class:: Agent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`abc.ABC`


   Universal base class for all agent types in the Haive framework.

   All components that can be executed as graphs are "Agents" but have
   different types that determine their capabilities:

   - REASONING: LLM-based agents that can reason and use tools
   - RETRIEVER: Agents that retrieve information from data sources
   - LOADER: Agents that load data from various sources
   - PROCESSOR: Agents that transform and process data
   - PIPELINE: Agents that chain processing operations
   - WORKFLOW: Agents that orchestrate multiple other agents
   - CHAIN: Agents that execute other agents sequentially

   The agent_type field determines what capabilities and methods are
   available to each agent instance.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Agent
      :collapse:

   .. py:method:: __getattr__(name: str) -> Any

      Route method calls based on agent capabilities.

      This allows agents to have type-specific methods that are only
      available when the agent type supports those capabilities.


      .. autolink-examples:: __getattr__
         :collapse:


   .. py:method:: __repr__() -> str

      Detailed string representation of the agent.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: __str__() -> str

      String representation of the agent.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: ainvoke(input_data: Any, config: dict[str, Any] | None = None) -> Any
      :async:


      Asynchronous invoke method.

      :param input_data: Input data for the agent
      :param config: Optional configuration for execution

      :returns: Agent execution result
      :rtype: Any


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph
      :abstractmethod:


      Build the graph representation for this agent.

      This method must be implemented by all agent subclasses to define
      how the agent should be represented as a graph structure.

      :returns: The graph representation of this agent
      :rtype: BaseGraph


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: can_orchestrate() -> bool

      Check if agent can orchestrate other agents.


      .. autolink-examples:: can_orchestrate
         :collapse:


   .. py:method:: can_process_batch() -> bool

      Check if agent supports batch processing.


      .. autolink-examples:: can_process_batch
         :collapse:


   .. py:method:: can_reason() -> bool

      Check if agent can perform reasoning operations.


      .. autolink-examples:: can_reason
         :collapse:


   .. py:method:: compile(**kwargs) -> langgraph.graph.graph.CompiledGraph

      Compile this agent to an executable LangGraph instance.

      :param \*\*kwargs: Additional compilation arguments

      :returns: Executable LangGraph instance
      :rtype: CompiledGraph


      .. autolink-examples:: compile
         :collapse:


   .. py:method:: get_capabilities() -> dict[str, bool]

      Get capabilities available to this agent.


      .. autolink-examples:: get_capabilities
         :collapse:


   .. py:method:: invoke(input_data: Any, config: dict[str, Any] | None = None) -> Any

      Invoke the agent with input data.

      :param input_data: Input data for the agent
      :param config: Optional configuration for execution

      :returns: Agent execution result
      :rtype: Any


      .. autolink-examples:: invoke
         :collapse:


   .. py:method:: is_orchestration_agent() -> bool

      Check if this agent orchestrates other agents.


      .. autolink-examples:: is_orchestration_agent
         :collapse:


   .. py:method:: is_processing_agent() -> bool

      Check if this agent is for deterministic processing.


      .. autolink-examples:: is_processing_agent
         :collapse:


   .. py:method:: is_reasoning_agent() -> bool

      Check if this agent has reasoning capabilities.


      .. autolink-examples:: is_reasoning_agent
         :collapse:


   .. py:attribute:: agent_type
      :type:  haive.core.engine.base.agent_types.AgentType
      :value: None



   .. py:attribute:: description
      :type:  str | None
      :value: None



   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel] | dict[str, Any] | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel] | dict[str, Any] | None
      :value: None



   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.state_schema.StateSchema] | type[pydantic.BaseModel] | dict[str, Any] | None
      :value: None



   .. py:attribute:: verbose
      :type:  bool
      :value: None



.. py:function:: get_agent_capabilities(agent_type: haive.core.engine.base.agent_types.AgentType) -> dict[str, bool]

   Get capabilities for agent type.


   .. autolink-examples:: get_agent_capabilities
      :collapse:

.. py:function:: is_orchestration_agent(agent_type: haive.core.engine.base.agent_types.AgentType) -> bool

   Check if agent type orchestrates other agents.


   .. autolink-examples:: is_orchestration_agent
      :collapse:

.. py:function:: is_processing_agent(agent_type: haive.core.engine.base.agent_types.AgentType) -> bool

   Check if agent type is for deterministic processing.


   .. autolink-examples:: is_processing_agent
      :collapse:

.. py:function:: is_reasoning_agent(agent_type: haive.core.engine.base.agent_types.AgentType) -> bool

   Check if agent type has reasoning capabilities.


   .. autolink-examples:: is_reasoning_agent
      :collapse:

.. py:data:: logger

