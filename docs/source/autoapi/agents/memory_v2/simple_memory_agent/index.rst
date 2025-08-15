agents.memory_v2.simple_memory_agent
====================================

.. py:module:: agents.memory_v2.simple_memory_agent

.. autoapi-nested-parse::

   SimpleMemoryAgent with token-aware memory management and summarization.

   This agent follows V3 enhanced patterns with automatic summarization
   when approaching token limits, similar to LangMem's approach.


   .. autolink-examples:: agents.memory_v2.simple_memory_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.simple_memory_agent.HAS_GRAPH_MODELS
   agents.memory_v2.simple_memory_agent.MEMORY_REWRITE_PROMPT
   agents.memory_v2.simple_memory_agent.MEMORY_SUMMARIZATION_PROMPT
   agents.memory_v2.simple_memory_agent.RUNNING_SUMMARY_UPDATE_PROMPT
   agents.memory_v2.simple_memory_agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.simple_memory_agent.SimpleMemoryAgent
   agents.memory_v2.simple_memory_agent.TokenAwareMemoryConfig


Module Contents
---------------

.. py:class:: SimpleMemoryAgent

   Bases: :py:obj:`haive.agents.simple.enhanced_agent_v3.EnhancedSimpleAgent`


   Memory agent with token tracking and automatic summarization.

   This agent follows V3 enhanced patterns and implements LangMem-style
   memory management with:

   - Automatic token tracking for all operations
   - Progressive summarization when approaching limits
   - Running summary maintenance
   - Memory rewriting for compression
   - Smart retrieval with token awareness

   The agent monitors token usage and automatically triggers summarization
   or memory rewriting to stay within context limits while preserving
   important information.

   .. rubric:: Examples

   Basic usage::

       agent = SimpleMemoryAgent(
           name="assistant_memory",
           memory_config=TokenAwareMemoryConfig(
               max_context_tokens=4000,
               summarization_strategy="progressive"
           )
       )

       # Store memories
       agent.run("Remember that I prefer coffee over tea")
       agent.run("My favorite coffee is Ethiopian single origin")

       # Retrieve with token awareness
       response = agent.run("What beverages do I like?")

   With custom thresholds::

       config = TokenAwareMemoryConfig(
           max_context_tokens=8000,
           warning_threshold=0.6,
           critical_threshold=0.8,
           preserve_recent_memories=20
       )

       agent = SimpleMemoryAgent(
           name="long_term_memory",
           memory_config=config,
           debug_mode=True
       )


   .. autolink-examples:: SimpleMemoryAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _prepare_input(input_data: Any) -> dict[str, Any]

      Prepare input for MemoryStateWithTokens.

      Override parent to ensure proper message format for our state schema.


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: _setup_graph_prompts() -> None

      Setup graph-specific prompts for entity and relationship extraction.


      .. autolink-examples:: _setup_graph_prompts
         :collapse:


   .. py:method:: _setup_graph_transformer() -> None

      Setup graph transformer for knowledge graph generation.


      .. autolink-examples:: _setup_graph_transformer
         :collapse:


   .. py:method:: _setup_summarization_prompts() -> None

      Setup summarization prompts.


      .. autolink-examples:: _setup_summarization_prompts
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build memory graph with pre-hook system and token-aware branching.

      The graph implements a pre-hook pattern:
      1. Pre-hook node (checks tokens, decides routing)
      2. Branching based on pre-hook decisions
      3. Memory processing (store/retrieve/search)
      4. Summarization (when triggered by pre-hook)
      5. Running summary updates

      Flow:
          START -> pre_hook -> {process_memory, summarize_critical, summarize_warning}
                            -> [optional: update_summary] -> END


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: check_tokens_node(state: agents.memory_v2.memory_state_original.MemoryState) -> dict[str, Any]

      Check token usage and determine if action needed.


      .. autolink-examples:: check_tokens_node
         :collapse:


   .. py:method:: consolidate_memories_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Consolidate related memories to reduce count.


      .. autolink-examples:: consolidate_memories_node
         :collapse:


   .. py:method:: create_summary_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Create initial running summary.


      .. autolink-examples:: create_summary_node
         :collapse:


   .. py:method:: emergency_compress_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Emergency compression when critically over limits.


      .. autolink-examples:: emergency_compress_node
         :collapse:


   .. py:method:: extract_entities_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Extract entities from content using LLM.


      .. autolink-examples:: extract_entities_node
         :collapse:


   .. py:method:: extract_relationships_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Extract relationships from content using LLM.


      .. autolink-examples:: extract_relationships_node
         :collapse:


   .. py:method:: get_memory_status() -> dict[str, Any]

      Get comprehensive memory and token status.


      .. autolink-examples:: get_memory_status
         :collapse:


   .. py:method:: pre_hook_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Pre-hook node that analyzes state and decides routing.

      This is the core of the pre-hook system. It:
      1. Analyzes current token usage
      2. Examines incoming messages
      3. Decides the appropriate route
      4. Prepares any necessary data for downstream nodes

      :param state: Current memory state with token tracking

      :returns: Command to update state with routing decisions


      .. autolink-examples:: pre_hook_node
         :collapse:


   .. py:method:: process_memory_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Process memory operations (store/retrieve/search).

      This is the main node that handles all memory operations based on
      the user's input, using the appropriate memory tools.


      .. autolink-examples:: process_memory_node
         :collapse:


   .. py:method:: rewrite_memories_node(state: agents.memory_v2.memory_state_original.MemoryState) -> dict[str, Any]

      Rewrite memories for maximum compression.


      .. autolink-examples:: rewrite_memories_node
         :collapse:


   .. py:method:: route_by_token_status(state: dict[str, Any]) -> str

      Route based on token usage status.


      .. autolink-examples:: route_by_token_status
         :collapse:


   .. py:method:: route_from_pre_hook(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> str

      Route based on pre-hook analysis.

      :param state: State with pre-hook analysis results

      :returns: Route name for conditional edge routing


      .. autolink-examples:: route_from_pre_hook
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup memory agent with token tracking and tools.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: summarize_critical_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Critical summarization when approaching token limits.


      .. autolink-examples:: summarize_critical_node
         :collapse:


   .. py:method:: summarize_memories_node(state: agents.memory_v2.memory_state_original.MemoryState) -> dict[str, Any]

      Summarize memories to reduce token usage.


      .. autolink-examples:: summarize_memories_node
         :collapse:


   .. py:method:: summarize_warning_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Warning-level summarization for memory consolidation.


      .. autolink-examples:: summarize_warning_node
         :collapse:


   .. py:method:: transform_to_graph_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Transform memories and messages into a knowledge graph.


      .. autolink-examples:: transform_to_graph_node
         :collapse:


   .. py:method:: update_graph_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Update existing knowledge graph with new content.


      .. autolink-examples:: update_graph_node
         :collapse:


   .. py:method:: update_running_summary_node(state: agents.memory_v2.memory_state_original.MemoryState) -> dict[str, Any]

      Update the running summary with new memories.


      .. autolink-examples:: update_running_summary_node
         :collapse:


   .. py:method:: update_summary_node(state: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens) -> langgraph.types.Command

      Update existing running summary.


      .. autolink-examples:: update_summary_node
         :collapse:


   .. py:attribute:: entity_extraction_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: graph_enabled
      :type:  bool
      :value: None



   .. py:attribute:: graph_transformer
      :type:  haive.agents.document_modifiers.kg.kg_base.models.GraphTransformer | None
      :value: None



   .. py:attribute:: last_summarization
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: memory_config
      :type:  TokenAwareMemoryConfig
      :value: None



   .. py:attribute:: memory_rewrite_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: memory_summarization_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: relationship_extraction_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: running_summary
      :type:  str | None
      :value: None



   .. py:attribute:: running_summary_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.StateSchema]
      :value: None



   .. py:attribute:: token_tracker
      :type:  agents.memory_v2.token_tracker.TokenTracker
      :value: None



   .. py:attribute:: use_prebuilt_base
      :type:  bool
      :value: None



.. py:class:: TokenAwareMemoryConfig(/, **data: Any)

   Bases: :py:obj:`agents.memory_v2.memory_tools.MemoryConfig`


   Configuration for token-aware memory management.

   Extends base MemoryConfig with token tracking and summarization settings.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TokenAwareMemoryConfig
      :collapse:

   .. py:attribute:: critical_threshold
      :type:  float
      :value: None



   .. py:attribute:: enable_running_summary
      :type:  bool
      :value: None



   .. py:attribute:: max_context_tokens
      :type:  int
      :value: None



   .. py:attribute:: max_tokens_before_summary
      :type:  int
      :value: None



   .. py:attribute:: preserve_recent_memories
      :type:  int
      :value: None



   .. py:attribute:: running_summary_max_tokens
      :type:  int
      :value: None



   .. py:attribute:: summarization_strategy
      :type:  str
      :value: None



   .. py:attribute:: target_compression_ratio
      :type:  float
      :value: None



   .. py:attribute:: warning_threshold
      :type:  float
      :value: None



.. py:data:: HAS_GRAPH_MODELS
   :value: True


.. py:data:: MEMORY_REWRITE_PROMPT

.. py:data:: MEMORY_SUMMARIZATION_PROMPT

.. py:data:: RUNNING_SUMMARY_UPDATE_PROMPT

.. py:data:: logger

