
:py:mod:`agents.planning.rewoo.models.tool_step`
================================================

.. py:module:: agents.planning.rewoo.models.tool_step

Tool Step Model - Generic step that validates against a tool list.

A concrete step implementation that works with LangChain tools and validates:
- Tool exists in provided tool list
- Tool arguments match tool schema
- Tool can be executed with given parameters


.. autolink-examples:: agents.planning.rewoo.models.tool_step
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo.models.tool_step.AbstractStep
   agents.planning.rewoo.models.tool_step.ToolStep


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AbstractStep:

   .. graphviz::
      :align: center

      digraph inheritance_AbstractStep {
        node [shape=record];
        "AbstractStep" [label="AbstractStep"];
        "pydantic.BaseModel" -> "AbstractStep";
        "abc.ABC" -> "AbstractStep";
      }

.. autopydantic_model:: agents.planning.rewoo.models.tool_step.AbstractStep
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

   Inheritance diagram for ToolStep:

   .. graphviz::
      :align: center

      digraph inheritance_ToolStep {
        node [shape=record];
        "ToolStep" [label="ToolStep"];
        "agents.planning.rewoo.models.steps.AbstractStep" -> "ToolStep";
      }

.. autoclass:: agents.planning.rewoo.models.tool_step.ToolStep
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning.rewoo.models.tool_step.create_tool_steps_from_plan
   agents.planning.rewoo.models.tool_step.validate_tool_compatibility

.. py:function:: create_tool_steps_from_plan(tool_plan: list[dict[str, Any]], available_tools: list[langchain_core.tools.BaseTool]) -> list[ToolStep]

   Create a list of ToolSteps from a plan description.


   .. autolink-examples:: create_tool_steps_from_plan
      :collapse:

.. py:function:: validate_tool_compatibility(tools: list[langchain_core.tools.BaseTool]) -> dict[str, Any]

   Validate a list of tools for compatibility issues.


   .. autolink-examples:: validate_tool_compatibility
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.rewoo.models.tool_step
   :collapse:
   
.. autolink-skip:: next
