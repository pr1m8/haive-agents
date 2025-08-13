
:py:mod:`agents.rag.db_rag.sql_rag.engines`
===========================================

.. py:module:: agents.rag.db_rag.sql_rag.engines

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




