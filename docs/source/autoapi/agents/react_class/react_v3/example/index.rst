agents.react_class.react_v3.example
===================================

.. py:module:: agents.react_class.react_v3.example

.. autoapi-nested-parse::

   Test script for ReactAgent demonstrating various usage patterns.

   from typing import Any
   This script shows how to:
   1. Create ReactAgents with different tools
   2. Use RetryPolicy with LangGraph
   3. Schema composition with tool integration
   4. Running agents with different input formats


   .. autolink-examples:: agents.react_class.react_v3.example
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.react_class.react_v3.example.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_v3.example.Calculator


Functions
---------

.. autoapisummary::

   agents.react_class.react_v3.example.calculate
   agents.react_class.react_v3.example.get_current_weather
   agents.react_class.react_v3.example.search_api
   agents.react_class.react_v3.example.test_all
   agents.react_class.react_v3.example.test_basic_react_agent
   agents.react_class.react_v3.example.test_multi_turn_conversation
   agents.react_class.react_v3.example.test_retry_policy
   agents.react_class.react_v3.example.test_structured_tool_agent


Module Contents
---------------

.. py:class:: Calculator(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Tool for performing simple calculations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Calculator
      :collapse:

   .. py:attribute:: a
      :type:  float
      :value: None



   .. py:attribute:: b
      :type:  float
      :value: None



   .. py:attribute:: operation
      :type:  str
      :value: None



.. py:function:: calculate(args: Calculator) -> str

   Perform a calculation based on the operation and numbers.


   .. autolink-examples:: calculate
      :collapse:

.. py:function:: get_current_weather(location: str) -> str

   Get the current weather in a given location.


   .. autolink-examples:: get_current_weather
      :collapse:

.. py:function:: search_api(query: str) -> str

   Search for information about a topic (simulates random failures).


   .. autolink-examples:: search_api
      :collapse:

.. py:function:: test_all() -> None

   Run all ReactAgent tests.


   .. autolink-examples:: test_all
      :collapse:

.. py:function:: test_basic_react_agent() -> Any

   Test a basic ReactAgent with simple tools.


   .. autolink-examples:: test_basic_react_agent
      :collapse:

.. py:function:: test_multi_turn_conversation() -> Any

   Test a ReactAgent with a multi-turn conversation.


   .. autolink-examples:: test_multi_turn_conversation
      :collapse:

.. py:function:: test_retry_policy() -> Any

   Test a ReactAgent with retry policies for flaky tools.


   .. autolink-examples:: test_retry_policy
      :collapse:

.. py:function:: test_structured_tool_agent() -> Any

   Test a ReactAgent with structured tools.


   .. autolink-examples:: test_structured_tool_agent
      :collapse:

.. py:data:: logger

