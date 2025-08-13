
:py:mod:`models.grade.letter_grade`
===================================

.. py:module:: models.grade.letter_grade

Letter grading model for traditional A-F evaluations.

This module implements a traditional letter grading system with support
for plus/minus modifiers and customizable grading scales.


.. autolink-examples:: models.grade.letter_grade
   :collapse:

Classes
-------

.. autoapisummary::

   models.grade.letter_grade.LetterGrade
   models.grade.letter_grade.LetterValue


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LetterGrade:

   .. graphviz::
      :align: center

      digraph inheritance_LetterGrade {
        node [shape=record];
        "LetterGrade" [label="LetterGrade"];
        "haive.agents.common.models.grade.base.Grade" -> "LetterGrade";
      }

.. autoclass:: models.grade.letter_grade.LetterGrade
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LetterValue:

   .. graphviz::
      :align: center

      digraph inheritance_LetterValue {
        node [shape=record];
        "LetterValue" [label="LetterValue"];
        "str" -> "LetterValue";
        "enum.Enum" -> "LetterValue";
      }

.. autoclass:: models.grade.letter_grade.LetterValue
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **LetterValue** is an Enum defined in ``models.grade.letter_grade``.





.. rubric:: Related Links

.. autolink-examples:: models.grade.letter_grade
   :collapse:
   
.. autolink-skip:: next
