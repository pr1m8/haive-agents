
:py:mod:`clean_dynamic_supervisor`
==================================

.. py:module:: clean_dynamic_supervisor

Clean Dynamic Supervisor Implementation.

A dynamic supervisor that can add/remove agents at runtime and
adapt routing based on agent capabilities.


.. autolink-examples:: clean_dynamic_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   clean_dynamic_supervisor.DynamicSupervisor
   clean_dynamic_supervisor.DynamicSupervisorState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisor {
        node [shape=record];
        "DynamicSupervisor" [label="DynamicSupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicSupervisor";
      }

.. autoclass:: clean_dynamic_supervisor.DynamicSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisorState {
        node [shape=record];
        "DynamicSupervisorState" [label="DynamicSupervisorState"];
        "pydantic.BaseModel" -> "DynamicSupervisorState";
      }

.. autopydantic_model:: clean_dynamic_supervisor.DynamicSupervisorState
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

.. autolink-examples:: clean_dynamic_supervisor
   :collapse:
   
.. autolink-skip:: next
