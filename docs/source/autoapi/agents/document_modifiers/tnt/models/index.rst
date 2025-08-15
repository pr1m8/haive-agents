agents.document_modifiers.tnt.models
====================================

.. py:module:: agents.document_modifiers.tnt.models

.. autoapi-nested-parse::

   Data models for taxonomy generation.

   This module defines the core data structures used in the taxonomy generation process,
   particularly the document model that represents individual pieces of content being
   processed.

   .. rubric:: Example

   Basic usage of document model::

       doc = Doc(
           id="doc1",
           content="Sample text",
           summary="Brief summary",
           explanation="Summary rationale",
           category="Technology"
       )


   .. autolink-examples:: agents.document_modifiers.tnt.models
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.document_modifiers.tnt.models.logger


Classes
-------

.. autoapisummary::

   agents.document_modifiers.tnt.models.Doc


Module Contents
---------------

.. py:class:: Doc(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a single document or chat log in the taxonomy generation process.

   This class serves as the fundamental data structure for content being processed
   through the taxonomy generation workflow. It tracks both the original content
   and metadata added during processing.

   .. attribute:: id

      Unique identifier for the document, used for tracking and reference.

      :type: str

   .. attribute:: content

      Original text content of the document or chat log.

      :type: str

   .. attribute:: summary

      Condensed version of the content, generated in the
      first step of processing. Defaults to empty string.

      :type: Optional[str]

   .. attribute:: explanation

      Rationale for how the summary was generated,
      added alongside the summary. Defaults to empty string.

      :type: Optional[str]

   .. attribute:: category

      Taxonomy category assigned to the document in
      later stages of processing. Defaults to empty string.

      :type: Optional[str]

   .. rubric:: Example

   >>> doc = Doc(
   ...     id="chat_123",
   ...     content="User asked about Python installation",
   ...     summary="Python setup inquiry",
   ...     explanation="Focused on main topic",
   ...     category="Technical Support"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Doc
      :collapse:

   .. py:method:: from_document(document: langchain_core.documents.Document) -> Doc
      :classmethod:



   .. py:attribute:: category
      :type:  str | None
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: explanation
      :type:  str | None
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict | None
      :value: None



   .. py:attribute:: summary
      :type:  str | None
      :value: None



.. py:data:: logger

