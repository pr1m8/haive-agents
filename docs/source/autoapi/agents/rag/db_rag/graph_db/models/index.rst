
:py:mod:`agents.rag.db_rag.graph_db.models`
===========================================

.. py:module:: agents.rag.db_rag.graph_db.models

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Config:

   .. graphviz::
      :align: center

      digraph inheritance_Config {
        node [shape=record];
        "Config" [label="Config"];
        "pydantic.BaseModel" -> "Config";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.models.Config
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

   Inheritance diagram for CypherQueryOutput:

   .. graphviz::
      :align: center

      digraph inheritance_CypherQueryOutput {
        node [shape=record];
        "CypherQueryOutput" [label="CypherQueryOutput"];
        "pydantic.BaseModel" -> "CypherQueryOutput";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.models.CypherQueryOutput
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

   Inheritance diagram for GuardrailsOutput:

   .. graphviz::
      :align: center

      digraph inheritance_GuardrailsOutput {
        node [shape=record];
        "GuardrailsOutput" [label="GuardrailsOutput"];
        "pydantic.BaseModel" -> "GuardrailsOutput";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.models.GuardrailsOutput
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

   Inheritance diagram for PropertyFilter:

   .. graphviz::
      :align: center

      digraph inheritance_PropertyFilter {
        node [shape=record];
        "PropertyFilter" [label="PropertyFilter"];
        "pydantic.BaseModel" -> "PropertyFilter";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.models.PropertyFilter
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

   Inheritance diagram for ValidateCypherOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ValidateCypherOutput {
        node [shape=record];
        "ValidateCypherOutput" [label="ValidateCypherOutput"];
        "pydantic.BaseModel" -> "ValidateCypherOutput";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.models.ValidateCypherOutput
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



Functions
---------

.. autoapisummary::

   agents.rag.db_rag.graph_db.models.validate_cypher_syntax
   agents.rag.db_rag.graph_db.models.validate_decision
   agents.rag.db_rag.graph_db.models.validate_filter_type

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.graph_db.models
   :collapse:
   
.. autolink-skip:: next
