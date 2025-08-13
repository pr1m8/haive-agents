
:py:mod:`agents.patterns.react_with_structured_output`
======================================================

.. py:module:: agents.patterns.react_with_structured_output

ReactAgent with Structured Output Pattern.

This pattern demonstrates ReactAgent → SimpleAgentV3 sequential execution
using the generalized hook system for structured output workflows.

Pattern: ReactAgent (reasoning/tools) → SimpleAgent (structured output)
Use Cases:
- Analysis with structured results
- Research with formatted reports
- Problem-solving with structured solutions
- Tool-based workflows with typed outputs


.. autolink-examples:: agents.patterns.react_with_structured_output
   :collapse:

Classes
-------

.. autoapisummary::

   agents.patterns.react_with_structured_output.AnalysisResult
   agents.patterns.react_with_structured_output.ProblemSolution
   agents.patterns.react_with_structured_output.ReactWithStructuredOutput
   agents.patterns.react_with_structured_output.ResearchReport


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AnalysisResult:

   .. graphviz::
      :align: center

      digraph inheritance_AnalysisResult {
        node [shape=record];
        "AnalysisResult" [label="AnalysisResult"];
        "pydantic.BaseModel" -> "AnalysisResult";
      }

.. autopydantic_model:: agents.patterns.react_with_structured_output.AnalysisResult
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ProblemSolution:

   .. graphviz::
      :align: center

      digraph inheritance_ProblemSolution {
        node [shape=record];
        "ProblemSolution" [label="ProblemSolution"];
        "pydantic.BaseModel" -> "ProblemSolution";
      }

.. autopydantic_model:: agents.patterns.react_with_structured_output.ProblemSolution
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactWithStructuredOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ReactWithStructuredOutput {
        node [shape=record];
        "ReactWithStructuredOutput" [label="ReactWithStructuredOutput"];
        "haive.agents.multi.agent.MultiAgent" -> "ReactWithStructuredOutput";
      }

.. autoclass:: agents.patterns.react_with_structured_output.ReactWithStructuredOutput
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResearchReport:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchReport {
        node [shape=record];
        "ResearchReport" [label="ResearchReport"];
        "pydantic.BaseModel" -> "ResearchReport";
      }

.. autopydantic_model:: agents.patterns.react_with_structured_output.ResearchReport
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

   agents.patterns.react_with_structured_output.calculator
   agents.patterns.react_with_structured_output.create_react_analysis_workflow
   agents.patterns.react_with_structured_output.create_react_problem_solving_workflow
   agents.patterns.react_with_structured_output.create_react_research_workflow
   agents.patterns.react_with_structured_output.data_analyzer
   agents.patterns.react_with_structured_output.example_analysis_workflow
   agents.patterns.react_with_structured_output.example_problem_solving_workflow
   agents.patterns.react_with_structured_output.example_research_workflow
   agents.patterns.react_with_structured_output.main
   agents.patterns.react_with_structured_output.web_search

.. py:function:: calculator(expression: str) -> str

   Calculate mathematical expressions.


   .. autolink-examples:: calculator
      :collapse:

.. py:function:: create_react_analysis_workflow(name: str = 'react_analysis', tools: list | None = None) -> ReactWithStructuredOutput

   Create a ReactAgent analysis workflow with structured output.

   :param name: Workflow name
   :param tools: Tools for analysis (web search, calculators, etc.)

   :returns: Configured analysis workflow


   .. autolink-examples:: create_react_analysis_workflow
      :collapse:

.. py:function:: create_react_problem_solving_workflow(name: str = 'react_problem_solver', tools: list | None = None) -> ReactWithStructuredOutput

   Create a ReactAgent problem-solving workflow with structured output.

   :param name: Workflow name
   :param tools: Tools for problem-solving (analysis tools, simulators, etc.)

   :returns: Configured problem-solving workflow


   .. autolink-examples:: create_react_problem_solving_workflow
      :collapse:

.. py:function:: create_react_research_workflow(name: str = 'react_research', tools: list | None = None) -> ReactWithStructuredOutput

   Create a ReactAgent research workflow with structured output.

   :param name: Workflow name
   :param tools: Tools for research (web search, document analysis, etc.)

   :returns: Configured research workflow


   .. autolink-examples:: create_react_research_workflow
      :collapse:

.. py:function:: data_analyzer(data: str) -> str

   Analyze data and provide insights.


   .. autolink-examples:: data_analyzer
      :collapse:

.. py:function:: example_analysis_workflow()
   :async:


   Example: ReactAgent analysis with structured output.


   .. autolink-examples:: example_analysis_workflow
      :collapse:

.. py:function:: example_problem_solving_workflow()
   :async:


   Example: ReactAgent problem-solving with structured solution.


   .. autolink-examples:: example_problem_solving_workflow
      :collapse:

.. py:function:: example_research_workflow()
   :async:


   Example: ReactAgent research with structured report.


   .. autolink-examples:: example_research_workflow
      :collapse:

.. py:function:: main()
   :async:


   Run all workflow examples.


   .. autolink-examples:: main
      :collapse:

.. py:function:: web_search(query: str) -> str

   Search the web for information.


   .. autolink-examples:: web_search
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.patterns.react_with_structured_output
   :collapse:
   
.. autolink-skip:: next
