
:py:mod:`agents.reasoning_and_critique.self_discover.self_discover_sequential_v2`
=================================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2

Self-Discover Sequential Agent V2 - Proper implementation following CLAUDE.md patterns.

This implementation:
1. Uses SimpleAgentV3 for enhanced features
2. No custom __init__ overrides
3. Uses MultiAgent for sequential composition
4. Consolidates Pydantic models to avoid conflicts
5. Follows "no mocks" testing philosophy


.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.AdaptedModule
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ExecutionStep
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ModuleAdaptationResult
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ModuleSelectionResult
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningExecution
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningStep
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningStructure
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.SelectedModule


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptedModule:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptedModule {
        node [shape=record];
        "AdaptedModule" [label="AdaptedModule"];
        "pydantic.BaseModel" -> "AdaptedModule";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.AdaptedModule
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

   Inheritance diagram for ExecutionStep:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionStep {
        node [shape=record];
        "ExecutionStep" [label="ExecutionStep"];
        "pydantic.BaseModel" -> "ExecutionStep";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ExecutionStep
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

   Inheritance diagram for ModuleAdaptationResult:

   .. graphviz::
      :align: center

      digraph inheritance_ModuleAdaptationResult {
        node [shape=record];
        "ModuleAdaptationResult" [label="ModuleAdaptationResult"];
        "pydantic.BaseModel" -> "ModuleAdaptationResult";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ModuleAdaptationResult
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

   Inheritance diagram for ModuleSelectionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ModuleSelectionResult {
        node [shape=record];
        "ModuleSelectionResult" [label="ModuleSelectionResult"];
        "pydantic.BaseModel" -> "ModuleSelectionResult";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ModuleSelectionResult
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

   Inheritance diagram for ReasoningExecution:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningExecution {
        node [shape=record];
        "ReasoningExecution" [label="ReasoningExecution"];
        "pydantic.BaseModel" -> "ReasoningExecution";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningExecution
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

   Inheritance diagram for ReasoningStep:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningStep {
        node [shape=record];
        "ReasoningStep" [label="ReasoningStep"];
        "pydantic.BaseModel" -> "ReasoningStep";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningStep
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

   Inheritance diagram for ReasoningStructure:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningStructure {
        node [shape=record];
        "ReasoningStructure" [label="ReasoningStructure"];
        "pydantic.BaseModel" -> "ReasoningStructure";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningStructure
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

   Inheritance diagram for SelectedModule:

   .. graphviz::
      :align: center

      digraph inheritance_SelectedModule {
        node [shape=record];
        "SelectedModule" [label="SelectedModule"];
        "pydantic.BaseModel" -> "SelectedModule";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.SelectedModule
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

   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_adapter_agent
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_executor_agent
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_selector_agent
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_self_discover_sequential
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_structurer_agent
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.main

.. py:function:: create_adapter_agent() -> haive.agents.simple.agent.SimpleAgent

   Create the adapter agent with proper configuration.


   .. autolink-examples:: create_adapter_agent
      :collapse:

.. py:function:: create_executor_agent() -> haive.agents.simple.agent.SimpleAgent

   Create the executor agent with proper configuration.


   .. autolink-examples:: create_executor_agent
      :collapse:

.. py:function:: create_selector_agent() -> haive.agents.simple.agent.SimpleAgent

   Create the selector agent with proper configuration.


   .. autolink-examples:: create_selector_agent
      :collapse:

.. py:function:: create_self_discover_sequential() -> haive.agents.multi.agent.MultiAgent

   Create the complete Self-Discover sequential workflow.

   This follows the proper pattern from CLAUDE.md:
   - Uses MultiAgent for composition
   - No custom classes or __init__ overrides
   - Clear sequential execution
   - Proper state handling between agents

   :returns: MultiAgent configured for Self-Discover workflow


   .. autolink-examples:: create_self_discover_sequential
      :collapse:

.. py:function:: create_structurer_agent() -> haive.agents.simple.agent.SimpleAgent

   Create the structurer agent with proper configuration.


   .. autolink-examples:: create_structurer_agent
      :collapse:

.. py:function:: main()
   :async:


   Example of using the Self-Discover sequential agent.


   .. autolink-examples:: main
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2
   :collapse:
   
.. autolink-skip:: next
