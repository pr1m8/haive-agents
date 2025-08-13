
:py:mod:`agents.reasoning_and_critique.self_discover.self_discover_working_v4`
==============================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_working_v4

Self-Discover Working V4 - A working implementation that properly handles agents.

This version creates a working self-discover implementation using the patterns
that are known to work in the codebase.


.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_working_v4
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_working_v4.AdaptedModules
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.FinalAnswer
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.ModuleSelection
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.ReasoningPlan


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptedModules:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptedModules {
        node [shape=record];
        "AdaptedModules" [label="AdaptedModules"];
        "pydantic.BaseModel" -> "AdaptedModules";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_working_v4.AdaptedModules
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

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_working_v4.FinalAnswer
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

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_working_v4.ModuleSelection
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

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_working_v4.ReasoningPlan
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

   agents.reasoning_and_critique.self_discover.self_discover_working_v4.create_self_discover_agents
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.create_self_discover_workflow
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.main
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.solve_with_self_discover

.. py:function:: create_self_discover_agents()

   Create the four agents for Self-Discover workflow.


   .. autolink-examples:: create_self_discover_agents
      :collapse:

.. py:function:: create_self_discover_workflow()

   Create the Self-Discover multi-agent workflow.


   .. autolink-examples:: create_self_discover_workflow
      :collapse:

.. py:function:: main()
   :async:


   Example of using Self-Discover workflow.


   .. autolink-examples:: main
      :collapse:

.. py:function:: solve_with_self_discover(task: str, modules: str | None = None)
   :async:


   Solve a task using Self-Discover workflow.

   :param task: The task to solve
   :param modules: Optional custom reasoning modules

   :returns: The final answer


   .. autolink-examples:: solve_with_self_discover
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_working_v4
   :collapse:
   
.. autolink-skip:: next
