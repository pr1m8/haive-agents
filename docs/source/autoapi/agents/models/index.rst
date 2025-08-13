
:py:mod:`agents.models`
=======================

.. py:module:: agents.models


Classes
-------

.. autoapisummary::

   agents.models.BBox
   agents.models.Prediction


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BBox:

   .. graphviz::
      :align: center

      digraph inheritance_BBox {
        node [shape=record];
        "BBox" [label="BBox"];
        "typing_extensions.TypedDict" -> "BBox";
      }

.. autoclass:: agents.models.BBox
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Prediction:

   .. graphviz::
      :align: center

      digraph inheritance_Prediction {
        node [shape=record];
        "Prediction" [label="Prediction"];
        "pydantic.BaseModel" -> "Prediction";
      }

.. autopydantic_model:: agents.models.Prediction
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

.. autolink-examples:: agents.models
   :collapse:
   
.. autolink-skip:: next
