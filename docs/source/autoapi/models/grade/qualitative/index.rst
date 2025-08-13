
:py:mod:`models.grade.qualitative`
==================================

.. py:module:: models.grade.qualitative

Qualitative grading model for text-based evaluations.

This module implements a qualitative grading system that provides
text-based assessments with sentiment analysis and quality indicators.


.. autolink-examples:: models.grade.qualitative
   :collapse:

Classes
-------

.. autoapisummary::

   models.grade.qualitative.QualitativeGrade
   models.grade.qualitative.QualityLevel
   models.grade.qualitative.SentimentType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QualitativeGrade:

   .. graphviz::
      :align: center

      digraph inheritance_QualitativeGrade {
        node [shape=record];
        "QualitativeGrade" [label="QualitativeGrade"];
        "haive.agents.common.models.grade.base.Grade" -> "QualitativeGrade";
      }

.. autoclass:: models.grade.qualitative.QualitativeGrade
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QualityLevel:

   .. graphviz::
      :align: center

      digraph inheritance_QualityLevel {
        node [shape=record];
        "QualityLevel" [label="QualityLevel"];
        "str" -> "QualityLevel";
        "enum.Enum" -> "QualityLevel";
      }

.. autoclass:: models.grade.qualitative.QualityLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QualityLevel** is an Enum defined in ``models.grade.qualitative``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SentimentType:

   .. graphviz::
      :align: center

      digraph inheritance_SentimentType {
        node [shape=record];
        "SentimentType" [label="SentimentType"];
        "str" -> "SentimentType";
        "enum.Enum" -> "SentimentType";
      }

.. autoclass:: models.grade.qualitative.SentimentType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **SentimentType** is an Enum defined in ``models.grade.qualitative``.





.. rubric:: Related Links

.. autolink-examples:: models.grade.qualitative
   :collapse:
   
.. autolink-skip:: next
