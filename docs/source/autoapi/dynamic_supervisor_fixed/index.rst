
:py:mod:`dynamic_supervisor_fixed`
==================================

.. py:module:: dynamic_supervisor_fixed

Fixed Dynamic Supervisor with Proper Graph Rebuilding.

This implementation correctly handles dynamic agent addition after compilation
based on BaseGraph2 limitations and requirements.


.. autolink-examples:: dynamic_supervisor_fixed
   :collapse:

Classes
-------

.. autoapisummary::

   dynamic_supervisor_fixed.DynamicSupervisorFixed


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisorFixed:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisorFixed {
        node [shape=record];
        "DynamicSupervisorFixed" [label="DynamicSupervisorFixed"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicSupervisorFixed";
      }

.. autoclass:: dynamic_supervisor_fixed.DynamicSupervisorFixed
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   dynamic_supervisor_fixed.test_dynamic_supervisor

.. py:function:: test_dynamic_supervisor()
   :async:


   Test the fixed dynamic supervisor.


   .. autolink-examples:: test_dynamic_supervisor
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: dynamic_supervisor_fixed
   :collapse:
   
.. autolink-skip:: next
