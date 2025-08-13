
:py:mod:`agents.patterns.sequential_workflow_agent`
===================================================

.. py:module:: agents.patterns.sequential_workflow_agent

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConditionalWorkflowAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalWorkflowAgent {
        node [shape=record];
        "ConditionalWorkflowAgent" [label="ConditionalWorkflowAgent"];
        "SequentialWorkflowAgent" -> "ConditionalWorkflowAgent";
      }

.. autoclass:: agents.patterns.sequential_workflow_agent.ConditionalWorkflowAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FinalReport:

   .. graphviz::
      :align: center

      digraph inheritance_FinalReport {
        node [shape=record];
        "FinalReport" [label="FinalReport"];
        "pydantic.BaseModel" -> "FinalReport";
      }

.. autopydantic_model:: agents.patterns.sequential_workflow_agent.FinalReport
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

   Inheritance diagram for IterativeRefinementAgent:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeRefinementAgent {
        node [shape=record];
        "IterativeRefinementAgent" [label="IterativeRefinementAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "IterativeRefinementAgent";
      }

.. autoclass:: agents.patterns.sequential_workflow_agent.IterativeRefinementAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PipelineAgent:

   .. graphviz::
      :align: center

      digraph inheritance_PipelineAgent {
        node [shape=record];
        "PipelineAgent" [label="PipelineAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "PipelineAgent";
      }

.. autoclass:: agents.patterns.sequential_workflow_agent.PipelineAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QualityAssessment:

   .. graphviz::
      :align: center

      digraph inheritance_QualityAssessment {
        node [shape=record];
        "QualityAssessment" [label="QualityAssessment"];
        "pydantic.BaseModel" -> "QualityAssessment";
      }

.. autopydantic_model:: agents.patterns.sequential_workflow_agent.QualityAssessment
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

   Inheritance diagram for ResearchBrief:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchBrief {
        node [shape=record];
        "ResearchBrief" [label="ResearchBrief"];
        "pydantic.BaseModel" -> "ResearchBrief";
      }

.. autopydantic_model:: agents.patterns.sequential_workflow_agent.ResearchBrief
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

   Inheritance diagram for ResearchFindings:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchFindings {
        node [shape=record];
        "ResearchFindings" [label="ResearchFindings"];
        "pydantic.BaseModel" -> "ResearchFindings";
      }

.. autopydantic_model:: agents.patterns.sequential_workflow_agent.ResearchFindings
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

   Inheritance diagram for SequentialWorkflowAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialWorkflowAgent {
        node [shape=record];
        "SequentialWorkflowAgent" [label="SequentialWorkflowAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "SequentialWorkflowAgent";
      }

.. autoclass:: agents.patterns.sequential_workflow_agent.SequentialWorkflowAgent
   :members:
   :undoc-members:
   :show-inheritance:


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



.. rubric:: Related Links

.. autolink-examples:: agents.patterns.sequential_workflow_agent
   :collapse:
   
.. autolink-skip:: next
