
:py:mod:`agents.structured.models`
==================================

.. py:module:: agents.structured.models

Pydantic models for structured output agents.

This module defines the common output models used by structured agents
for converting unstructured text into organized data.


.. autolink-examples:: agents.structured.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.structured.models.AnalysisOutput
   agents.structured.models.DecisionOutput
   agents.structured.models.GenericStructuredOutput
   agents.structured.models.TaskOutput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AnalysisOutput:

   .. graphviz::
      :align: center

      digraph inheritance_AnalysisOutput {
        node [shape=record];
        "AnalysisOutput" [label="AnalysisOutput"];
        "pydantic.BaseModel" -> "AnalysisOutput";
      }

.. autopydantic_model:: agents.structured.models.AnalysisOutput
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

   Inheritance diagram for DecisionOutput:

   .. graphviz::
      :align: center

      digraph inheritance_DecisionOutput {
        node [shape=record];
        "DecisionOutput" [label="DecisionOutput"];
        "pydantic.BaseModel" -> "DecisionOutput";
      }

.. autopydantic_model:: agents.structured.models.DecisionOutput
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

   Inheritance diagram for GenericStructuredOutput:

   .. graphviz::
      :align: center

      digraph inheritance_GenericStructuredOutput {
        node [shape=record];
        "GenericStructuredOutput" [label="GenericStructuredOutput"];
        "pydantic.BaseModel" -> "GenericStructuredOutput";
      }

.. autopydantic_model:: agents.structured.models.GenericStructuredOutput
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

   Inheritance diagram for TaskOutput:

   .. graphviz::
      :align: center

      digraph inheritance_TaskOutput {
        node [shape=record];
        "TaskOutput" [label="TaskOutput"];
        "pydantic.BaseModel" -> "TaskOutput";
      }

.. autopydantic_model:: agents.structured.models.TaskOutput
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





.. rubric:: Related Links

.. autolink-examples:: agents.structured.models
   :collapse:
   
.. autolink-skip:: next
