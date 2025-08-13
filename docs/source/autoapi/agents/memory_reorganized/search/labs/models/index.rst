
:py:mod:`agents.memory_reorganized.search.labs.models`
======================================================

.. py:module:: agents.memory_reorganized.search.labs.models

Data models for Labs Agent.


.. autolink-examples:: agents.memory_reorganized.search.labs.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.search.labs.models.AssetType
   agents.memory_reorganized.search.labs.models.InteractiveApp
   agents.memory_reorganized.search.labs.models.LabsRequest
   agents.memory_reorganized.search.labs.models.LabsResponse
   agents.memory_reorganized.search.labs.models.ProjectAsset
   agents.memory_reorganized.search.labs.models.WorkflowStep


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AssetType:

   .. graphviz::
      :align: center

      digraph inheritance_AssetType {
        node [shape=record];
        "AssetType" [label="AssetType"];
        "str" -> "AssetType";
        "enum.Enum" -> "AssetType";
      }

.. autoclass:: agents.memory_reorganized.search.labs.models.AssetType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **AssetType** is an Enum defined in ``agents.memory_reorganized.search.labs.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for InteractiveApp:

   .. graphviz::
      :align: center

      digraph inheritance_InteractiveApp {
        node [shape=record];
        "InteractiveApp" [label="InteractiveApp"];
        "pydantic.BaseModel" -> "InteractiveApp";
      }

.. autopydantic_model:: agents.memory_reorganized.search.labs.models.InteractiveApp
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

   Inheritance diagram for LabsRequest:

   .. graphviz::
      :align: center

      digraph inheritance_LabsRequest {
        node [shape=record];
        "LabsRequest" [label="LabsRequest"];
        "pydantic.BaseModel" -> "LabsRequest";
      }

.. autopydantic_model:: agents.memory_reorganized.search.labs.models.LabsRequest
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

   Inheritance diagram for LabsResponse:

   .. graphviz::
      :align: center

      digraph inheritance_LabsResponse {
        node [shape=record];
        "LabsResponse" [label="LabsResponse"];
        "haive.agents.memory.search.base.SearchResponse" -> "LabsResponse";
      }

.. autoclass:: agents.memory_reorganized.search.labs.models.LabsResponse
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ProjectAsset:

   .. graphviz::
      :align: center

      digraph inheritance_ProjectAsset {
        node [shape=record];
        "ProjectAsset" [label="ProjectAsset"];
        "pydantic.BaseModel" -> "ProjectAsset";
      }

.. autopydantic_model:: agents.memory_reorganized.search.labs.models.ProjectAsset
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

   Inheritance diagram for WorkflowStep:

   .. graphviz::
      :align: center

      digraph inheritance_WorkflowStep {
        node [shape=record];
        "WorkflowStep" [label="WorkflowStep"];
        "pydantic.BaseModel" -> "WorkflowStep";
      }

.. autopydantic_model:: agents.memory_reorganized.search.labs.models.WorkflowStep
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

.. autolink-examples:: agents.memory_reorganized.search.labs.models
   :collapse:
   
.. autolink-skip:: next
