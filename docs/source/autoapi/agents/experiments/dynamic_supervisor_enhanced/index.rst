
:py:mod:`agents.experiments.dynamic_supervisor_enhanced`
========================================================

.. py:module:: agents.experiments.dynamic_supervisor_enhanced

Enhanced Dynamic Supervisor with self-modification capabilities.


.. autolink-examples:: agents.experiments.dynamic_supervisor_enhanced
   :collapse:

Classes
-------

.. autoapisummary::

   agents.experiments.dynamic_supervisor_enhanced.SelfModifyingSupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfModifyingSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_SelfModifyingSupervisor {
        node [shape=record];
        "SelfModifyingSupervisor" [label="SelfModifyingSupervisor"];
        "haive.agents.experiments.dynamic_supervisor.DynamicSupervisorAgent" -> "SelfModifyingSupervisor";
      }

.. autoclass:: agents.experiments.dynamic_supervisor_enhanced.SelfModifyingSupervisor
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.experiments.dynamic_supervisor_enhanced.create_agent_management_tools
   agents.experiments.dynamic_supervisor_enhanced.demo_self_modifying_supervisor

.. py:function:: create_agent_management_tools(supervisor_instance) -> Any

   Create tools that allow the supervisor to manage its own agent registry.


   .. autolink-examples:: create_agent_management_tools
      :collapse:

.. py:function:: demo_self_modifying_supervisor()
   :async:




.. rubric:: Related Links

.. autolink-examples:: agents.experiments.dynamic_supervisor_enhanced
   :collapse:
   
.. autolink-skip:: next
