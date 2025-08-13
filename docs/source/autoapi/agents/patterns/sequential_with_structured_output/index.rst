
:py:mod:`agents.patterns.sequential_with_structured_output`
===========================================================

.. py:module:: agents.patterns.sequential_with_structured_output

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialAgentWithStructuredOutput:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialAgentWithStructuredOutput {
        node [shape=record];
        "SequentialAgentWithStructuredOutput" [label="SequentialAgentWithStructuredOutput"];
        "Generic[OutputT]" -> "SequentialAgentWithStructuredOutput";
      }

.. autoclass:: agents.patterns.sequential_with_structured_output.SequentialAgentWithStructuredOutput
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialHooks:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialHooks {
        node [shape=record];
        "SequentialHooks" [label="SequentialHooks"];
        "pydantic.BaseModel" -> "SequentialHooks";
      }

.. autopydantic_model:: agents.patterns.sequential_with_structured_output.SequentialHooks
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.patterns.sequential_with_structured_output.create_analysis_to_report
   agents.patterns.sequential_with_structured_output.create_react_to_structured

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



.. rubric:: Related Links

.. autolink-examples:: agents.patterns.sequential_with_structured_output
   :collapse:
   
.. autolink-skip:: next
