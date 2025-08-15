agents.memory_reorganized.base.token_state
==========================================

.. py:module:: agents.memory_reorganized.base.token_state

.. autoapi-nested-parse::

   Memory state with integrated token tracking and summarization hooks.

   This module extends MessagesStateWithTokenUsage to add memory-specific functionality
   with pre-hooks for summarization and token management.


   .. autolink-examples:: agents.memory_reorganized.base.token_state
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.base.token_state.GRAPH_AVAILABLE
   agents.memory_reorganized.base.token_state.logger
   agents.memory_reorganized.base.token_state.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.token_state.MemoryStateWithTokens


Module Contents
---------------

.. py:class:: MemoryStateWithTokens

   Bases: :py:obj:`haive.core.schema.prebuilt.messages.messages_with_token_usage.MessagesStateWithTokenUsage`


   MessagesState with memory and token-aware summarization hooks.

   This state combines:
   - MessagesStateWithTokenUsage (automatic token tracking)
   - Memory management (current memories, retrieved memories)
   - Pre-hook system for summarization triggers
   - Token threshold monitoring with branching logic

   Features:
   - Automatic token tracking from parent class
   - Memory storage and retrieval tracking
   - Pre-execution hooks that check token thresholds
   - Summarization triggers when thresholds are exceeded
   - Running summary maintenance
   - Branch decision logic for token management

   .. rubric:: Example

   >>> state = MemoryStateWithTokens()
   >>> state.add_message(user_message)
   >>>
   >>> # Pre-hook automatically checks tokens
   >>> if state.should_trigger_summarization():
   >>>     state.prepare_for_summarization()
   >>>
   >>> # Branch logic for routing
   >>> route = state.get_memory_route()  # "process", "summarize", "rewrite"


   .. autolink-examples:: MemoryStateWithTokens
      :collapse:

   .. py:method:: add_message_with_hooks(message: langchain_core.messages.AnyMessage) -> dict[str, Any]

      Add message with pre-hook processing.

      This method:
      1. Runs pre-message hook
      2. Adds the message normally
      3. Updates token tracking
      4. Returns hook results for routing decisions

      :param message: Message to add

      :returns: Hook results for routing decisions


      .. autolink-examples:: add_message_with_hooks
         :collapse:


   .. py:method:: apply_summarization_result(summary: str, summarized_message_ids: list[str], summarized_memory_ids: list[str]) -> None

      Apply results of summarization operation.

      :param summary: Generated summary text
      :param summarized_message_ids: IDs of messages that were summarized
      :param summarized_memory_ids: IDs of memories that were summarized


      .. autolink-examples:: apply_summarization_result
         :collapse:


   .. py:method:: get_comprehensive_status() -> dict[str, Any]

      Get comprehensive state status for debugging/monitoring.


      .. autolink-examples:: get_comprehensive_status
         :collapse:


   .. py:method:: get_memory_route() -> str

      Determine routing decision based on current state.

      :returns: Route name for graph branching logic


      .. autolink-examples:: get_memory_route
         :collapse:


   .. py:method:: pre_message_hook(message: langchain_core.messages.AnyMessage) -> dict[str, Any]

      Pre-hook executed before adding any message.

      This hook:
      1. Checks current token usage
      2. Determines if summarization is needed
      3. Prepares summarization data if required
      4. Returns decision for routing

      :param message: Message about to be added

      :returns: Dict with hook results and routing decisions


      .. autolink-examples:: pre_message_hook
         :collapse:


   .. py:method:: prepare_for_summarization() -> dict[str, Any]

      Prepare state for summarization operation.

      This method:
      1. Identifies messages/memories to summarize
      2. Preserves recent important content
      3. Calculates target compression ratios
      4. Prepares summarization context

      :returns: Dict with summarization preparation data


      .. autolink-examples:: prepare_for_summarization
         :collapse:


   .. py:method:: reset_for_new_session() -> None

      Reset state for new conversation session.


      .. autolink-examples:: reset_for_new_session
         :collapse:


   .. py:method:: should_trigger_summarization() -> bool

      Check if summarization should be triggered.


      .. autolink-examples:: should_trigger_summarization
         :collapse:


   .. py:attribute:: critical_threshold
      :type:  float
      :value: None



   .. py:attribute:: current_memories
      :type:  list[haive.agents.memory_reorganized.base.memory_state_original.UnifiedMemoryEntry]
      :value: None



   .. py:property:: estimated_total_tokens
      :type: int


      Estimate total tokens for messages + memories.

      .. autolink-examples:: estimated_total_tokens
         :collapse:


   .. py:attribute:: graph_generation_enabled
      :type:  bool
      :value: None



   .. py:attribute:: graph_nodes
      :type:  list[haive.agents.document_modifiers.kg.kg_map_merge.models.EntityNode]
      :value: None



   .. py:attribute:: graph_relationships
      :type:  list[haive.agents.document_modifiers.kg.kg_map_merge.models.EntityRelationship]
      :value: None



   .. py:attribute:: knowledge_graph
      :type:  Optional[haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph]
      :value: None



   .. py:attribute:: last_graph_update
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: last_operation
      :type:  Optional[dict[str, Any]]
      :value: None



   .. py:attribute:: last_summarization
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: max_context_tokens
      :type:  int
      :value: None



   .. py:attribute:: memory_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: memory_stats
      :type:  haive.agents.memory_reorganized.base.memory_state_original.MemoryStats
      :value: None



   .. py:attribute:: memory_token_usage
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: retrieved_memories
      :type:  list[haive.agents.memory_reorganized.base.memory_state_original.UnifiedMemoryEntry]
      :value: None



   .. py:attribute:: running_summary
      :type:  Optional[str]
      :value: None



   .. py:attribute:: summarized_message_ids
      :type:  list[str]
      :value: None



   .. py:property:: token_status
      :type: str


      Get current token status.

      .. autolink-examples:: token_status
         :collapse:


   .. py:property:: token_usage_ratio
      :type: float


      Calculate current token usage as ratio of max.

      .. autolink-examples:: token_usage_ratio
         :collapse:


   .. py:property:: total_memory_tokens
      :type: int


      Calculate total tokens used by memories.

      .. autolink-examples:: total_memory_tokens
         :collapse:


   .. py:attribute:: warning_threshold
      :type:  float
      :value: None



.. py:data:: GRAPH_AVAILABLE
   :value: True


.. py:data:: logger

.. py:data:: logger

