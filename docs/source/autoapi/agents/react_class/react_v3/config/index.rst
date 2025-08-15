agents.react_class.react_v3.config
==================================

.. py:module:: agents.react_class.react_v3.config

.. autoapi-nested-parse::

   Configuration for the ReactAgent - a tool-using agent with ReAct pattern.

   from typing import Any
   This module defines the configuration class for ReactAgent, which implements the
   ReAct (Reasoning and Acting) pattern for tool-using agents.


   .. autolink-examples:: agents.react_class.react_v3.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.react_class.react_v3.config.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_v3.config.ReactAgentConfig


Module Contents
---------------

.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a ReAct agent with tool integration.

   This agent implements the Reasoning+Acting pattern:
   1. Reasoning about what to do based on the input
   2. Acting by using tools when necessary
   3. Observing the results and continuing the process


   .. autolink-examples:: ReactAgentConfig
      :collapse:

   .. py:method:: build_agent() -> Any

      Build and return a ReactAgent instance.

      :returns: Configured ReactAgent


      .. autolink-examples:: build_agent
         :collapse:


   .. py:method:: get_tool_schemas() -> dict[str, Any]

      Get the input and output schemas for all tools.

      :returns: Dictionary mapping tool names to their schemas


      .. autolink-examples:: get_tool_schemas
         :collapse:


   .. py:method:: get_tools_by_name() -> dict[str, langchain_core.tools.BaseTool]

      Get a dictionary mapping tool names to tools.

      :returns: Dictionary mapping tool names to tool instances


      .. autolink-examples:: get_tools_by_name
         :collapse:


   .. py:method:: setup_defaults() -> Any

      Set up default retry policies if not provided.


      .. autolink-examples:: setup_defaults
         :collapse:


   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: include_tool_names_in_prompt
      :type:  bool
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: reasoning_node_name
      :type:  str
      :value: None



   .. py:attribute:: reasoning_retry
      :type:  langgraph.pregel.RetryPolicy | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.state_schema.StateSchema] | None
      :value: None



   .. py:attribute:: system_prompt
      :type:  str
      :value: None



   .. py:attribute:: tool_node_name
      :type:  str
      :value: None



   .. py:attribute:: tool_retry
      :type:  langgraph.pregel.RetryPolicy | None
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



.. py:data:: logger

