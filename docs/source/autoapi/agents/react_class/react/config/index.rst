agents.react_class.react.config
===============================

.. py:module:: agents.react_class.react.config


Classes
-------

.. autoapisummary::

   agents.react_class.react.config.ReactAgentConfig


Module Contents
---------------

.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`


   Configuration for React Agent, extending SimpleAgentConfig.

   React Agent routes between an LLM and tools to perform multi-step
   reasoning and action to accomplish tasks.


   .. autolink-examples:: ReactAgentConfig
      :collapse:

   .. py:method:: ensure_valid_configuration() -> Any

      Validate the configuration.


      .. autolink-examples:: ensure_valid_configuration
         :collapse:


   .. py:attribute:: llm_node_name
      :type:  str
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: output_node_name
      :type:  str
      :value: None



   .. py:attribute:: router_node_name
      :type:  str
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: structured_output_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: system_prompt
      :type:  str | None
      :value: None



   .. py:attribute:: tool_choice
      :type:  Literal['auto', 'any', 'none'] | dict[str, Any] | None
      :value: None



   .. py:attribute:: tool_node_name
      :type:  str
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool | dict[str, Any]]
      :value: None



