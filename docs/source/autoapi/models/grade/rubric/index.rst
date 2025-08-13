
:py:mod:`models.grade.rubric`
=============================

.. py:module:: models.grade.rubric

Rubric grading model for multi-criteria evaluations.

This module implements a rubric-based grading system that evaluates
multiple criteria with individual scores and weights.


.. autolink-examples:: models.grade.rubric
   :collapse:

Classes
-------

.. autoapisummary::

   models.grade.rubric.RubricCriterion
   models.grade.rubric.RubricGrade


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RubricCriterion:

   .. graphviz::
      :align: center

      digraph inheritance_RubricCriterion {
        node [shape=record];
        "RubricCriterion" [label="RubricCriterion"];
        "pydantic.BaseModel" -> "RubricCriterion";
      }

.. autopydantic_model:: models.grade.rubric.RubricCriterion
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

   Inheritance diagram for RubricGrade:

   .. graphviz::
      :align: center

      digraph inheritance_RubricGrade {
        node [shape=record];
        "RubricGrade" [label="RubricGrade"];
        "haive.agents.common.models.grade.base.Grade" -> "RubricGrade";
      }

.. autoclass:: models.grade.rubric.RubricGrade
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: models.grade.rubric
   :collapse:
   
.. autolink-skip:: next
