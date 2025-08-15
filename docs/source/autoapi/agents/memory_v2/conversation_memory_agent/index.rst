agents.memory_v2.conversation_memory_agent
==========================================

.. py:module:: agents.memory_v2.conversation_memory_agent

.. autoapi-nested-parse::

   Conversation Memory Agent using BaseRAGAgent.

   This module provides conversation memory storage and retrieval using BaseRAGAgent
   with semantic search over conversation history and optional time-weighting.


   .. autolink-examples:: agents.memory_v2.conversation_memory_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.conversation_memory_agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.conversation_memory_agent.ConversationMemoryAgent
   agents.memory_v2.conversation_memory_agent.ConversationMemoryConfig
   agents.memory_v2.conversation_memory_agent.MessageDocumentConverter


Functions
---------

.. autoapisummary::

   agents.memory_v2.conversation_memory_agent.demo_conversation_memory


Module Contents
---------------

.. py:class:: ConversationMemoryAgent(config: ConversationMemoryConfig = None, name: str = 'conversation_memory', user_id: str | None = None)

   Memory agent for conversation history using BaseRAGAgent.

   This agent provides:
   - Semantic search over conversation history
   - Automatic message-to-document conversion
   - Real BaseRAGAgent integration with vector stores
   - Incremental conversation updates
   - Time-weighted retrieval (optional)

   .. rubric:: Examples

   Basic usage::

       agent = ConversationMemoryAgent("user_123")
       await agent.initialize()

       # Add conversation
       messages = [HumanMessage("I work at Google")]
       await agent.add_conversation(messages)

       # Retrieve context
       docs = await agent.retrieve_context("Where do I work?")

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


   .. py:method:: create(user_id: str | None = None, vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, embedding_model: str = 'sentence-transformers/all-mpnet-base-v2', name: str = 'conversation_memory') -> ConversationMemoryAgent
      :classmethod:


      Factory method to create ConversationMemoryAgent.


      .. autolink-examples:: create
         :collapse:


   .. py:method:: get_conversation_summary() -> dict[str, Any]
      :async:


      Get summary of stored conversations.


      .. autolink-examples:: get_conversation_summary
         :collapse:


   .. py:method:: initialize() -> None
      :async:


      Initialize the underlying RAG agent.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: retrieve_context(query: str, k: int | None = None) -> list[langchain_core.documents.Document]
      :async:


      Retrieve relevant conversation context using BaseRAGAgent.

      :param query: Search query
      :param k: Number of documents to retrieve

      :returns: List of relevant conversation documents


      .. autolink-examples:: retrieve_context
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



   .. py:attribute:: user_id
      :value: 'user_Instance of uuid.UUID'



.. py:class:: ConversationMemoryConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for ConversationMemoryAgent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConversationMemoryConfig
      :collapse:

   .. py:attribute:: embedding_model
      :type:  haive.core.models.embeddings.base.HuggingFaceEmbeddingConfig
      :value: None



   .. py:attribute:: enable_time_weighting
      :type:  bool
      :value: None



   .. py:attribute:: max_memories_per_query
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: recency_weight
      :type:  float
      :value: None



   .. py:attribute:: similarity_threshold
      :type:  float
      :value: None



   .. py:attribute:: time_decay_rate
      :type:  float
      :value: None



   .. py:attribute:: vector_store_provider
      :type:  haive.core.engine.vectorstore.VectorStoreProvider
      :value: None



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



.. py:function:: demo_conversation_memory()
   :async:


   Demo conversation memory agent functionality.


   .. autolink-examples:: demo_conversation_memory
      :collapse:

.. py:data:: logger

