agents.rag.db_rag.sql_rag.engines
=================================

.. py:module:: agents.rag.db_rag.sql_rag.engines

.. autoapi-nested-parse::

   LLM engine configurations for SQL RAG Agent.

   This module defines pre-configured AugLLMConfig instances for each step
   in the SQL RAG workflow. Each engine is optimized for its specific task
   with appropriate prompts and output models.

   .. rubric:: Example

   Using default engines::

       >>> from haive.agents.rag.db_rag.sql_rag.engines import default_sql_engines
       >>>
       >>> # Access a specific engine
       >>> sql_generator = default_sql_engines["generate_sql"]
       >>> print(sql_generator.name)
       'generate_sql_config'

   Customizing engines::

       >>> from haive.core.engine.aug_llm import AugLLMConfig
       >>> from haive.agents.rag.db_rag.sql_rag.engines import default_sql_engines
       >>>
       >>> # Create custom SQL generator with different model
       >>> custom_sql_gen = AugLLMConfig(
       ...     name="custom_sql_generator",
       ...     model="gpt-4",
       ...     temperature=0.1,
       ...     prompt_template=GENERATE_SQL_PROMPT,
       ...     structured_output_model=SQLQueryOutput
       ... )
       >>>
       >>> # Use with custom engines dict
       >>> custom_engines = {
       ...     **default_sql_engines,
       ...     "generate_sql": custom_sql_gen
       >>> }


   .. autolink-examples:: agents.rag.db_rag.sql_rag.engines
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.engines.analyze_query_aug_llm_config
   agents.rag.db_rag.sql_rag.engines.answer_grading_aug_llm_config
   agents.rag.db_rag.sql_rag.engines.default_sql_engines
   agents.rag.db_rag.sql_rag.engines.generate_final_answer_aug_llm_config
   agents.rag.db_rag.sql_rag.engines.generate_sql_aug_llm_config
   agents.rag.db_rag.sql_rag.engines.guardrails_aug_llm_config
   agents.rag.db_rag.sql_rag.engines.hallucination_check_aug_llm_config
   agents.rag.db_rag.sql_rag.engines.validate_sql_aug_llm_config


Module Contents
---------------

.. py:data:: analyze_query_aug_llm_config

   Engine for analyzing natural language queries.

   This engine breaks down user questions to identify:
   - Relevant database tables
   - Required columns
   - Necessary joins
   - Aggregations needed
   - WHERE clause constraints

   :returns: Structured analysis of query requirements.
   :rtype: SQLAnalysisOutput

   .. rubric:: Example

   >>> engine = analyze_query_aug_llm_config
   >>> result = engine.invoke({
   ...     "question": "Top 5 customers by total purchase amount",
   ...     "schema": db_schema,
   ...     "dialect": "postgresql"
   ... })
   >>> print(result.relevant_tables)
   ['customers', 'orders']

   .. autolink-examples:: analyze_query_aug_llm_config
      :collapse:

.. py:data:: answer_grading_aug_llm_config

   Engine for grading answer relevance.

   This engine evaluates whether the generated answer actually
   addresses the user's original question.

   :returns: Binary score for answer relevance.
   :rtype: GradeAnswer

   .. rubric:: Example

   >>> engine = answer_grading_aug_llm_config
   >>> result = engine.invoke({
   ...     "question": "What's our best selling product?",
   ...     "answer": "We have 500 products in our catalog"  # Doesn't answer question
   ... })
   >>> print(result.binary_score)
   'no'  # Answer doesn't address question

   .. autolink-examples:: answer_grading_aug_llm_config
      :collapse:

.. py:data:: default_sql_engines

   Default engine configuration dictionary.

   This dictionary contains all the pre-configured engines needed
   for the SQL RAG workflow. It can be used as-is or customized
   by replacing specific engines.

   .. rubric:: Example

   Using defaults::

       >>> config = SQLRAGConfig(engines=default_sql_engines)

   Customizing specific engine::

       >>> custom_engines = {
       ...     **default_sql_engines,
       ...     "generate_sql": my_custom_sql_generator
       ... }
       >>> config = SQLRAGConfig(engines=custom_engines)

   .. autolink-examples:: default_sql_engines
      :collapse:

.. py:data:: generate_final_answer_aug_llm_config

   Engine for generating natural language answers.

   This engine converts SQL query results into clear, comprehensive
   answers that directly address the user's question.

   :returns: Natural language answer based on query results.
   :rtype: str

   .. rubric:: Example

   >>> engine = generate_final_answer_aug_llm_config
   >>> answer = engine.invoke({
   ...     "question": "Who are our top customers?",
   ...     "sql_query": "SELECT name, total_spent FROM customers ORDER BY total_spent DESC LIMIT 5",
   ...     "query_result": "John Doe|5000\nJane Smith|4500\n..."
   ... })
   >>> print(answer)
   'Your top customers are: 1. John Doe ($5,000), 2. Jane Smith ($4,500)...'

   .. autolink-examples:: generate_final_answer_aug_llm_config
      :collapse:

.. py:data:: generate_sql_aug_llm_config

   Engine for generating SQL queries from natural language.

   This engine converts analyzed queries into syntactically correct SQL,
   considering the database dialect and schema constraints.

   :returns: Generated SQL query with optional parameters.
   :rtype: SQLQueryOutput

   .. rubric:: Example

   >>> engine = generate_sql_aug_llm_config
   >>> result = engine.invoke({
   ...     "question": "Show all orders from last month",
   ...     "schema": db_schema,
   ...     "dialect": "mysql",
   ...     "query_analysis": analysis_output
   ... })
   >>> print(result.query)
   'SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'

   .. autolink-examples:: generate_sql_aug_llm_config
      :collapse:

.. py:data:: guardrails_aug_llm_config

   Engine for domain relevance checking (guardrails).

   This engine determines if a user's question is about querying
   the database or something unrelated that should be rejected.

   :returns: Decision to proceed or end with reason.
   :rtype: GuardrailsOutput

   .. rubric:: Example

   >>> engine = guardrails_aug_llm_config
   >>> result = engine.invoke({
   ...     "question": "What's the weather like?",
   ...     "schema": db_schema,
   ...     "tables": ["orders", "customers"]
   ... })
   >>> print(result.decision)
   'end'
   >>> print(result.reason)
   'Question is about weather, not database content'

   .. autolink-examples:: guardrails_aug_llm_config
      :collapse:

.. py:data:: hallucination_check_aug_llm_config

   Engine for detecting hallucinations in answers.

   This engine verifies that generated answers only contain
   information supported by the actual query results.

   :returns: Binary score for hallucination presence.
   :rtype: GradeHallucinations

   .. rubric:: Example

   >>> engine = hallucination_check_aug_llm_config
   >>> result = engine.invoke({
   ...     "question": "Total sales?",
   ...     "query_result": "total|1000",
   ...     "answer": "Total sales are $1000 with 50% growth"  # Growth not in data
   ... })
   >>> print(result.binary_score)
   'no'  # Hallucination detected

   .. autolink-examples:: hallucination_check_aug_llm_config
      :collapse:

.. py:data:: validate_sql_aug_llm_config

   Engine for validating generated SQL queries.

   This engine checks SQL queries for:
   - Syntax errors
   - Invalid table/column references
   - Missing GROUP BY clauses
   - Potential performance issues
   - Security concerns

   :returns: Validation results with errors and suggestions.
   :rtype: SQLValidationOutput

   .. rubric:: Example

   >>> engine = validate_sql_aug_llm_config
   >>> result = engine.invoke({
   ...     "sql_query": "SELECT category, SUM(amount) FROM sales",
   ...     "schema": db_schema,
   ...     "dialect": "postgresql"
   ... })
   >>> print(result.errors)
   ['Missing GROUP BY clause for non-aggregated column: category']

   .. autolink-examples:: validate_sql_aug_llm_config
      :collapse:

