
:py:mod:`agents.base.debug_utils`
=================================

.. py:module:: agents.base.debug_utils

Debug utilities for agent execution with Rich UI.

Provides comprehensive debugging and logging capabilities for agent execution,
particularly focused on runnable config and recursion limit issues.


.. autolink-examples:: agents.base.debug_utils
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.debug_utils.AgentDebugger


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentDebugger:

   .. graphviz::
      :align: center

      digraph inheritance_AgentDebugger {
        node [shape=record];
        "AgentDebugger" [label="AgentDebugger"];
      }

.. autoclass:: agents.base.debug_utils.AgentDebugger
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.base.debug_utils.debug_runnable_config
   agents.base.debug_utils.disable_agent_debugging
   agents.base.debug_utils.enable_agent_debugging
   agents.base.debug_utils.get_agent_debugger

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



.. rubric:: Related Links

.. autolink-examples:: agents.base.debug_utils
   :collapse:
   
.. autolink-skip:: next
