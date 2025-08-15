agents.self_healing_code
========================

.. py:module:: agents.self_healing_code

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: agents.self_healing_code
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/self_healing_code/agent/index
   /autoapi/agents/self_healing_code/branches/index
   /autoapi/agents/self_healing_code/state/index


Classes
-------

.. autoapisummary::

   agents.self_healing_code.SelfHealingCodeAgent
   agents.self_healing_code.SelfHealingCodeAgentConfig


Package Contents
----------------

.. py:class:: SelfHealingCodeAgent

   Bases: :py:obj:`AgentArchitecture`


   .. py:method:: bug_report_node()

      Generate Bug Report.


      .. autolink-examples:: bug_report_node
         :collapse:


   .. py:method:: code_execution_node()

      Run Arbitrary Code.


      .. autolink-examples:: code_execution_node
         :collapse:


   .. py:method:: code_patching_node()

      Fix Arbitrary Code.


      .. autolink-examples:: code_patching_node
         :collapse:


   .. py:method:: code_update_node()

      Update Arbitratry Code.


      .. autolink-examples:: code_update_node
         :collapse:


   .. py:method:: memory_filter_node()


   .. py:method:: memory_generation_node()

      Generate relevant memories based on new bug report.


      .. autolink-examples:: memory_generation_node
         :collapse:


   .. py:method:: memory_modification_node()

      Modify relevant memories based on new interaction.


      .. autolink-examples:: memory_modification_node
         :collapse:


   .. py:method:: memory_search_node()

      Find memories relevant to the current bug report.


      .. autolink-examples:: memory_search_node
         :collapse:


   .. py:method:: setup_workflow() -> None


   .. py:attribute:: config
      :type:  SelfHealingCodeAgentConfig


   .. py:attribute:: state
      :type:  SelfHealingCodeState


.. py:class:: SelfHealingCodeAgentConfig

   Bases: :py:obj:`AgentArchitectureConfig`


   .. py:attribute:: state_schema
      :type:  SelfHealingCodeState


