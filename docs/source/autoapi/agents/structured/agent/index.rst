
:py:mod:`agents.structured.agent`
=================================

.. py:module:: agents.structured.agent

Structured output agent implementation.

This module provides the StructuredOutputAgent that converts any agent's output
into structured formats using Pydantic models and tool-based extraction.


.. autolink-examples:: agents.structured.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.structured.agent.StructuredOutputAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StructuredOutputAgent:

   .. graphviz::
      :align: center

      digraph inheritance_StructuredOutputAgent {
        node [shape=record];
        "StructuredOutputAgent" [label="StructuredOutputAgent"];
        "SimpleAgentV3" -> "StructuredOutputAgent";
      }

.. autoclass:: agents.structured.agent.StructuredOutputAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.structured.agent.create_structured_agent

.. py:function:: create_structured_agent(output_model: type[pydantic.BaseModel], name: str = 'structured_output', temperature: float = 0.1, custom_context: str | None = None, **kwargs) -> StructuredOutputAgent

   Factory function to create a structured output agent.

   This is a convenience function for creating structured agents
   with common configurations.

   :param output_model: The Pydantic model for output structure
   :param name: Agent name (defaults to "structured_output")
   :param temperature: LLM temperature (defaults to 0.1 for consistency)
   :param custom_context: Additional extraction context
   :param \*\*kwargs: Additional arguments passed to StructuredOutputAgent

   :returns: Configured StructuredOutputAgent

   .. rubric:: Examples

   Basic creation::

       agent = create_structured_agent(
           output_model=TaskOutput,
           name="task_structurer"
       )

   With custom context::

       agent = create_structured_agent(
           output_model=GenericStructuredOutput,
           custom_context="Focus on technical details",
           temperature=0.2
       )


   .. autolink-examples:: create_structured_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.structured.agent
   :collapse:
   
.. autolink-skip:: next
