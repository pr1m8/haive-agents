
:py:mod:`agents.patterns.react_structured_agent_variants`
=========================================================

.. py:module:: agents.patterns.react_structured_agent_variants

React Structured Agent Variants - Building on base Agent patterns.

This module creates various ReactAgent → SimpleAgent patterns using the base
agent.py architecture, as requested. Shows different ways to combine agents
for structured workflows with reasoning and output formatting.

Variants include:
1. Basic React → Simple structured flow
2. Multi-stage reasoning with structured outputs
3. Tool-enhanced React → Simple patterns
4. Reflection-enabled variants


.. autolink-examples:: agents.patterns.react_structured_agent_variants
   :collapse:

Classes
-------

.. autoapisummary::

   agents.patterns.react_structured_agent_variants.AnalysisResult
   agents.patterns.react_structured_agent_variants.MultiStageReasoningAgent
   agents.patterns.react_structured_agent_variants.ReactToStructuredAgent
   agents.patterns.react_structured_agent_variants.ReflectiveStructuredAgent
   agents.patterns.react_structured_agent_variants.StructuredSolution
   agents.patterns.react_structured_agent_variants.ToolEnhancedStructuredAgent


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

.. autopydantic_model:: agents.patterns.react_structured_agent_variants.AnalysisResult
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

   Inheritance diagram for MultiStageReasoningAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiStageReasoningAgent {
        node [shape=record];
        "MultiStageReasoningAgent" [label="MultiStageReasoningAgent"];
        "haive.agents.base.agent.Agent" -> "MultiStageReasoningAgent";
      }

.. autoclass:: agents.patterns.react_structured_agent_variants.MultiStageReasoningAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactToStructuredAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactToStructuredAgent {
        node [shape=record];
        "ReactToStructuredAgent" [label="ReactToStructuredAgent"];
        "haive.agents.base.agent.Agent" -> "ReactToStructuredAgent";
      }

.. autoclass:: agents.patterns.react_structured_agent_variants.ReactToStructuredAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectiveStructuredAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectiveStructuredAgent {
        node [shape=record];
        "ReflectiveStructuredAgent" [label="ReflectiveStructuredAgent"];
        "haive.agents.base.agent.Agent" -> "ReflectiveStructuredAgent";
      }

.. autoclass:: agents.patterns.react_structured_agent_variants.ReflectiveStructuredAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StructuredSolution:

   .. graphviz::
      :align: center

      digraph inheritance_StructuredSolution {
        node [shape=record];
        "StructuredSolution" [label="StructuredSolution"];
        "pydantic.BaseModel" -> "StructuredSolution";
      }

.. autopydantic_model:: agents.patterns.react_structured_agent_variants.StructuredSolution
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

   Inheritance diagram for ToolEnhancedStructuredAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ToolEnhancedStructuredAgent {
        node [shape=record];
        "ToolEnhancedStructuredAgent" [label="ToolEnhancedStructuredAgent"];
        "ReactToStructuredAgent" -> "ToolEnhancedStructuredAgent";
      }

.. autoclass:: agents.patterns.react_structured_agent_variants.ToolEnhancedStructuredAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.patterns.react_structured_agent_variants.create_multi_stage_reasoning_agent
   agents.patterns.react_structured_agent_variants.create_react_structured_agent
   agents.patterns.react_structured_agent_variants.create_reflective_structured_agent
   agents.patterns.react_structured_agent_variants.create_tool_enhanced_agent
   agents.patterns.react_structured_agent_variants.example_basic_react_structured
   agents.patterns.react_structured_agent_variants.example_multi_stage
   agents.patterns.react_structured_agent_variants.example_reflective

.. py:function:: create_multi_stage_reasoning_agent(name: str = 'multi_stage', stages: list[dict[str, Any]] | None = None, debug: bool = True) -> MultiStageReasoningAgent

   Create a multi-stage reasoning agent.


   .. autolink-examples:: create_multi_stage_reasoning_agent
      :collapse:

.. py:function:: create_react_structured_agent(name: str = 'react_structured', tools: list[Any] | None = None, output_model: type[pydantic.BaseModel] = StructuredSolution, debug: bool = True) -> ReactToStructuredAgent

   Create a React → Structured agent.


   .. autolink-examples:: create_react_structured_agent
      :collapse:

.. py:function:: create_reflective_structured_agent(name: str = 'reflective', include_reflection: bool = True, output_model: type[pydantic.BaseModel] = StructuredSolution, debug: bool = True) -> ReflectiveStructuredAgent

   Create a reflective structured agent.


   .. autolink-examples:: create_reflective_structured_agent
      :collapse:

.. py:function:: create_tool_enhanced_agent(name: str = 'tool_enhanced', output_model: type[pydantic.BaseModel] = AnalysisResult, debug: bool = True) -> ToolEnhancedStructuredAgent

   Create a tool-enhanced structured agent.


   .. autolink-examples:: create_tool_enhanced_agent
      :collapse:

.. py:function:: example_basic_react_structured()
   :async:


   Example of basic React → Structured flow.


   .. autolink-examples:: example_basic_react_structured
      :collapse:

.. py:function:: example_multi_stage()
   :async:


   Example of multi-stage reasoning.


   .. autolink-examples:: example_multi_stage
      :collapse:

.. py:function:: example_reflective()
   :async:


   Example of reflective structured output.


   .. autolink-examples:: example_reflective
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.patterns.react_structured_agent_variants
   :collapse:
   
.. autolink-skip:: next
