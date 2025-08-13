
:py:mod:`agents.reasoning_and_critique.lats.models`
===================================================

.. py:module:: agents.reasoning_and_critique.lats.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.models.Node
   agents.reasoning_and_critique.lats.models.Reflection


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Node:

   .. graphviz::
      :align: center

      digraph inheritance_Node {
        node [shape=record];
        "Node" [label="Node"];
      }

.. autoclass:: agents.reasoning_and_critique.lats.models.Node
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Reflection:

   .. graphviz::
      :align: center

      digraph inheritance_Reflection {
        node [shape=record];
        "Reflection" [label="Reflection"];
        "pydantic.BaseModel" -> "Reflection";
      }

.. autopydantic_model:: agents.reasoning_and_critique.lats.models.Reflection
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





.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.lats.models
   :collapse:
   
.. autolink-skip:: next
