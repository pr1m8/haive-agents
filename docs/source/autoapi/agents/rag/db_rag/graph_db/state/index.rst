
:py:mod:`agents.rag.db_rag.graph_db.state`
==========================================

.. py:module:: agents.rag.db_rag.graph_db.state

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




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for InputState:

   .. graphviz::
      :align: center

      digraph inheritance_InputState {
        node [shape=record];
        "InputState" [label="InputState"];
        "pydantic.BaseModel" -> "InputState";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.state.InputState
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

.. autopydantic_model:: agents.rag.db_rag.graph_db.state.OutputState
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

.. autoclass:: agents.rag.db_rag.graph_db.state.OverallState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.graph_db.state
   :collapse:
   
.. autolink-skip:: next
