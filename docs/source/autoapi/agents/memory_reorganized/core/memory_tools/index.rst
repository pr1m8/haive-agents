
:py:mod:`agents.memory_reorganized.core.memory_tools`
=====================================================

.. py:module:: agents.memory_reorganized.core.memory_tools

Memory tools for modular memory operations.

Provides separate tools for memory operations following proper Haive patterns. Tools are
designed to be used by memory agents and can be easily tested and composed together.


.. autolink-examples:: agents.memory_reorganized.core.memory_tools
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.core.memory_tools.MemoryConfig
   agents.memory_reorganized.core.memory_tools.MemoryMetadata


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryConfig {
        node [shape=record];
        "MemoryConfig" [label="MemoryConfig"];
        "pydantic.BaseModel" -> "MemoryConfig";
      }

.. autopydantic_model:: agents.memory_reorganized.core.memory_tools.MemoryConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryMetadata:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryMetadata {
        node [shape=record];
        "MemoryMetadata" [label="MemoryMetadata"];
        "pydantic.BaseModel" -> "MemoryMetadata";
      }

.. autopydantic_model:: agents.memory_reorganized.core.memory_tools.MemoryMetadata
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.memory_reorganized.core.memory_tools._get_storage_key
   agents.memory_reorganized.core.memory_tools._load_memories_from_file
   agents.memory_reorganized.core.memory_tools._save_memories_to_file
   agents.memory_reorganized.core.memory_tools.classify_memory
   agents.memory_reorganized.core.memory_tools.get_memory_stats
   agents.memory_reorganized.core.memory_tools.retrieve_memory
   agents.memory_reorganized.core.memory_tools.search_memory
   agents.memory_reorganized.core.memory_tools.store_memory

.. py:function:: _get_storage_key(namespace: str = 'default') -> str

   Get storage key for a namespace.


   .. autolink-examples:: _get_storage_key
      :collapse:

.. py:function:: _load_memories_from_file(storage_path: str, namespace: str = 'default') -> list[haive.agents.memory_reorganized.core.memory_state_original.EnhancedMemoryItem]

   Load memories from JSON file.


   .. autolink-examples:: _load_memories_from_file
      :collapse:

.. py:function:: _save_memories_to_file(memories: list[haive.agents.memory_reorganized.core.memory_state_original.EnhancedMemoryItem], storage_path: str, namespace: str = 'default') -> None

   Save memories to JSON file.


   .. autolink-examples:: _save_memories_to_file
      :collapse:

.. py:function:: classify_memory(content: str, context: str | None = None, config: dict[str, Any] | None = None) -> dict[str, Any]

   Classify memory type and extract metadata.

   Analyzes memory content to automatically determine memory type,
   importance level, and extract relevant metadata like entities and tags.

   :param content: Memory content to classify
   :param context: Optional context for better classification
   :param config: Optional configuration override

   :returns: Dictionary with classification results and extracted metadata

   .. rubric:: Examples

   Basic classification::

       result = classify_memory("I met Alice at the conference")
       print(result["memory_type"])  # "episodic"
       print(result["entities"])     # ["Alice"]

   With context::

       result = classify_memory(
           "The project deadline is next Friday",
           context="work meeting discussion"
       )


   .. autolink-examples:: classify_memory
      :collapse:

.. py:function:: get_memory_stats(namespace: str = 'default', config: dict[str, Any] | None = None) -> dict[str, Any]

   Get comprehensive statistics about stored memories.

   Provides detailed analytics about memory storage, including
   counts by type and importance, performance metrics, and usage patterns.

   :param namespace: Namespace to analyze
   :param config: Optional configuration override

   :returns: Dictionary with comprehensive memory statistics

   .. rubric:: Examples

   Get basic stats::

       stats = get_memory_stats()
       print(f"Total memories: {stats['total_memories']}")
       print(f"Memory types: {stats['memory_types']}")


   .. autolink-examples:: get_memory_stats
      :collapse:

.. py:function:: retrieve_memory(query: str, memory_type: str | None = None, importance_filter: list[str] | None = None, limit: int = 5, namespace: str = 'default', config: dict[str, Any] | None = None) -> list[dict[str, Any]]

   Retrieve memories based on query and filters.

   Searches for relevant memories using content similarity and metadata filters.
   Returns the most relevant memories sorted by relevance score.

   :param query: Search query to find relevant memories
   :param memory_type: Filter by specific memory type
   :param importance_filter: Filter by importance levels
   :param limit: Maximum number of memories to return
   :param namespace: Namespace to search in
   :param config: Optional configuration override

   :returns: List of memory dictionaries with content, metadata, and similarity scores

   .. rubric:: Examples

   Basic retrieval::

       memories = retrieve_memory("coffee preferences")
       for memory in memories:
           print(f"Content: {memory['content']}")
           print(f"Score: {memory['similarity_score']}")

   Filtered retrieval::

       memories = retrieve_memory(
           "research work",
           memory_type="episodic",
           importance_filter=["high", "critical"]
       )


   .. autolink-examples:: retrieve_memory
      :collapse:

.. py:function:: search_memory(query: str | None = None, filters: dict[str, Any] | None = None, sort_by: str = 'timestamp', sort_order: str = 'desc', limit: int = 10, namespace: str = 'default', config: dict[str, Any] | None = None) -> list[dict[str, Any]]

   Search memories with flexible filtering and sorting options.

   Provides advanced search capabilities with multiple filter options
   and sorting criteria for comprehensive memory exploration.

   :param query: Optional text query for content search
   :param filters: Dictionary of filters to apply
   :param sort_by: Field to sort by (timestamp, importance, retrieval_count)
   :param sort_order: Sort order (asc, desc)
   :param limit: Maximum number of results
   :param namespace: Namespace to search in
   :param config: Optional configuration override

   :returns: List of memory dictionaries matching the search criteria

   .. rubric:: Examples

   Search by filters::

       memories = search_memory(
           filters={
               "memory_type": "semantic",
               "importance": ["high", "critical"],
               "tags": ["work", "projects"]
           }
       )

   Search with query and sorting::

       memories = search_memory(
           query="coffee",
           sort_by="retrieval_count",
           sort_order="desc"
       )


   .. autolink-examples:: search_memory
      :collapse:

.. py:function:: store_memory(content: str, memory_type: str = 'semantic', importance: str = 'medium', tags: list[str] | None = None, context_id: str | None = None, namespace: str = 'default', config: dict[str, Any] | None = None) -> str

   Store a memory with classification and metadata.

   Stores a memory entry with automatic classification, metadata extraction,
   and optional embedding generation for similarity search.

   :param content: The memory content to store
   :param memory_type: Type of memory (semantic, episodic, procedural)
   :param importance: Importance level (critical, high, medium, low, transient)
   :param tags: Optional list of tags for categorization
   :param context_id: Optional ID to group related memories
   :param namespace: Namespace for memory organization
   :param config: Optional configuration override

   :returns: String indicating success and memory ID

   .. rubric:: Examples

   Basic usage::

       result = store_memory("I prefer coffee over tea", "semantic", "medium")
       # Returns: "Memory stored successfully with ID: uuid-string"

   With tags and context::

       result = store_memory(
           "Alice introduced herself as a researcher",
           memory_type="episodic",
           tags=["people", "introductions"],
           context_id="meeting_2024_01_15"
       )


   .. autolink-examples:: store_memory
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.core.memory_tools
   :collapse:
   
.. autolink-skip:: next
