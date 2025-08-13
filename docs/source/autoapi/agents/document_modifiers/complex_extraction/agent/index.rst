
:py:mod:`agents.document_modifiers.complex_extraction.agent`
============================================================

.. py:module:: agents.document_modifiers.complex_extraction.agent

Complex Extraction Agent for structured data extraction from text.

This module provides the ComplexExtractionAgent class which implements sophisticated
structured data extraction using validation with retries and optional JSONPatch-based
error correction to reliably extract data according to specified schemas.

The agent supports multiple retry strategies and can handle complex validation
scenarios where initial extraction attempts may fail.

Classes:
    ComplexExtractionAgent: Main agent for complex structured data extraction

.. rubric:: Examples

Basic usage::

    from haive.agents.document_modifiers.complex_extraction import ComplexExtractionAgent
    from haive.agents.document_modifiers.complex_extraction.config import ComplexExtractionAgentConfig
    from pydantic import BaseModel

    class PersonInfo(BaseModel):
        name: str
        age: int
        occupation: str

    config = ComplexExtractionAgentConfig(
        extraction_model=PersonInfo,
        max_retries=3
    )
    agent = ComplexExtractionAgent(config)

    text = "John Smith is a 35-year-old software engineer."
    result = agent.run(text)
    person_data = result["extracted_data"]

With JSONPatch error correction::

    config = ComplexExtractionAgentConfig(
        extraction_model=PersonInfo,
        use_jsonpatch=True,
        max_retries=5
    )
    agent = ComplexExtractionAgent(config)
    result = agent.run(complex_text)

.. seealso::

   - :class:`~haive.agents.document_modifiers.complex_extraction.config.ComplexExtractionAgentConfig`: Configuration class
   - :class:`~haive.agents.document_modifiers.complex_extraction.models.RetryStrategy`: Retry strategy configuration


.. autolink-examples:: agents.document_modifiers.complex_extraction.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.agent.ComplexExtractionAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ComplexExtractionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ComplexExtractionAgent {
        node [shape=record];
        "ComplexExtractionAgent" [label="ComplexExtractionAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.document_modifiers.complex_extraction.config.ComplexExtractionAgentConfig]" -> "ComplexExtractionAgent";
      }

.. autoclass:: agents.document_modifiers.complex_extraction.agent.ComplexExtractionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.complex_extraction.agent
   :collapse:
   
.. autolink-skip:: next
