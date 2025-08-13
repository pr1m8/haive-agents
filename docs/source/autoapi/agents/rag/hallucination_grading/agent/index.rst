
:py:mod:`agents.rag.hallucination_grading.agent`
================================================

.. py:module:: agents.rag.hallucination_grading.agent

Hallucination Grading Agents.

Modular agents for detecting and grading hallucinations in RAG responses.
Can be plugged into any workflow with compatible I/O schemas.


.. autolink-examples:: agents.rag.hallucination_grading.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.hallucination_grading.agent.AdvancedHallucinationGrade
   agents.rag.hallucination_grading.agent.AdvancedHallucinationGraderAgent
   agents.rag.hallucination_grading.agent.HallucinationGrade
   agents.rag.hallucination_grading.agent.HallucinationGraderAgent
   agents.rag.hallucination_grading.agent.RealtimeHallucinationCheck
   agents.rag.hallucination_grading.agent.RealtimeHallucinationGraderAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdvancedHallucinationGrade:

   .. graphviz::
      :align: center

      digraph inheritance_AdvancedHallucinationGrade {
        node [shape=record];
        "AdvancedHallucinationGrade" [label="AdvancedHallucinationGrade"];
        "pydantic.BaseModel" -> "AdvancedHallucinationGrade";
      }

.. autopydantic_model:: agents.rag.hallucination_grading.agent.AdvancedHallucinationGrade
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

   Inheritance diagram for AdvancedHallucinationGraderAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdvancedHallucinationGraderAgent {
        node [shape=record];
        "AdvancedHallucinationGraderAgent" [label="AdvancedHallucinationGraderAgent"];
        "haive.agents.base.agent.Agent" -> "AdvancedHallucinationGraderAgent";
      }

.. autoclass:: agents.rag.hallucination_grading.agent.AdvancedHallucinationGraderAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HallucinationGrade:

   .. graphviz::
      :align: center

      digraph inheritance_HallucinationGrade {
        node [shape=record];
        "HallucinationGrade" [label="HallucinationGrade"];
        "pydantic.BaseModel" -> "HallucinationGrade";
      }

.. autopydantic_model:: agents.rag.hallucination_grading.agent.HallucinationGrade
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

   Inheritance diagram for HallucinationGraderAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HallucinationGraderAgent {
        node [shape=record];
        "HallucinationGraderAgent" [label="HallucinationGraderAgent"];
        "haive.agents.base.agent.Agent" -> "HallucinationGraderAgent";
      }

.. autoclass:: agents.rag.hallucination_grading.agent.HallucinationGraderAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RealtimeHallucinationCheck:

   .. graphviz::
      :align: center

      digraph inheritance_RealtimeHallucinationCheck {
        node [shape=record];
        "RealtimeHallucinationCheck" [label="RealtimeHallucinationCheck"];
        "pydantic.BaseModel" -> "RealtimeHallucinationCheck";
      }

.. autopydantic_model:: agents.rag.hallucination_grading.agent.RealtimeHallucinationCheck
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

   Inheritance diagram for RealtimeHallucinationGraderAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RealtimeHallucinationGraderAgent {
        node [shape=record];
        "RealtimeHallucinationGraderAgent" [label="RealtimeHallucinationGraderAgent"];
        "haive.agents.base.agent.Agent" -> "RealtimeHallucinationGraderAgent";
      }

.. autoclass:: agents.rag.hallucination_grading.agent.RealtimeHallucinationGraderAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.hallucination_grading.agent.create_hallucination_grader
   agents.rag.hallucination_grading.agent.get_hallucination_grader_io_schema

.. py:function:: create_hallucination_grader(grader_type: Literal['basic', 'advanced', 'realtime'] = 'basic', llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Create a hallucination grader agent.

   :param grader_type: Type of grader to create
   :param llm_config: LLM configuration
   :param \*\*kwargs: Additional arguments

   :returns: Configured hallucination grader agent


   .. autolink-examples:: create_hallucination_grader
      :collapse:

.. py:function:: get_hallucination_grader_io_schema() -> dict[str, list[str]]

   Get I/O schema for hallucination graders for compatibility checking.


   .. autolink-examples:: get_hallucination_grader_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.hallucination_grading.agent
   :collapse:
   
.. autolink-skip:: next
