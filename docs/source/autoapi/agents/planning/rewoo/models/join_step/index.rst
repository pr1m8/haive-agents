
:py:mod:`agents.planning.rewoo.models.join_step`
================================================

.. py:module:: agents.planning.rewoo.models.join_step

Join Step - Automatic DAG and Parallelization with Auto-detection.

Inspired by haive.core.common.structures.tree, this implements a JoinStep that
automatically detects parallel branches and creates join points for DAG execution.

Similar to AutoTree's pattern of automatically detecting BaseModel relationships,
JoinStep automatically detects step dependencies and creates optimal join points
for parallel execution.


.. autolink-examples:: agents.planning.rewoo.models.join_step
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo.models.join_step.AbstractStep
   agents.planning.rewoo.models.join_step.JoinStep
   agents.planning.rewoo.models.join_step.JoinStrategy


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AbstractStep:

   .. graphviz::
      :align: center

      digraph inheritance_AbstractStep {
        node [shape=record];
        "AbstractStep" [label="AbstractStep"];
        "pydantic.BaseModel" -> "AbstractStep";
        "abc.ABC" -> "AbstractStep";
      }

.. autopydantic_model:: agents.planning.rewoo.models.join_step.AbstractStep
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

   Inheritance diagram for JoinStep:

   .. graphviz::
      :align: center

      digraph inheritance_JoinStep {
        node [shape=record];
        "JoinStep" [label="JoinStep"];
        "agents.planning.rewoo.models.steps.AbstractStep" -> "JoinStep";
      }

.. autoclass:: agents.planning.rewoo.models.join_step.JoinStep
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for JoinStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_JoinStrategy {
        node [shape=record];
        "JoinStrategy" [label="JoinStrategy"];
        "str" -> "JoinStrategy";
        "enum.Enum" -> "JoinStrategy";
      }

.. autoclass:: agents.planning.rewoo.models.join_step.JoinStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **JoinStrategy** is an Enum defined in ``agents.planning.rewoo.models.join_step``.





.. rubric:: Related Links

.. autolink-examples:: agents.planning.rewoo.models.join_step
   :collapse:
   
.. autolink-skip:: next
