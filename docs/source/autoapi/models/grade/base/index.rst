
:py:mod:`models.grade.base`
===========================

.. py:module:: models.grade.base

Base classes for grade models.

This module defines the fundamental abstractions for all grading models
including the grade type enumeration and abstract base class.


.. autolink-examples:: models.grade.base
   :collapse:

Classes
-------

.. autoapisummary::

   models.grade.base.Grade
   models.grade.base.GradeType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Grade:

   .. graphviz::
      :align: center

      digraph inheritance_Grade {
        node [shape=record];
        "Grade" [label="Grade"];
        "pydantic.BaseModel" -> "Grade";
        "abc.ABC" -> "Grade";
      }

.. autopydantic_model:: models.grade.base.Grade
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

   Inheritance diagram for GradeType:

   .. graphviz::
      :align: center

      digraph inheritance_GradeType {
        node [shape=record];
        "GradeType" [label="GradeType"];
        "str" -> "GradeType";
        "enum.Enum" -> "GradeType";
      }

.. autoclass:: models.grade.base.GradeType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GradeType** is an Enum defined in ``models.grade.base``.





.. rubric:: Related Links

.. autolink-examples:: models.grade.base
   :collapse:
   
.. autolink-skip:: next
