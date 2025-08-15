agents.document_modifiers.kg.kg_map_merge.state
===============================================

.. py:module:: agents.document_modifiers.kg.kg_map_merge.state


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.state.KnowledgeGraphState


Module Contents
---------------

.. py:class:: KnowledgeGraphState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State model for the parallel knowledge graph transformer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeGraphState
      :collapse:

   .. py:method:: should_continue() -> Literal['map_graph_documents', 'map_nodes', 'map_relationships', 'merge_graphs', 'end']

      Determine the next step in the graph creation process.


      .. autolink-examples:: should_continue
         :collapse:


   .. py:attribute:: contents
      :type:  list[langchain_core.documents.Document]


   .. py:attribute:: final_knowledge_graph
      :type:  haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph | None
      :value: None



   .. py:attribute:: graph_documents
      :type:  Annotated[list[langchain_community.graphs.graph_document.GraphDocument], operator.add]
      :value: None



   .. py:attribute:: index
      :type:  int
      :value: None



   .. py:attribute:: knowledge_graphs
      :type:  Annotated[list[haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph], operator.add]
      :value: None



   .. py:attribute:: nodes
      :type:  list[haive.agents.document_modifiers.kg.kg_map_merge.models.EntityNode]
      :value: None



   .. py:attribute:: relationships
      :type:  list[haive.agents.document_modifiers.kg.kg_map_merge.models.EntityRelationship]
      :value: None



