agents.rag.db_rag.sql_rag.state
===============================

.. py:module:: agents.rag.db_rag.sql_rag.state

.. autoapi-nested-parse::

   State schemas for SQL RAG Agent.

   This module defines the state schemas used throughout the SQL RAG workflow.
   It includes input, output, and intermediate state representations that flow
   through the agent's graph nodes.

   The state pattern enables tracking of all intermediate steps, results, and
   metadata throughout the query generation and execution process.

   .. rubric:: Example

   Working with agent states::

       >>> from haive.agents.rag.db_rag.sql_rag.state import OverallState
       >>>
       >>> # Initialize state with a question
       >>> state = OverallState(question="Show me top customers by revenue")
       >>>
       >>> # State updates through workflow
       >>> state.steps.append("analyze_query")
       >>> state.analysis = {"relevant_tables": ["customers", "orders"]}
       >>> state.sql_query = "SELECT c.name, SUM(o.total) FROM customers c..."
       >>>
       >>> # Final output
       >>> state.answer = "The top customers by revenue are..."


   .. autolink-examples:: agents.rag.db_rag.sql_rag.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.state.InputState
   agents.rag.db_rag.sql_rag.state.OutputState
   agents.rag.db_rag.sql_rag.state.OverallState


Module Contents
---------------

.. py:class:: InputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input state for the SQL database agent.

   This represents the initial input to the agent - just the natural
   language question to be answered.

   .. attribute:: question

      The natural language question to ask the SQL database.

      :type: str

   .. rubric:: Example

   >>> input_state = InputState(
   ...     question="What were the total sales last month?"
   ... )

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


   Output state for the SQL database agent.

   This represents the final output from the agent including the answer
   and any validation results.

   .. attribute:: answer

      The natural language answer to the question.

      :type: str

   .. attribute:: sql_statement

      The SQL query that was executed.

      :type: str

   .. attribute:: hallucination_check

      Result of hallucination detection.

      :type: Optional[str]

   .. attribute:: answer_grade

      Result of answer quality grading.

      :type: Optional[str]

   .. rubric:: Example

   >>> output = OutputState(
   ...     answer="Total sales last month were $125,000 across 350 orders.",
   ...     sql_statement="SELECT SUM(total), COUNT(*) FROM orders WHERE date >= '2024-01-01'",
   ...     hallucination_check="no",
   ...     answer_grade="yes"
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



   .. py:attribute:: answer_grade
      :type:  str | None
      :value: None



   .. py:attribute:: hallucination_check
      :type:  str | None
      :value: None



   .. py:attribute:: sql_statement
      :type:  str
      :value: None



.. py:class:: OverallState(/, **data: Any)

   Bases: :py:obj:`InputState`, :py:obj:`OutputState`


   Overall state for the SQL database agent workflow.

   This comprehensive state class tracks all information throughout the
   agent's execution, including inputs, intermediate results, and outputs.
   It inherits from both InputState and OutputState to provide a complete view.

   .. attribute:: Input

      question (str): The question to ask the SQL database.

      :type: inherited from InputState

   .. attribute:: Intermediate

      steps (List[str]): Workflow steps executed.
      next_action (str): The next action to take in the workflow.
      analysis (Dict[str, Any]): Query analysis results.
      sql_errors (List[str]): SQL validation errors.
      sql_query (str): The generated SQL query.
      query_result (str): Raw results from database query.
      database_records (Any): Parsed database query results.
      messages (List[Any]): Conversation messages.

   .. attribute:: Output

      answer (str): The final answer.
      hallucination_check (Optional[str]): Hallucination detection result.
      answer_grade (Optional[str]): Answer quality grade.

      :type: inherited from OutputState

   .. rubric:: Example

   Tracking workflow state::

       >>> state = OverallState(question="Show revenue by product category")
       >>>
       >>> # After analysis
       >>> state.analysis = {
       ...     "relevant_tables": ["products", "orders", "order_items"],
       ...     "aggregations": ["SUM(price * quantity)"]
       ... }
       >>> state.steps.append("analyze_query")
       >>>
       >>> # After SQL generation
       >>> state.sql_query = "SELECT p.category, SUM(oi.price * oi.quantity) as revenue..."
       >>> state.steps.append("generate_query")
       >>>
       >>> # After execution
       >>> state.query_result = "Electronics|50000\\nClothing|30000\\n..."
       >>> state.steps.append("execute_query")
       >>>
       >>> # Final answer
       >>> state.answer = "Revenue by category: Electronics ($50,000), Clothing ($30,000)..."
       >>> state.steps.append("generate_answer")

   .. note::

      The steps list provides an audit trail of the workflow execution,
      useful for debugging and understanding the agent's decision process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: OverallState
      :collapse:

   .. py:attribute:: analysis
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: database_records
      :type:  Any
      :value: None



   .. py:attribute:: messages
      :type:  list[Any]
      :value: None



   .. py:attribute:: next_action
      :type:  str
      :value: None



   .. py:attribute:: query_result
      :type:  str
      :value: None



   .. py:attribute:: sql_errors
      :type:  list[str]
      :value: None



   .. py:attribute:: sql_query
      :type:  str
      :value: None



   .. py:attribute:: steps
      :type:  list[str]
      :value: None



