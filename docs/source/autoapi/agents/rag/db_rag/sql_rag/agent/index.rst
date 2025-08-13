
:py:mod:`agents.rag.db_rag.sql_rag.agent`
=========================================

.. py:module:: agents.rag.db_rag.sql_rag.agent

SQL RAG Agent for natural language database querying.

This module implements a sophisticated SQL Retrieval-Augmented Generation (RAG) agent
that enables natural language querying of SQL databases. The agent uses a multi-step
workflow to analyze queries, generate SQL, validate results, and produce accurate answers.

.. rubric:: Example

Basic usage of the SQL RAG Agent::

    >>> from haive.agents.rag.db_rag.sql_rag import SQLRAGAgent, SQLRAGConfig
    >>>
    >>> # Create configuration
    >>> config = SQLRAGConfig(
    ...     domain_name="sales",
    ...     db_config=SQLDatabaseConfig(
    ...         db_type="postgresql",
    ...         db_name="sales_db"
    ...     )
    ... )
    >>>
    >>> # Initialize agent
    >>> agent = SQLRAGAgent(config)
    >>>
    >>> # Query the database
    >>> result = agent.invoke({
    ...     "question": "What were the total sales last quarter?"
    ... })
    >>> print(result["answer"])
    'Total sales last quarter were $1.2M across 450 transactions...'

.. attribute:: logger

   Module-level logger for debugging and monitoring.

   :type: logging.Logger

.. note::

   This agent requires proper database credentials and connection details
   to be configured either through environment variables or explicit configuration.


.. autolink-examples:: agents.rag.db_rag.sql_rag.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.agent.SQLRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SQLRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SQLRAGAgent {
        node [shape=record];
        "SQLRAGAgent" [label="SQLRAGAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.rag.db_rag.sql_rag.config.SQLRAGConfig]" -> "SQLRAGAgent";
      }

.. autoclass:: agents.rag.db_rag.sql_rag.agent.SQLRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.sql_rag.agent
   :collapse:
   
.. autolink-skip:: next
