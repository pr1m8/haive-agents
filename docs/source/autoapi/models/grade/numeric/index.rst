
:py:mod:`models.grade.numeric`
==============================

.. py:module:: models.grade.numeric

Numeric grading models for score-based evaluations.

This module implements numeric grading systems including general numeric
scores and percentage-based grading.


.. autolink-examples:: models.grade.numeric
   :collapse:

Classes
-------

.. autoapisummary::

   models.grade.numeric.NumericGrade
   models.grade.numeric.PercentageGrade


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NumericGrade:

   .. graphviz::
      :align: center

      digraph inheritance_NumericGrade {
        node [shape=record];
        "NumericGrade" [label="NumericGrade"];
        "haive.agents.common.models.grade.base.Grade" -> "NumericGrade";
      }

.. autoclass:: models.grade.numeric.NumericGrade
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PercentageGrade:

   .. graphviz::
      :align: center

      digraph inheritance_PercentageGrade {
        node [shape=record];
        "PercentageGrade" [label="PercentageGrade"];
        "NumericGrade" -> "PercentageGrade";
      }

.. autoclass:: models.grade.numeric.PercentageGrade
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: models.grade.numeric
   :collapse:
   
.. autolink-skip:: next
