example
=======

.. py:module:: example

.. autoapi-nested-parse::

   Example demonstrating the MultiAgent system.

   from typing import Any
   This example shows how to create and use a multi-agent system
   with different agent types and coordination strategies.


   .. autolink-examples:: example
      :collapse:


Attributes
----------

.. autoapisummary::

   example.logger


Classes
-------

.. autoapisummary::

   example.ResearchAgent
   example.WritingAgent


Functions
---------

.. autoapisummary::

   example.create_parallel_specialist_system
   example.create_research_writing_system
   example.demo_multi_agent_system
   example.save_and_load_demo


Module Contents
---------------

.. py:class:: ResearchAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Agent specialized for research tasks.


   .. autolink-examples:: ResearchAgent
      :collapse:

   .. py:method:: invoke(input_data: dict[str, Any]) -> dict[str, Any]

      Process input and perform research.

      This is a simplified example that just simulates research.


      .. autolink-examples:: invoke
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up the research agent.


      .. autolink-examples:: setup_agent
         :collapse:


.. py:class:: WritingAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Agent specialized for writing tasks.


   .. autolink-examples:: WritingAgent
      :collapse:

   .. py:method:: invoke(input_data: dict[str, Any]) -> dict[str, Any]

      Process input and perform writing.

      This is a simplified example that uses research results if available.


      .. autolink-examples:: invoke
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up the writing agent.


      .. autolink-examples:: setup_agent
         :collapse:


.. py:function:: create_parallel_specialist_system() -> Any

   Create a multi-agent system with multiple specialist agents.

   This would use parallel coordination strategy.

   :returns: MultiAgent system


   .. autolink-examples:: create_parallel_specialist_system
      :collapse:

.. py:function:: create_research_writing_system() -> haive.agents.multi.agent.MultiAgent

   Create a multi-agent system with research and writing agents.

   :returns: MultiAgent system


   .. autolink-examples:: create_research_writing_system
      :collapse:

.. py:function:: demo_multi_agent_system() -> None

   Demonstrate a multi-agent system in action.


   .. autolink-examples:: demo_multi_agent_system
      :collapse:

.. py:function:: save_and_load_demo() -> None

   Demonstrate saving and loading a multi-agent system.


   .. autolink-examples:: save_and_load_demo
      :collapse:

.. py:data:: logger

