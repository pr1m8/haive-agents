agent_v4
========

.. py:module:: agent_v4

.. autoapi-nested-parse::

   ReactAgent V4 - Simple loop pattern with proper inheritance.

   Minimal ReactAgent that:
   1. Inherits properly from SimpleAgentV3
   2. Implements tool_node back to agent_node loop
   3. No fancy features, just the core pattern


   .. autolink-examples:: agent_v4
      :collapse:


Attributes
----------

.. autoapisummary::

   agent_v4.logger


Classes
-------

.. autoapisummary::

   agent_v4.ReactAgentV4


Module Contents
---------------

.. py:class:: ReactAgentV4

   Bases: :py:obj:`SimpleAgentV3`


   ReactAgent with simple looping behavior.

   Inherits all SimpleAgentV3 features and modifies graph to loop:
   - tool_node goes back to agent_node (not END)
   - parse_output goes back to agent_node (not END)


   .. autolink-examples:: ReactAgentV4
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with ReAct looping pattern.


      .. autolink-examples:: build_graph
         :collapse:


.. py:data:: logger

