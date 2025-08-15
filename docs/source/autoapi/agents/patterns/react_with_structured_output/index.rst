agents.patterns.react_with_structured_output
============================================

.. py:module:: agents.patterns.react_with_structured_output

.. autoapi-nested-parse::

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


Module Contents
---------------

.. py:class:: AnalysisResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured analysis result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AnalysisResult
      :collapse:

   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: key_findings
      :type:  list[str]
      :value: None



   .. py:attribute:: recommendations
      :type:  list[str]
      :value: None



   .. py:attribute:: summary
      :type:  str
      :value: None



   .. py:attribute:: supporting_evidence
      :type:  list[str]
      :value: None



.. py:class:: ProblemSolution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured problem solution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ProblemSolution
      :collapse:

   .. py:attribute:: implementation_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: problem_statement
      :type:  str
      :value: None



   .. py:attribute:: proposed_solutions
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: risks_and_mitigation
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: root_causes
      :type:  list[str]
      :value: None



   .. py:attribute:: success_metrics
      :type:  list[str]
      :value: None



.. py:class:: ReactWithStructuredOutput(**data)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   ReactAgent → SimpleAgentV3 with structured output pattern.

   This pattern uses ReactAgent for reasoning and tool usage, then
   SimpleAgentV3 for converting the results to structured output.

   Initialize the pattern with agents.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactWithStructuredOutput
      :collapse:

   .. py:method:: _setup_pattern_hooks()

      Set up hooks for monitoring the pattern execution.


      .. autolink-examples:: _setup_pattern_hooks
         :collapse:


   .. py:method:: create_analysis_pattern(name: str = 'analysis_workflow', tools: list | None = None, reasoning_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, structuring_config: haive.core.engine.aug_llm.AugLLMConfig | None = None) -> ReactWithStructuredOutput
      :classmethod:


      Create a ReactAgent → StructuredOutput pattern for analysis tasks.

      :param name: Name for the workflow
      :param tools: Tools for the ReactAgent
      :param reasoning_config: Configuration for reasoning agent
      :param structuring_config: Configuration for structuring agent

      :returns: Configured ReactWithStructuredOutput instance


      .. autolink-examples:: create_analysis_pattern
         :collapse:


   .. py:method:: create_problem_solving_pattern(name: str = 'problem_solving_workflow', tools: list | None = None, reasoning_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, structuring_config: haive.core.engine.aug_llm.AugLLMConfig | None = None) -> ReactWithStructuredOutput
      :classmethod:


      Create a ReactAgent → StructuredOutput pattern for problem-solving tasks.


      .. autolink-examples:: create_problem_solving_pattern
         :collapse:


   .. py:method:: create_research_pattern(name: str = 'research_workflow', tools: list | None = None, reasoning_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, structuring_config: haive.core.engine.aug_llm.AugLLMConfig | None = None) -> ReactWithStructuredOutput
      :classmethod:


      Create a ReactAgent → StructuredOutput pattern for research tasks.


      .. autolink-examples:: create_research_pattern
         :collapse:


   .. py:attribute:: include_tool_calls
      :type:  bool
      :value: None



   .. py:attribute:: preserve_reasoning
      :type:  bool
      :value: None



   .. py:attribute:: reasoning_agent
      :type:  haive.agents.react.agent.ReactAgent
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: structuring_agent
      :type:  SimpleAgentV3
      :value: None



.. py:class:: ResearchReport(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured research report.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchReport
      :collapse:

   .. py:attribute:: conclusions
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence_level
      :type:  str
      :value: None



   .. py:attribute:: executive_summary
      :type:  str
      :value: None



   .. py:attribute:: findings
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: methodology
      :type:  str
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



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

