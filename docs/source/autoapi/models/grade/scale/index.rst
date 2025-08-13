
:py:mod:`models.grade.scale`
============================

.. py:module:: models.grade.scale

Scale grading model for Likert-style evaluations.

This module implements scale-based grading systems including Likert scales,
satisfaction ratings, and custom ordinal scales.


.. autolink-examples:: models.grade.scale
   :collapse:

Classes
-------

.. autoapisummary::

   models.grade.scale.LikertScale
   models.grade.scale.SatisfactionScale
   models.grade.scale.ScaleGrade


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LikertScale:

   .. graphviz::
      :align: center

      digraph inheritance_LikertScale {
        node [shape=record];
        "LikertScale" [label="LikertScale"];
        "str" -> "LikertScale";
        "enum.Enum" -> "LikertScale";
      }

.. autoclass:: models.grade.scale.LikertScale
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **LikertScale** is an Enum defined in ``models.grade.scale``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SatisfactionScale:

   .. graphviz::
      :align: center

      digraph inheritance_SatisfactionScale {
        node [shape=record];
        "SatisfactionScale" [label="SatisfactionScale"];
        "str" -> "SatisfactionScale";
        "enum.Enum" -> "SatisfactionScale";
      }

.. autoclass:: models.grade.scale.SatisfactionScale
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **SatisfactionScale** is an Enum defined in ``models.grade.scale``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ScaleGrade:

   .. graphviz::
      :align: center

      digraph inheritance_ScaleGrade {
        node [shape=record];
        "ScaleGrade" [label="ScaleGrade"];
        "haive.agents.common.models.grade.base.Grade" -> "ScaleGrade";
      }

.. autoclass:: models.grade.scale.ScaleGrade
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: models.grade.scale
   :collapse:
   
.. autolink-skip:: next
