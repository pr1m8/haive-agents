
:py:mod:`agents.task_analysis.execution.models`
===============================================

.. py:module:: agents.task_analysis.execution.models


Classes
-------

.. autoapisummary::

   agents.task_analysis.execution.models.ExecutionPhase
   agents.task_analysis.execution.models.ExecutionPlan
   agents.task_analysis.execution.models.JoinPoint
   agents.task_analysis.execution.models.ResourceAllocation
   agents.task_analysis.execution.models.ResourceType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionPhase:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionPhase {
        node [shape=record];
        "ExecutionPhase" [label="ExecutionPhase"];
        "pydantic.BaseModel" -> "ExecutionPhase";
      }

.. autopydantic_model:: agents.task_analysis.execution.models.ExecutionPhase
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

   Inheritance diagram for ExecutionPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionPlan {
        node [shape=record];
        "ExecutionPlan" [label="ExecutionPlan"];
        "pydantic.BaseModel" -> "ExecutionPlan";
      }

.. autopydantic_model:: agents.task_analysis.execution.models.ExecutionPlan
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

   Inheritance diagram for JoinPoint:

   .. graphviz::
      :align: center

      digraph inheritance_JoinPoint {
        node [shape=record];
        "JoinPoint" [label="JoinPoint"];
        "pydantic.BaseModel" -> "JoinPoint";
      }

.. autopydantic_model:: agents.task_analysis.execution.models.JoinPoint
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

   Inheritance diagram for ResourceAllocation:

   .. graphviz::
      :align: center

      digraph inheritance_ResourceAllocation {
        node [shape=record];
        "ResourceAllocation" [label="ResourceAllocation"];
        "pydantic.BaseModel" -> "ResourceAllocation";
      }

.. autopydantic_model:: agents.task_analysis.execution.models.ResourceAllocation
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

   Inheritance diagram for ResourceType:

   .. graphviz::
      :align: center

      digraph inheritance_ResourceType {
        node [shape=record];
        "ResourceType" [label="ResourceType"];
        "str" -> "ResourceType";
        "enum.Enum" -> "ResourceType";
      }

.. autoclass:: agents.task_analysis.execution.models.ResourceType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ResourceType** is an Enum defined in ``agents.task_analysis.execution.models``.





.. rubric:: Related Links

.. autolink-examples:: agents.task_analysis.execution.models
   :collapse:
   
.. autolink-skip:: next
