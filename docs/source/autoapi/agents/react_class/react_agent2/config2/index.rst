agents.react_class.react_agent2.config2
=======================================

.. py:module:: agents.react_class.react_agent2.config2


Attributes
----------

.. autoapisummary::

   agents.react_class.react_agent2.config2.DEFAULT_REACT_SYSTEM_PROMPT


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.config2.ReactAgentConfig


Module Contents
---------------

.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a React agent that can use tools.

   Enables step-by-step reasoning with tool usage for information gathering.


   .. autolink-examples:: ReactAgentConfig
      :collapse:

   .. py:method:: align_output_format(v, info) -> Any
      :classmethod:


      Align the structured output model and response format.


      .. autolink-examples:: align_output_format
         :collapse:


   .. py:method:: create_prompt_template(system_prompt: str | None = None, additional_input_vars: list[str] | None = None) -> langchain_core.prompts.ChatPromptTemplate
      :classmethod:


      Create a flexible prompt template that supports system prompt.
      and additional input variables.

      :param system_prompt: Custom system prompt
      :param additional_input_vars: List of additional input variables to include

      :returns: ChatPromptTemplate with flexible input handling


      .. autolink-examples:: create_prompt_template
         :collapse:


   .. py:method:: ensure_tools_list(v) -> Any
      :classmethod:


      Ensure tools are always a list.


      .. autolink-examples:: ensure_tools_list
         :collapse:


   .. py:method:: from_aug_llm(aug_llm: haive.core.engine.aug_llm.AugLLMConfig, tools: list[langchain_core.tools.BaseTool] | None = None, name: str | None = None, max_iterations: int = 10, **kwargs) -> ReactAgentConfig
      :classmethod:


      Create a ReactAgentConfig from an existing AugLLMConfig.

      :param aug_llm: Existing AugLLMConfig to use
      :param tools: Optional list of tools
      :param name: Optional agent name
      :param max_iterations: Maximum number of iterations
      :param \*\*kwargs: Additional kwargs for the config

      :returns: ReactAgentConfig instance


      .. autolink-examples:: from_aug_llm
         :collapse:


   .. py:method:: from_scratch(system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, tools: list[langchain_core.tools.BaseTool] | None = None, name: str | None = None, max_iterations: int = 10, **kwargs) -> ReactAgentConfig
      :classmethod:


      Create a ReactAgentConfig from scratch.

      :param system_prompt: Optional system prompt
      :param model: Model name to use
      :param temperature: Temperature for generation
      :param tools: Optional list of tools
      :param name: Optional agent name
      :param max_iterations: Maximum number of iterations
      :param \*\*kwargs: Additional kwargs for the config

      :returns: ReactAgentConfig instance


      .. autolink-examples:: from_scratch
         :collapse:


   .. py:method:: from_tools(tools: list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | langchain_core.tools.Tool], system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, name: str | None = None, max_iterations: int = 10, **kwargs) -> ReactAgentConfig
      :classmethod:


      Create a ReactAgentConfig from a list of tools.

      :param tools: List of tools
      :param system_prompt: Optional system prompt
      :param model: Model name to use
      :param temperature: Temperature for generation
      :param name: Optional agent name
      :param max_iterations: Maximum number of iterations
      :param \*\*kwargs: Additional kwargs for the config

      :returns: ReactAgentConfig instance


      .. autolink-examples:: from_tools
         :collapse:


   .. py:method:: update_system_prompt(v) -> Any
      :classmethod:


      Update the system prompt in the engine if provided.


      .. autolink-examples:: update_system_prompt
         :collapse:


   .. py:attribute:: agent_node_name
      :type:  str
      :value: None



   .. py:attribute:: debug
      :type:  bool
      :value: None



   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: input_mapping
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: output_mapping
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: response_format
      :type:  type[pydantic.BaseModel] | dict[str, Any] | None
      :value: None



   .. py:attribute:: routing_function
      :type:  collections.abc.Callable | None
      :value: None



   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: system_prompt
      :type:  str | None
      :value: None



   .. py:attribute:: tool_node_name
      :type:  str
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | langchain_core.tools.Tool]
      :value: None



   .. py:attribute:: use_memory
      :type:  bool
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



.. py:data:: DEFAULT_REACT_SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an intelligent assistant with access to tools.
      You solve problems step-by-step by thinking carefully and using tools when needed.
      
      When you need information, use the appropriate tool to gather it.
      After seeing a tool's results, reflect on what you've learned and decide if you
      need more information or can now answer the question.
      
      FORMAT:
      1. If you need to use a tool, format your response like this:
        Thought: I need to find out X, so I should use the Y tool.
        Action: Use the correct tool name and provide the required parameters.
      
      2. If you have enough information to provide a final answer, respond
         conversationally to the user.
      
      Remember to be helpful, accurate, and respond directly to what the user is asking.
      """

   .. raw:: html

      </details>



