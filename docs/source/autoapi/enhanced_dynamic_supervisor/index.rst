
:py:mod:`enhanced_dynamic_supervisor`
=====================================

.. py:module:: enhanced_dynamic_supervisor

Enhanced DynamicSupervisor implementation extending SupervisorAgent.

DynamicSupervisor = SupervisorAgent + dynamic worker management + adaptive strategies.


.. autolink-examples:: enhanced_dynamic_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   enhanced_dynamic_supervisor.DynamicSupervisor
   enhanced_dynamic_supervisor.MockWorkerTemplate


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisor {
        node [shape=record];
        "DynamicSupervisor" [label="DynamicSupervisor"];
        "haive.agents.multi.enhanced_supervisor_agent.SupervisorAgent" -> "DynamicSupervisor";
      }

.. autoclass:: enhanced_dynamic_supervisor.DynamicSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MockWorkerTemplate:

   .. graphviz::
      :align: center

      digraph inheritance_MockWorkerTemplate {
        node [shape=record];
        "MockWorkerTemplate" [label="MockWorkerTemplate"];
      }

.. autoclass:: enhanced_dynamic_supervisor.MockWorkerTemplate
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: enhanced_dynamic_supervisor
   :collapse:
   
.. autolink-skip:: next
