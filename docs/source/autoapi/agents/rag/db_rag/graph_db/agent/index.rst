
:py:mod:`agents.rag.db_rag.graph_db.agent`
==========================================

.. py:module:: agents.rag.db_rag.graph_db.agent

Graph Database RAG Agent implementation.

This module implements the main Graph Database RAG Agent that provides natural
language querying capabilities for Neo4j databases. The agent uses a multi-step
workflow to convert questions to Cypher queries, validate them, execute them,
and generate natural language responses.

The agent workflow consists of the following steps:
    1. **Domain Relevance Check**: Validates if the query is within the configured domain
    2. **Query Generation**: Converts natural language to Cypher using few-shot learning
    3. **Query Validation**: Checks the Cypher query against the database schema
    4. **Query Correction**: Fixes any errors found during validation
    5. **Query Execution**: Runs the validated query against Neo4j
    6. **Answer Generation**: Converts database results to natural language

.. rubric:: Example

Basic usage of the Graph DB RAG Agent::

    >>> from haive.agents.rag.db_rag.graph_db import GraphDBRAGAgent, GraphDBRAGConfig
    >>>
    >>> # Configure the agent for a movie domain
    >>> config = GraphDBRAGConfig(
    ...     domain_name="movies",
    ...     domain_categories=["movie", "actor", "director"],
    ...     graph_db_config=GraphDBConfig(
    ...         graph_db_uri="bolt://localhost:7687",
    ...         graph_db_user="neo4j",
    ...         graph_db_password="password"
    ...     )
    ... )
    >>>
    >>> # Create and use the agent
    >>> agent = GraphDBRAGAgent(config)
    >>> result = agent.invoke({"question": "Who directed The Matrix?"})
    >>> print(result["answer"])
    The Wachowskis directed The Matrix.

Using the agent with streaming::

    >>> # Stream the workflow execution
    >>> for chunk in agent.stream({"question": "What are the top 5 rated movies?"}):
    ...     if "answer" in chunk:
    ...         print(chunk["answer"])

.. note::

   The agent requires a connection to a Neo4j database and uses environment
   variables for configuration if not explicitly provided.

.. seealso::

   - :class:`GraphDBRAGConfig`: Configuration options for the agent
   - :class:`OverallState`: State management during workflow execution
   - :mod:`haive.agents.rag.db_rag.graph_db.engines`: LLM engines used by the agent


.. autolink-examples:: agents.rag.db_rag.graph_db.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.db_rag.graph_db.agent.GraphDBRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphDBRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GraphDBRAGAgent {
        node [shape=record];
        "GraphDBRAGAgent" [label="GraphDBRAGAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.rag.db_rag.graph_db.config.GraphDBRAGConfig]" -> "GraphDBRAGAgent";
      }

.. autoclass:: agents.rag.db_rag.graph_db.agent.GraphDBRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.graph_db.agent.check_domain_relevance
   agents.rag.db_rag.graph_db.agent.correct_query
   agents.rag.db_rag.graph_db.agent.domain_router
   agents.rag.db_rag.graph_db.agent.execute_query
   agents.rag.db_rag.graph_db.agent.generate_answer
   agents.rag.db_rag.graph_db.agent.generate_query
   agents.rag.db_rag.graph_db.agent.setup_workflow
   agents.rag.db_rag.graph_db.agent.validate_query
   agents.rag.db_rag.graph_db.agent.validation_router

.. py:function:: check_domain_relevance(query: str, domain_categories: list = None) -> bool

   Check if a query is relevant to the specified domain.

   :param query: The query to check
   :param domain_categories: List of domain categories to check against

   :returns: True if the query is domain-relevant, False otherwise


   .. autolink-examples:: check_domain_relevance
      :collapse:

.. py:function:: correct_query(query: str, errors: list = None) -> str

   Correct a Cypher query based on provided errors.

   :param query: The original query
   :param errors: List of error messages

   :returns: Corrected query string


   .. autolink-examples:: correct_query
      :collapse:

.. py:function:: domain_router(query: str, domain_categories: list = None) -> str

   Route queries based on domain relevance.


   .. autolink-examples:: domain_router
      :collapse:

.. py:function:: execute_query(query: str, db_connection=None) -> dict

   Execute a Cypher query against the database.


   .. autolink-examples:: execute_query
      :collapse:

.. py:function:: generate_answer(query_results: dict, original_query: str = '') -> str

   Generate natural language answer from query results.


   .. autolink-examples:: generate_answer
      :collapse:

.. py:function:: generate_query(natural_language_query: str) -> str

   Generate Cypher query from natural language.


   .. autolink-examples:: generate_query
      :collapse:

.. py:function:: setup_workflow()

   Set up the graph DB RAG workflow.


   .. autolink-examples:: setup_workflow
      :collapse:

.. py:function:: validate_query(query: str, schema: dict = None) -> dict

   Validate a Cypher query against database schema.


   .. autolink-examples:: validate_query
      :collapse:

.. py:function:: validation_router(validation_result: dict) -> str

   Route based on validation results.


   .. autolink-examples:: validation_router
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.graph_db.agent
   :collapse:
   
.. autolink-skip:: next
