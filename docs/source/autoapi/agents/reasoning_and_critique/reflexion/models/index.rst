
:py:mod:`agents.reasoning_and_critique.reflexion.models`
========================================================

.. py:module:: agents.reasoning_and_critique.reflexion.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflexion.models.AnswerQuestion
   agents.reasoning_and_critique.reflexion.models.Reflection
   agents.reasoning_and_critique.reflexion.models.ReviseAnswer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AnswerQuestion:

   .. graphviz::
      :align: center

      digraph inheritance_AnswerQuestion {
        node [shape=record];
        "AnswerQuestion" [label="AnswerQuestion"];
        "pydantic.BaseModel" -> "AnswerQuestion";
      }

.. autopydantic_model:: agents.reasoning_and_critique.reflexion.models.AnswerQuestion
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

   Inheritance diagram for Reflection:

   .. graphviz::
      :align: center

      digraph inheritance_Reflection {
        node [shape=record];
        "Reflection" [label="Reflection"];
        "pydantic.BaseModel" -> "Reflection";
      }

.. autopydantic_model:: agents.reasoning_and_critique.reflexion.models.Reflection
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

   Inheritance diagram for ReviseAnswer:

   .. graphviz::
      :align: center

      digraph inheritance_ReviseAnswer {
        node [shape=record];
        "ReviseAnswer" [label="ReviseAnswer"];
        "AnswerQuestion" -> "ReviseAnswer";
      }

.. autoclass:: agents.reasoning_and_critique.reflexion.models.ReviseAnswer
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.reflexion.models
   :collapse:
   
.. autolink-skip:: next
