agents.rag.db_rag.base.db_config
================================

.. py:module:: agents.rag.db_rag.base.db_config


Attributes
----------

.. autoapisummary::

   agents.rag.db_rag.base.db_config.T


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.base.db_config.BaseDBConfig


Module Contents
---------------

.. py:class:: BaseDBConfig(/, **data: Any)

   Bases: :py:obj:`abc.ABC`, :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Abstract base configuration model for database connections.

   This class defines the common interface that all database
   configurations should implement, regardless of database type.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseDBConfig
      :collapse:

   .. py:method:: get_connection_string() -> str
      :abstractmethod:


      Generate a connection string for the database.


      .. autolink-examples:: get_connection_string
         :collapse:


   .. py:method:: get_db() -> T | None
      :abstractmethod:


      Creates and returns a database connection object.


      .. autolink-examples:: get_db
         :collapse:


   .. py:method:: get_db_schema() -> dict[str, Any] | None
      :abstractmethod:


      Retrieves the schema information from the database.


      .. autolink-examples:: get_db_schema
         :collapse:


   .. py:attribute:: db_type
      :type:  str
      :value: None



.. py:data:: T

