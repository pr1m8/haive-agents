
:py:mod:`agents.task_analysis.context.models`
=============================================

.. py:module:: agents.task_analysis.context.models


Classes
-------

.. autoapisummary::

   agents.task_analysis.context.models.ContextAnalysis
   agents.task_analysis.context.models.ContextDomain
   agents.task_analysis.context.models.ContextFlow
   agents.task_analysis.context.models.ContextFreshness
   agents.task_analysis.context.models.ContextRequirement
   agents.task_analysis.context.models.ContextSize


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContextAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_ContextAnalysis {
        node [shape=record];
        "ContextAnalysis" [label="ContextAnalysis"];
        "pydantic.BaseModel" -> "ContextAnalysis";
      }

.. autopydantic_model:: agents.task_analysis.context.models.ContextAnalysis
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

   Inheritance diagram for ContextDomain:

   .. graphviz::
      :align: center

      digraph inheritance_ContextDomain {
        node [shape=record];
        "ContextDomain" [label="ContextDomain"];
        "pydantic.BaseModel" -> "ContextDomain";
      }

.. autopydantic_model:: agents.task_analysis.context.models.ContextDomain
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

   Inheritance diagram for ContextFlow:

   .. graphviz::
      :align: center

      digraph inheritance_ContextFlow {
        node [shape=record];
        "ContextFlow" [label="ContextFlow"];
        "pydantic.BaseModel" -> "ContextFlow";
      }

.. autopydantic_model:: agents.task_analysis.context.models.ContextFlow
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

   Inheritance diagram for ContextFreshness:

   .. graphviz::
      :align: center

      digraph inheritance_ContextFreshness {
        node [shape=record];
        "ContextFreshness" [label="ContextFreshness"];
        "str" -> "ContextFreshness";
        "enum.Enum" -> "ContextFreshness";
      }

.. autoclass:: agents.task_analysis.context.models.ContextFreshness
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ContextFreshness** is an Enum defined in ``agents.task_analysis.context.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContextRequirement:

   .. graphviz::
      :align: center

      digraph inheritance_ContextRequirement {
        node [shape=record];
        "ContextRequirement" [label="ContextRequirement"];
        "pydantic.BaseModel" -> "ContextRequirement";
      }

.. autopydantic_model:: agents.task_analysis.context.models.ContextRequirement
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

   Inheritance diagram for ContextSize:

   .. graphviz::
      :align: center

      digraph inheritance_ContextSize {
        node [shape=record];
        "ContextSize" [label="ContextSize"];
        "str" -> "ContextSize";
        "enum.Enum" -> "ContextSize";
      }

.. autoclass:: agents.task_analysis.context.models.ContextSize
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ContextSize** is an Enum defined in ``agents.task_analysis.context.models``.





.. rubric:: Related Links

.. autolink-examples:: agents.task_analysis.context.models
   :collapse:
   
.. autolink-skip:: next
