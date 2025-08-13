
:py:mod:`agents.long_term_memory.nodes`
=======================================

.. py:module:: agents.long_term_memory.nodes



Functions
---------

.. autoapisummary::

   agents.long_term_memory.nodes.load_memories

.. py:function:: load_memories(state: haive.agents.long_term_memory.state.LongTermMemoryState, config: langchain_core.runnables.RunnableConfig) -> haive.agents.long_term_memory.state.LongTermMemoryState

   Load memories for the current conversation.

   :param state: The current state of the conversation.
   :type state: schemas.State
   :param config: The runtime configuration for the agent.
   :type config: RunnableConfig

   :returns: The updated state with loaded memories.
   :rtype: State


   .. autolink-examples:: load_memories
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.long_term_memory.nodes
   :collapse:
   
.. autolink-skip:: next
