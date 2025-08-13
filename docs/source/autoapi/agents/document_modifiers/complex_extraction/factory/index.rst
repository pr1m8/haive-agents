
:py:mod:`agents.document_modifiers.complex_extraction.factory`
==============================================================

.. py:module:: agents.document_modifiers.complex_extraction.factory



Functions
---------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.factory.create_complex_extraction_agent

.. py:function:: create_complex_extraction_agent(extraction_model: type[pydantic.BaseModel], system_prompt: str | None = None, model: str = 'gpt-4o', max_retries: int = 3, force_tool_choice: bool = True, use_jsonpatch: bool = True, parse_pydantic: bool = False, **kwargs) -> haive.agents.document_modifiers.complex_extraction.agent.ComplexExtractionAgent

   Create a complex extraction agent.

   :param extraction_model: Pydantic model for extraction
   :param system_prompt: System prompt
   :param model: Model name
   :param max_retries: Maximum retry attempts
   :param force_tool_choice: Whether to force the tool choice
   :param use_jsonpatch: Whether to use JSONPatch for validation
   :param parse_pydantic: Whether to parse extracted data into a Pydantic object
   :param \*\*kwargs: Additional arguments for agent configuration

   :returns: ComplexExtractionAgent instance


   .. autolink-examples:: create_complex_extraction_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.complex_extraction.factory
   :collapse:
   
.. autolink-skip:: next
