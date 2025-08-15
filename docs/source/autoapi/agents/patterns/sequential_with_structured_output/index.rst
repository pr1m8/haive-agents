agents.patterns.sequential_with_structured_output
=================================================

.. py:module:: agents.patterns.sequential_with_structured_output

.. autoapi-nested-parse::

   Generic Sequential Agent Pattern with Structured Output Hooks.

   This module provides a flexible pattern for creating sequential agent flows
   where the first agent performs some task and the second agent structures
   the output into a specific format.

   .. rubric:: Examples

   Common sequential patterns::

       ReactAgent → StructuredOutputAgent
       ResearchAgent → SummaryAgent
       AnalysisAgent → ReportAgent


   .. autolink-examples:: agents.patterns.sequential_with_structured_output
      :collapse:


Classes
-------

.. autoapisummary::

   agents.patterns.sequential_with_structured_output.SequentialAgentWithStructuredOutput
   agents.patterns.sequential_with_structured_output.SequentialHooks


Functions
---------

.. autoapisummary::

   agents.patterns.sequential_with_structured_output.create_analysis_to_report
   agents.patterns.sequential_with_structured_output.create_react_to_structured


Module Contents
---------------

.. py:class:: SequentialAgentWithStructuredOutput(first_agent: haive.agents.base.agent.Agent, structured_output_model: type[OutputT], structured_output_prompt: langchain_core.prompts.ChatPromptTemplate | None = None, second_agent: haive.agents.base.agent.Agent | None = None, hooks: SequentialHooks | None = None, name: str = 'sequential_structured', debug: bool = False)

   Bases: :py:obj:`Generic`\ [\ :py:obj:`OutputT`\ ]


   Generic sequential agent pattern with structured output.

   This class orchestrates two agents in sequence:
   1. First agent performs the main task (e.g., reasoning, research)
   2. Second agent structures the output into a specific format

   The pattern is flexible and works with any agent types.

   Initialize sequential agent with structured output.

   :param first_agent: The agent that performs the main task
   :param structured_output_model: Pydantic model for structured output
   :param structured_output_prompt: Optional custom prompt for structuring
   :param second_agent: Optional custom second agent (otherwise creates SimpleAgent)
   :param hooks: Optional hooks for customizing behavior
   :param name: Name for this sequential pattern
   :param debug: Enable debug mode


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SequentialAgentWithStructuredOutput
      :collapse:

   .. py:method:: _create_structured_output_agent(custom_prompt: langchain_core.prompts.ChatPromptTemplate | None = None) -> haive.agents.simple.agent.SimpleAgent

      Create default agent for structured output.


      .. autolink-examples:: _create_structured_output_agent
         :collapse:


   .. py:method:: _default_transform(first_result: Any, original_input: Any, context: dict[str, Any] | None = None) -> dict[str, Any]

      Default transformation of first agent output for second agent.


      .. autolink-examples:: _default_transform
         :collapse:


   .. py:method:: arun(input_data: Any, context: dict[str, Any] | None = None, **kwargs) -> OutputT
      :async:


      Run the sequential agent pipeline asynchronously.

      :param input_data: Input for the first agent
      :param context: Optional context to pass through pipeline
      :param \*\*kwargs: Additional arguments for agents

      :returns: Structured output according to the model


      .. autolink-examples:: arun
         :collapse:


   .. py:attribute:: debug
      :value: False



   .. py:attribute:: first_agent


   .. py:attribute:: hooks


   .. py:attribute:: name
      :value: 'sequential_structured'



   .. py:attribute:: structured_output_model


.. py:class:: SequentialHooks(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Hooks for customizing sequential agent behavior.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SequentialHooks
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: error_handler
      :type:  collections.abc.Callable[[Exception], Any] | None
      :value: None



   .. py:attribute:: intermediate_transform
      :type:  collections.abc.Callable[[Any], dict[str, Any]] | None
      :value: None



   .. py:attribute:: post_process
      :type:  collections.abc.Callable[[Any], Any] | None
      :value: None



   .. py:attribute:: pre_process
      :type:  collections.abc.Callable[[dict[str, Any]], dict[str, Any]] | None
      :value: None



.. py:function:: create_analysis_to_report(analysis_prompt: langchain_core.prompts.ChatPromptTemplate, report_model: type[OutputT], name: str = 'analysis_report', analysis_config: dict[str, Any] | None = None, report_prompt: langchain_core.prompts.ChatPromptTemplate | None = None, hooks: SequentialHooks | None = None, debug: bool = False) -> SequentialAgentWithStructuredOutput[OutputT]

   Create an Analysis → Report pipeline.

   :param analysis_prompt: Prompt for analysis agent
   :param report_model: Model for structured report
   :param name: Name for the pipeline
   :param analysis_config: Optional config for analysis agent
   :param report_prompt: Optional custom report prompt
   :param hooks: Optional behavior hooks
   :param debug: Enable debug mode

   :returns: Configured sequential agent pipeline


   .. autolink-examples:: create_analysis_to_report
      :collapse:

.. py:function:: create_react_to_structured(tools: list[Any], structured_output_model: type[OutputT], name: str = 'react_structured', react_config: dict[str, Any] | None = None, structured_prompt: langchain_core.prompts.ChatPromptTemplate | None = None, hooks: SequentialHooks | None = None, debug: bool = False) -> SequentialAgentWithStructuredOutput[OutputT]

   Create a ReactAgent → StructuredOutput pipeline.

   :param tools: Tools for the ReactAgent
   :param structured_output_model: Output model for structuring
   :param name: Name for the pipeline
   :param react_config: Optional config for ReactAgent
   :param structured_prompt: Optional custom structuring prompt
   :param hooks: Optional behavior hooks
   :param debug: Enable debug mode

   :returns: Configured sequential agent pipeline


   .. autolink-examples:: create_react_to_structured
      :collapse:

