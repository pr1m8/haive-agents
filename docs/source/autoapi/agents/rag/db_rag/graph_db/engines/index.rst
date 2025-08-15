agents.rag.db_rag.graph_db.engines
==================================

.. py:module:: agents.rag.db_rag.graph_db.engines


Attributes
----------

.. autoapisummary::

   agents.rag.db_rag.graph_db.engines.CORRECT_CYPHER_PROMPT_TEMPLATE
   agents.rag.db_rag.graph_db.engines.CORRECT_CYPHER_SYSTEM_PROMPT
   agents.rag.db_rag.graph_db.engines.CORRECT_CYPHER_USER_PROMPT
   agents.rag.db_rag.graph_db.engines.GENERATE_FINAL_HUMAN_PROMPT
   agents.rag.db_rag.graph_db.engines.GENERATE_FINAL_PROMPT_TEMPLATE
   agents.rag.db_rag.graph_db.engines.GUARDRAILS_PROMPT_TEMPLATE
   agents.rag.db_rag.graph_db.engines.GUARDRAILS_SYSTEM_PROMPT
   agents.rag.db_rag.graph_db.engines.TEXT2CYPHER_PROMPT_TEMPLATE
   agents.rag.db_rag.graph_db.engines.TEXT2CYPHER_SYSTEM_PROMPT
   agents.rag.db_rag.graph_db.engines.TEXT2CYPHER_USER_PROMPT
   agents.rag.db_rag.graph_db.engines.VALIDATE_CYPHER_SYSTEM_PROMPT
   agents.rag.db_rag.graph_db.engines.VALIDATE_CYPHER_USER_PROMPT
   agents.rag.db_rag.graph_db.engines.correct_cypher_aug_llm_config
   agents.rag.db_rag.graph_db.engines.generate_final_aug_llm_config
   agents.rag.db_rag.graph_db.engines.guardrails_aug_llm_config
   agents.rag.db_rag.graph_db.engines.text2cypher_aug_llm_config
   agents.rag.db_rag.graph_db.engines.validate_cypher_aug_llm_config
   agents.rag.db_rag.graph_db.engines.validate_cypher_prompt


Module Contents
---------------

.. py:data:: CORRECT_CYPHER_PROMPT_TEMPLATE

.. py:data:: CORRECT_CYPHER_SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a Cypher expert reviewing a statement written by a junior developer.
      You need to correct the Cypher statement based on the provided errors. No pre-amble.
      Do not wrap the response in any backticks or anything else. Respond with a Cypher statement only!"""

   .. raw:: html

      </details>



.. py:data:: CORRECT_CYPHER_USER_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Check for invalid syntax or semantics and return a corrected Cypher statement.
      
      Schema:
      {schema}
      
      Note: Do not include any explanations or apologies in your responses.
      Do not wrap the response in any backticks or anything else.
      Respond with a Cypher statement only!
      
      Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
      
      The question is:
      {question}
      
      The Cypher statement is:
      {cypher}
      
      The errors are:
      {errors}"""

   .. raw:: html

      </details>



.. py:data:: GENERATE_FINAL_HUMAN_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Use the following results retrieved from a database to provide
      a succinct, definitive answer to the user's question.
      
      Respond as if you are answering the question directly.
      
      Results: {results}
      Question: {question}"""

   .. raw:: html

      </details>



.. py:data:: GENERATE_FINAL_PROMPT_TEMPLATE

.. py:data:: GUARDRAILS_PROMPT_TEMPLATE

.. py:data:: GUARDRAILS_SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """As an intelligent assistant, your primary objective is to decide whether a given question is related to the {domain_name} domain or not.
      If the question is related to {domain_name}, output "{category}". Otherwise, output "end".
      To make this decision, assess the content of the question and determine if it refers to any topics in the {domain_name} domain.
      Provide only the specified output: "{category}" or "end"."""

   .. raw:: html

      </details>



.. py:data:: TEXT2CYPHER_PROMPT_TEMPLATE

.. py:data:: TEXT2CYPHER_SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a Neo4j expert. Given an input question, create a syntactically correct Cypher query to run.
      Do not wrap the response in any backticks or anything else. Respond with a Cypher statement only!"""

   .. raw:: html

      </details>



.. py:data:: TEXT2CYPHER_USER_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Below are a number of examples of questions and their corresponding Cypher queries.
      
      {fewshot_examples}
      
      User input: {question}
      Cypher query:"""

   .. raw:: html

      </details>



.. py:data:: VALIDATE_CYPHER_SYSTEM_PROMPT
   :value: 'You are a Cypher expert reviewing a statement written by a junior developer.'


.. py:data:: VALIDATE_CYPHER_USER_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You must check the following:
      * Are there any syntax errors in the Cypher statement?
      * Are there any missing or undefined variables in the Cypher statement?
      * Are any node labels missing from the schema?
      * Are any relationship types missing from the schema?
      * Are any of the properties not included in the schema?
      * Does the Cypher statement include enough information to answer the question?
      
      Examples of good errors:
      * Label (:Foo) does not exist, did you mean (:Bar)?
      * Property bar does not exist for label Foo, did you mean baz?
      * Relationship FOO does not exist, did you mean FOO_BAR?
      
      Schema:
      {schema}
      
      The question is:
      {question}
      
      The Cypher statement is:
      {cypher}
      
      Make sure you don't make any mistakes!"""

   .. raw:: html

      </details>



.. py:data:: correct_cypher_aug_llm_config

   Engine for correcting Cypher queries based on validation errors.

   This engine takes a Cypher statement with identified errors and produces
   a corrected version that should be valid against the schema.

   Input Variables:
       - schema: The Neo4j database schema
       - question: The original natural language question
       - cypher: The Cypher statement with errors
       - errors: List of identified errors

   Output:
       CypherQueryOutput with corrected query

   .. autolink-examples:: correct_cypher_aug_llm_config
      :collapse:

.. py:data:: generate_final_aug_llm_config

   Engine for generating natural language answers from query results.

   Takes raw database results and converts them into a human-friendly
   response that directly answers the user's question.

   Input Variables:
       - results: The database query results (list of records)
       - question: The original user question for context

   Output:
       String containing the natural language answer

   .. autolink-examples:: generate_final_aug_llm_config
      :collapse:

.. py:data:: guardrails_aug_llm_config

   Engine for checking domain relevance of user questions.

   This engine acts as a guardrail to ensure questions are within the
   configured domain before attempting to generate Cypher queries.

   Input Variables:
       - domain_name: The configured domain (e.g., "movies")
       - category: The default category for the domain
       - question: The user's question to check

   Output:
       GuardrailsOutput with routing decision

   .. autolink-examples:: guardrails_aug_llm_config
      :collapse:

.. py:data:: text2cypher_aug_llm_config

   Engine for converting natural language questions to Cypher queries.

   Uses few-shot examples to learn the mapping between questions and Cypher
   for the specific domain and schema.

   Input Variables:
       - question: The natural language question
       - fewshot_examples: Examples of question-to-Cypher mappings

   Output:
       String containing the generated Cypher query

   .. autolink-examples:: text2cypher_aug_llm_config
      :collapse:

.. py:data:: validate_cypher_aug_llm_config

   Engine for validating Cypher queries against the database schema.

   This engine checks for syntax errors, schema mismatches, and logical issues
   in generated Cypher queries.

   Input Variables:
       - schema: The Neo4j database schema
       - question: The original question for context
       - cypher: The Cypher statement to validate

   Output:
       ValidateCypherOutput with validation results

   .. autolink-examples:: validate_cypher_aug_llm_config
      :collapse:

.. py:data:: validate_cypher_prompt

