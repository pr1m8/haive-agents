
:py:mod:`models.task_analysis.solvability`
==========================================

.. py:module:: models.task_analysis.solvability

Task solvability and readiness assessment.

This module analyzes whether tasks are currently solvable, what barriers exist,
and what would be required to make unsolvable tasks solvable.


.. autolink-examples:: models.task_analysis.solvability
   :collapse:

Classes
-------

.. autoapisummary::

   models.task_analysis.solvability.SolvabilityAssessment
   models.task_analysis.solvability.SolvabilityBarrier


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SolvabilityAssessment:

   .. graphviz::
      :align: center

      digraph inheritance_SolvabilityAssessment {
        node [shape=record];
        "SolvabilityAssessment" [label="SolvabilityAssessment"];
        "pydantic.BaseModel" -> "SolvabilityAssessment";
      }

.. autopydantic_model:: models.task_analysis.solvability.SolvabilityAssessment
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

   Inheritance diagram for SolvabilityBarrier:

   .. graphviz::
      :align: center

      digraph inheritance_SolvabilityBarrier {
        node [shape=record];
        "SolvabilityBarrier" [label="SolvabilityBarrier"];
        "str" -> "SolvabilityBarrier";
        "enum.Enum" -> "SolvabilityBarrier";
      }

.. autoclass:: models.task_analysis.solvability.SolvabilityBarrier
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **SolvabilityBarrier** is an Enum defined in ``models.task_analysis.solvability``.





.. rubric:: Related Links

.. autolink-examples:: models.task_analysis.solvability
   :collapse:
   
.. autolink-skip:: next
