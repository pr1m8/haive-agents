agents.base.compiled_agent
==========================

.. py:module:: agents.base.compiled_agent

.. autoapi-nested-parse::

   CompiledAgent - Agent class based on CompiledStateGraph architecture.

   This module provides the new CompiledAgent class that inherits from CompiledStateGraph
   while maintaining compatibility with the existing Agent interface. This class represents
   the future direction for agent architecture in the Haive framework.


   .. autolink-examples:: agents.base.compiled_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.compiled_agent.logger


Classes
-------

.. autoapisummary::

   agents.base.compiled_agent.CompiledAgent


Module Contents
---------------

.. py:class:: CompiledAgent

   Bases: :py:obj:`haive.core.graph.state_graph.compiled_state_graph.CompiledStateGraph`, :py:obj:`haive.agents.base.mixins.execution_mixin.ExecutionMixin`, :py:obj:`haive.agents.base.mixins.state_mixin.StateMixin`, :py:obj:`haive.agents.base.mixins.persistence_mixin.PersistenceMixin`, :py:obj:`haive.agents.base.serialization_mixin.SerializationMixin`


   Agent class based on CompiledStateGraph architecture.

   This class represents LLM-based reasoning agents that can:
   - Reason about problems and make decisions
   - Use tools to interact with external systems
   - Maintain conversation memory and context
   - Coordinate with other agents in multi-agent workflows

   CompiledAgent should be used for components that require:
   - LLM-powered reasoning capabilities
   - Tool usage and coordination
   - Dynamic decision making
   - Conversation and memory management

   .. attribute:: engine

      Primary LLM engine for reasoning (required)

   .. attribute:: engines

      Dictionary of additional engines used by this agent

   .. attribute:: tools

      List of tools available to this agent

   .. attribute:: agent_type

      Always EngineType.AGENT for agents

   .. attribute:: conversation_memory

      Whether to maintain conversation history

   .. attribute:: max_iterations

      Maximum reasoning iterations before stopping


   .. autolink-examples:: CompiledAgent
      :collapse:

   .. py:method:: _setup_schemas() -> None

      Generate schemas from available engines.

      This method creates state, input, and output schemas based on the
      engines available to this agent. It uses SchemaComposer for basic
      composition (agents with sub-agents should use AgentSchemaComposer).


      .. autolink-examples:: _setup_schemas
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


   .. py:method:: areason(problem: Any, context: dict[str, Any] | None = None) -> Any
      :async:


      Asynchronous version of reason method.

      Default implementation calls the synchronous reason method.
      Subclasses can override for true async reasoning.

      :param problem: The problem or input to reason about
      :param context: Optional context information for reasoning

      :returns: The reasoning result or solution
      :rtype: Any


      .. autolink-examples:: areason
         :collapse:


   .. py:method:: can_reason() -> bool

      Check if this agent has reasoning capabilities.

      :returns: True if agent has LLM engine for reasoning
      :rtype: bool


      .. autolink-examples:: can_reason
         :collapse:


   .. py:method:: compile() -> Any

      Compile the agent into an executable graph.

      :returns: Compiled graph ready for execution
      :rtype: Any


      .. autolink-examples:: compile
         :collapse:


   .. py:method:: get_agent_capabilities() -> dict[str, Any]

      Get information about agent capabilities.

      :returns: Information about agent's capabilities
      :rtype: dict


      .. autolink-examples:: get_agent_capabilities
         :collapse:


   .. py:method:: get_available_tools() -> list[str]

      Get list of available tool names.

      :returns: List of tool names available to this agent
      :rtype: list[str]


      .. autolink-examples:: get_available_tools
         :collapse:


   .. py:method:: get_component_type() -> str

      Get the component type identifier.


      .. autolink-examples:: get_component_type
         :collapse:


   .. py:method:: invoke(input_data: Any, config: dict[str, Any] | None = None) -> Any

      Invoke the agent with input data.

      This method provides the standard invocation interface for agents.
      It compiles the agent's graph and executes it with the provided input.

      :param input_data: Input data for the agent
      :param config: Optional configuration for execution

      :returns: Agent execution result
      :rtype: Any


      .. autolink-examples:: invoke
         :collapse:


   .. py:method:: reason(problem: Any, context: dict[str, Any] | None = None) -> Any
      :abstractmethod:


      Reason about a problem and provide a solution.

      This method must be implemented by all agent subclasses to define
      their reasoning capabilities. The reasoning process may involve:
      - Analyzing the problem
      - Using available tools
      - Making decisions based on context
      - Generating solutions or responses

      :param problem: The problem or input to reason about
      :param context: Optional context information for reasoning

      :returns: The reasoning result or solution
      :rtype: Any

      :raises NotImplementedError: If not implemented by subclass


      .. autolink-examples:: reason
         :collapse:


   .. py:method:: setup_agent() -> None

      Hook for subclass-specific setup logic.

      This method is called during initialization and can be overridden
      by subclasses for custom setup logic. Maintained for backward
      compatibility with existing Agent interface.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: use_tool(tool_name: str, **kwargs) -> Any

      Use a specific tool by name.

      :param tool_name: Name of the tool to use
      :param \*\*kwargs: Arguments to pass to the tool

      :returns: Tool execution result
      :rtype: Any

      :raises ValueError: If tool is not found


      .. autolink-examples:: use_tool
         :collapse:


   .. py:method:: validate_agent_requirements() -> CompiledAgent
      :classmethod:


      Validate that agent has required LLM capabilities.

      Agents must have an LLM engine for reasoning. This validator ensures
      that the agent is properly configured with reasoning capabilities.


      .. autolink-examples:: validate_agent_requirements
         :collapse:


   .. py:attribute:: agent_type
      :type:  Literal[haive.core.engine.base.EngineType.AGENT]
      :value: None



   .. py:attribute:: conversation_memory
      :type:  bool
      :value: None



   .. py:attribute:: engine
      :type:  haive.core.engine.base.Engine | None
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.base.Engine]
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: set_schema
      :type:  bool
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



.. py:data:: logger

