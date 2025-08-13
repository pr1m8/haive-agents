
:py:mod:`agents.reasoning_and_critique.tot.state`
=================================================

.. py:module:: agents.reasoning_and_critique.tot.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.state.TOTInput
   agents.reasoning_and_critique.tot.state.TOTOutput
   agents.reasoning_and_critique.tot.state.TOTState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TOTInput:

   .. graphviz::
      :align: center

      digraph inheritance_TOTInput {
        node [shape=record];
        "TOTInput" [label="TOTInput"];
        "pydantic.BaseModel" -> "TOTInput";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.state.TOTInput
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

   Inheritance diagram for TOTOutput:

   .. graphviz::
      :align: center

      digraph inheritance_TOTOutput {
        node [shape=record];
        "TOTOutput" [label="TOTOutput"];
        "pydantic.BaseModel" -> "TOTOutput";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.state.TOTOutput
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

   Inheritance diagram for TOTState:

   .. graphviz::
      :align: center

      digraph inheritance_TOTState {
        node [shape=record];
        "TOTState" [label="TOTState"];
        "TOTInput" -> "TOTState";
        "TOTOutput" -> "TOTState";
      }

.. autoclass:: agents.reasoning_and_critique.tot.state.TOTState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.state
   :collapse:
   
.. autolink-skip:: next
