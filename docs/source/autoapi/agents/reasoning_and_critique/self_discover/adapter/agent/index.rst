
:py:mod:`agents.reasoning_and_critique.self_discover.adapter.agent`
===================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.adapter.agent

Self-Discover Adapter Agent implementation.


.. autolink-examples:: agents.reasoning_and_critique.self_discover.adapter.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.adapter.agent.AdaptedModules
   agents.reasoning_and_critique.self_discover.adapter.agent.AdapterAgent


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptedModules:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptedModules {
        node [shape=record];
        "AdaptedModules" [label="AdaptedModules"];
        "pydantic.BaseModel" -> "AdaptedModules";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.adapter.agent.AdaptedModules
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

   Inheritance diagram for AdapterAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdapterAgent {
        node [shape=record];
        "AdapterAgent" [label="AdapterAgent"];
        "haive.agents.simple.SimpleAgent" -> "AdapterAgent";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.adapter.agent.AdapterAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.adapter.agent
   :collapse:
   
.. autolink-skip:: next
