agents.react_class.react_v2.example
===================================

.. py:module:: agents.react_class.react_v2.example


Attributes
----------

.. autoapisummary::

   agents.react_class.react_v2.example.calculator_tool
   agents.react_class.react_v2.example.final_result
   agents.react_class.react_v2.example.react_config
   agents.react_class.react_v2.example.search_tool
   agents.react_class.react_v2.example.system_prompt
   agents.react_class.react_v2.example.travel_agent
   agents.react_class.react_v2.example.user_input
   agents.react_class.react_v2.example.weather_tool


Classes
-------

.. autoapisummary::

   agents.react_class.react_v2.example.TripPlan


Functions
---------

.. autoapisummary::

   agents.react_class.react_v2.example.calculate
   agents.react_class.react_v2.example.get_weather
   agents.react_class.react_v2.example.search_database
   agents.react_class.react_v2.example.simulate_react_agent_with_human


Module Contents
---------------

.. py:class:: TripPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A structured trip plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TripPlan
      :collapse:

   .. py:attribute:: activities
      :type:  list[str]
      :value: None



   .. py:attribute:: budget_estimate
      :type:  float
      :value: None



   .. py:attribute:: destination
      :type:  str
      :value: None



   .. py:attribute:: duration_days
      :type:  int
      :value: None



   .. py:attribute:: weather_summary
      :type:  str | None
      :value: None



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

.. py:data:: calculator_tool

.. py:data:: final_result

.. py:data:: react_config

.. py:data:: search_tool

.. py:data:: system_prompt
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a helpful travel assistant that helps users plan trips.
      You have access to tools that can help you gather information.
      Always use tools when appropriate and think step by step.
      
      When you don't have enough information, use the request_human_assistance tool
      to ask the user for more details.
      """

   .. raw:: html

      </details>



.. py:data:: travel_agent

.. py:data:: user_input
   :value: "I want to plan a trip but I'm not sure where to go. Can you help?"


.. py:data:: weather_tool

