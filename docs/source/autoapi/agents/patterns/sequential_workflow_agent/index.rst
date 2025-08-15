agents.patterns.sequential_workflow_agent
=========================================

.. py:module:: agents.patterns.sequential_workflow_agent

.. autoapi-nested-parse::

   Sequential Workflow Agent - Using MultiAgent with SimpleAgentV3 patterns.

   This module demonstrates creating sequential multi-agent workflows using the
   MultiAgent as a base, with SimpleAgentV3 agents as components.

   Shows various sequential patterns:
   1. Simple linear workflows
   2. Conditional branching workflows
   3. Iterative refinement workflows
   4. Pipeline-style processing


   .. autolink-examples:: agents.patterns.sequential_workflow_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.patterns.sequential_workflow_agent.ConditionalWorkflowAgent
   agents.patterns.sequential_workflow_agent.FinalReport
   agents.patterns.sequential_workflow_agent.IterativeRefinementAgent
   agents.patterns.sequential_workflow_agent.PipelineAgent
   agents.patterns.sequential_workflow_agent.QualityAssessment
   agents.patterns.sequential_workflow_agent.ResearchBrief
   agents.patterns.sequential_workflow_agent.ResearchFindings
   agents.patterns.sequential_workflow_agent.SequentialWorkflowAgent


Functions
---------

.. autoapisummary::

   agents.patterns.sequential_workflow_agent.create_conditional_workflow
   agents.patterns.sequential_workflow_agent.create_iterative_workflow
   agents.patterns.sequential_workflow_agent.create_pipeline
   agents.patterns.sequential_workflow_agent.create_research_workflow
   agents.patterns.sequential_workflow_agent.example_conditional_workflow
   agents.patterns.sequential_workflow_agent.example_iterative_refinement
   agents.patterns.sequential_workflow_agent.example_pipeline
   agents.patterns.sequential_workflow_agent.example_research_workflow


Module Contents
---------------

.. py:class:: ConditionalWorkflowAgent

   Bases: :py:obj:`SequentialWorkflowAgent`


   Conditional workflow with branching logic.

   This variant adds conditional routing between stages based on
   intermediate results.


   .. autolink-examples:: ConditionalWorkflowAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Setup conditional workflow with routing.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: routing_conditions
      :type:  dict[str, callable]
      :value: None



.. py:class:: FinalReport(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final formatted report.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FinalReport
      :collapse:

   .. py:attribute:: conclusions
      :type:  list[str]
      :value: None



   .. py:attribute:: executive_summary
      :type:  str
      :value: None



   .. py:attribute:: recommendations
      :type:  list[str]
      :value: None



   .. py:attribute:: sections
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



.. py:class:: IterativeRefinementAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Iterative refinement workflow with feedback loops.

   This pattern implements iterative improvement through multiple passes.


   .. autolink-examples:: IterativeRefinementAgent
      :collapse:

   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: quality_threshold
      :type:  float
      :value: None



.. py:class:: PipelineAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Pipeline-style agent for data transformation workflows.

   Each stage transforms data for the next stage in a pipeline pattern.


   .. autolink-examples:: PipelineAgent
      :collapse:

   .. py:method:: _create_pipeline_stages() -> list[haive.agents.simple.agent.SimpleAgent]

      Create standard pipeline stages.


      .. autolink-examples:: _create_pipeline_stages
         :collapse:


.. py:class:: QualityAssessment(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Quality assessment for iterative refinement.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QualityAssessment
      :collapse:

   .. py:attribute:: meets_threshold
      :type:  bool
      :value: None



   .. py:attribute:: quality_score
      :type:  float
      :value: None



   .. py:attribute:: specific_feedback
      :type:  list[str]
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: None



   .. py:attribute:: weaknesses
      :type:  list[str]
      :value: None



.. py:class:: ResearchBrief(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Research brief from analyzer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchBrief
      :collapse:

   .. py:attribute:: key_questions
      :type:  list[str]
      :value: None



   .. py:attribute:: priority_areas
      :type:  list[str]
      :value: None



   .. py:attribute:: scope
      :type:  str
      :value: None



   .. py:attribute:: topic
      :type:  str
      :value: None



.. py:class:: ResearchFindings(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Detailed research findings.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchFindings
      :collapse:

   .. py:attribute:: confidence_scores
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: evidence
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: gaps
      :type:  list[str]
      :value: None



   .. py:attribute:: main_findings
      :type:  list[str]
      :value: None



   .. py:attribute:: topic
      :type:  str
      :value: None



.. py:class:: SequentialWorkflowAgent

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Sequential workflow agent for multi-stage processing.

   This agent orchestrates a sequence of SimpleAgentV3 agents to
   accomplish complex tasks through staged processing.

   .. rubric:: Example

   >>> workflow = SequentialWorkflowAgent(
   ...     name="research_pipeline",
   ...     stages=["analyze", "research", "synthesize", "format"],
   ...     debug=True
   ... )
   >>> report = await workflow.arun("Research AI ethics implications")


   .. autolink-examples:: SequentialWorkflowAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Setup workflow stages as SimpleAgentV3 instances.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: stage_configs
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: stages
      :type:  list[str]
      :value: None



.. py:function:: create_conditional_workflow(name: str = 'conditional_workflow', routing_conditions: dict[str, callable] | None = None, debug: bool = True) -> ConditionalWorkflowAgent

   Create a conditional workflow with branching.


   .. autolink-examples:: create_conditional_workflow
      :collapse:

.. py:function:: create_iterative_workflow(name: str = 'iterative_workflow', max_iterations: int = 3, quality_threshold: float = 0.85, debug: bool = True) -> IterativeRefinementAgent

   Create an iterative refinement workflow.


   .. autolink-examples:: create_iterative_workflow
      :collapse:

.. py:function:: create_pipeline(name: str = 'data_pipeline', debug: bool = True) -> PipelineAgent

   Create a data processing pipeline.


   .. autolink-examples:: create_pipeline
      :collapse:

.. py:function:: create_research_workflow(name: str = 'research_workflow', stages: list[str] | None = None, debug: bool = True) -> SequentialWorkflowAgent

   Create a research workflow with default stages.


   .. autolink-examples:: create_research_workflow
      :collapse:

.. py:function:: example_conditional_workflow()
   :async:


   Example of conditional workflow with branching.


   .. autolink-examples:: example_conditional_workflow
      :collapse:

.. py:function:: example_iterative_refinement()
   :async:


   Example of iterative refinement workflow.


   .. autolink-examples:: example_iterative_refinement
      :collapse:

.. py:function:: example_pipeline()
   :async:


   Example of pipeline processing.


   .. autolink-examples:: example_pipeline
      :collapse:

.. py:function:: example_research_workflow()
   :async:


   Example of research workflow execution.


   .. autolink-examples:: example_research_workflow
      :collapse:

