example_delegation
==================

.. py:module:: example_delegation

.. autoapi-nested-parse::

   Example delegation tasks following LangGraph tutorial pattern.

   This example demonstrates the Haive Supervisor agent managing specialized
   worker agents for different types of tasks, similar to the LangGraph tutorial.


   .. autolink-examples:: example_delegation
      :collapse:


Attributes
----------

.. autoapisummary::

   example_delegation.console
   example_delegation.logger


Functions
---------

.. autoapisummary::

   example_delegation.create_mock_math_agent
   example_delegation.create_mock_research_agent
   example_delegation.create_mock_writing_agent
   example_delegation.create_supervisor_agent
   example_delegation.main
   example_delegation.test_delegation_flow
   example_delegation.test_dynamic_agent_management


Module Contents
---------------

.. py:function:: create_mock_math_agent() -> haive.agents.simple.agent.SimpleAgent

   Create a mock math agent for testing.


   .. autolink-examples:: create_mock_math_agent
      :collapse:

.. py:function:: create_mock_research_agent() -> haive.agents.simple.agent.SimpleAgent

   Create a mock research agent for testing.


   .. autolink-examples:: create_mock_research_agent
      :collapse:

.. py:function:: create_mock_writing_agent() -> haive.agents.simple.agent.SimpleAgent

   Create a mock writing agent for testing.


   .. autolink-examples:: create_mock_writing_agent
      :collapse:

.. py:function:: create_supervisor_agent() -> haive.agents.supervisor.agent.SupervisorAgent

   Create the supervisor agent.


   .. autolink-examples:: create_supervisor_agent
      :collapse:

.. py:function:: main() -> None

   Main test function.


   .. autolink-examples:: main
      :collapse:

.. py:function:: test_delegation_flow()
   :async:


   Test the delegation flow with various task types.


   .. autolink-examples:: test_delegation_flow
      :collapse:

.. py:function:: test_dynamic_agent_management()
   :async:


   Test dynamic agent registration/removal.


   .. autolink-examples:: test_dynamic_agent_management
      :collapse:

.. py:data:: console

.. py:data:: logger

