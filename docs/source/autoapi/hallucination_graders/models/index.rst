
:py:mod:`hallucination_graders.models`
======================================

.. py:module:: hallucination_graders.models


Classes
-------

.. autoapisummary::

   hallucination_graders.models.HallucinationBinaryResponse
   hallucination_graders.models.HallucinationClaim
   hallucination_graders.models.HallucinationDetectionResponse
   hallucination_graders.models.HallucinationType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HallucinationBinaryResponse:

   .. graphviz::
      :align: center

      digraph inheritance_HallucinationBinaryResponse {
        node [shape=record];
        "HallucinationBinaryResponse" [label="HallucinationBinaryResponse"];
        "pydantic.BaseModel" -> "HallucinationBinaryResponse";
      }

.. autopydantic_model:: hallucination_graders.models.HallucinationBinaryResponse
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

   Inheritance diagram for HallucinationClaim:

   .. graphviz::
      :align: center

      digraph inheritance_HallucinationClaim {
        node [shape=record];
        "HallucinationClaim" [label="HallucinationClaim"];
        "pydantic.BaseModel" -> "HallucinationClaim";
      }

.. autopydantic_model:: hallucination_graders.models.HallucinationClaim
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

   Inheritance diagram for HallucinationDetectionResponse:

   .. graphviz::
      :align: center

      digraph inheritance_HallucinationDetectionResponse {
        node [shape=record];
        "HallucinationDetectionResponse" [label="HallucinationDetectionResponse"];
        "pydantic.BaseModel" -> "HallucinationDetectionResponse";
      }

.. autopydantic_model:: hallucination_graders.models.HallucinationDetectionResponse
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

   Inheritance diagram for HallucinationType:

   .. graphviz::
      :align: center

      digraph inheritance_HallucinationType {
        node [shape=record];
        "HallucinationType" [label="HallucinationType"];
        "str" -> "HallucinationType";
        "enum.Enum" -> "HallucinationType";
      }

.. autoclass:: hallucination_graders.models.HallucinationType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HallucinationType** is an Enum defined in ``hallucination_graders.models``.





.. rubric:: Related Links

.. autolink-examples:: hallucination_graders.models
   :collapse:
   
.. autolink-skip:: next
