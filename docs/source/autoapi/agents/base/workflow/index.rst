
:py:mod:`agents.base.workflow`
==============================

.. py:module:: agents.base.workflow

Workflow base class - Pure workflow orchestration without engine dependencies.

This module provides the abstract Workflow class for building pure orchestration
workflows that handle routing, transformation, and coordination without requiring
language model engines.

Classes:
    Workflow: Abstract base class for pure workflow orchestration.

.. rubric:: Example

Creating a simple data processing workflow::

    from haive.agents.base.workflow import Workflow

    class DataProcessor(Workflow):
        async def execute(self, data):
            # Pure processing logic, no LLM
            processed = transform_data(data)
            validated = validate_data(processed)
            return validated

    processor = DataProcessor(name="data_processor")
    result = await processor.execute(raw_data)

.. seealso:: :class:`haive.agents.base.agent.Agent`: Full agent with engine support


.. autolink-examples:: agents.base.workflow
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.workflow.Workflow


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Workflow:

   .. graphviz::
      :align: center

      digraph inheritance_Workflow {
        node [shape=record];
        "Workflow" [label="Workflow"];
        "pydantic.BaseModel" -> "Workflow";
        "abc.ABC" -> "Workflow";
      }

.. autopydantic_model:: agents.base.workflow.Workflow
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





.. rubric:: Related Links

.. autolink-examples:: agents.base.workflow
   :collapse:
   
.. autolink-skip:: next
