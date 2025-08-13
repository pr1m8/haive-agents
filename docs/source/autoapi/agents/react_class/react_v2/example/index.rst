
:py:mod:`agents.react_class.react_v2.example`
=============================================

.. py:module:: agents.react_class.react_v2.example


Classes
-------

.. autoapisummary::

   agents.react_class.react_v2.example.TripPlan


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TripPlan:

   .. graphviz::
      :align: center

      digraph inheritance_TripPlan {
        node [shape=record];
        "TripPlan" [label="TripPlan"];
        "pydantic.BaseModel" -> "TripPlan";
      }

.. autopydantic_model:: agents.react_class.react_v2.example.TripPlan
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

   agents.react_class.react_v2.example.calculate
   agents.react_class.react_v2.example.get_weather
   agents.react_class.react_v2.example.search_database
   agents.react_class.react_v2.example.simulate_react_agent_with_human

.. py:function:: calculate(expression: str) -> str

   Calculate a mathematical expression.


   .. autolink-examples:: calculate
      :collapse:

.. py:function:: get_weather(location: str) -> str

   Get the current weather for a location.


   .. autolink-examples:: get_weather
      :collapse:

.. py:function:: search_database(query: str) -> str

   Search the database for information.


   .. autolink-examples:: search_database
      :collapse:

.. py:function:: simulate_react_agent_with_human() -> Any



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_v2.example
   :collapse:
   
.. autolink-skip:: next
