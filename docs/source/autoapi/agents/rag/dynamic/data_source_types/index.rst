agents.rag.dynamic.data_source_types
====================================

.. py:module:: agents.rag.dynamic.data_source_types


Classes
-------

.. autoapisummary::

   agents.rag.dynamic.data_source_types.DataSourceType


Module Contents
---------------

.. py:class:: DataSourceType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of data sources available.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DataSourceType
      :collapse:

   .. py:attribute:: API
      :value: 'api'



   .. py:attribute:: DOCUMENT_STORE
      :value: 'document_store'



   .. py:attribute:: GRAPH_DB
      :value: 'graph_db'



   .. py:attribute:: SQL_DB
      :value: 'sql_db'



   .. py:attribute:: VECTOR_DB
      :value: 'vector_db'



   .. py:attribute:: WEB_SEARCH
      :value: 'web_search'



