agents.base.structured_output_handler
=====================================

.. py:module:: agents.base.structured_output_handler

.. autoapi-nested-parse::

   Structured output handler for clean extraction from LangGraph state.

   This module provides utilities to handle LangGraph's AddableValuesDict
   return type and extract structured output cleanly.


   .. autolink-examples:: agents.base.structured_output_handler
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.structured_output_handler.LangGraphResult
   agents.base.structured_output_handler.T


Classes
-------

.. autoapisummary::

   agents.base.structured_output_handler.StructuredOutputHandler


Functions
---------

.. autoapisummary::

   agents.base.structured_output_handler.extract_structured_output
   agents.base.structured_output_handler.require_structured_output


Module Contents
---------------

.. py:class:: StructuredOutputHandler(output_model: type[T], field_name: str | None = None, common_fields: list[str] | None = None)

   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Handler for extracting structured output from LangGraph results.

   This class provides a clean interface for working with LangGraph's
   AddableValuesDict return type, making it easy to extract structured
   output from graph execution results.

   .. rubric:: Examples

   Basic usage::

       handler = StructuredOutputHandler(AnalysisResult)
       result = await agent.arun(input_data)
       analysis = handler.extract(result)

   With custom field name::

       handler = StructuredOutputHandler(
           AnalysisResult,
           field_name="custom_output"
       )

   With validation::

       analysis = handler.extract_or_raise(result)
       # Raises ValueError if not found

   Initialize the handler.

   :param output_model: The Pydantic model class for structured output
   :param field_name: Optional specific field name to extract
   :param common_fields: Additional field names to check


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StructuredOutputHandler
      :collapse:

   .. py:method:: _generate_field_name() -> str

      Generate field name from model name using robust naming utilities.


      .. autolink-examples:: _generate_field_name
         :collapse:


   .. py:method:: extract(result: dict | langgraph.pregel.io.AddableValuesDict | Any) -> T | None

      Extract structured output from result.

      This method handles various result types including AddableValuesDict,
      regular dicts, and objects with dict-like interfaces.

      :param result: The result from LangGraph execution

      :returns: The extracted structured output or None if not found


      .. autolink-examples:: extract
         :collapse:


   .. py:method:: extract_or_default(result: Any, default: T | None = None) -> T | None

      Extract structured output or return default.

      :param result: The result from LangGraph execution
      :param default: Default value to return if not found

      :returns: The extracted output or default value


      .. autolink-examples:: extract_or_default
         :collapse:


   .. py:method:: extract_or_raise(result: Any) -> T

      Extract structured output or raise an error.

      :param result: The result from LangGraph execution

      :returns: The extracted structured output

      :raises ValueError: If structured output not found


      .. autolink-examples:: extract_or_raise
         :collapse:


   .. py:attribute:: common_fields


   .. py:property:: expected_fields
      :type: list[str]


      Get list of field names that will be searched.

      .. autolink-examples:: expected_fields
         :collapse:


   .. py:attribute:: field_name


   .. py:attribute:: output_model


.. py:function:: extract_structured_output(result: Any, output_model: type[T], field_name: str | None = None) -> T | None

   Convenience function to extract structured output.

   :param result: The result from LangGraph execution
   :param output_model: The expected Pydantic model type
   :param field_name: Optional specific field name

   :returns: The extracted structured output or None

   .. rubric:: Examples

   Basic extraction::

       analysis = extract_structured_output(result, AnalysisResult)

   With field name::

       output = extract_structured_output(
           result,
           CustomOutput,
           field_name="my_output"
       )


   .. autolink-examples:: extract_structured_output
      :collapse:

.. py:function:: require_structured_output(result: Any, output_model: type[T], field_name: str | None = None) -> T

   Extract structured output or raise error.

   :param result: The result from LangGraph execution
   :param output_model: The expected Pydantic model type
   :param field_name: Optional specific field name

   :returns: The extracted structured output

   :raises ValueError: If output not found

   .. rubric:: Examples

   Require output::

       analysis = require_structured_output(result, AnalysisResult)
       # Raises ValueError if not found


   .. autolink-examples:: require_structured_output
      :collapse:

.. py:data:: LangGraphResult

.. py:data:: T

