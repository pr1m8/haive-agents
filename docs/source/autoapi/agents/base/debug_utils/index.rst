agents.base.debug_utils
=======================

.. py:module:: agents.base.debug_utils

.. autoapi-nested-parse::

   Debug utilities for agent execution with Rich UI.

   Provides comprehensive debugging and logging capabilities for agent execution,
   particularly focused on runnable config and recursion limit issues.


   .. autolink-examples:: agents.base.debug_utils
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.debug_utils._global_debugger
   agents.base.debug_utils.debug_console
   agents.base.debug_utils.debug_logger


Classes
-------

.. autoapisummary::

   agents.base.debug_utils.AgentDebugger


Functions
---------

.. autoapisummary::

   agents.base.debug_utils.debug_runnable_config
   agents.base.debug_utils.disable_agent_debugging
   agents.base.debug_utils.enable_agent_debugging
   agents.base.debug_utils.get_agent_debugger


Module Contents
---------------

.. py:class:: AgentDebugger(agent_name: str = 'Agent', enabled: bool = False)

   Rich UI debugger for agent execution.


   .. autolink-examples:: AgentDebugger
      :collapse:

   .. py:method:: disable() -> None

      Disable debugging output.


      .. autolink-examples:: disable
         :collapse:


   .. py:method:: enable() -> None

      Enable debugging output.


      .. autolink-examples:: enable
         :collapse:


   .. py:method:: log_agent_execution_start(input_data: Any, config: langchain_core.runnables.RunnableConfig)

      Log the start of agent execution.


      .. autolink-examples:: log_agent_execution_start
         :collapse:


   .. py:method:: log_config_preparation(base_config: langchain_core.runnables.RunnableConfig | None, runtime_config: langchain_core.runnables.RunnableConfig, thread_id: str | None, kwargs: dict[str, Any])

      Log the config preparation process.


      .. autolink-examples:: log_config_preparation
         :collapse:


   .. py:method:: log_recursion_limit_flow(step: str, recursion_limit: Any, source: str = '')

      Track recursion limit through the execution flow.


      .. autolink-examples:: log_recursion_limit_flow
         :collapse:


   .. py:method:: log_runnable_config(config: langchain_core.runnables.RunnableConfig, context: str = '')

      Log runnable config with rich formatting.


      .. autolink-examples:: log_runnable_config
         :collapse:


   .. py:attribute:: agent_name
      :value: 'Agent'



   .. py:attribute:: console


   .. py:attribute:: enabled
      :value: False



.. py:function:: debug_runnable_config(config: langchain_core.runnables.RunnableConfig, context: str = '', agent_name: str = 'Agent')

   Quick function to debug a runnable config.


   .. autolink-examples:: debug_runnable_config
      :collapse:

.. py:function:: disable_agent_debugging() -> None

   Disable global agent debugging.


   .. autolink-examples:: disable_agent_debugging
      :collapse:

.. py:function:: enable_agent_debugging() -> None

   Enable global agent debugging.


   .. autolink-examples:: enable_agent_debugging
      :collapse:

.. py:function:: get_agent_debugger(agent_name: str = 'Agent') -> AgentDebugger

   Get or create agent debugger.


   .. autolink-examples:: get_agent_debugger
      :collapse:

.. py:data:: _global_debugger
   :type:  AgentDebugger | None
   :value: None


.. py:data:: debug_console

.. py:data:: debug_logger

