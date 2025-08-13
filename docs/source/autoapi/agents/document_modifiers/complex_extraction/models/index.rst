
:py:mod:`agents.document_modifiers.complex_extraction.models`
=============================================================

.. py:module:: agents.document_modifiers.complex_extraction.models


Classes
-------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.models.JsonPatch
   agents.document_modifiers.complex_extraction.models.PatchFunctionParameters
   agents.document_modifiers.complex_extraction.models.RetryStrategy


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for JsonPatch:

   .. graphviz::
      :align: center

      digraph inheritance_JsonPatch {
        node [shape=record];
        "JsonPatch" [label="JsonPatch"];
        "pydantic.BaseModel" -> "JsonPatch";
      }

.. autopydantic_model:: agents.document_modifiers.complex_extraction.models.JsonPatch
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

   Inheritance diagram for PatchFunctionParameters:

   .. graphviz::
      :align: center

      digraph inheritance_PatchFunctionParameters {
        node [shape=record];
        "PatchFunctionParameters" [label="PatchFunctionParameters"];
        "pydantic.BaseModel" -> "PatchFunctionParameters";
      }

.. autopydantic_model:: agents.document_modifiers.complex_extraction.models.PatchFunctionParameters
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

   Inheritance diagram for RetryStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RetryStrategy {
        node [shape=record];
        "RetryStrategy" [label="RetryStrategy"];
        "TypedDict" -> "RetryStrategy";
      }

.. autoclass:: agents.document_modifiers.complex_extraction.models.RetryStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.complex_extraction.models
   :collapse:
   
.. autolink-skip:: next
