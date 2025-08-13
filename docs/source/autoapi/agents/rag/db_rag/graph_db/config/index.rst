
:py:mod:`agents.rag.db_rag.graph_db.config`
===========================================

.. py:module:: agents.rag.db_rag.graph_db.config

Configuration module for the Graph Database RAG Agent.

This module provides configuration classes for connecting to Neo4j databases
and configuring the Graph DB RAG Agent with appropriate engines, schemas,
and domain-specific settings.

.. rubric:: Example

Basic configuration setup::

    >>> from haive.agents.rag.db_rag.graph_db.config import GraphDBRAGConfig
    >>>
    >>> # Create config with default settings
    >>> config = GraphDBRAGConfig(
    ...     domain_name="movies",
    ...     domain_categories=["movie", "actor", "director"]
    ... )
    >>>
    >>> # Create agent with config
    >>> agent = GraphDBRAGAgent(config)

Environment Variables:
    The following environment variables are used for Neo4j connection:

    - NEO4J_URI: The URI of the Neo4j database (e.g., "bolt://localhost:7687")
    - NEO4J_USER: Username for Neo4j authentication
    - NEO4J_PASSWORD: Password for Neo4j authentication
    - NEO4J_DATABASE: Database name (optional, defaults to "neo4j")


.. autolink-examples:: agents.rag.db_rag.graph_db.config
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.db_rag.graph_db.config.ExampleConfig
   agents.rag.db_rag.graph_db.config.GraphDBConfig
   agents.rag.db_rag.graph_db.config.GraphDBRAGConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExampleConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ExampleConfig {
        node [shape=record];
        "ExampleConfig" [label="ExampleConfig"];
        "pydantic.BaseModel" -> "ExampleConfig";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.config.ExampleConfig
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

   Inheritance diagram for GraphDBConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GraphDBConfig {
        node [shape=record];
        "GraphDBConfig" [label="GraphDBConfig"];
        "pydantic.BaseModel" -> "GraphDBConfig";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.config.GraphDBConfig
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

   Inheritance diagram for GraphDBRAGConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GraphDBRAGConfig {
        node [shape=record];
        "GraphDBRAGConfig" [label="GraphDBRAGConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "GraphDBRAGConfig";
      }

.. autoclass:: agents.rag.db_rag.graph_db.config.GraphDBRAGConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.graph_db.config.get_graph_db
   agents.rag.db_rag.graph_db.config.get_graph_db_schema
   agents.rag.db_rag.graph_db.config.validate_engines

.. py:function:: get_graph_db(uri: str = None, user: str = None, password: str = None, database: str = 'neo4j')

   Get a Neo4j database connection.

   :param uri: Neo4j URI (defaults to NEO4J_URI env var)
   :param user: Username (defaults to NEO4J_USER env var)
   :param password: Password (defaults to NEO4J_PASSWORD env var)
   :param database: Database name (defaults to "neo4j")

   :returns: Mock database connection (placeholder implementation)


   .. autolink-examples:: get_graph_db
      :collapse:

.. py:function:: get_graph_db_schema(db_connection=None) -> dict

   Get the schema from a Neo4j database.

   :param db_connection: Database connection object

   :returns: Dictionary representing the database schema


   .. autolink-examples:: get_graph_db_schema
      :collapse:

.. py:function:: validate_engines(engines: dict) -> bool

   Validate that all required engines are properly configured.

   :param engines: Dictionary of engine configurations

   :returns: True if all engines are valid, False otherwise


   .. autolink-examples:: validate_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.graph_db.config
   :collapse:
   
.. autolink-skip:: next
