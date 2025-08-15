agents.multi.sequential.agent
=============================

.. py:module:: agents.multi.sequential.agent

.. autoapi-nested-parse::

   Sequential multi-agent implementation for the Haive framework.


   .. autolink-examples:: agents.multi.sequential.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.multi.sequential.agent.logger


Classes
-------

.. autoapisummary::

   agents.multi.sequential.agent.SequentialMultiAgent


Functions
---------

.. autoapisummary::

   agents.multi.sequential.agent.placeholder_node


Module Contents
---------------

.. py:class:: SequentialMultiAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Multi-agent system that executes agents sequentially.

   Each agent runs in order, with the output of one feeding into the next.
   The execution follows a chain pattern: Agent1 -> Agent2 -> ... -> AgentN

   Initialize with sequential coordination mode.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SequentialMultiAgent
      :collapse:

   .. py:method:: _setup_node(state: Any) -> langgraph.types.Command

      Initialize the multi-agent state.


      .. autolink-examples:: _setup_node
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build a sequential execution graph.


      .. autolink-examples:: build_graph
         :collapse:


.. py:function:: placeholder_node(_state: dict[str, Any])

   Placeholder node that does nothing.


   .. autolink-examples:: placeholder_node
      :collapse:

.. py:data:: logger

