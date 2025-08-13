
:py:mod:`agents.agent`
======================

.. py:module:: agents.agent


Classes
-------

.. autoapisummary::

   agents.agent.BBox
   agents.agent.Prediction
   agents.agent.WebNavAgent
   agents.agent.WebNavAgentConfig
   agents.agent.WebNavState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BBox:

   .. graphviz::
      :align: center

      digraph inheritance_BBox {
        node [shape=record];
        "BBox" [label="BBox"];
        "pydantic.BaseModel" -> "BBox";
      }

.. autopydantic_model:: agents.agent.BBox
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

   Inheritance diagram for Prediction:

   .. graphviz::
      :align: center

      digraph inheritance_Prediction {
        node [shape=record];
        "Prediction" [label="Prediction"];
        "pydantic.BaseModel" -> "Prediction";
      }

.. autopydantic_model:: agents.agent.Prediction
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

   Inheritance diagram for WebNavAgent:

   .. graphviz::
      :align: center

      digraph inheritance_WebNavAgent {
        node [shape=record];
        "WebNavAgent" [label="WebNavAgent"];
        "haive.core.engine.agent.agent.Agent[WebNavAgentConfig]" -> "WebNavAgent";
      }

.. autoclass:: agents.agent.WebNavAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WebNavAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_WebNavAgentConfig {
        node [shape=record];
        "WebNavAgentConfig" [label="WebNavAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "WebNavAgentConfig";
      }

.. autoclass:: agents.agent.WebNavAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WebNavState:

   .. graphviz::
      :align: center

      digraph inheritance_WebNavState {
        node [shape=record];
        "WebNavState" [label="WebNavState"];
        "pydantic.BaseModel" -> "WebNavState";
      }

.. autopydantic_model:: agents.agent.WebNavState
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



Functions
---------

.. autoapisummary::

   agents.agent.debug_print
   agents.agent.run_web_navigator

.. py:function:: debug_print(message: str)

   Helper function to print and log debug messages.


   .. autolink-examples:: debug_print
      :collapse:

.. py:function:: run_web_navigator()
   :async:




.. rubric:: Related Links

.. autolink-examples:: agents.agent
   :collapse:
   
.. autolink-skip:: next
