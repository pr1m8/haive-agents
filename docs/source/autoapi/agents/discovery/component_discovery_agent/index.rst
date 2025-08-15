agents.discovery.component_discovery_agent
==========================================

.. py:module:: agents.discovery.component_discovery_agent

.. autoapi-nested-parse::

   Component Discovery Agent for Dynamic Activation.

   This module provides ComponentDiscoveryAgent, a RAG-based agent for discovering
   components from documentation. It uses MetaStateSchema for tracking and follows
   the Dynamic Activation Pattern.

   Based on: @project_docs/active/patterns/dynamic_activation_pattern.md


   .. autolink-examples:: agents.discovery.component_discovery_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.discovery.component_discovery_agent.logger


Classes
-------

.. autoapisummary::

   agents.discovery.component_discovery_agent.ComponentDiscoveryAgent


Module Contents
---------------

.. py:class:: ComponentDiscoveryAgent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   RAG-based agent for discovering components from documentation.

   This agent uses retrieval-augmented generation to find components that
   can satisfy specific requirements. It wraps a BaseRAGAgent in MetaStateSchema
   for tracking and recompilation support.

   Key Features:
       - RAG-based component discovery from documentation
       - MetaStateSchema integration for tracking
       - Automatic document loading from various sources
       - Component parsing and metadata extraction
       - Caching for performance
       - Error handling and logging

   :param document_path: Path to documentation or component sources
   :param discovery_agent: BaseRAGAgent for performing retrieval
   :param meta_state: MetaStateSchema wrapper for the discovery agent
   :param discovery_config: Configuration for discovery behavior
   :param component_cache: Cache for discovered components

   .. rubric:: Examples

   Basic usage::

       from haive.agents.discovery.component_discovery_agent import ComponentDiscoveryAgent

       # Create discovery agent
       agent = ComponentDiscoveryAgent(
           document_path="@haive-tools/docs"
       )

       # Discover components
       components = await agent.discover_components("math tools")

       for comp in components:
           print(f"Found: {comp['name']} - {comp['description']}")

   With custom configuration::

       agent = ComponentDiscoveryAgent(
           document_path="/path/to/docs",
           discovery_config={
               "max_results": 5,
               "similarity_threshold": 0.7,
               "use_cache": True
           }
       )

       # Discover specific capabilities
       components = await agent.discover_components(
           "tools for data visualization and charting"
       )

   From Haive components::

       # Use HaiveComponentDiscovery for automatic loading
       agent = ComponentDiscoveryAgent(
           document_path="@haive-tools"
       )

       # Find tools that can handle specific tasks
       tools = await agent.discover_components("file processing tools")

       # Parse and load actual tool instances
       for tool_doc in tools:
           tool_instance = await agent.load_component_from_doc(tool_doc)
           if tool_instance:
               print(f"Loaded tool: {tool_instance.name}")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComponentDiscoveryAgent
      :collapse:

   .. py:method:: _extract_description(doc: langchain_core.documents.Document) -> str

      Extract description from document content.

      :param doc: Document to extract description from

      :returns: Extracted description string


      .. autolink-examples:: _extract_description
         :collapse:


   .. py:method:: _is_relevant_document(doc: langchain_core.documents.Document, output: str) -> bool

      Check if a document is relevant to the discovery output.

      :param doc: Document to check
      :param output: Discovery output

      :returns: True if document is relevant


      .. autolink-examples:: _is_relevant_document
         :collapse:


   .. py:method:: _load_at_notation(path: str) -> list[langchain_core.documents.Document]

      Load documents from @ notation paths.

      :param path: Path with @ notation

      :returns: List of Document objects


      .. autolink-examples:: _load_at_notation
         :collapse:


   .. py:method:: _load_documents(path: str) -> list[langchain_core.documents.Document]

      Load documents from the specified path.

      :param path: Path to documents (supports @haive-* notation)

      :returns: List of Document objects


      .. autolink-examples:: _load_documents
         :collapse:


   .. py:method:: _load_from_filesystem(path: str) -> list[langchain_core.documents.Document]

      Load documents from filesystem path.

      :param path: Filesystem path

      :returns: List of Document objects


      .. autolink-examples:: _load_from_filesystem
         :collapse:


   .. py:method:: _load_haive_components(path: str) -> list[langchain_core.documents.Document]

      Load components using HaiveComponentDiscovery.

      :param path: Path in @haive-* format

      :returns: List of Document objects


      .. autolink-examples:: _load_haive_components
         :collapse:


   .. py:method:: _parse_components(output: str) -> list[dict[str, Any]]

      Parse component data from discovery output.

      :param output: Raw output from discovery agent

      :returns: List of parsed component dictionaries


      .. autolink-examples:: _parse_components
         :collapse:


   .. py:method:: _setup_fallback_agent() -> None

      Setup a minimal fallback agent when initialization fails.


      .. autolink-examples:: _setup_fallback_agent
         :collapse:


   .. py:method:: clear_cache() -> None

      Clear the component cache.

      .. rubric:: Examples

      Clear cache::

          agent.clear_cache()
          print("Cache cleared")


      .. autolink-examples:: clear_cache
         :collapse:


   .. py:method:: discover_components(query: str) -> list[dict[str, Any]]
      :async:


      Discover components based on a query.

      :param query: Natural language query describing needed components

      :returns: List of component dictionaries with metadata

      .. rubric:: Examples

      Discover math tools::

          components = await agent.discover_components("math and calculation tools")

      Discover with specific requirements::

          components = await agent.discover_components(
              "tools for file processing and data extraction"
          )


      .. autolink-examples:: discover_components
         :collapse:


   .. py:method:: get_cache_stats() -> dict[str, Any]

      Get statistics about the component cache.

      :returns: Dictionary with cache statistics

      .. rubric:: Examples

      Check cache status::

          stats = agent.get_cache_stats()
          print(f"Cached queries: {stats['cached_queries']}")
          print(f"Total components: {stats['total_components']}")


      .. autolink-examples:: get_cache_stats
         :collapse:


   .. py:method:: load_component_from_doc(component_doc: dict[str, Any]) -> Any | None
      :async:


      Load actual component instance from component document.

      :param component_doc: Component dictionary from discovery

      :returns: Loaded component instance or None if loading fails

      .. rubric:: Examples

      Load discovered component::

          components = await agent.discover_components("calculator")
          for comp_doc in components:
              instance = await agent.load_component_from_doc(comp_doc)
              if instance:
                  print(f"Loaded: {instance}")


      .. autolink-examples:: load_component_from_doc
         :collapse:


   .. py:method:: setup_discovery_agent() -> ComponentDiscoveryAgent

      Initialize the discovery agent after model creation.

      This validator:
      1. Loads documents from the specified path
      2. Creates BaseRAGAgent with documents
      3. Wraps agent in MetaStateSchema
      4. Sets up configuration defaults
      5. Initializes caching system


      .. autolink-examples:: setup_discovery_agent
         :collapse:


   .. py:attribute:: _documents
      :type:  list[langchain_core.documents.Document] | None
      :value: None



   .. py:attribute:: _haive_discovery
      :type:  haive.core.utils.haive_discovery.HaiveComponentDiscovery | None
      :value: None



   .. py:attribute:: component_cache
      :type:  dict[str, list[dict[str, Any]]]
      :value: None



   .. py:attribute:: discovery_agent
      :type:  haive.agents.rag.base.agent.BaseRAGAgent | None
      :value: None



   .. py:attribute:: discovery_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: document_path
      :type:  str
      :value: None



   .. py:attribute:: meta_state
      :type:  haive.core.schema.prebuilt.meta_state.MetaStateSchema | None
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


.. py:data:: logger

