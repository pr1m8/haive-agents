
:py:mod:`simple_test_runner`
============================

.. py:module:: simple_test_runner

Simple Test Runner for Dynamic Supervisor.

from typing import Any, Dict, List
This demonstrates the core flow of how dynamic agent addition/removal works
and how it would integrate with eventual agent building capabilities.


.. autolink-examples:: simple_test_runner
   :collapse:

Classes
-------

.. autoapisummary::

   simple_test_runner.MockAgent
   simple_test_runner.MockEngine
   simple_test_runner.SimpleDynamicSupervisorTest


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MockAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MockAgent {
        node [shape=record];
        "MockAgent" [label="MockAgent"];
      }

.. autoclass:: simple_test_runner.MockAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MockEngine:

   .. graphviz::
      :align: center

      digraph inheritance_MockEngine {
        node [shape=record];
        "MockEngine" [label="MockEngine"];
      }

.. autoclass:: simple_test_runner.MockEngine
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleDynamicSupervisorTest:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleDynamicSupervisorTest {
        node [shape=record];
        "SimpleDynamicSupervisorTest" [label="SimpleDynamicSupervisorTest"];
      }

.. autoclass:: simple_test_runner.SimpleDynamicSupervisorTest
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   simple_test_runner.main
   simple_test_runner.run_simple_test
   simple_test_runner.simulate_agent_building_flow

.. py:function:: main()
   :async:


   Run all test scenarios.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_simple_test()
   :async:


   Run the simple test scenario.


   .. autolink-examples:: run_simple_test
      :collapse:

.. py:function:: simulate_agent_building_flow()
   :async:


   Simulate how eventual agent building would work.


   .. autolink-examples:: simulate_agent_building_flow
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: simple_test_runner
   :collapse:
   
.. autolink-skip:: next
