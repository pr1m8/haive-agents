agents.document_modifiers.kg.kg_map_merge.models
================================================

.. py:module:: agents.document_modifiers.kg.kg_map_merge.models


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.models.EntityNode
   agents.document_modifiers.kg.kg_map_merge.models.EntityRelationship
   agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph


Functions
---------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.models.main


Module Contents
---------------

.. py:class:: EntityNode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents an entity node in the knowledge graph.
   Extends the basic Node class with additional metadata and validation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EntityNode
      :collapse:

   .. py:method:: from_graph_node(node: langchain_community.graphs.graph_document.Node)
      :classmethod:


      Create an EntityNode from a GraphDocument Node.

      :param node: The input graph node
      :type node: Node

      :returns: Converted node with additional validation
      :rtype: EntityNode


      .. autolink-examples:: from_graph_node
         :collapse:


   .. py:method:: validate_node() -> EntityNode

      Validate the node properties.


      .. autolink-examples:: validate_node
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: type
      :type:  str
      :value: None



.. py:class:: EntityRelationship(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a relationship between two entities in a knowledge graph.
   Extends the basic Relationship class with additional metadata and validation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EntityRelationship
      :collapse:

   .. py:method:: from_graph_relationship(relationship: langchain_community.graphs.graph_document.Relationship, confidence_score: float = 0.5, supporting_evidence: str | None = None)
      :classmethod:


      Create an EntityRelationship from a GraphDocument Relationship.

      :param relationship: The input graph relationship
      :type relationship: Relationship
      :param confidence_score: Confidence score for the relationship
      :type confidence_score: float, optional
      :param supporting_evidence: Evidence supporting the relationship
      :type supporting_evidence: str, optional

      :returns: Converted relationship with additional validation
      :rtype: EntityRelationship


      .. autolink-examples:: from_graph_relationship
         :collapse:


   .. py:method:: validate_relationship() -> EntityRelationship

      Validate the relationship properties.


      .. autolink-examples:: validate_relationship
         :collapse:


   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: supporting_evidence
      :type:  str | None
      :value: None



   .. py:attribute:: target
      :type:  str
      :value: None



   .. py:attribute:: type
      :type:  str
      :value: None



.. py:class:: KnowledgeGraph(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a comprehensive knowledge graph.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeGraph
      :collapse:

   .. py:method:: add_node(node: EntityNode)

      Add a node to the knowledge graph.

      :param node: Node to add
      :type node: EntityNode


      .. autolink-examples:: add_node
         :collapse:


   .. py:method:: add_relationship(relationship: EntityRelationship)

      Add a relationship to the knowledge graph.

      :param relationship: Relationship to add
      :type relationship: EntityRelationship


      .. autolink-examples:: add_relationship
         :collapse:


   .. py:method:: merge(other_graph: KnowledgeGraph)

      Merge another knowledge graph into this one.

      :param other_graph: Graph to merge
      :type other_graph: KnowledgeGraph


      .. autolink-examples:: merge
         :collapse:


   .. py:attribute:: nodes
      :type:  list[EntityNode]
      :value: None



   .. py:attribute:: relationships
      :type:  list[EntityRelationship]
      :value: None



.. py:function:: main() -> None

