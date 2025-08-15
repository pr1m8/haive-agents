agents.react_class.react_v2.config
==================================

.. py:module:: agents.react_class.react_v2.config

.. autoapi-nested-parse::

   Configuration for the ReactAgent.


   .. autolink-examples:: agents.react_class.react_v2.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.react_class.react_v2.config.ToolsInput
   agents.react_class.react_v2.config.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_v2.config.ReactAgentConfig


Module Contents
---------------

.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`


   Configuration for a React agent that can use tools and follow ReAct reasoning pattern.


   .. autolink-examples:: ReactAgentConfig
      :collapse:

   .. py:method:: from_tools(tools: ToolsInput, model: str = 'gpt-4o', system_prompt: str | None = None, name: str | None = None, temperature: float = 0.7, parallel_tool_execution: bool = False, max_iterations: int = 10, max_retries: int = 3, **kwargs) -> ReactAgentConfig
      :classmethod:


      Create a ReactAgentConfig with tools from scratch.

      :param tools: Tools to use (list or dict)
      :param model: Model name to use
      :param system_prompt: Optional system prompt
      :param name: Optional agent name
      :param temperature: Temperature for generation
      :param parallel_tool_execution: Whether to execute tools in parallel
      :param max_iterations: Maximum number of reasoning iterations
      :param max_retries: Maximum number of retries for tool failures
      :param \*\*kwargs: Additional kwargs for the config

      :returns: ReactAgentConfig instance


      .. autolink-examples:: from_tools
         :collapse:


   .. py:method:: validate_tools(v) -> Any
      :classmethod:


      Validate that tools are properly configured.


      .. autolink-examples:: validate_tools
         :collapse:


   .. py:method:: with_structured_output(model_class: type[pydantic.BaseModel], tools: ToolsInput, system_prompt: str | None = None, name: str | None = None, parallel_tool_execution: bool = False, **kwargs) -> ReactAgentConfig
      :classmethod:


      Create a ReactAgentConfig with structured output and tools.

      :param model_class: Pydantic model class for structured output
      :param tools: Tools to use (list or dict)
      :param system_prompt: Optional system prompt
      :param name: Optional agent name
      :param parallel_tool_execution: Whether to execute tools in parallel
      :param \*\*kwargs: Additional kwargs for the config

      :returns: ReactAgentConfig instance


      .. autolink-examples:: with_structured_output
         :collapse:


   .. py:attribute:: agent_node_name
      :type:  str
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: max_retries
      :type:  int
      :value: None



   .. py:attribute:: parallel_tool_execution
      :type:  bool
      :value: None



   .. py:attribute:: retry_delay
      :type:  float
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: tool_choice
      :type:  str | None
      :value: None



   .. py:attribute:: tools
      :type:  ToolsInput
      :value: None



   .. py:attribute:: tools_node_prefix
      :type:  str
      :value: None



   .. py:attribute:: use_structured_output_node
      :type:  bool
      :value: None



.. py:data:: ToolsInput

.. py:data:: logger

