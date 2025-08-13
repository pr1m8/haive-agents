
:py:mod:`agents.document_modifiers.base.utils`
==============================================

.. py:module:: agents.document_modifiers.base.utils

Utility functions for document processing.


.. autolink-examples:: agents.document_modifiers.base.utils
   :collapse:


Functions
---------

.. autoapisummary::

   agents.document_modifiers.base.utils.documents_to_strings
   agents.document_modifiers.base.utils.normalize_contents
   agents.document_modifiers.base.utils.strings_to_documents

.. py:function:: documents_to_strings(documents: list[langchain_core.documents.Document]) -> list[str]

   Convert a list of Documents to a list of strings.


   .. autolink-examples:: documents_to_strings
      :collapse:

.. py:function:: normalize_contents(contents: Any) -> list[str]

   Normalize inputs to strings.

   Accepts:
   - List[str]
   - List[Document]
   - Mixed list of strings and documents
   - Single string or Document

   :param contents: The content to normalize

   :returns: List of strings extracted from the input

   :raises TypeError: If unsupported content type is encountered


   .. autolink-examples:: normalize_contents
      :collapse:

.. py:function:: strings_to_documents(strings: list[str]) -> list[langchain_core.documents.Document]

   Convert a list of strings to a list of Documents.


   .. autolink-examples:: strings_to_documents
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.base.utils
   :collapse:
   
.. autolink-skip:: next
