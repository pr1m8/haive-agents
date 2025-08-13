
:py:mod:`agents.reasoning_and_critique.self_discover.executor.agent`
====================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.executor.agent

Self-Discover Executor Agent implementation.


.. autolink-examples:: agents.reasoning_and_critique.self_discover.executor.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.executor.agent.ExecutionResult
   agents.reasoning_and_critique.self_discover.executor.agent.ExecutorAgent


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionResult {
        node [shape=record];
        "ExecutionResult" [label="ExecutionResult"];
        "pydantic.BaseModel" -> "ExecutionResult";
      }

.. autopydantic_model:: agents.reasoning_and_critique.self_discover.executor.agent.ExecutionResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutorAgent {
        node [shape=record];
        "ExecutorAgent" [label="ExecutorAgent"];
        "haive.agents.simple.SimpleAgent" -> "ExecutorAgent";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.executor.agent.ExecutorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.executor.agent
   :collapse:
   
.. autolink-skip:: next
