agents.rag.db_rag.graph_db.state
================================

.. py:module:: agents.rag.db_rag.graph_db.state

.. autoapi-nested-parse::

   State definitions for the Graph Database RAG Agent.

   This module defines the state schemas used throughout the Graph DB RAG workflow,
   including input, output, and overall state management for Cypher query generation
   and execution.

   .. rubric:: Example

   Basic usage of the state classes::

       >>> from haive.agents.rag.db_rag.graph_db.state import InputState, OverallState
       >>>
       >>> # Create input state
       >>> input_state = InputState(question="What movies were released in 2023?")
       >>>
       >>> # Create overall state for workflow
       >>> state = OverallState(
       ...     question="What movies were released in 2023?",
       ...     next_action="generate_query"
       ... )

   .. note::

      The state classes use Pydantic v2 for validation and serialization.
      All fields have sensible defaults to support partial state updates.


   .. autolink-examples:: agents.rag.db_rag.graph_db.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.graph_db.state.InputState
   agents.rag.db_rag.graph_db.state.OutputState
   agents.rag.db_rag.graph_db.state.OverallState


Module Contents
---------------

.. py:class:: InputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input state for the graph database agent.

   This class defines the initial input structure for queries to the
   Graph DB RAG agent. It contains only the user's natural language question.

   .. attribute:: question

      The user's natural language question to be converted to Cypher
      and executed against the Neo4j database.

   .. rubric:: Example

   >>> input_state = InputState(question="Who directed The Matrix?")
   >>> print(input_state.question)
   Who directed The Matrix?

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: InputState
      :collapse:

   .. py:attribute:: question
      :type:  str
      :value: None



.. py:class:: OutputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output state for the graph database agent.

   This class defines the final output structure returned by the Graph DB RAG
   agent after processing a query. It includes the answer, execution steps,
   and the generated Cypher statement.

   .. attribute:: answer

      The natural language answer generated from the query results.
      Defaults to empty string if no answer has been generated yet.

   .. attribute:: steps

      List of workflow steps executed during query processing.
      Useful for debugging and understanding the agent's reasoning.

   .. attribute:: cypher_statement

      The final Cypher query that was executed.
      Useful for learning and debugging purposes.

   .. rubric:: Example

   >>> output = OutputState(
   ...     answer="The Wachowskis directed The Matrix.",
   ...     steps=["check_domain", "generate_query", "execute_query"],
   ...     cypher_statement="MATCH (p:Person)-[:DIRECTED]->(m:Movie {title: 'The Matrix'}) RETURN p.name"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: OutputState
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: cypher_statement
      :type:  str
      :value: None



   .. py:attribute:: steps
      :type:  list[str]
      :value: None



.. py:class:: OverallState(/, **data: Any)

   Bases: :py:obj:`InputState`, :py:obj:`OutputState`


   Complete state for the graph database agent workflow.

   This class combines input and output states with additional fields needed
   for the internal workflow execution. It tracks the current state of query
   processing including errors, validation results, and database records.

   .. attribute:: next_action

      The next workflow step to execute. Used for routing
      decisions in the graph. Common values include:
      - "generate_query": Generate Cypher from natural language
      - "validate_query": Validate the generated Cypher
      - "correct_cypher": Fix errors in the Cypher statement
      - "execute_query": Run the query against Neo4j
      - "end": Terminate the workflow

   .. attribute:: cypher_errors

      List of validation errors found in the Cypher statement.
      Used by the correction step to fix issues.

   .. attribute:: database_records

      Records retrieved from the Neo4j database.
      Can be a list of dictionaries or a string message if no results.

   .. rubric:: Example

   >>> state = OverallState(
   ...     question="What are the top rated movies?",
   ...     next_action="generate_query",
   ...     cypher_statement="MATCH (m:Movie) RETURN m.title, m.rating ORDER BY m.rating DESC LIMIT 5",
   ...     database_records=[
   ...         {"m.title": "The Shawshank Redemption", "m.rating": 9.3},
   ...         {"m.title": "The Godfather", "m.rating": 9.2}
   ...     ]
   ... )

   .. note::

      This state is passed between all nodes in the workflow graph,
      accumulating information as the query is processed.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: OverallState
      :collapse:

   .. py:attribute:: cypher_errors
      :type:  list[str]
      :value: None



   .. py:attribute:: database_records
      :type:  list[dict]
      :value: None



   .. py:attribute:: next_action
      :type:  str
      :value: None



