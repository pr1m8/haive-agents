
:py:mod:`agents.base.structured_output_handler`
===============================================

.. py:module:: agents.base.structured_output_handler

Structured output handler for clean extraction from LangGraph state.

This module provides utilities to handle LangGraph's AddableValuesDict
return type and extract structured output cleanly.


.. autolink-examples:: agents.base.structured_output_handler
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.structured_output_handler.StructuredOutputHandler


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StructuredOutputHandler:

   .. graphviz::
      :align: center

      digraph inheritance_StructuredOutputHandler {
        node [shape=record];
        "StructuredOutputHandler" [label="StructuredOutputHandler"];
        "Generic[T]" -> "StructuredOutputHandler";
      }

.. autoclass:: agents.base.structured_output_handler.StructuredOutputHandler
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.base.structured_output_handler.extract_structured_output
   agents.base.structured_output_handler.require_structured_output

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



.. rubric:: Related Links

.. autolink-examples:: agents.base.structured_output_handler
   :collapse:
   
.. autolink-skip:: next
