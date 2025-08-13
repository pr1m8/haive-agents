
:py:mod:`internal_dynamic_supervisor`
=====================================

.. py:module:: internal_dynamic_supervisor

Internal Dynamic Supervisor - Agents Added by Supervisor Decisions.

The supervisor itself decides when to add/remove agents based on requests,
not external management calls.


.. autolink-examples:: internal_dynamic_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   internal_dynamic_supervisor.InternalDynamicSupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for InternalDynamicSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_InternalDynamicSupervisor {
        node [shape=record];
        "InternalDynamicSupervisor" [label="InternalDynamicSupervisor"];
        "haive.agents.multi.base.agent.MultiAgent" -> "InternalDynamicSupervisor";
      }

.. autoclass:: internal_dynamic_supervisor.InternalDynamicSupervisor
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   internal_dynamic_supervisor.test_internal_dynamic

.. py:function:: test_internal_dynamic()
   :async:


   Test the internal dynamic supervisor.


   .. autolink-examples:: test_internal_dynamic
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: internal_dynamic_supervisor
   :collapse:
   
.. autolink-skip:: next
