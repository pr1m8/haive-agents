
:py:mod:`agents.rag.db_rag.sql_rag.prompts`
===========================================

.. py:module:: agents.rag.db_rag.sql_rag.prompts

Prompt templates for SQL RAG Agent.

This module contains all the prompt templates used throughout the SQL RAG
workflow. Each prompt is carefully crafted to guide the LLM through specific
tasks while maintaining consistency and accuracy.

The prompts follow a structured format with clear system instructions and
user templates that include necessary context variables.

.. rubric:: Example

Using prompts with LangChain::

    >>> from langchain_core.prompts import ChatPromptTemplate
    >>> from haive.agents.rag.db_rag.sql_rag.prompts import GENERATE_SQL_PROMPT
    >>>
    >>> # Format prompt with variables
    >>> messages = GENERATE_SQL_PROMPT.format_messages(
    ...     schema=db_schema,
    ...     dialect="postgresql",
    ...     question="Show top products",
    ...     query_analysis=analysis_result
    ... )
    >>>
    >>> # Use with LLM
    >>> llm = ChatOpenAI()
    >>> response = llm.invoke(messages)


.. autolink-examples:: agents.rag.db_rag.sql_rag.prompts
   :collapse:




