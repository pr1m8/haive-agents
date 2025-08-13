
:py:mod:`agents.rag.db_rag.sql_rag.config`
==========================================

.. py:module:: agents.rag.db_rag.sql_rag.config

Configuration module for SQL RAG Agent.

This module provides configuration classes for setting up SQL database connections
and agent behavior. It supports multiple database types and includes extensive
customization options for the agent workflow.

.. rubric:: Example

Basic PostgreSQL configuration::

    >>> from haive.agents.rag.db_rag.sql_rag.config import SQLRAGConfig, SQLDatabaseConfig
    >>>
    >>> # Configure database connection
    >>> db_config = SQLDatabaseConfig(
    ...     db_type="postgresql",
    ...     db_host="localhost",
    ...     db_name="sales_db",
    ...     db_user="admin",
    ...     db_password="secure_password",
    ...     include_tables=["orders", "customers", "products"]
    ... )
    >>>
    >>> # Configure agent
    >>> agent_config = SQLRAGConfig(
    ...     domain_name="sales",
    ...     db_config=db_config,
    ...     hallucination_check=True,
    ...     max_iterations=3
    ... )

.. note::

   Database credentials can be provided through environment variables
   for security. See SQLDatabaseConfig for supported variables.


.. autolink-examples:: agents.rag.db_rag.sql_rag.config
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.config.SQLDatabaseConfig
   agents.rag.db_rag.sql_rag.config.SQLRAGConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SQLDatabaseConfig:

   .. graphviz::
      :align: center

      digraph inheritance_SQLDatabaseConfig {
        node [shape=record];
        "SQLDatabaseConfig" [label="SQLDatabaseConfig"];
        "pydantic.BaseModel" -> "SQLDatabaseConfig";
      }

.. autopydantic_model:: agents.rag.db_rag.sql_rag.config.SQLDatabaseConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SQLRAGConfig:

   .. graphviz::
      :align: center

      digraph inheritance_SQLRAGConfig {
        node [shape=record];
        "SQLRAGConfig" [label="SQLRAGConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "SQLRAGConfig";
      }

.. autoclass:: agents.rag.db_rag.sql_rag.config.SQLRAGConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.sql_rag.config
   :collapse:
   
.. autolink-skip:: next
