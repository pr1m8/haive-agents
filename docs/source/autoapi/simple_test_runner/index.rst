simple_test_runner
==================

.. py:module:: simple_test_runner

.. autoapi-nested-parse::

   Simple Test Runner for Dynamic Supervisor.

   from typing import Any, Dict, List
   This demonstrates the core flow of how dynamic agent addition/removal works
   and how it would integrate with eventual agent building capabilities.


   .. autolink-examples:: simple_test_runner
      :collapse:


Attributes
----------

.. autoapisummary::

   simple_test_runner.console


Classes
-------

.. autoapisummary::

   simple_test_runner.MockAgent
   simple_test_runner.MockEngine
   simple_test_runner.SimpleDynamicSupervisorTest


Functions
---------

.. autoapisummary::

   simple_test_runner.main
   simple_test_runner.run_simple_test
   simple_test_runner.simulate_agent_building_flow


Module Contents
---------------

.. py:class:: MockAgent(name: str, agent_type: Any = 'MockAgent', tools: list[str] | None = None)

   Mock agent for testing.


   .. autolink-examples:: MockAgent
      :collapse:

   .. py:method:: ainvoke(state, config=None)
      :async:


      Mock agent execution.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:attribute:: agent_type
      :value: 'MockAgent'



   .. py:attribute:: engine


   .. py:attribute:: name


   .. py:attribute:: tools
      :value: []



.. py:class:: MockEngine(name: str = 'mock_engine')

   Mock engine for testing without real LLM.


   .. autolink-examples:: MockEngine
      :collapse:

   .. py:method:: ainvoke(messages, config=None)
      :async:


      Mock LLM response for testing.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:attribute:: name
      :value: 'mock_engine'



   .. py:attribute:: tool_routes


   .. py:attribute:: tools
      :value: []



.. py:class:: SimpleDynamicSupervisorTest

   Simplified test of dynamic supervisor capabilities.


   .. autolink-examples:: SimpleDynamicSupervisorTest
      :collapse:

   .. py:method:: execute_agent(agent_name, request)
      :async:


      Execute a specific agent.


      .. autolink-examples:: execute_agent
         :collapse:


   .. py:method:: print_status() -> None

      Print current supervisor status.


      .. autolink-examples:: print_status
         :collapse:


   .. py:method:: register_agent(agent, capability_description, execution_config=None)
      :async:


      Register an agent in the test supervisor.


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: route_request(request)
      :async:


      Simulate routing a request to an agent.


      .. autolink-examples:: route_request
         :collapse:


   .. py:method:: unregister_agent(agent_name)
      :async:


      Remove an agent from the test supervisor.


      .. autolink-examples:: unregister_agent
         :collapse:


   .. py:attribute:: agent_configs


   .. py:attribute:: agents


   .. py:attribute:: choice_options
      :value: ['END']



   .. py:attribute:: execution_history
      :value: []



   .. py:attribute:: routing_decisions
      :value: []



   .. py:attribute:: tool_to_agent_mapping


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

.. py:data:: console

