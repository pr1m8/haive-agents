agents.rag.dynamic.models
=========================

.. py:module:: agents.rag.dynamic.models


Classes
-------

.. autoapisummary::

   agents.rag.dynamic.models.DataSourceConfig


Module Contents
---------------

.. py:class:: DataSourceConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base configuration for a data source.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DataSourceConfig
      :collapse:

   .. py:method:: create_retriever() -> haive.core.models.retriever.base.RetrieverConfig
      :abstractmethod:


      Create a retriever for this data source.


      .. autolink-examples:: create_retriever
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: source_type
      :type:  haive.agents.rag.dynamic.data_source_types.DataSourceType
      :value: None



