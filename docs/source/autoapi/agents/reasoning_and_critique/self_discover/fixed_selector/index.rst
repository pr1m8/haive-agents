
:py:mod:`agents.reasoning_and_critique.self_discover.fixed_selector`
====================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.fixed_selector

Fixed SelfDiscoverSelector that properly handles prompt template variables.


.. autolink-examples:: agents.reasoning_and_critique.self_discover.fixed_selector
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.fixed_selector.FixedSelfDiscoverSelector
   agents.reasoning_and_critique.self_discover.fixed_selector.ModuleSelectionOutput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FixedSelfDiscoverSelector:

   .. graphviz::
      :align: center

      digraph inheritance_FixedSelfDiscoverSelector {
        node [shape=record];
        "FixedSelfDiscoverSelector" [label="FixedSelfDiscoverSelector"];
        "SimpleAgentV3" -> "FixedSelfDiscoverSelector";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.fixed_selector.FixedSelfDiscoverSelector
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ModuleSelectionOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ModuleSelectionOutput {
        node [shape=record];
        "ModuleSelectionOutput" [label="ModuleSelectionOutput"];
        "pydantic.BaseModel" -> "ModuleSelectionOutput";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.fixed_selector.ModuleSelectionOutput
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

.. autolink-examples:: agents.reasoning_and_critique.self_discover.fixed_selector
   :collapse:
   
.. autolink-skip:: next
