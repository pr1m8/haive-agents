agents.document_modifiers.kg.kg_map_merge.utils
===============================================

.. py:module:: agents.document_modifiers.kg.kg_map_merge.utils


Functions
---------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.utils.create_knowledge_graph
   agents.document_modifiers.kg.kg_map_merge.utils.visualize_graph


Module Contents
---------------

.. py:function:: create_knowledge_graph(documents: list[str | langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, allowed_nodes: list[str] | None = None, allowed_relationships: list[str] | list[tuple[str, str, str]] | None = None, node_properties: bool | list[str] = False, relationship_properties: bool | list[str] = False, additional_transformer_args: dict[str, Any] | None = None, custom_system_prompt: str | None = None) -> langchain_neo4j.graphs.graph_document.GraphDocument
   :async:


   Create a knowledge graph from multiple documents using parallel processing.

   :param documents: List of documents or text strings
   :param llm_config: LLM configuration to use
   :param allowed_nodes: List of allowed node types (optional)
   :param allowed_relationships: List of allowed relationship types (optional)
   :param node_properties: Whether to extract node properties and which ones
   :param relationship_properties: Whether to extract relationship properties and which ones
   :param additional_transformer_args: Additional arguments for the GraphTransformer
   :param custom_system_prompt: Custom system prompt for graph extraction

   :returns: The merged knowledge graph


   .. autolink-examples:: create_knowledge_graph
      :collapse:

.. py:function:: visualize_graph(graph_document: langchain_neo4j.graphs.graph_document.GraphDocument, output_file: str = 'knowledge_graph.png')

   Visualize the graph document using NetworkX and matplotlib.


   .. autolink-examples:: visualize_graph
      :collapse:

