agents.memory_v2.standalone_rag_memory
======================================

.. py:module:: agents.memory_v2.standalone_rag_memory

.. autoapi-nested-parse::

   Standalone RAG-based Memory Agent using BaseRAGAgent with retrievers.

   This module provides memory-capable agents built on BaseRAGAgent without
   dependencies on the broken memory module. All models are defined here.

   Key features:
   1. ConversationMemoryAgent - conversation history with time-weighting
   2. FactualMemoryAgent - factual information storage and retrieval
   3. PreferencesMemoryAgent - user preferences with generation
   4. UnifiedMemoryRAGAgent - coordinates all memory types
   5. Real BaseRAGAgent integration with different retrievers
   6. Vector store persistence across different backends

   NO MOCKS - All components use real BaseRAGAgent with real retrievers.


   .. autolink-examples:: agents.memory_v2.standalone_rag_memory
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.standalone_rag_memory.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.standalone_rag_memory.ConversationMemoryAgent
   agents.memory_v2.standalone_rag_memory.FactualMemoryAgent
   agents.memory_v2.standalone_rag_memory.ImportanceLevel
   agents.memory_v2.standalone_rag_memory.MemoryRAGConfig
   agents.memory_v2.standalone_rag_memory.MemoryType
   agents.memory_v2.standalone_rag_memory.MessageDocumentConverter
   agents.memory_v2.standalone_rag_memory.PreferencesMemoryAgent
   agents.memory_v2.standalone_rag_memory.StandaloneMemoryItem
   agents.memory_v2.standalone_rag_memory.UnifiedMemoryRAGAgent


Functions
---------

.. autoapisummary::

   agents.memory_v2.standalone_rag_memory.create_conversation_memory_agent
   agents.memory_v2.standalone_rag_memory.create_unified_memory_agent
   agents.memory_v2.standalone_rag_memory.demo


Module Contents
---------------

.. py:class:: ConversationMemoryAgent(config: MemoryRAGConfig, name: str = 'conversation_memory')

   Memory agent for conversation history using BaseRAGAgent.

   Initialize conversation memory agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConversationMemoryAgent
      :collapse:

   .. py:method:: _update_vector_store() -> None
      :async:


      Update vector store with new documents.


      .. autolink-examples:: _update_vector_store
         :collapse:


   .. py:method:: add_conversation(messages: list[langchain_core.messages.BaseMessage]) -> None
      :async:


      Add conversation messages to memory.


      .. autolink-examples:: add_conversation
         :collapse:


   .. py:method:: initialize() -> None
      :async:


      Initialize the underlying RAG agent.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: retrieve_conversation_context(query: str, k: int | None = None) -> list[langchain_core.documents.Document]
      :async:


      Retrieve relevant conversation context.


      .. autolink-examples:: retrieve_conversation_context
         :collapse:


   .. py:attribute:: _documents
      :type:  list[langchain_core.documents.Document]
      :value: []



   .. py:attribute:: _initialized
      :value: False



   .. py:attribute:: _rag_agent
      :type:  haive.agents.rag.base.agent.BaseRAGAgent | None
      :value: None



   .. py:attribute:: config


   .. py:attribute:: message_converter


   .. py:attribute:: name
      :value: 'conversation_memory'



.. py:class:: FactualMemoryAgent(config: MemoryRAGConfig, name: str = 'factual_memory')

   Memory agent for factual information using BaseRAGAgent.

   Initialize factual memory agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FactualMemoryAgent
      :collapse:

   .. py:method:: _memories_to_documents(memories: list[StandaloneMemoryItem]) -> list[langchain_core.documents.Document]

      Convert multiple memories to documents.


      .. autolink-examples:: _memories_to_documents
         :collapse:


   .. py:method:: _memory_to_document(memory: StandaloneMemoryItem) -> langchain_core.documents.Document

      Convert memory item to document.


      .. autolink-examples:: _memory_to_document
         :collapse:


   .. py:method:: _update_vector_store() -> None
      :async:


      Update vector store with new documents.


      .. autolink-examples:: _update_vector_store
         :collapse:


   .. py:method:: add_memories(memories: list[StandaloneMemoryItem]) -> None
      :async:


      Add multiple factual memories.


      .. autolink-examples:: add_memories
         :collapse:


   .. py:method:: add_memory(memory: StandaloneMemoryItem) -> None
      :async:


      Add a factual memory.


      .. autolink-examples:: add_memory
         :collapse:


   .. py:method:: initialize() -> None
      :async:


      Initialize the underlying RAG agent.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: retrieve_facts(query: str, k: int | None = None) -> list[dict[str, Any]]
      :async:


      Retrieve relevant factual memories.


      .. autolink-examples:: retrieve_facts
         :collapse:


   .. py:attribute:: _initialized
      :value: False



   .. py:attribute:: _memories
      :type:  list[StandaloneMemoryItem]
      :value: []



   .. py:attribute:: _rag_agent
      :type:  haive.agents.rag.base.agent.BaseRAGAgent | None
      :value: None



   .. py:attribute:: config


   .. py:attribute:: name
      :value: 'factual_memory'



.. py:class:: ImportanceLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Importance levels for memories.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ImportanceLevel
      :collapse:

   .. py:attribute:: CRITICAL
      :value: 'critical'



   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



.. py:class:: MemoryRAGConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for RAG-based memory agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryRAGConfig
      :collapse:

   .. py:attribute:: embedding_model
      :type:  haive.core.models.embeddings.base.HuggingFaceEmbeddingConfig
      :value: None



   .. py:attribute:: enable_time_weighting
      :type:  bool
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_memories_per_query
      :type:  int
      :value: None



   .. py:attribute:: memory_collection_name
      :type:  str
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: persistent_storage
      :type:  bool
      :value: None



   .. py:attribute:: recency_weight
      :type:  float
      :value: None



   .. py:attribute:: similarity_threshold
      :type:  float
      :value: None



   .. py:attribute:: storage_path
      :type:  str | None
      :value: None



   .. py:attribute:: time_decay_rate
      :type:  float
      :value: None



   .. py:attribute:: vector_store_provider
      :type:  haive.core.engine.vectorstore.VectorStoreProvider
      :value: None



.. py:class:: MemoryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of memories that can be stored.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryType
      :collapse:

   .. py:attribute:: CONVERSATIONAL
      :value: 'conversational'



   .. py:attribute:: EPISODIC
      :value: 'episodic'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: PERSONAL_CONTEXT
      :value: 'personal_context'



   .. py:attribute:: PREFERENCE
      :value: 'preference'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



   .. py:attribute:: SEMANTIC
      :value: 'semantic'



.. py:class:: MessageDocumentConverter(user_id: str | None = None, conversation_id: str | None = None)

   Convert messages to documents for RAG storage.

   Initialize converter.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MessageDocumentConverter
      :collapse:

   .. py:method:: convert_message(message: langchain_core.messages.BaseMessage) -> langchain_core.documents.Document

      Convert single message to document.


      .. autolink-examples:: convert_message
         :collapse:


   .. py:method:: convert_messages(messages: list[langchain_core.messages.BaseMessage]) -> list[langchain_core.documents.Document]

      Convert multiple messages to documents.


      .. autolink-examples:: convert_messages
         :collapse:


   .. py:attribute:: conversation_id
      :value: 'conv_Instance of uuid.UUID'



   .. py:attribute:: turn_counter
      :value: 0



   .. py:attribute:: user_id
      :value: None



.. py:class:: PreferencesMemoryAgent(config: MemoryRAGConfig, name: str = 'preferences_memory')

   Memory agent for user preferences using SimpleRAGAgent for generation.

   Initialize preferences memory agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PreferencesMemoryAgent
      :collapse:

   .. py:method:: _preferences_to_documents(preferences: list[StandaloneMemoryItem]) -> list[langchain_core.documents.Document]

      Convert preferences to documents.


      .. autolink-examples:: _preferences_to_documents
         :collapse:


   .. py:method:: _update_agent() -> None
      :async:


      Update the RAG agent with current preferences.


      .. autolink-examples:: _update_agent
         :collapse:


   .. py:method:: add_preference(preference: StandaloneMemoryItem) -> None
      :async:


      Add a user preference.


      .. autolink-examples:: add_preference
         :collapse:


   .. py:method:: get_preferences_for(context: str) -> str
      :async:


      Get relevant preferences and generate summary.


      .. autolink-examples:: get_preferences_for
         :collapse:


   .. py:method:: initialize() -> None
      :async:


      Initialize the underlying RAG agent.


      .. autolink-examples:: initialize
         :collapse:


   .. py:attribute:: _initialized
      :value: False



   .. py:attribute:: _preferences
      :type:  list[StandaloneMemoryItem]
      :value: []



   .. py:attribute:: _rag_agent
      :type:  haive.agents.rag.simple.agent.SimpleRAGAgent | None
      :value: None



   .. py:attribute:: config


   .. py:attribute:: name
      :value: 'preferences_memory'



.. py:class:: StandaloneMemoryItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Standalone memory item for RAG-based storage.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StandaloneMemoryItem
      :collapse:

   .. py:method:: mark_accessed()

      Mark memory as accessed.


      .. autolink-examples:: mark_accessed
         :collapse:


   .. py:attribute:: access_count
      :type:  int
      :value: None



   .. py:property:: age_hours
      :type: float


      Get memory age in hours.

      .. autolink-examples:: age_hours
         :collapse:


   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: conversation_id
      :type:  str | None
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: importance
      :type:  ImportanceLevel
      :value: None



   .. py:attribute:: last_accessed
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: memory_type
      :type:  MemoryType
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: session_id
      :type:  str | None
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



   .. py:attribute:: user_id
      :type:  str | None
      :value: None



.. py:class:: UnifiedMemoryRAGAgent(config: MemoryRAGConfig, user_id: str | None = None)

   Unified memory agent coordinating multiple specialized memory agents.

   Initialize unified memory agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: UnifiedMemoryRAGAgent
      :collapse:

   .. py:method:: as_tool(name: str | None = None, description: str | None = None, **config_kwargs)
      :classmethod:


      Convert this agent to a tool for use in other agents.


      .. autolink-examples:: as_tool
         :collapse:


   .. py:method:: get_memory_summary() -> dict[str, Any]
      :async:


      Get summary of all stored memories.


      .. autolink-examples:: get_memory_summary
         :collapse:


   .. py:method:: initialize() -> None
      :async:


      Initialize all memory agents.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: process_conversation(messages: list[langchain_core.messages.BaseMessage]) -> dict[str, Any]
      :async:


      Process conversation and extract memories.


      .. autolink-examples:: process_conversation
         :collapse:


   .. py:method:: retrieve_context(query: str, memory_types: list[str] | None = None) -> dict[str, Any]
      :async:


      Retrieve relevant context from all memory types.


      .. autolink-examples:: retrieve_context
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: conversation_memory


   .. py:attribute:: factual_memory


   .. py:attribute:: message_converter


   .. py:attribute:: preferences_memory


   .. py:attribute:: user_id
      :value: 'user_Instance of uuid.UUID'



.. py:function:: create_conversation_memory_agent(vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, embedding_model: str = 'sentence-transformers/all-mpnet-base-v2', enable_time_weighting: bool = True, name: str = 'conversation_memory') -> ConversationMemoryAgent

   Factory function to create conversation memory agent.


   .. autolink-examples:: create_conversation_memory_agent
      :collapse:

.. py:function:: create_unified_memory_agent(user_id: str | None = None, llm_config: haive.core.engine.aug_llm.AugLLMConfig = None, vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, embedding_model: str = 'sentence-transformers/all-mpnet-base-v2') -> UnifiedMemoryRAGAgent

   Factory function to create unified memory agent.


   .. autolink-examples:: create_unified_memory_agent
      :collapse:

.. py:function:: demo()
   :async:


.. py:data:: logger

