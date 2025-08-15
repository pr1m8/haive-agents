agents.react_class.react_agent2.agent2
======================================

.. py:module:: agents.react_class.react_agent2.agent2


Attributes
----------

.. autoapisummary::

   agents.react_class.react_agent2.agent2.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.agent2.MessageNormalizingToolNode
   agents.react_class.react_agent2.agent2.ReactAgent


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.agent2.chat
   agents.react_class.react_agent2.agent2.create_react_agent
   agents.react_class.react_agent2.agent2.has_tool_calls
   agents.react_class.react_agent2.agent2.run
   agents.react_class.react_agent2.agent2.setup_workflow
   agents.react_class.react_agent2.agent2.should_use_tools
   agents.react_class.react_agent2.agent2.stream
   agents.react_class.react_agent2.agent2.structured_output_node


Module Contents
---------------

.. py:class:: MessageNormalizingToolNode(tools: list[str])

   A wrapper around ToolNode that ensures proper serialization and message type compatibility.
   This fixes the Pydantic serialization warnings by properly normalizing message objects.

   Initialize with the tools to use.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MessageNormalizingToolNode
      :collapse:

   .. py:method:: __call__(state: dict[str, Any])

      Process the state with tools, ensuring message compatibility.


      .. autolink-examples:: __call__
         :collapse:


   .. py:attribute:: tool_node


   .. py:attribute:: tools


.. py:class:: ReactAgent(config: haive.agents.react_class.react_agent2.config2.ReactAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.react_class.react_agent2.config2.ReactAgentConfig`\ ]


   A React agent implementation using LangGraph.

   This agent implements the ReAct pattern (Reasoning, Action, Observation)
   to solve complex tasks using language models and tools.

   Initialize the ReactAgent with a configuration.

   :param config: ReactAgentConfig instance


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: _create_structured_output_node() -> collections.abc.Callable

      Create a node that generates structured output.

      :returns: Function to use as a node in the graph


      .. autolink-examples:: _create_structured_output_node
         :collapse:


   .. py:method:: _prepare_input(input_data: str | list[str] | dict[str, Any] | pydantic.BaseModel) -> dict[str, Any]

      Prepare input for the agent, ensuring proper initialization and message normalization.

      :param input_data: Input in various formats

      :returns: Properly formatted input state for the agent


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: _update_system_prompt(config: haive.agents.react_class.react_agent2.config2.ReactAgentConfig) -> None

      Update the engine's system prompt if a custom one is provided.

      :param config: ReactAgentConfig instance


      .. autolink-examples:: _update_system_prompt
         :collapse:


   .. py:method:: chat() -> None

      Start an interactive chat session with the agent.


      .. autolink-examples:: chat
         :collapse:


   .. py:method:: run(input_data: str | list[str] | dict[str, Any] | pydantic.BaseModel, **kwargs) -> dict[str, Any]

      Run the agent with the given input.

      :param input_data: Input data in various formats
      :param \*\*kwargs: Additional runtime configuration

      :returns: Final state or output


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the ReAct agent workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: stream(input_data: str | list[str] | dict[str, Any] | pydantic.BaseModel, **kwargs)

      Stream the agent execution with given input.

      :param input_data: Input data in various formats
      :param \*\*kwargs: Additional runtime configuration

      :returns: Generator yielding states


      .. autolink-examples:: stream
         :collapse:


   .. py:attribute:: tool_node


   .. py:attribute:: tools


.. py:function:: chat() -> None

   Module-level chat function.


   .. autolink-examples:: chat
      :collapse:

.. py:function:: create_react_agent(tools: list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | langchain_core.tools.Tool], model: str = 'gpt-4o', temperature: float = 0.7, system_prompt: str | None = None, name: str | None = None, max_iterations: int = 10, response_format: type[pydantic.BaseModel] | dict[str, Any] | None = None, use_memory: bool = True, visualize: bool = True, debug: bool = False, structured_output_model: type[pydantic.BaseModel] | dict[str, Any] | None = None, additional_input_vars: list[str] | None = None, **kwargs) -> ReactAgent

   Create a React agent with the specified configuration.

   :param tools: List of tools for the agent
   :param model: Model name to use (default: "gpt-4o")
   :param temperature: Temperature for generation (default: 0.7)
   :param system_prompt: Optional system prompt
   :param name: Optional name for the agent
   :param max_iterations: Maximum number of iterations (default: 10)
   :param response_format: Optional schema for structured output
   :param use_memory: Whether to use memory (default: True)
   :param visualize: Whether to generate graph visualization (default: True)
   :param debug: Whether to enable debug mode (default: False)
   :param structured_output_model: Optional schema for structured output
   :param additional_input_vars: Additional input variables for prompt
   :param \*\*kwargs: Additional configuration parameters

   :returns: ReactAgent instance


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: has_tool_calls(state: dict[str, Any])

   Check if the last message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: run(agent, input_data)

   Module-level run function.


   .. autolink-examples:: run
      :collapse:

.. py:function:: setup_workflow()

   Module-level setup_workflow function.


   .. autolink-examples:: setup_workflow
      :collapse:

.. py:function:: should_use_tools(state)

   Module-level should_use_tools function.


   .. autolink-examples:: should_use_tools
      :collapse:

.. py:function:: stream(agent, input_data)

   Module-level stream function.


   .. autolink-examples:: stream
      :collapse:

.. py:function:: structured_output_node(state)

   Module-level structured_output_node function.


   .. autolink-examples:: structured_output_node
      :collapse:

.. py:data:: logger

