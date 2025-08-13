
:py:mod:`agents.document_modifiers.summarizer.map_branch.state`
===============================================================

.. py:module:: agents.document_modifiers.summarizer.map_branch.state

State for the summarizer agent.


.. autolink-examples:: agents.document_modifiers.summarizer.map_branch.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.map_branch.state.InputState
   agents.document_modifiers.summarizer.map_branch.state.OutputState
   agents.document_modifiers.summarizer.map_branch.state.SummaryState


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

.. autopydantic_model:: agents.document_modifiers.summarizer.map_branch.state.InputState
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

.. autopydantic_model:: agents.document_modifiers.summarizer.map_branch.state.OutputState
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

   Inheritance diagram for SummaryState:

   .. graphviz::
      :align: center

      digraph inheritance_SummaryState {
        node [shape=record];
        "SummaryState" [label="SummaryState"];
        "InputState" -> "SummaryState";
        "OutputState" -> "SummaryState";
      }

.. autoclass:: agents.document_modifiers.summarizer.map_branch.state.SummaryState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.summarizer.map_branch.state
   :collapse:
   
.. autolink-skip:: next
