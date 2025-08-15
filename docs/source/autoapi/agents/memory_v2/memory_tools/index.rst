agents.memory_v2.memory_tools
=============================

.. py:module:: agents.memory_v2.memory_tools

.. autoapi-nested-parse::

   Memory tools for modular memory operations.

   Provides separate tools for memory operations following proper Haive patterns.
   Tools are designed to be used by memory agents and can be easily tested
   and composed together.


   .. autolink-examples:: agents.memory_v2.memory_tools
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.memory_tools._MEMORY_CONFIG
   agents.memory_v2.memory_tools._MEMORY_STORAGE


Classes
-------

.. autoapisummary::

   agents.memory_v2.memory_tools.MemoryConfig
   agents.memory_v2.memory_tools.MemoryMetadata


Functions
---------

.. autoapisummary::

   agents.memory_v2.memory_tools._get_storage_key
   agents.memory_v2.memory_tools._load_memories_from_file
   agents.memory_v2.memory_tools._save_memories_to_file
   agents.memory_v2.memory_tools.classify_memory
   agents.memory_v2.memory_tools.get_memory_stats
   agents.memory_v2.memory_tools.retrieve_memory
   agents.memory_v2.memory_tools.search_memory
   agents.memory_v2.memory_tools.store_memory


Module Contents
---------------

.. py:class:: MemoryConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for memory operations.

   Provides centralized configuration for memory storage, retrieval,
   and classification operations with proper validation.

   .. attribute:: storage_backend

      Backend for memory storage (json_file, sqlite, neo4j, vector_db)

   .. attribute:: storage_path

      Path for file-based storage backends

   .. attribute:: max_memories

      Maximum number of memories to store (-1 for unlimited)

   .. attribute:: memory_ttl

      Time-to-live for memories in seconds (-1 for permanent)

   .. attribute:: enable_embedding

      Whether to generate embeddings for similarity search

   .. attribute:: embedding_model

      Model to use for embeddings

   .. attribute:: similarity_threshold

      Minimum similarity score for retrieval

   .. attribute:: classification_enabled

      Whether to automatically classify memories

   .. attribute:: auto_cleanup

      Whether to automatically clean up old/low-importance memories

   .. attribute:: cache_size

      Size of in-memory cache for frequently accessed memories

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryConfig
      :collapse:

   .. py:method:: validate_storage_path(v, info)
      :classmethod:


      Validate storage path based on backend.


      .. autolink-examples:: validate_storage_path
         :collapse:


   .. py:attribute:: auto_cleanup
      :type:  bool
      :value: None



   .. py:attribute:: cache_size
      :type:  int
      :value: None



   .. py:attribute:: classification_enabled
      :type:  bool
      :value: None



   .. py:attribute:: embedding_model
      :type:  str
      :value: None



   .. py:attribute:: enable_embedding
      :type:  bool
      :value: None



   .. py:attribute:: max_memories
      :type:  int
      :value: None



   .. py:attribute:: memory_ttl
      :type:  int
      :value: None



   .. py:attribute:: similarity_threshold
      :type:  float
      :value: None



   .. py:attribute:: storage_backend
      :type:  str
      :value: None



   .. py:attribute:: storage_path
      :type:  str | None
      :value: None



.. py:class:: MemoryMetadata(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   !!! abstract "Usage Documentation"
       [Models](../concepts/models.md)

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of the class variables defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The core schema of the model.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

   .. attribute:: __pydantic_serializer__

      The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The `pydantic-core` `SchemaValidator` used to validate instances of the model.

   .. attribute:: __pydantic_fields__

      A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.

   .. attribute:: __pydantic_computed_fields__

      A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

   .. attribute:: __pydantic_extra__

      A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
      is set to `'allow'`.

   .. attribute:: __pydantic_fields_set__

      The names of fields explicitly set during instantiation.

   .. attribute:: __pydantic_private__

      Values of private attributes set on the model instance.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryMetadata
      :collapse:

   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: importance
      :type:  float
      :value: None



   .. py:attribute:: memory_type
      :type:  str
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



.. py:function:: _get_storage_key(namespace: str = 'default') -> str

   Get storage key for a namespace.


   .. autolink-examples:: _get_storage_key
      :collapse:

.. py:function:: _load_memories_from_file(storage_path: str, namespace: str = 'default') -> list[agents.memory_v2.memory_state_original.EnhancedMemoryItem]

   Load memories from JSON file.


   .. autolink-examples:: _load_memories_from_file
      :collapse:

.. py:function:: _save_memories_to_file(memories: list[agents.memory_v2.memory_state_original.EnhancedMemoryItem], storage_path: str, namespace: str = 'default') -> None

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

.. py:data:: _MEMORY_CONFIG
   :type:  MemoryConfig | None
   :value: None


.. py:data:: _MEMORY_STORAGE
   :type:  dict[str, list[agents.memory_v2.memory_state_original.EnhancedMemoryItem]]

