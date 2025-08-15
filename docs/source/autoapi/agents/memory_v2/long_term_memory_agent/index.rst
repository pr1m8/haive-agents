agents.memory_v2.long_term_memory_agent
=======================================

.. py:module:: agents.memory_v2.long_term_memory_agent

.. autoapi-nested-parse::

   Long-Term Memory Agent following LangChain patterns.

   This implementation follows the LangChain long-term memory agent documentation:
   https://python.langchain.com/docs/versions/migrating_memory/long_term_memory_agent/

   Key features:
   1. Load memories first approach
   2. Semantic memory retrieval across conversations
   3. Text and structured knowledge storage
   4. Time-weighted retrieval
   5. ReactAgent tool integration

   Architecture:
   - BaseRAGAgent for memory retrieval
   - SimpleRAGAgent for memory-enhanced responses
   - Memory extraction and storage pipeline
   - Cross-conversation persistence


   .. autolink-examples:: agents.memory_v2.long_term_memory_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.long_term_memory_agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.long_term_memory_agent.KnowledgeTriple
   agents.memory_v2.long_term_memory_agent.LongTermMemoryAgent
   agents.memory_v2.long_term_memory_agent.LongTermMemoryStore
   agents.memory_v2.long_term_memory_agent.MemoryEntry


Functions
---------

.. autoapisummary::

   agents.memory_v2.long_term_memory_agent.create_long_term_memory_agent
   agents.memory_v2.long_term_memory_agent.demo_long_term_memory


Module Contents
---------------

.. py:class:: KnowledgeTriple(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured knowledge in (subject, predicate, object) format.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeTriple
      :collapse:

   .. py:method:: to_memory_entry(**kwargs) -> MemoryEntry

      Convert to MemoryEntry.


      .. autolink-examples:: to_memory_entry
         :collapse:


   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: object
      :type:  str
      :value: None



   .. py:attribute:: predicate
      :type:  str
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: subject
      :type:  str
      :value: None



.. py:class:: LongTermMemoryAgent(user_id: str, llm_config: haive.core.models.llm.base.LLMConfig | None = None, storage_path: str = './memory_store', embedding_model: str = 'sentence-transformers/all-mpnet-base-v2', vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, name: str = 'long_term_memory_agent')

   Long-term memory agent following LangChain patterns.

   This agent implements the "load memories first" approach:
   1. Load relevant memories from storage
   2. Use BaseRAGAgent for semantic memory retrieval
   3. Enhanced response generation with memory context
   4. Extract and store new memories from conversation

   .. rubric:: Examples

   Basic usage::

       agent = LongTermMemoryAgent(user_id="user123")
       await agent.initialize()

       # Memory-enhanced conversation
       response = await agent.run("What do you remember about my work?")

   With specific LLM config::

       llm_config = AzureLLMConfig(deployment_name="gpt-4", ...)
       agent = LongTermMemoryAgent(
           user_id="user123",
           llm_config=llm_config
       )

   Initialize long-term memory agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LongTermMemoryAgent
      :collapse:

   .. py:method:: _extract_and_store_memories(query: str, response: str) -> None
      :async:


      Extract memories from query and response.


      .. autolink-examples:: _extract_and_store_memories
         :collapse:


   .. py:method:: _extract_memories_from_content(content: str) -> list[dict[str, Any]]

      Extract memories from content using heuristics.


      .. autolink-examples:: _extract_memories_from_content
         :collapse:


   .. py:method:: _refresh_agents() -> None
      :async:


      Refresh agents with updated memories.


      .. autolink-examples:: _refresh_agents
         :collapse:


   .. py:method:: add_conversation(messages: list[langchain_core.messages.BaseMessage]) -> list[MemoryEntry]
      :async:


      Add conversation and extract memories.


      .. autolink-examples:: add_conversation
         :collapse:


   .. py:method:: as_memory_tool(user_id: str, **config_kwargs)
      :classmethod:


      Create memory tool for ReactAgent integration.


      .. autolink-examples:: as_memory_tool
         :collapse:


   .. py:method:: get_memory_summary() -> dict[str, Any]

      Get summary of stored memories.


      .. autolink-examples:: get_memory_summary
         :collapse:


   .. py:method:: initialize() -> None
      :async:


      Initialize memory retrieval and enhanced response agents.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: run(query: str, extract_memories: bool = True) -> dict[str, Any]
      :async:


      Run memory-enhanced conversation.

      This implements the "load memories first" pattern:
      1. Retrieve relevant memories using BaseRAGAgent
      2. Generate enhanced response using SimpleRAGAgent with memory context
      3. Extract and store new memories from the interaction


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: _initialized
      :value: False



   .. py:attribute:: embedding_model


   .. py:attribute:: llm_config
      :value: None



   .. py:attribute:: memory_enhanced_agent
      :type:  haive.agents.rag.simple.agent.SimpleRAGAgent | None
      :value: None



   .. py:attribute:: memory_retriever
      :type:  haive.agents.rag.base.agent.BaseRAGAgent | None
      :value: None



   .. py:attribute:: memory_store


   .. py:attribute:: name
      :value: 'long_term_memory_agent'



   .. py:attribute:: user_id


   .. py:attribute:: vector_store_provider


.. py:class:: LongTermMemoryStore(storage_path: str = './memory_store')

   Persistent storage for long-term memories.

   Initialize memory store.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LongTermMemoryStore
      :collapse:

   .. py:method:: _load_memories() -> None

      Load memories from storage.


      .. autolink-examples:: _load_memories
         :collapse:


   .. py:method:: _save_memory(memory: MemoryEntry) -> None

      Save individual memory to file.


      .. autolink-examples:: _save_memory
         :collapse:


   .. py:method:: add_knowledge_triple(triple: KnowledgeTriple, **kwargs) -> MemoryEntry

      Add knowledge triple as memory.


      .. autolink-examples:: add_knowledge_triple
         :collapse:


   .. py:method:: add_memory(memory: MemoryEntry) -> None

      Add memory to store.


      .. autolink-examples:: add_memory
         :collapse:


   .. py:method:: get_memories(user_id: str | None = None, limit: int | None = None) -> list[MemoryEntry]

      Get memories, optionally filtered by user.


      .. autolink-examples:: get_memories
         :collapse:


   .. py:method:: search_memories(query: str, user_id: str | None = None, limit: int = 5) -> list[MemoryEntry]

      Simple text search in memories.


      .. autolink-examples:: search_memories
         :collapse:


   .. py:attribute:: knowledge_triples
      :type:  dict[str, KnowledgeTriple]


   .. py:attribute:: memories
      :type:  dict[str, MemoryEntry]


   .. py:attribute:: storage_path


.. py:class:: MemoryEntry(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual memory entry with timestamp and metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryEntry
      :collapse:

   .. py:method:: mark_accessed(query: str | None = None, relevance: float | None = None)

      Mark memory as accessed.


      .. autolink-examples:: mark_accessed
         :collapse:


   .. py:method:: to_document() -> langchain_core.documents.Document

      Convert to LangChain Document for RAG.


      .. autolink-examples:: to_document
         :collapse:


   .. py:attribute:: access_count
      :type:  int
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
      :type:  float
      :value: None



   .. py:attribute:: last_accessed
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: memory_type
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: relevance_scores
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: session_id
      :type:  str | None
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



   .. py:attribute:: updated_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: user_id
      :type:  str | None
      :value: None



.. py:function:: create_long_term_memory_agent(user_id: str, llm_config: haive.core.models.llm.base.LLMConfig | None = None, storage_path: str = './memory_store') -> LongTermMemoryAgent

   Factory function to create long-term memory agent.


   .. autolink-examples:: create_long_term_memory_agent
      :collapse:

.. py:function:: demo_long_term_memory()
   :async:


   Demo the long-term memory agent functionality.


   .. autolink-examples:: demo_long_term_memory
      :collapse:

.. py:data:: logger

