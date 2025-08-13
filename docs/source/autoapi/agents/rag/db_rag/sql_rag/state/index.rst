
:py:mod:`agents.rag.db_rag.sql_rag.state`
=========================================

.. py:module:: agents.rag.db_rag.sql_rag.state

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




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for InputState:

   .. graphviz::
      :align: center

      digraph inheritance_InputState {
        node [shape=record];
        "InputState" [label="InputState"];
        "pydantic.BaseModel" -> "InputState";
      }

.. autopydantic_model:: agents.rag.db_rag.sql_rag.state.InputState
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

   Inheritance diagram for OutputState:

   .. graphviz::
      :align: center

      digraph inheritance_OutputState {
        node [shape=record];
        "OutputState" [label="OutputState"];
        "pydantic.BaseModel" -> "OutputState";
      }

.. autopydantic_model:: agents.rag.db_rag.sql_rag.state.OutputState
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

   Inheritance diagram for OverallState:

   .. graphviz::
      :align: center

      digraph inheritance_OverallState {
        node [shape=record];
        "OverallState" [label="OverallState"];
        "InputState" -> "OverallState";
        "OutputState" -> "OverallState";
      }

.. autoclass:: agents.rag.db_rag.sql_rag.state.OverallState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.sql_rag.state
   :collapse:
   
.. autolink-skip:: next
