agents.rag.db_rag.graph_db.models
=================================

.. py:module:: agents.rag.db_rag.graph_db.models

.. autoapi-nested-parse::

   Pydantic models for structured outputs in the Graph DB RAG Agent.

   This module defines the structured output models used by various LLM engines
   in the Graph DB RAG workflow. These models ensure type safety and validation
   for LLM responses.

   .. rubric:: Example

   Using the models for structured LLM outputs::

       >>> from haive.agents.rag.db_rag.graph_db.models import CypherQueryOutput
       >>>
       >>> # Create a Cypher query output
       >>> cypher_output = CypherQueryOutput(
       ...     query="MATCH (m:Movie) WHERE m.year = $year RETURN m.title",
       ...     parameters={"year": 2023}
       ... )
       >>> print(cypher_output.query)
       MATCH (m:Movie) WHERE m.year = $year RETURN m.title


   .. autolink-examples:: agents.rag.db_rag.graph_db.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.graph_db.models.Config
   agents.rag.db_rag.graph_db.models.CypherQueryOutput
   agents.rag.db_rag.graph_db.models.GuardrailsOutput
   agents.rag.db_rag.graph_db.models.PropertyFilter
   agents.rag.db_rag.graph_db.models.ValidateCypherOutput


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.graph_db.models.validate_cypher_syntax
   agents.rag.db_rag.graph_db.models.validate_decision
   agents.rag.db_rag.graph_db.models.validate_filter_type


Module Contents
---------------

.. py:class:: Config(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Top-level configuration class for Graph DB RAG models.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Config
      :collapse:

   .. py:attribute:: allowed_categories
      :type:  list[str]
      :value: None



   .. py:attribute:: domain_name
      :type:  str
      :value: None



   .. py:attribute:: validation_enabled
      :type:  bool
      :value: None



.. py:class:: CypherQueryOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for Cypher query generation.

   This model ensures that generated Cypher queries are properly formatted
   and optionally include parameters for parameterized queries.

   .. attribute:: query

      The generated Cypher query string. Must start with a valid
      Cypher keyword (MATCH, CREATE, etc.).

   .. attribute:: parameters

      Optional dictionary of query parameters for parameterized
      queries. Keys are parameter names (without $), values are the
      parameter values.

   .. rubric:: Example

   >>> # Simple query without parameters
   >>> output = CypherQueryOutput(
   ...     query="MATCH (m:Movie) RETURN m.title LIMIT 10"
   ... )

   >>> # Parameterized query
   >>> output = CypherQueryOutput(
   ...     query="MATCH (m:Movie) WHERE m.year = $year RETURN m.title",
   ...     parameters={"year": 2023}
   ... )

   :raises ValueError: If the query doesn't start with a valid Cypher keyword.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CypherQueryOutput
      :collapse:

   .. py:method:: validate_cypher_syntax(query: str) -> str
      :classmethod:


      Validate that the query starts with a valid Cypher keyword.

      :param query: The Cypher query string to validate.

      :returns: The validated query string.
      :rtype: str

      :raises ValueError: If the query doesn't start with a valid keyword.


      .. autolink-examples:: validate_cypher_syntax
         :collapse:


   .. py:attribute:: parameters
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



.. py:class:: GuardrailsOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output for domain relevance checking.

   This model represents the decision on whether a query is relevant to
   the configured domain. It supports multiple categories within a domain.

   .. attribute:: decision

      The routing decision. Either "end" (not relevant) or one
      of the allowed categories (relevant to that category).

   .. attribute:: allowed_categories

      List of valid categories for the domain. The
      "end" option is always implicitly included.

   .. rubric:: Example

   >>> # Query about movies in a movie domain
   >>> output = GuardrailsOutput(
   ...     decision="movie",
   ...     allowed_categories=["movie", "actor", "director"]
   ... )

   >>> # Query not relevant to the domain
   >>> output = GuardrailsOutput(
   ...     decision="end",
   ...     allowed_categories=["movie", "actor", "director"]
   ... )

   .. note::

      The validate_decision method should be called after instantiation
      to ensure the decision is valid.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GuardrailsOutput
      :collapse:

   .. py:class:: Config

      Pydantic model configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:method:: validate_decision() -> None

      Validate that the decision is within allowed values.

      :raises ValueError: If the decision is not 'end' or in allowed_categories.

      .. rubric:: Example

      >>> output = GuardrailsOutput(decision="movie")
      >>> output.validate_decision()  # No error

      >>> output = GuardrailsOutput(decision="invalid")
      >>> output.validate_decision()  # Raises ValueError


      .. autolink-examples:: validate_decision
         :collapse:


   .. py:attribute:: allowed_categories
      :type:  list[str]
      :value: None



   .. py:attribute:: decision
      :type:  str
      :value: None



.. py:class:: PropertyFilter(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a filter condition on a node property in a Cypher query.

   This model captures property-based filtering conditions that appear in
   WHERE clauses or inline property matches in Cypher queries.

   .. attribute:: node_label

      The Neo4j label of the node being filtered (e.g., "Movie", "Person").

   .. attribute:: property_key

      The property name being filtered (e.g., "title", "year").

   .. attribute:: property_value

      The value to match against. Can be string, number, or boolean.

   .. attribute:: filter_type

      The comparison operator used. Defaults to equality.

   .. rubric:: Example

   >>> # Filter for movies released after 2020
   >>> filter = PropertyFilter(
   ...     node_label="Movie",
   ...     property_key="year",
   ...     property_value=2020,
   ...     filter_type=">"
   ... )

   >>> # Filter for person named "Keanu Reeves"
   >>> filter = PropertyFilter(
   ...     node_label="Person",
   ...     property_key="name",
   ...     property_value="Keanu Reeves"
   ... )

   :raises ValueError: If filter_type is not one of the valid operators.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PropertyFilter
      :collapse:

   .. py:method:: validate_filter_type(v) -> Literal['=', '!=', '>', '<', '>=', '<='] | None
      :classmethod:


      Validate that the filter type is a supported operator.

      :param v: The filter type value to validate.

      :returns: The validated filter type.
      :rtype: str

      :raises ValueError: If the filter type is not supported.


      .. autolink-examples:: validate_filter_type
         :collapse:


   .. py:attribute:: filter_type
      :type:  Literal['=', '!=', '>', '<', '>=', '<='] | None
      :value: None



   .. py:attribute:: node_label
      :type:  str
      :value: None



   .. py:attribute:: property_key
      :type:  str
      :value: None



   .. py:attribute:: property_value
      :type:  Any | None
      :value: None



.. py:class:: ValidateCypherOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Validation result for a Cypher query.

   This model captures the results of validating a Cypher query against
   the database schema, including any errors found and filters detected.

   .. attribute:: is_valid

      Whether the Cypher query is valid and can be executed.

   .. attribute:: errors

      List of syntax or semantic errors found. Each error should
      explain what's wrong and potentially how to fix it.

   .. attribute:: filters

      List of property filters detected in the query. Useful for
      understanding what the query is filtering on.

   .. rubric:: Example

   >>> # Valid query result
   >>> result = ValidateCypherOutput(
   ...     is_valid=True,
   ...     errors=[],
   ...     filters=[PropertyFilter(
   ...         node_label="Movie",
   ...         property_key="year",
   ...         property_value=2023
   ...     )]
   ... )

   >>> # Invalid query result
   >>> result = ValidateCypherOutput(
   ...     is_valid=False,
   ...     errors=[
   ...         "Label 'Film' does not exist in schema. Did you mean 'Movie'?",
   ...         "Property 'release_date' does not exist for Movie. Use 'year' instead."
   ...     ]
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ValidateCypherOutput
      :collapse:

   .. py:attribute:: errors
      :type:  list[str] | None
      :value: None



   .. py:attribute:: filters
      :type:  list[PropertyFilter] | None
      :value: None



   .. py:attribute:: is_valid
      :type:  bool
      :value: None



.. py:function:: validate_cypher_syntax(query: str) -> bool

   Validate Cypher query syntax.

   :param query: Cypher query string to validate

   :returns: True if syntax is valid, False otherwise


   .. autolink-examples:: validate_cypher_syntax
      :collapse:

.. py:function:: validate_decision(decision: str, allowed_values: list[str]) -> bool

   Validate decision against allowed values.

   :param decision: Decision value to validate
   :param allowed_values: List of allowed decision values

   :returns: True if decision is valid, False otherwise


   .. autolink-examples:: validate_decision
      :collapse:

.. py:function:: validate_filter_type(filter_type: str) -> bool

   Validate filter type for property filtering.

   :param filter_type: Filter type to validate

   :returns: True if filter type is valid, False otherwise


   .. autolink-examples:: validate_filter_type
      :collapse:

