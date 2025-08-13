
:py:mod:`agents.memory_reorganized.integrations.langmem_agent`
==============================================================

.. py:module:: agents.memory_reorganized.integrations.langmem_agent

Agent core module.

This module provides agent functionality for the Haive framework.

Classes:
    LTMState: LTMState implementation.
    LTMAgent: LTMAgent implementation.

Functions:
    extraction_succeeded: Extraction Succeeded functionality.
    has_processing_errors: Has Processing Errors functionality.
    needs_kg_processing: Needs Kg Processing functionality.


.. autolink-examples:: agents.memory_reorganized.integrations.langmem_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.integrations.langmem_agent.LTMAgent
   agents.memory_reorganized.integrations.langmem_agent.LTMState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LTMAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LTMAgent {
        node [shape=record];
        "LTMAgent" [label="LTMAgent"];
        "haive.agents.base.agent.Agent" -> "LTMAgent";
      }

.. autoclass:: agents.memory_reorganized.integrations.langmem_agent.LTMAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LTMState:

   .. graphviz::
      :align: center

      digraph inheritance_LTMState {
        node [shape=record];
        "LTMState" [label="LTMState"];
        "pydantic.BaseModel" -> "LTMState";
      }

.. autopydantic_model:: agents.memory_reorganized.integrations.langmem_agent.LTMState
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

   agents.memory_reorganized.integrations.langmem_agent.extraction_succeeded
   agents.memory_reorganized.integrations.langmem_agent.has_processing_errors
   agents.memory_reorganized.integrations.langmem_agent.needs_categorization
   agents.memory_reorganized.integrations.langmem_agent.needs_consolidation
   agents.memory_reorganized.integrations.langmem_agent.needs_kg_processing
   agents.memory_reorganized.integrations.langmem_agent.needs_tool_activation
   agents.memory_reorganized.integrations.langmem_agent.processing_complete

.. py:function:: extraction_succeeded(state: LTMState) -> bool

   Check if memory extraction succeeded.


   .. autolink-examples:: extraction_succeeded
      :collapse:

.. py:function:: has_processing_errors(state: LTMState) -> bool

   Check if there are critical processing errors.


   .. autolink-examples:: has_processing_errors
      :collapse:

.. py:function:: needs_categorization(state: LTMState) -> bool

   Check if categorization is needed.


   .. autolink-examples:: needs_categorization
      :collapse:

.. py:function:: needs_consolidation(state: LTMState) -> bool

   Check if consolidation is needed.


   .. autolink-examples:: needs_consolidation
      :collapse:

.. py:function:: needs_kg_processing(state: LTMState) -> bool

   Check if KG processing is needed.


   .. autolink-examples:: needs_kg_processing
      :collapse:

.. py:function:: needs_tool_activation(state: LTMState) -> bool

   Check if memory tools should be activated.


   .. autolink-examples:: needs_tool_activation
      :collapse:

.. py:function:: processing_complete(state: LTMState) -> bool

   Check if all processing is complete.


   .. autolink-examples:: processing_complete
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.integrations.langmem_agent
   :collapse:
   
.. autolink-skip:: next
