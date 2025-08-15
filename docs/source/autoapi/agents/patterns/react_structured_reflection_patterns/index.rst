agents.patterns.react_structured_reflection_patterns
====================================================

.. py:module:: agents.patterns.react_structured_reflection_patterns

.. autoapi-nested-parse::

   Comprehensive ReactAgent → SimpleAgent Patterns with V3, V4, and Enhanced Base Agent.

   This demonstrates all variations of ReactAgent → SimpleAgent workflows:
   1. V3: ReactAgent → SimpleAgent (structured output)
   2. V4: MultiAgent composition
   3. Enhanced Base: Using enhanced base agent with hooks
   4. Reflection: ReactAgent → SimpleAgentV3 → ReflectionAgent
   5. Graded Reflection: ReactAgent → GradingAgent → SimpleAgentV3 → ReflectionAgent

   Each pattern showcases the generalized hook system and different architectural approaches.


   .. autolink-examples:: agents.patterns.react_structured_reflection_patterns
      :collapse:


Classes
-------

.. autoapisummary::

   agents.patterns.react_structured_reflection_patterns.ProblemAnalysis
   agents.patterns.react_structured_reflection_patterns.ReactToStructuredV3
   agents.patterns.react_structured_reflection_patterns.ReactToStructuredV4
   agents.patterns.react_structured_reflection_patterns.ReactWithGradedReflection
   agents.patterns.react_structured_reflection_patterns.ReactWithReflection
   agents.patterns.react_structured_reflection_patterns.ResearchFindings
   agents.patterns.react_structured_reflection_patterns.TaskAnalysis


Functions
---------

.. autoapisummary::

   agents.patterns.react_structured_reflection_patterns.create_graded_reflection_pattern
   agents.patterns.react_structured_reflection_patterns.create_reflection_pattern
   agents.patterns.react_structured_reflection_patterns.create_v3_pattern
   agents.patterns.react_structured_reflection_patterns.create_v4_pattern
   agents.patterns.react_structured_reflection_patterns.data_analysis
   agents.patterns.react_structured_reflection_patterns.example_graded_reflection_pattern
   agents.patterns.react_structured_reflection_patterns.example_reflection_pattern
   agents.patterns.react_structured_reflection_patterns.example_v3_pattern
   agents.patterns.react_structured_reflection_patterns.example_v4_pattern
   agents.patterns.react_structured_reflection_patterns.main
   agents.patterns.react_structured_reflection_patterns.stakeholder_analysis
   agents.patterns.react_structured_reflection_patterns.web_research


Module Contents
---------------

.. py:class:: ProblemAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured problem analysis.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ProblemAnalysis
      :collapse:

   .. py:attribute:: impact_assessment
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: problem_definition
      :type:  str
      :value: None



   .. py:attribute:: recommended_approach
      :type:  str
      :value: None



   .. py:attribute:: root_causes
      :type:  list[str]
      :value: None



   .. py:attribute:: solution_options
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: stakeholders
      :type:  list[str]
      :value: None



.. py:class:: ReactToStructuredV3(name: str, tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis, reasoning_config: haive.core.engine.aug_llm.AugLLMConfig = None, structuring_config: haive.core.engine.aug_llm.AugLLMConfig = None)

   V3 Pattern: ReactAgent → SimpleAgentV3 with structured output.


   .. autolink-examples:: ReactToStructuredV3
      :collapse:

   .. py:method:: _setup_v3_hooks()

      Set up hooks for V3 pattern monitoring.


      .. autolink-examples:: _setup_v3_hooks
         :collapse:


   .. py:method:: arun(input_data: str) -> pydantic.BaseModel
      :async:


      Execute V3 pattern: ReactAgent → SimpleAgentV3.


      .. autolink-examples:: arun
         :collapse:


   .. py:attribute:: name


   .. py:attribute:: reasoning_agent


   .. py:attribute:: structured_output_model


   .. py:attribute:: structuring_agent


.. py:class:: ReactToStructuredV4(**data)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   V4 Pattern: MultiAgent with ReactAgent → SimpleAgentV3.


   .. autolink-examples:: ReactToStructuredV4
      :collapse:

   .. py:method:: _setup_v4_hooks()

      Set up hooks for V4 pattern monitoring.


      .. autolink-examples:: _setup_v4_hooks
         :collapse:


   .. py:method:: create_analysis_workflow(name: str = 'v4_analysis', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactToStructuredV4
      :classmethod:


      Create V4 analysis workflow.


      .. autolink-examples:: create_analysis_workflow
         :collapse:


   .. py:attribute:: reasoning_agent
      :type:  haive.agents.react.agent.ReactAgent
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: structuring_agent
      :type:  SimpleAgentV3
      :value: None



.. py:class:: ReactWithGradedReflection(name: str, tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis)

   Graded Reflection Pattern: ReactAgent → GradingAgent → SimpleAgentV3 → ReflectionAgent.


   .. autolink-examples:: ReactWithGradedReflection
      :collapse:

   .. py:method:: _setup_graded_reflection_hooks()

      Set up hooks for graded reflection pattern monitoring.


      .. autolink-examples:: _setup_graded_reflection_hooks
         :collapse:


   .. py:method:: arun(input_data: str) -> dict[str, Any]
      :async:


      Execute Graded Reflection pattern.


      .. autolink-examples:: arun
         :collapse:


   .. py:attribute:: name


   .. py:attribute:: reasoning_agent


   .. py:attribute:: structured_output_model


   .. py:attribute:: structuring_agent


.. py:class:: ReactWithReflection(name: str, tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis, reasoning_config: haive.core.engine.aug_llm.AugLLMConfig = None, structuring_config: haive.core.engine.aug_llm.AugLLMConfig = None)

   Enhanced Base Agent Pattern: ReactAgent → SimpleAgentV3 → ReflectionAgent.


   .. autolink-examples:: ReactWithReflection
      :collapse:

   .. py:method:: _setup_reflection_hooks()

      Set up hooks for reflection pattern monitoring.


      .. autolink-examples:: _setup_reflection_hooks
         :collapse:


   .. py:method:: arun(input_data: str) -> dict[str, Any]
      :async:


      Execute Enhanced Base Agent pattern with reflection.


      .. autolink-examples:: arun
         :collapse:


   .. py:attribute:: name


   .. py:attribute:: reasoning_agent


   .. py:attribute:: structured_output_model


   .. py:attribute:: structuring_agent


.. py:class:: ResearchFindings(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured research findings.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchFindings
      :collapse:

   .. py:attribute:: confidence_assessment
      :type:  str
      :value: None



   .. py:attribute:: data_sources
      :type:  list[str]
      :value: None



   .. py:attribute:: key_findings
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: methodology
      :type:  str
      :value: None



   .. py:attribute:: next_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: research_question
      :type:  str
      :value: None



.. py:class:: TaskAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis of a complex task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskAnalysis
      :collapse:

   .. py:attribute:: complexity_level
      :type:  str
      :value: None



   .. py:attribute:: estimated_effort
      :type:  str
      :value: None



   .. py:attribute:: key_components
      :type:  list[str]
      :value: None



   .. py:attribute:: potential_challenges
      :type:  list[str]
      :value: None



   .. py:attribute:: success_criteria
      :type:  list[str]
      :value: None



   .. py:attribute:: task_summary
      :type:  str
      :value: None



.. py:function:: create_graded_reflection_pattern(name: str = 'react_graded_reflection', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactWithGradedReflection

   Create graded reflection pattern.


   .. autolink-examples:: create_graded_reflection_pattern
      :collapse:

.. py:function:: create_reflection_pattern(name: str = 'react_with_reflection', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactWithReflection

   Create Enhanced Base Agent pattern with reflection.


   .. autolink-examples:: create_reflection_pattern
      :collapse:

.. py:function:: create_v3_pattern(name: str = 'react_structured_v3', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactToStructuredV3

   Create V3 pattern: ReactAgent → SimpleAgentV3.


   .. autolink-examples:: create_v3_pattern
      :collapse:

.. py:function:: create_v4_pattern(name: str = 'react_structured_v4', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactToStructuredV4

   Create V4 pattern: MultiAgent composition.


   .. autolink-examples:: create_v4_pattern
      :collapse:

.. py:function:: data_analysis(data_description: str) -> str

   Analyze data and extract insights.


   .. autolink-examples:: data_analysis
      :collapse:

.. py:function:: example_graded_reflection_pattern()
   :async:


   Example: Graded Reflection Pattern.


   .. autolink-examples:: example_graded_reflection_pattern
      :collapse:

.. py:function:: example_reflection_pattern()
   :async:


   Example: Enhanced Base Agent with Reflection.


   .. autolink-examples:: example_reflection_pattern
      :collapse:

.. py:function:: example_v3_pattern()
   :async:


   Example: V3 Architecture Pattern.


   .. autolink-examples:: example_v3_pattern
      :collapse:

.. py:function:: example_v4_pattern()
   :async:


   Example: V4 Architecture Pattern.


   .. autolink-examples:: example_v4_pattern
      :collapse:

.. py:function:: main()
   :async:


   Run all pattern examples.


   .. autolink-examples:: main
      :collapse:

.. py:function:: stakeholder_analysis(context: str) -> str

   Analyze stakeholders for a given context.


   .. autolink-examples:: stakeholder_analysis
      :collapse:

.. py:function:: web_research(topic: str) -> str

   Research a topic using web sources.


   .. autolink-examples:: web_research
      :collapse:

