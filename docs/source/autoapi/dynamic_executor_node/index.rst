dynamic_executor_node
=====================

.. py:module:: dynamic_executor_node

.. autoapi-nested-parse::

   Dynamic Executor Node for Dynamic Supervisor.

   This node dynamically executes agents by name, properly handling state extraction
   and merging based on the EngineNode/AgentNode patterns.


   .. autolink-examples:: dynamic_executor_node
      :collapse:


Attributes
----------

.. autoapisummary::

   dynamic_executor_node.logger


Classes
-------

.. autoapisummary::

   dynamic_executor_node.DynamicExecutorNode


Functions
---------

.. autoapisummary::

   dynamic_executor_node.create_dynamic_executor_node


Module Contents
---------------

.. py:class:: DynamicExecutorNode(agent_registry: dict[str, Any])

   Node that dynamically executes agents by name with proper state handling.

   Initialize with agent registry.

   :param agent_registry: Dictionary mapping agent names to agent instances


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DynamicExecutorNode
      :collapse:

   .. py:method:: __call__(state: dict[str, Any] | pydantic.BaseModel, config: dict[str, Any] | None = None) -> dict[str, Any]
      :async:


      Execute the targeted agent with proper state extraction.

      This follows the pattern from AgentNode:
      1. Get target agent name from state
      2. Extract fields for agent's state schema
      3. Execute agent
      4. Merge results back


      .. autolink-examples:: __call__
         :collapse:


   .. py:method:: _prepare_agent_input(agent: Any, state: dict[str, Any]) -> dict[str, Any]

      Prepare input for agent based on its state schema.

      Following AgentNode pattern:
      - Use agent's own state schema
      - Extract only fields the agent expects
      - Preserve message objects


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: _process_agent_result(result: Any, state: dict[str, Any], agent_name: str) -> dict[str, Any]

      Process agent result and create state update.

      Following EngineNode pattern for result wrapping.


      .. autolink-examples:: _process_agent_result
         :collapse:


   .. py:attribute:: agent_registry


.. py:function:: create_dynamic_executor_node(agent_registry: dict[str, Any]) -> DynamicExecutorNode

   Factory function to create a dynamic executor node.

   :param agent_registry: Dictionary mapping agent names to agent instances

   :returns: DynamicExecutorNode instance


   .. autolink-examples:: create_dynamic_executor_node
      :collapse:

.. py:data:: logger

