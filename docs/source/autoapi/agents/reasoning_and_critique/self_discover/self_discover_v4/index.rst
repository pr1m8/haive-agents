
:py:mod:`agents.reasoning_and_critique.self_discover.self_discover_v4`
======================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_v4

Self-Discover V4 - Using SimpleAgentV3 and MultiAgent.

Clean implementation following CLAUDE.md patterns:
- SimpleAgentV3 for individual agents
- MultiAgent for orchestration
- No custom __init__ overrides
- Proper state handling


.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_v4
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_v4.AdaptationResult
   agents.reasoning_and_critique.self_discover.self_discover_v4.AdaptedModule
   agents.reasoning_and_critique.self_discover.self_discover_v4.FinalAnswer
   agents.reasoning_and_critique.self_discover.self_discover_v4.ModuleSelection
   agents.reasoning_and_critique.self_discover.self_discover_v4.ReasoningPlan
   agents.reasoning_and_critique.self_discover.self_discover_v4.ReasoningStep
   agents.reasoning_and_critique.self_discover.self_discover_v4.SelectedModule
   agents.reasoning_and_critique.self_discover.self_discover_v4.SelfDiscoverV4


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptationResult:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptationResult {
        node [shape=record];
        "AdaptationResult" [label="AdaptationResult"];
        "pydantic.BaseModel" -> "AdaptationResult";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_v4.AdaptationResult
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

   Inheritance diagram for AdaptedModule:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptedModule {
        node [shape=record];
        "AdaptedModule" [label="AdaptedModule"];
        "pydantic.BaseModel" -> "AdaptedModule";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_v4.AdaptedModule
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

   Inheritance diagram for FinalAnswer:

   .. graphviz::
      :align: center

      digraph inheritance_FinalAnswer {
        node [shape=record];
        "FinalAnswer" [label="FinalAnswer"];
        "pydantic.BaseModel" -> "FinalAnswer";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_v4.FinalAnswer
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

   Inheritance diagram for ModuleSelection:

   .. graphviz::
      :align: center

      digraph inheritance_ModuleSelection {
        node [shape=record];
        "ModuleSelection" [label="ModuleSelection"];
        "pydantic.BaseModel" -> "ModuleSelection";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_v4.ModuleSelection
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

   Inheritance diagram for ReasoningPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningPlan {
        node [shape=record];
        "ReasoningPlan" [label="ReasoningPlan"];
        "pydantic.BaseModel" -> "ReasoningPlan";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_v4.ReasoningPlan
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

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_v4.ReasoningStep
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

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_v4.SelectedModule
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

   Inheritance diagram for SelfDiscoverV4:

   .. graphviz::
      :align: center

      digraph inheritance_SelfDiscoverV4 {
        node [shape=record];
        "SelfDiscoverV4" [label="SelfDiscoverV4"];
        "haive.agents.multi.agent.MultiAgent" -> "SelfDiscoverV4";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.self_discover_v4.SelfDiscoverV4
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_v4.create_adapter
   agents.reasoning_and_critique.self_discover.self_discover_v4.create_executor
   agents.reasoning_and_critique.self_discover.self_discover_v4.create_selector
   agents.reasoning_and_critique.self_discover.self_discover_v4.create_self_discover_v4
   agents.reasoning_and_critique.self_discover.self_discover_v4.create_structurer
   agents.reasoning_and_critique.self_discover.self_discover_v4.main

.. py:function:: create_adapter() -> haive.agents.simple.agent.SimpleAgent

   Create the module adapter agent.


   .. autolink-examples:: create_adapter
      :collapse:

.. py:function:: create_executor() -> haive.agents.simple.agent.SimpleAgent

   Create the plan executor agent.


   .. autolink-examples:: create_executor
      :collapse:

.. py:function:: create_selector() -> haive.agents.simple.agent.SimpleAgent

   Create the module selector agent.


   .. autolink-examples:: create_selector
      :collapse:

.. py:function:: create_self_discover_v4() -> SelfDiscoverV4

   Create a ready-to-use Self-Discover V4 agent.


   .. autolink-examples:: create_self_discover_v4
      :collapse:

.. py:function:: create_structurer() -> haive.agents.simple.agent.SimpleAgent

   Create the plan structurer agent.


   .. autolink-examples:: create_structurer
      :collapse:

.. py:function:: main()
   :async:


   Example of using Self-Discover V4.


   .. autolink-examples:: main
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_v4
   :collapse:
   
.. autolink-skip:: next
