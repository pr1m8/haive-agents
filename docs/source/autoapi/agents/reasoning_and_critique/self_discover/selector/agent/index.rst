
:py:mod:`agents.reasoning_and_critique.self_discover.selector.agent`
====================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.selector.agent

Self-Discover Selector Agent implementation.


.. autolink-examples:: agents.reasoning_and_critique.self_discover.selector.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.selector.agent.ModuleSelection
   agents.reasoning_and_critique.self_discover.selector.agent.SelectorAgent


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ModuleSelection:

   .. graphviz::
      :align: center

      digraph inheritance_ModuleSelection {
        node [shape=record];
        "ModuleSelection" [label="ModuleSelection"];
        "pydantic.BaseModel" -> "ModuleSelection";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.selector.agent.ModuleSelection
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

   Inheritance diagram for SelectorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelectorAgent {
        node [shape=record];
        "SelectorAgent" [label="SelectorAgent"];
        "haive.agents.simple.SimpleAgent" -> "SelectorAgent";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.selector.agent.SelectorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.selector.agent
   :collapse:
   
.. autolink-skip:: next
