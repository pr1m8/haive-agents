
:py:mod:`agents.multi.sequential.agent`
=======================================

.. py:module:: agents.multi.sequential.agent

Sequential multi-agent implementation for the Haive framework.


.. autolink-examples:: agents.multi.sequential.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.sequential.agent.SequentialMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialMultiAgent {
        node [shape=record];
        "SequentialMultiAgent" [label="SequentialMultiAgent"];
        "haive.agents.multi.base.MultiAgent" -> "SequentialMultiAgent";
      }

.. autoclass:: agents.multi.sequential.agent.SequentialMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.multi.sequential.agent.placeholder_node

.. py:function:: placeholder_node(_state: dict[str, Any])

   Placeholder node that does nothing.


   .. autolink-examples:: placeholder_node
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.multi.sequential.agent
   :collapse:
   
.. autolink-skip:: next
