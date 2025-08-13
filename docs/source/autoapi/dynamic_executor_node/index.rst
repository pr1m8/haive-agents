
:py:mod:`dynamic_executor_node`
===============================

.. py:module:: dynamic_executor_node

Dynamic Executor Node for Dynamic Supervisor.

This node dynamically executes agents by name, properly handling state extraction
and merging based on the EngineNode/AgentNode patterns.


.. autolink-examples:: dynamic_executor_node
   :collapse:

Classes
-------

.. autoapisummary::

   dynamic_executor_node.DynamicExecutorNode


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicExecutorNode:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicExecutorNode {
        node [shape=record];
        "DynamicExecutorNode" [label="DynamicExecutorNode"];
      }

.. autoclass:: dynamic_executor_node.DynamicExecutorNode
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   dynamic_executor_node.create_dynamic_executor_node

.. py:function:: create_dynamic_executor_node(agent_registry: dict[str, Any]) -> DynamicExecutorNode

   Factory function to create a dynamic executor node.

   :param agent_registry: Dictionary mapping agent names to agent instances

   :returns: DynamicExecutorNode instance


   .. autolink-examples:: create_dynamic_executor_node
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: dynamic_executor_node
   :collapse:
   
.. autolink-skip:: next
