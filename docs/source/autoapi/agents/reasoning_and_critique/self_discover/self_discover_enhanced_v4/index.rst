
:py:mod:`agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4`
===============================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4

Self-Discover Agent Implementation following LangGraph tutorial pattern.

Based on the official LangGraph Self-Discover tutorial:
https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/

This implementation follows the exact pattern from the tutorial with proper
state management and structured output parsing.


.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.AdaptedModulesOutput
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.FinalAnswerOutput
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.ModuleSelectionOutput
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.ReasoningStructureOutput
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverAdapter
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverExecutor
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverSelector
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverState
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverStructurer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptedModulesOutput:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptedModulesOutput {
        node [shape=record];
        "AdaptedModulesOutput" [label="AdaptedModulesOutput"];
        "pydantic.BaseModel" -> "AdaptedModulesOutput";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.AdaptedModulesOutput
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

   Inheritance diagram for FinalAnswerOutput:

   .. graphviz::
      :align: center

      digraph inheritance_FinalAnswerOutput {
        node [shape=record];
        "FinalAnswerOutput" [label="FinalAnswerOutput"];
        "pydantic.BaseModel" -> "FinalAnswerOutput";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.FinalAnswerOutput
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

   Inheritance diagram for ModuleSelectionOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ModuleSelectionOutput {
        node [shape=record];
        "ModuleSelectionOutput" [label="ModuleSelectionOutput"];
        "pydantic.BaseModel" -> "ModuleSelectionOutput";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.ModuleSelectionOutput
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

   Inheritance diagram for ReasoningStructureOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningStructureOutput {
        node [shape=record];
        "ReasoningStructureOutput" [label="ReasoningStructureOutput"];
        "pydantic.BaseModel" -> "ReasoningStructureOutput";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.ReasoningStructureOutput
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

   Inheritance diagram for SelfDiscoverAdapter:

   .. graphviz::
      :align: center

      digraph inheritance_SelfDiscoverAdapter {
        node [shape=record];
        "SelfDiscoverAdapter" [label="SelfDiscoverAdapter"];
        "SimpleAgentV3" -> "SelfDiscoverAdapter";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverAdapter
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfDiscoverExecutor:

   .. graphviz::
      :align: center

      digraph inheritance_SelfDiscoverExecutor {
        node [shape=record];
        "SelfDiscoverExecutor" [label="SelfDiscoverExecutor"];
        "SimpleAgentV3" -> "SelfDiscoverExecutor";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverExecutor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfDiscoverSelector:

   .. graphviz::
      :align: center

      digraph inheritance_SelfDiscoverSelector {
        node [shape=record];
        "SelfDiscoverSelector" [label="SelfDiscoverSelector"];
        "SimpleAgentV3" -> "SelfDiscoverSelector";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverSelector
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfDiscoverState:

   .. graphviz::
      :align: center

      digraph inheritance_SelfDiscoverState {
        node [shape=record];
        "SelfDiscoverState" [label="SelfDiscoverState"];
        "TypedDict" -> "SelfDiscoverState";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfDiscoverStructurer:

   .. graphviz::
      :align: center

      digraph inheritance_SelfDiscoverStructurer {
        node [shape=record];
        "SelfDiscoverStructurer" [label="SelfDiscoverStructurer"];
        "SimpleAgentV3" -> "SelfDiscoverStructurer";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverStructurer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.main
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.run_self_discover_workflow

.. py:function:: main()
   :async:


   Example of using Self-Discover Enhanced V4.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_self_discover_workflow(task: str, modules: str | None = None) -> dict[str, Any]
   :async:


   Run the Self-Discover workflow sequentially.

   :param task: The task to solve
   :param modules: Optional custom reasoning modules

   :returns: Dict containing the final answer and reasoning


   .. autolink-examples:: run_self_discover_workflow
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4
   :collapse:
   
.. autolink-skip:: next
