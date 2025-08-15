agents.document_modifiers.base.state
====================================

.. py:module:: agents.document_modifiers.base.state

.. autoapi-nested-parse::

   Base state schema for document modification agents.

   from typing import Any
   This module defines the DocumentModifierState class which serves as the
   foundation for all document processing agents in the haive framework.


   .. autolink-examples:: agents.document_modifiers.base.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_modifiers.base.state.DocumentModifierState


Module Contents
---------------

.. py:class:: DocumentModifierState

   Bases: :py:obj:`haive.core.schema.StateSchema`


   Base state schema for document modification agents.

   This class provides the core state management for all document processing
   operations. It handles document collections, provides computed properties
   for common operations, and includes validation to ensure data integrity.

   The state maintains a list of documents and provides utilities for:
   - Accessing combined document text
   - Counting documents
   - Adding/removing documents
   - Validating document collections

   .. attribute:: name

      Optional identifier for this document modifier instance.

   .. attribute:: description

      Optional description of the modifier's purpose.

   .. attribute:: documents

      List of Document objects to be processed.

   Properties:
       documents_text: Combined text content of all documents.
       num_documents: Total count of documents in the collection.

   .. rubric:: Example

   Creating and using document state::

       >>> from langchain_core.documents import Document
       >>> docs = [Document(page_content="Hello"), Document(page_content="World")]
       >>> state = DocumentModifierState.from_documents(docs)
       >>> print(state.documents_text)
       'Hello\\nWorld'
       >>> print(state.num_documents)
       2

   Adding documents dynamically::

       >>> new_doc = Document(page_content="New content")
       >>> state.documents.append(new_doc)
       >>> print(state.num_documents)
       3

   :raises ValueError: If no documents are provided (empty list).

   .. note::

      The state automatically validates that at least one document
      is present to prevent processing empty collections.


   .. autolink-examples:: DocumentModifierState
      :collapse:

   .. py:method:: add_document(document: langchain_core.documents.Document) -> DocumentModifierState
      :classmethod:


      Add a single document to the state.

      Note: This method has issues with the class method implementation.
      Consider using instance methods instead for document manipulation.

      :param document: Document to add to the collection.

      :returns: New state instance with the document added.


      .. autolink-examples:: add_document
         :collapse:


   .. py:method:: add_documents(documents: list[langchain_core.documents.Document]) -> DocumentModifierState
      :classmethod:


      Add multiple documents to the state.

      Note: This method has issues with the class method implementation.
      Consider using instance methods instead for document manipulation.

      :param documents: List of documents to add.

      :returns: New state instance with documents added.


      .. autolink-examples:: add_documents
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document]) -> DocumentModifierState
      :classmethod:


      Create a DocumentModifierState from a list of documents.

      This is a convenience factory method for creating state instances
      when you already have a collection of documents.

      :param documents: List of Document objects to initialize the state with.

      :returns: New DocumentModifierState instance containing the provided documents.

      :raises ValueError: If the documents list is empty.

      .. rubric:: Example

      >>> docs = [Document(page_content="Content 1"), Document(page_content="Content 2")]
      >>> state = DocumentModifierState.from_documents(docs)
      >>> print(state.num_documents)
      2


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: remove_document(document: langchain_core.documents.Document) -> DocumentModifierState
      :classmethod:


      Remove a specific document from the state.

      Note: This method has issues with the class method implementation.
      Consider using instance methods instead for document manipulation.

      :param document: Document to remove from the collection.

      :returns: New state instance with the document removed.


      .. autolink-examples:: remove_document
         :collapse:


   .. py:method:: remove_documents(documents: list[langchain_core.documents.Document]) -> DocumentModifierState
      :classmethod:


      Remove multiple documents from the state.

      Note: This method has issues with the class method implementation.
      Consider using instance methods instead for document manipulation.

      :param documents: List of documents to remove.

      :returns: New state instance with documents removed.


      .. autolink-examples:: remove_documents
         :collapse:


   .. py:method:: validate_documents() -> DocumentModifierState

      Validate that at least one document is present.

      This validator runs after model initialization to ensure
      the state contains at least one document for processing.

      :returns: Self if validation passes.

      :raises ValueError: If documents list is empty.


      .. autolink-examples:: validate_documents
         :collapse:


   .. py:method:: validate_documents_field(v) -> Any
      :classmethod:


      Validate the documents field during assignment.

      :param v: The documents list being validated.

      :returns: The validated documents list.

      .. note::

         This validator ensures type safety but allows empty lists
         during field assignment. The model validator handles the
         non-empty requirement.


      .. autolink-examples:: validate_documents_field
         :collapse:


   .. py:attribute:: description
      :type:  str | None
      :value: None



   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:property:: documents_text
      :type: str


      Get the combined text content of all documents.

      This property concatenates the page_content of all documents
      in the collection, separated by newlines. Useful for operations
      that need to process all document text at once.

      :returns: String containing all document texts joined by newlines.

      .. rubric:: Example

      >>> state.documents = [Document(page_content="First"), Document(page_content="Second")]
      >>> print(state.documents_text)
      'First\\nSecond'

      .. autolink-examples:: documents_text
         :collapse:


   .. py:attribute:: name
      :type:  str | None
      :value: None



   .. py:property:: num_documents
      :type: int


      Get the total number of documents in the collection.

      :returns: Integer count of documents currently in the state.

      .. rubric:: Example

      >>> print(f"Processing {state.num_documents} documents")
      Processing 5 documents

      .. autolink-examples:: num_documents
         :collapse:


