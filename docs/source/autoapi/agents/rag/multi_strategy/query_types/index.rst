agents.rag.multi_strategy.query_types
=====================================

.. py:module:: agents.rag.multi_strategy.query_types


Classes
-------

.. autoapisummary::

   agents.rag.multi_strategy.query_types.QueryType


Module Contents
---------------

.. py:class:: QueryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of queries that can be handled by specialized strategies.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryType
      :collapse:

   .. py:attribute:: ANALYTICAL
      :value: 'analytical'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: RELATIONAL
      :value: 'relational'



   .. py:attribute:: TEMPORAL
      :value: 'temporal'



