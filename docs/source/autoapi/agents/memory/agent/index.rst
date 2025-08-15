agents.memory.agent
===================

.. py:module:: agents.memory.agent


Attributes
----------

.. autoapisummary::

   agents.memory.agent.logger


Classes
-------

.. autoapisummary::

   agents.memory.agent.MemoryAgent


Module Contents
---------------

.. py:class:: MemoryAgent(config: haive.agents.memory.config.MemoryAgentConfig)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Memory Agent implementation that extends ReactAgent.

   Adds long-term memory capabilities for persisting information
   about users across conversations.

   Initialize the Memory Agent with its configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryAgent
      :collapse:

   .. py:method:: _add_memory_system_message_node(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Add a node for adding a memory-enhanced system message.


      .. autolink-examples:: _add_memory_system_message_node
         :collapse:


   .. py:method:: _extract_memories(state: dict[str, Any]) -> dict[str, Any]

      Extract memories from conversation.

      :param state: Current state with messages

      :returns: Updated state with extracted memories


      .. autolink-examples:: _extract_memories
         :collapse:


   .. py:method:: _extract_query(state: dict[str, Any]) -> dict[str, Any]

      Extract query from messages and store in state.

      :param state: Current state with messages

      :returns: Updated state with extracted query


      .. autolink-examples:: _extract_query
         :collapse:


   .. py:method:: _get_current_user_id() -> str

      Get the current user ID from runtime config.


      .. autolink-examples:: _get_current_user_id
         :collapse:


   .. py:method:: _init_memory_tools()

      Initialize memory-related tools.


      .. autolink-examples:: _init_memory_tools
         :collapse:


   .. py:method:: _load_memories(state: dict[str, Any]) -> dict[str, Any]

      Load relevant memories for the current user.

      :param state: Current state

      :returns: Updated state with loaded memories


      .. autolink-examples:: _load_memories
         :collapse:


   .. py:method:: _route_after_llm(state: dict[str, Any]) -> str

      Determine where to route after the LLM node.

      :param state: Current state

      :returns: Next node name


      .. autolink-examples:: _route_after_llm
         :collapse:


   .. py:method:: _save_memories(state: dict[str, Any]) -> dict[str, Any]

      Save extracted memories to vector store.

      :param state: Current state with extracted memories

      :returns: Updated state


      .. autolink-examples:: _save_memories
         :collapse:


   .. py:method:: run(input_data: str | dict[str, Any], user_id: str | None = None, **kwargs) -> dict[str, Any]

      Run the memory agent.

      :param input_data: Input query or state
      :param user_id: Optional user ID for memory context
      :param \*\*kwargs: Additional parameters

      :returns: Result from agent execution


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow graph with memory management nodes.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: config


.. py:data:: logger

