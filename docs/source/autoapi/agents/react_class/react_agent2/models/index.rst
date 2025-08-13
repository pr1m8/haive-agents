
:py:mod:`agents.react_class.react_agent2.models`
================================================

.. py:module:: agents.react_class.react_agent2.models


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.models.Action
   agents.react_class.react_agent2.models.ActionType
   agents.react_class.react_agent2.models.ReactionData
   agents.react_class.react_agent2.models.ReactState
   agents.react_class.react_agent2.models.Thought


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Action:

   .. graphviz::
      :align: center

      digraph inheritance_Action {
        node [shape=record];
        "Action" [label="Action"];
        "pydantic.BaseModel" -> "Action";
      }

.. autopydantic_model:: agents.react_class.react_agent2.models.Action
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

   Inheritance diagram for ActionType:

   .. graphviz::
      :align: center

      digraph inheritance_ActionType {
        node [shape=record];
        "ActionType" [label="ActionType"];
        "str" -> "ActionType";
        "enum.Enum" -> "ActionType";
      }

.. autoclass:: agents.react_class.react_agent2.models.ActionType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ActionType** is an Enum defined in ``agents.react_class.react_agent2.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactState:

   .. graphviz::
      :align: center

      digraph inheritance_ReactState {
        node [shape=record];
        "ReactState" [label="ReactState"];
        "pydantic.BaseModel" -> "ReactState";
      }

.. autopydantic_model:: agents.react_class.react_agent2.models.ReactState
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

   Inheritance diagram for ReactionData:

   .. graphviz::
      :align: center

      digraph inheritance_ReactionData {
        node [shape=record];
        "ReactionData" [label="ReactionData"];
        "pydantic.BaseModel" -> "ReactionData";
      }

.. autopydantic_model:: agents.react_class.react_agent2.models.ReactionData
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

   Inheritance diagram for Thought:

   .. graphviz::
      :align: center

      digraph inheritance_Thought {
        node [shape=record];
        "Thought" [label="Thought"];
        "pydantic.BaseModel" -> "Thought";
      }

.. autopydantic_model:: agents.react_class.react_agent2.models.Thought
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

.. autolink-examples:: agents.react_class.react_agent2.models
   :collapse:
   
.. autolink-skip:: next
