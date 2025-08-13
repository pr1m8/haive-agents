
:py:mod:`agents.reasoning_and_critique.self_discover.agent`
===========================================================

.. py:module:: agents.reasoning_and_critique.self_discover.agent

Self-Discover MultiAgent implementation.


.. autolink-examples:: agents.reasoning_and_critique.self_discover.agent
   :collapse:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.agent.create_self_discover_agent
   agents.reasoning_and_critique.self_discover.agent.get_default_modules
   agents.reasoning_and_critique.self_discover.agent.main

.. py:function:: create_self_discover_agent(name: str = 'self_discover') -> haive.agents.multi.agent.MultiAgent

   Create a Self-Discover MultiAgent with the four-stage process.

   :param name: Name for the multi-agent system

   :returns: MultiAgent configured for Self-Discover workflow


   .. autolink-examples:: create_self_discover_agent
      :collapse:

.. py:function:: get_default_modules() -> str

   Get default reasoning modules for Self-Discover process.


   .. autolink-examples:: get_default_modules
      :collapse:

.. py:function:: main()
   :async:


   Example usage of Self-Discover agent.


   .. autolink-examples:: main
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.agent
   :collapse:
   
.. autolink-skip:: next
