agents.document_modifiers.tnt.state
===================================

.. py:module:: agents.document_modifiers.tnt.state

.. autoapi-nested-parse::

   State management for taxonomy generation workflow.

   This module defines the state schema used throughout the taxonomy generation process.
   It provides a structured way to track documents, their groupings into minibatches,
   and the evolution of taxonomy clusters over multiple iterations.

   .. rubric:: Example

   Basic usage of the state class::

       state = TaxonomyGenerationState(
           documents=[Doc(id="1", content="text")],
           minibatches=[[0]],
           clusters=[[{"id": 1, "name": "Category"}]]
       )


   .. autolink-examples:: agents.document_modifiers.tnt.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_modifiers.tnt.state.TaxonomyGenerationState


Module Contents
---------------

.. py:class:: TaxonomyGenerationState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents the state passed between graph nodes in the taxonomy generation process.

   This class maintains the complete state of the taxonomy generation workflow,
   tracking raw documents, their organization into processing batches, and the
   history of taxonomy revisions.

   .. attribute:: documents

      List of document objects, each containing:
      - id: Unique identifier
      - content: Raw text
      - summary: Generated summary (added in first step)
      - explanation: Summary explanation (added in first step)
      - category: Assigned taxonomy category (added later)

      :type: List[Doc]

   .. attribute:: minibatches

      Groups of document indices for batch processing.
      Each inner list contains indices referencing documents in the documents list.

      :type: List[List[int]]

   .. attribute:: clusters

      History of taxonomy revisions. Each revision is a
      list of cluster dictionaries containing:
      - id: Cluster identifier
      - name: Category name
      - description: Category description

      :type: List[List[dict]]

   .. rubric:: Example

   >>> docs = [Doc(id="1", content="text")]
   >>> state = TaxonomyGenerationState(
   ...     documents=docs,
   ...     minibatches=[[0]],
   ...     clusters=[[{"id": 1, "name": "Tech", "description": "Technology"}]]
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaxonomyGenerationState
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document]) -> TaxonomyGenerationState
      :classmethod:


      Initialize state from a list of LangChain Document objects.


      .. autolink-examples:: from_documents
         :collapse:


   .. py:attribute:: clusters
      :type:  Annotated[list[list[dict]], operator.add]
      :value: None



   .. py:attribute:: documents
      :type:  list[haive.agents.document_modifiers.tnt.models.Doc]
      :value: None



   .. py:attribute:: minibatches
      :type:  list[list[int]]
      :value: None



