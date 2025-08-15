agents.structured_output.agent
==============================

.. py:module:: agents.structured_output.agent

.. autoapi-nested-parse::

   Generalized Structured Output Agent for enhancing any agent with structured output parsing.


   .. autolink-examples:: agents.structured_output.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.structured_output.agent.StructuredOutputAgent


Module Contents
---------------

.. py:class:: StructuredOutputAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Agent that adds structured output parsing to any other agent.

   This agent acts as a post-processor that takes the output from any agent
   and ensures it conforms to a structured format. It can work standalone or
   as part of a sequential multi-agent chain.

   Key features:
   - Works with any agent type (SimpleAgent, ReactAgent, etc.)
   - Preserves original context and input
   - Uses PydanticToolsParser for robust parsing
   - Can be chained sequentially with any agent
   - Supports multiple output models

   .. rubric:: Example

   .. code-block:: python

       # Enhance any agent with structured output
       enhanced_agent = StructuredOutputAgent.enhance_agent(
       base_agent=my_agent,
       output_models=[SearchResult, AnalysisResult]
       )

       # Or use as standalone post-processor
       processor = StructuredOutputAgent.create_processor(
       output_models=[ResultModel],
       include_original_input=True
       )


   .. autolink-examples:: StructuredOutputAgent
      :collapse:

   .. py:method:: create_processor(output_models: list[type[pydantic.BaseModel]], name: str = 'structured_output_processor', include_original_input: bool = True, system_message: str | None = None, **kwargs) -> StructuredOutputAgent
      :classmethod:


      Create a standalone structured output processor.

      :param output_models: List of Pydantic models for output formats
      :param name: Name for the processor
      :param include_original_input: Include original input for context
      :param system_message: Custom system message (auto-generated if not provided)
      :param \*\*kwargs: Additional configuration

      :returns: Configured StructuredOutputAgent instance


      .. autolink-examples:: create_processor
         :collapse:


   .. py:method:: create_reflection_processor(reflection_models: list[type[pydantic.BaseModel]], name: str = 'reflection_processor', **kwargs) -> StructuredOutputAgent
      :classmethod:


      Create a processor specifically for reflection patterns.

      This is optimized for reflection/reflexion agents that need to
      analyze their own outputs and provide structured feedback.

      :param reflection_models: Models for reflection (e.g., Critique, Improvement)
      :param name: Name for the processor
      :param \*\*kwargs: Additional configuration

      :returns: StructuredOutputAgent configured for reflection


      .. autolink-examples:: create_reflection_processor
         :collapse:


   .. py:method:: create_validation_processor(validation_models: list[type[pydantic.BaseModel]], name: str = 'validation_processor', **kwargs) -> StructuredOutputAgent
      :classmethod:


      Create a processor for validation patterns.

      :param validation_models: Models for validation results
      :param name: Name for the processor
      :param \*\*kwargs: Additional configuration

      :returns: StructuredOutputAgent configured for validation


      .. autolink-examples:: create_validation_processor
         :collapse:


   .. py:method:: enhance_agent(base_agent: haive.agents.base.agent.Agent, output_models: list[type[pydantic.BaseModel]], name: str | None = None, include_original_input: bool = True, **kwargs) -> haive.agents.multi.experiments.implementations.proper_base.ProperMultiAgent
      :classmethod:


      Enhance any agent with structured output capabilities.

      Creates a sequential multi-agent that runs:
      1. Base agent (processes input normally)
      2. StructuredOutputAgent (ensures output is structured)

      :param base_agent: The agent to enhance
      :param output_models: List of Pydantic models for output formats
      :param name: Name for the enhanced agent
      :param include_original_input: Include original input for context
      :param \*\*kwargs: Additional arguments for the structured output agent

      :returns: ProperMultiAgent configured for sequential execution


      .. autolink-examples:: enhance_agent
         :collapse:


   .. py:method:: process_with_context(content: str, original_input: str | None = None) -> dict[str, Any]

      Process content with optional original context.

      :param content: The content to structure
      :param original_input: Original task/query for context

      :returns: Structured output result


      .. autolink-examples:: process_with_context
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup hook to configure structured output state.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: fallback_on_error
      :type:  bool
      :value: None



   .. py:attribute:: include_original_input
      :type:  bool
      :value: None



   .. py:attribute:: output_models
      :type:  list[type[pydantic.BaseModel]]
      :value: None



