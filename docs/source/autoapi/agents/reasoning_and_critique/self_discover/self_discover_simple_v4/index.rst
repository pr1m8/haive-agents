
:py:mod:`agents.reasoning_and_critique.self_discover.self_discover_simple_v4`
=============================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4

Self-Discover Simple V4 - Minimal implementation with proper state handling.

This version:
- Uses a single shared state dict
- Each agent updates the state with its output
- No complex state transformations
- Clear, simple flow


.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.AdaptedModules
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.ModuleList
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.Plan
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.Solution


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

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4.AdaptedModules
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

   Inheritance diagram for ModuleList:

   .. graphviz::
      :align: center

      digraph inheritance_ModuleList {
        node [shape=record];
        "ModuleList" [label="ModuleList"];
        "pydantic.BaseModel" -> "ModuleList";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4.ModuleList
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

   Inheritance diagram for Plan:

   .. graphviz::
      :align: center

      digraph inheritance_Plan {
        node [shape=record];
        "Plan" [label="Plan"];
        "pydantic.BaseModel" -> "Plan";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4.Plan
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

   Inheritance diagram for Solution:

   .. graphviz::
      :align: center

      digraph inheritance_Solution {
        node [shape=record];
        "Solution" [label="Solution"];
        "pydantic.BaseModel" -> "Solution";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4.Solution
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

   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.create_agents
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.create_self_discover_simple
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.main
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.run_self_discover

.. py:function:: create_agents()

   Create the four agents for Self-Discover.


   .. autolink-examples:: create_agents
      :collapse:

.. py:function:: create_self_discover_simple()

   Create the Self-Discover agent.


   .. autolink-examples:: create_self_discover_simple
      :collapse:

.. py:function:: main()
   :async:


.. py:function:: run_self_discover(task: str, modules: str | None = None)
   :async:


   Run Self-Discover on a task.

   :param task: The task to solve
   :param modules: Optional custom modules (defaults to MODULES)

   :returns: Dict with the solution


   .. autolink-examples:: run_self_discover
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4
   :collapse:
   
.. autolink-skip:: next
