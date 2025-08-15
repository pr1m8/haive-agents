agents.document_modifiers.kg.kg_base.models
===========================================

.. py:module:: agents.document_modifiers.kg.kg_base.models

.. autoapi-nested-parse::

   Core models for knowledge graph document transformation.

   This module provides the fundamental GraphTransformer class for converting
   documents into knowledge graphs using LLM-based extraction techniques.


   .. autolink-examples:: agents.document_modifiers.kg.kg_base.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_base.models.GraphTransformer


Module Contents
---------------

.. py:class:: GraphTransformer

   Bases: :py:obj:`langchain_core.documents.BaseDocumentTransformer`


   A document transformer that converts documents into knowledge graphs.

   This transformer uses LLM-based extraction to identify entities, relationships,
   and their properties from unstructured text documents. It builds structured
   knowledge graphs that can be used for various downstream tasks.

   The transformer supports both strict and flexible modes, allowing users to
   define specific entity types and relationship patterns or let the LLM
   discover them automatically.

   .. rubric:: Examples

   Basic entity and relationship extraction::

       from haive.agents.document_modifiers.kg.kg_base.models import GraphTransformer
       from langchain_core.documents import Document

       transformer = GraphTransformer()
       docs = [Document(page_content="John works at Acme Corp in Boston.")]
       graphs = transformer.transform_documents(
           documents=docs,
           allowed_nodes=["Person", "Organization", "Location"],
           allowed_relationships=[
               ("Person", "WORKS_FOR", "Organization"),
               ("Organization", "LOCATED_IN", "Location")
           ]
       )

       # Access extracted entities and relationships
       for graph in graphs:
           print(f"Entities: {[node.id for node in graph.nodes]}")
           print(f"Relations: {[rel.type for rel in graph.relationships]}")

   With property extraction::

       graphs = transformer.transform_documents(
           documents=docs,
           allowed_nodes=["Person", "Organization"],
           allowed_relationships=[("Person", "WORKS_FOR", "Organization")],
           node_properties=["role", "founded_year"],
           relationship_properties=["since", "department"],
           additional_instructions="Extract job roles and employment details."
       )

   .. attribute:: None - This class is stateless and can be reused for multiple transformations.

      


   .. autolink-examples:: GraphTransformer
      :collapse:

   .. py:method:: transform_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig = AzureLLMConfig(), allowed_nodes: list[str] | None = None, allowed_relationships: list[str] | list[tuple[str, str, str]] | None = None, prompt: langchain_core.prompts.ChatPromptTemplate | None = None, strict_mode: bool = True, node_properties: bool | list[str] = False, relationship_properties: bool | list[str] = False, ignore_tool_usage: bool = True, additional_instructions: str = '') -> list[langchain_neo4j.graphs.graph_document.GraphDocument]

      Transform documents into knowledge graphs using LLM-based extraction.

      Processes a list of documents and extracts entities, relationships, and
      their properties to construct structured knowledge graphs. The method
      supports various configuration options to control the extraction process.

      :param documents: List of documents to transform into graphs. Each document
                        should contain meaningful text content for entity extraction.
      :param llm_config: Configuration for the LLM to use for extraction.
                         Defaults to AzureLLMConfig() for Azure OpenAI integration.
      :param allowed_nodes: List of allowed entity types (e.g., ["Person", "Organization"]).
                            If None or empty, the LLM will discover entity types automatically.
      :param allowed_relationships: List of allowed relationship types or tuples.
                                    Can be either:
                                    - List of relationship names: ["WORKS_FOR", "LOCATED_IN"]
                                    - List of (source, relation, target) tuples: [("Person", "WORKS_FOR", "Organization")]
                                    If None or empty, the LLM will discover relationships automatically.
      :param prompt: Custom prompt template for extraction. If None, uses the
                     default LLMGraphTransformer prompt.
      :param strict_mode: Whether to enforce strict adherence to allowed_nodes and
                          allowed_relationships. If True, only specified types are extracted.
                          If False, additional types may be discovered.
      :param node_properties: Properties to extract for entities. Can be:
                              - False: No properties extracted
                              - True: Extract all discoverable properties
                              - List[str]: Extract specific properties by name
      :param relationship_properties: Properties to extract for relationships.
                                      Follows same format as node_properties.
      :param ignore_tool_usage: Whether to ignore function calling capabilities
                                for property extraction. If True, uses text-based extraction only.
      :param additional_instructions: Additional instructions to guide the LLM
                                      during extraction (e.g., "Focus on temporal relationships").

      :returns: List of GraphDocument objects, one per input document. Each
                GraphDocument contains:
                - nodes: List of extracted entities with their properties
                - relationships: List of extracted relationships with their properties
                - source: Reference to the original document

      :raises TypeError: If allowed_relationships is not a list.
      :raises ValueError: If documents list is empty or contains invalid documents.
      :raises LLMError: If the LLM fails to process the documents.

      .. rubric:: Example

      Extract entities and relationships from multiple documents::

          docs = [
              Document(page_content="Alice works at TechCorp as a software engineer."),
              Document(page_content="TechCorp is located in San Francisco."),
              Document(page_content="Bob also works at TechCorp in the marketing department.")
          ]

          graphs = transformer.transform_documents(
              documents=docs,
              allowed_nodes=["Person", "Organization", "Location"],
              allowed_relationships=[
                  ("Person", "WORKS_FOR", "Organization"),
                  ("Organization", "LOCATED_IN", "Location")
              ],
              node_properties=["role", "department"],
              relationship_properties=["since"]
          )

          # Process results
          for i, graph in enumerate(graphs):
              print(f"Document {i+1} extracted {len(graph.nodes)} entities")
              for node in graph.nodes:
                  print(f"  Entity: {node.id} ({node.type})")
                  if node.properties:
                      print(f"    Properties: {node.properties}")

      .. note::

         Property extraction requires LLMs with function calling capabilities.
         If the LLM doesn't support function calling, node_properties and
         relationship_properties will be ignored to prevent errors.


      .. autolink-examples:: transform_documents
         :collapse:


