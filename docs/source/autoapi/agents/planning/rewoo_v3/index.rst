
:py:mod:`agents.planning.rewoo_v3`
==================================

.. py:module:: agents.planning.rewoo_v3

ReWOO V3 Agent - Reasoning WithOut Observation using Enhanced MultiAgent V3.

This package implements the ReWOO (Reasoning WithOut Observation) methodology
using our proven Enhanced MultiAgent V3 patterns from Plan-and-Execute V3 success.

ReWOO separates planning, execution, and synthesis phases for improved efficiency:
1. Planner creates complete reasoning plan upfront with evidence placeholders
2. Worker executes all tool calls in batch to collect evidence
3. Solver synthesizes all evidence into comprehensive final answer

Key advantages over traditional iterative agents:
- 5x token efficiency improvement
- Parallel/batch tool execution capability
- Robust handling of partial failures
- Modular design for fine-tuning

Usage:
    >>> from haive.agents.planning.rewoo_v3 import ReWOOV3Agent
    >>> from haive.core.engine.aug_llm import AugLLMConfig
    >>>
    >>> config = AugLLMConfig(temperature=0.7)
    >>> agent = ReWOOV3Agent(
    ...     name="research_agent",
    ...     config=config,
    ...     tools=[search_tool, calculator_tool]
    ... )
    >>>
    >>> result = await agent.arun("Research market trends and calculate growth rates")
    >>> print(f"Answer: {result.final_answer}")
    >>> print(f"Confidence: {result.confidence}")
    >>> print(f"Evidence collected: {result.evidence_collected}")

Architecture:
    - ReWOOV3Agent: Main coordinator using Enhanced MultiAgent V3
    - ReWOOV3State: State schema with computed fields for dynamic prompts
    - ReWOOPlan/EvidenceCollection/ReWOOSolution: Structured output models
    - ChatPromptTemplates: Dynamic prompts with state field placeholders


.. autolink-examples:: agents.planning.rewoo_v3
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo_v3.EvidenceCollection
   agents.planning.rewoo_v3.EvidenceItem
   agents.planning.rewoo_v3.EvidenceStatus
   agents.planning.rewoo_v3.PlanStep
   agents.planning.rewoo_v3.ReWOOPlan
   agents.planning.rewoo_v3.ReWOOSolution
   agents.planning.rewoo_v3.ReWOOV3Agent
   agents.planning.rewoo_v3.ReWOOV3Input
   agents.planning.rewoo_v3.ReWOOV3Output
   agents.planning.rewoo_v3.ReWOOV3State


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EvidenceCollection:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceCollection {
        node [shape=record];
        "EvidenceCollection" [label="EvidenceCollection"];
        "pydantic.BaseModel" -> "EvidenceCollection";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.EvidenceCollection
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

   Inheritance diagram for EvidenceItem:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceItem {
        node [shape=record];
        "EvidenceItem" [label="EvidenceItem"];
        "pydantic.BaseModel" -> "EvidenceItem";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.EvidenceItem
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

   Inheritance diagram for EvidenceStatus:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceStatus {
        node [shape=record];
        "EvidenceStatus" [label="EvidenceStatus"];
        "str" -> "EvidenceStatus";
        "enum.Enum" -> "EvidenceStatus";
      }

.. autoclass:: agents.planning.rewoo_v3.EvidenceStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **EvidenceStatus** is an Enum defined in ``agents.planning.rewoo_v3``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanStep:

   .. graphviz::
      :align: center

      digraph inheritance_PlanStep {
        node [shape=record];
        "PlanStep" [label="PlanStep"];
        "pydantic.BaseModel" -> "PlanStep";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.PlanStep
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

   Inheritance diagram for ReWOOPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOPlan {
        node [shape=record];
        "ReWOOPlan" [label="ReWOOPlan"];
        "pydantic.BaseModel" -> "ReWOOPlan";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.ReWOOPlan
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

   Inheritance diagram for ReWOOSolution:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOSolution {
        node [shape=record];
        "ReWOOSolution" [label="ReWOOSolution"];
        "pydantic.BaseModel" -> "ReWOOSolution";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.ReWOOSolution
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

   Inheritance diagram for ReWOOV3Agent:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3Agent {
        node [shape=record];
        "ReWOOV3Agent" [label="ReWOOV3Agent"];
      }

.. autoclass:: agents.planning.rewoo_v3.ReWOOV3Agent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOV3Input:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3Input {
        node [shape=record];
        "ReWOOV3Input" [label="ReWOOV3Input"];
        "pydantic.BaseModel" -> "ReWOOV3Input";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.ReWOOV3Input
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

   Inheritance diagram for ReWOOV3Output:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3Output {
        node [shape=record];
        "ReWOOV3Output" [label="ReWOOV3Output"];
        "pydantic.BaseModel" -> "ReWOOV3Output";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.ReWOOV3Output
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

   Inheritance diagram for ReWOOV3State:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3State {
        node [shape=record];
        "ReWOOV3State" [label="ReWOOV3State"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "ReWOOV3State";
      }

.. autoclass:: agents.planning.rewoo_v3.ReWOOV3State
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.planning.rewoo_v3
   :collapse:
   
.. autolink-skip:: next
