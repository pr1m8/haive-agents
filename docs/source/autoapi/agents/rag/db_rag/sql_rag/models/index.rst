agents.rag.db_rag.sql_rag.models
================================

.. py:module:: agents.rag.db_rag.sql_rag.models


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.models.GradeAnswer
   agents.rag.db_rag.sql_rag.models.GradeHallucinations
   agents.rag.db_rag.sql_rag.models.GuardrailsOutput
   agents.rag.db_rag.sql_rag.models.Query
   agents.rag.db_rag.sql_rag.models.SQLAnalysisOutput
   agents.rag.db_rag.sql_rag.models.SQLQueryOutput
   agents.rag.db_rag.sql_rag.models.SQLValidationOutput


Module Contents
---------------

.. py:class:: GradeAnswer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Binary score to assess answer addresses question.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GradeAnswer
      :collapse:

   .. py:attribute:: binary_score
      :type:  str
      :value: None



.. py:class:: GradeHallucinations(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Binary score for hallucination present in generated answer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GradeHallucinations
      :collapse:

   .. py:attribute:: binary_score
      :type:  str
      :value: None



.. py:class:: GuardrailsOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from the guardrails check.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GuardrailsOutput
      :collapse:

   .. py:attribute:: decision
      :type:  str
      :value: None



   .. py:attribute:: reason
      :type:  str | None
      :value: None



.. py:class:: Query(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a query to the SQL database.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Query
      :collapse:

   .. py:attribute:: question
      :type:  str
      :value: None



.. py:class:: SQLAnalysisOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents the analysis of a natural language query.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SQLAnalysisOutput
      :collapse:

   .. py:attribute:: aggregations
      :type:  list[str]
      :value: None



   .. py:attribute:: complexity
      :type:  Literal['simple', 'medium', 'complex']
      :value: None



   .. py:attribute:: constraints
      :type:  list[str]
      :value: None



   .. py:attribute:: joins_needed
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: needed_columns
      :type:  list[str]
      :value: None



   .. py:attribute:: relevant_tables
      :type:  list[str]
      :value: None



.. py:class:: SQLQueryOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Validated structured output model for SQL query generation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SQLQueryOutput
      :collapse:

   .. py:method:: validate_sql_syntax(query: str) -> str
      :classmethod:


      Ensure the query starts with a valid SQL keyword.


      .. autolink-examples:: validate_sql_syntax
         :collapse:


   .. py:attribute:: parameters
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



.. py:class:: SQLValidationOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents the validation result of a SQL query's output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SQLValidationOutput
      :collapse:

   .. py:attribute:: errors
      :type:  list[str]
      :value: None



   .. py:attribute:: is_valid
      :type:  bool
      :value: None



   .. py:attribute:: suggestions
      :type:  str | None
      :value: None



