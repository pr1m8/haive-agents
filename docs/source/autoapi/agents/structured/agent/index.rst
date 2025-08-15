agents.structured.agent
=======================

.. py:module:: agents.structured.agent

.. autoapi-nested-parse::

   Structured output agent implementation.

   This module provides the StructuredOutputAgent that converts any agent's output
   into structured formats using Pydantic models and tool-based extraction.


   .. autolink-examples:: agents.structured.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.structured.agent.StructuredOutputAgent


Functions
---------

.. autoapisummary::

   agents.structured.agent.create_structured_agent


Module Contents
---------------

.. py:class:: StructuredOutputAgent

   Bases: :py:obj:`SimpleAgentV3`


   Agent that converts any input into structured output.

   This agent specializes in taking unstructured text (typically from another
   agent's output) and converting it into a well-defined Pydantic model structure.
   It always uses tool-based structured output (v2) for reliable extraction.

   The agent can be used in multi-agent workflows where you need to:
   - Convert free-form agent responses into structured data
   - Extract specific fields from complex outputs
   - Ensure type-safe data flow between agents
   - Create consistent output formats across different agent types

   .. rubric:: Examples

   Basic usage with generic output::

       agent = StructuredOutputAgent(
           name="structurer",
           output_model=GenericStructuredOutput
       )
       result = agent.run("Some unstructured text...")

   Custom output model::

       class CustomOutput(BaseModel):
           title: str
           points: List[str]
           score: float

       agent = StructuredOutputAgent(
           name="custom_structurer",
           output_model=CustomOutput,
           custom_context="Focus on extracting title and scoring"
       )

   In multi-agent workflow::

       # Any agent produces unstructured output
       react_agent = ReactAgent(name="analyzer", ...)

       # StructuredOutputAgent converts it
       structurer = StructuredOutputAgent(
           name="structurer",
           output_model=AnalysisOutput
       )

       # Add both to workflow
       agents = [react_agent, structurer]


   .. autolink-examples:: StructuredOutputAgent
      :collapse:

   .. py:method:: extract_from_messages(messages: list) -> Any

      Extract structured output from a list of messages.

      This is useful when processing conversation history or
      multiple agent outputs.

      :param messages: List of messages to process

      :returns: Structured output matching the output_model


      .. autolink-examples:: extract_from_messages
         :collapse:


   .. py:method:: extract_from_state(state: Any) -> Any

      Extract structured output from agent state.

      This is useful in multi-agent workflows where you need
      to structure another agent's output from the shared state.

      :param state: Agent state containing messages

      :returns: Structured output matching the output_model


      .. autolink-examples:: extract_from_state
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None

      Initialize the agent after Pydantic initialization.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: custom_context
      :type:  str | None
      :value: None



   .. py:attribute:: custom_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: output_model
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel]
      :value: None



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

