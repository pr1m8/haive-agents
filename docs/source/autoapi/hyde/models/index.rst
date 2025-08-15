hyde.models
===========

.. py:module:: hyde.models


Classes
-------

.. autoapisummary::

   hyde.models.HyDEResponse
   hyde.models.HypotheticalDocument


Module Contents
---------------

.. py:class:: HyDEResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   HyDE (Hypothetical Document Embeddings) response.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HyDEResponse
      :collapse:

   .. py:attribute:: hypothetical_documents
      :type:  list[HypotheticalDocument]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: query_analysis
      :type:  str
      :value: None



   .. py:attribute:: retrieval_strategy
      :type:  str
      :value: None



   .. py:attribute:: search_queries
      :type:  list[str]
      :value: None



.. py:class:: HypotheticalDocument(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A hypothetical document generated for HyDE.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HypotheticalDocument
      :collapse:

   .. py:method:: to_query() -> str

      Convert the hypothetical document to a query.


      .. autolink-examples:: to_query
         :collapse:


   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: document_type
      :type:  str
      :value: None



   .. py:attribute:: key_concepts
      :type:  list[str]
      :value: None



   .. py:attribute:: relevance_explanation
      :type:  str
      :value: None



