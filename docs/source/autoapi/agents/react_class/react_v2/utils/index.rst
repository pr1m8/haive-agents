agents.react_class.react_v2.utils
=================================

.. py:module:: agents.react_class.react_v2.utils

.. autoapi-nested-parse::

   Utility functions for creating and customizing ReactAgents.


   .. autolink-examples:: agents.react_class.react_v2.utils
      :collapse:


Functions
---------

.. autoapisummary::

   agents.react_class.react_v2.utils.create_agent_with_custom_engine
   agents.react_class.react_v2.utils.create_react_agent
   agents.react_class.react_v2.utils.create_structured_react_agent
   agents.react_class.react_v2.utils.organize_tools_by_category


Module Contents
---------------

.. py:function:: create_agent_with_custom_engine(engine: haive.core.engine.aug_llm.AugLLMConfig, tools: haive.agents.react.config.ToolsInput, name: str | None = None, max_iterations: int = 10, parallel_tool_execution: bool = False, max_retries: int = 3, retry_delay: float = 0.5, **kwargs) -> haive.agents.react.agent.ReactAgent

   Create a ReactAgent with a custom engine configuration.

   :param engine: Custom AugLLMConfig
   :param tools: Tools available to the agent (list or node mapping)
   :param name: Optional agent name
   :param max_iterations: Maximum number of iterations
   :param parallel_tool_execution: Whether to execute tools in parallel
   :param max_retries: Maximum number of retries for tool failures
   :param retry_delay: Delay between retry attempts in seconds
   :param \*\*kwargs: Additional configuration options

   :returns: Configured ReactAgent instance


   .. autolink-examples:: create_agent_with_custom_engine
      :collapse:

.. py:function:: create_react_agent(tools: haive.agents.react.config.ToolsInput, model: str = 'gpt-4o', system_prompt: str | None = None, name: str | None = None, max_iterations: int = 10, temperature: float = 0.7, parallel_tool_execution: bool = False, max_retries: int = 3, retry_delay: float = 0.5, **kwargs) -> haive.agents.react.agent.ReactAgent

   Create a ReactAgent with the specified tools and configuration.

   :param tools: Tools available to the agent (list or node mapping)
   :param model: The model name to use
   :param system_prompt: Optional system prompt
   :param name: Optional agent name
   :param max_iterations: Maximum number of iterations
   :param temperature: Temperature for LLM generation
   :param parallel_tool_execution: Whether to execute tools in parallel
   :param max_retries: Maximum number of retries for tool failures
   :param retry_delay: Delay between retry attempts in seconds
   :param \*\*kwargs: Additional configuration options

   :returns: Configured ReactAgent instance


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: create_structured_react_agent(output_model: type[pydantic.BaseModel], tools: haive.agents.react.config.ToolsInput, model: str = 'gpt-4o', system_prompt: str | None = None, name: str | None = None, max_iterations: int = 10, temperature: float = 0.7, parallel_tool_execution: bool = False, max_retries: int = 3, retry_delay: float = 0.5, **kwargs) -> haive.agents.react.agent.ReactAgent

   Create a ReactAgent that produces structured output according to the specified model.

   :param output_model: Pydantic model for structured output
   :param tools: Tools available to the agent (list or node mapping)
   :param model: The model name to use
   :param system_prompt: Optional system prompt
   :param name: Optional agent name
   :param max_iterations: Maximum number of iterations
   :param temperature: Temperature for LLM generation
   :param parallel_tool_execution: Whether to execute tools in parallel
   :param max_retries: Maximum number of retries for tool failures
   :param retry_delay: Delay between retry attempts in seconds
   :param \*\*kwargs: Additional configuration options

   :returns: Configured ReactAgent instance with structured output support


   .. autolink-examples:: create_structured_react_agent
      :collapse:

.. py:function:: organize_tools_by_category(tools: list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | langchain_core.tools.Tool | collections.abc.Callable], categories: dict[str, list[str]] | None = None) -> dict[str, list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | langchain_core.tools.Tool | collections.abc.Callable]]

   Organize tools into categories for parallel processing.

   :param tools: List of tools to organize
   :param categories: Optional mapping of category names to tool names

   :returns: Dictionary mapping category names to tool lists


   .. autolink-examples:: organize_tools_by_category
      :collapse:

