
:py:mod:`agents.base.typed_agent`
=================================

.. py:module:: agents.base.typed_agent

Typed agent base classes with clear separation of concerns.

This module provides a cleaner agent hierarchy that matches the state schema
hierarchy, with better separation between different types of agents.


.. autolink-examples:: agents.base.typed_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.typed_agent.AdaptiveAgent
   agents.base.typed_agent.BaseAgent
   agents.base.typed_agent.BaseExecutor
   agents.base.typed_agent.DataProcessor
   agents.base.typed_agent.LLMAgent
   agents.base.typed_agent.MetaAgent
   agents.base.typed_agent.ReactiveAgent
   agents.base.typed_agent.ToolExecutor
   agents.base.typed_agent.WorkflowAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveAgent {
        node [shape=record];
        "AdaptiveAgent" [label="AdaptiveAgent"];
        "WorkflowAgent" -> "AdaptiveAgent";
      }

.. autoclass:: agents.base.typed_agent.AdaptiveAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BaseAgent {
        node [shape=record];
        "BaseAgent" [label="BaseAgent"];
        "BaseExecutor[haive.core.schema.base_state_schemas.AgentState]" -> "BaseAgent";
      }

.. autoclass:: agents.base.typed_agent.BaseAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseExecutor:

   .. graphviz::
      :align: center

      digraph inheritance_BaseExecutor {
        node [shape=record];
        "BaseExecutor" [label="BaseExecutor"];
        "abc.ABC" -> "BaseExecutor";
        "Generic[TState]" -> "BaseExecutor";
      }

.. autoclass:: agents.base.typed_agent.BaseExecutor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DataProcessor:

   .. graphviz::
      :align: center

      digraph inheritance_DataProcessor {
        node [shape=record];
        "DataProcessor" [label="DataProcessor"];
        "BaseExecutor[haive.core.schema.base_state_schemas.DataProcessingState]" -> "DataProcessor";
      }

.. autoclass:: agents.base.typed_agent.DataProcessor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LLMAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LLMAgent {
        node [shape=record];
        "LLMAgent" [label="LLMAgent"];
        "BaseAgent" -> "LLMAgent";
      }

.. autoclass:: agents.base.typed_agent.LLMAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MetaAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MetaAgent {
        node [shape=record];
        "MetaAgent" [label="MetaAgent"];
        "WorkflowAgent" -> "MetaAgent";
      }

.. autoclass:: agents.base.typed_agent.MetaAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactiveAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactiveAgent {
        node [shape=record];
        "ReactiveAgent" [label="ReactiveAgent"];
        "LLMAgent" -> "ReactiveAgent";
      }

.. autoclass:: agents.base.typed_agent.ReactiveAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolExecutor:

   .. graphviz::
      :align: center

      digraph inheritance_ToolExecutor {
        node [shape=record];
        "ToolExecutor" [label="ToolExecutor"];
        "BaseExecutor[haive.core.schema.base_state_schemas.ToolExecutorState]" -> "ToolExecutor";
      }

.. autoclass:: agents.base.typed_agent.ToolExecutor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WorkflowAgent:

   .. graphviz::
      :align: center

      digraph inheritance_WorkflowAgent {
        node [shape=record];
        "WorkflowAgent" [label="WorkflowAgent"];
        "BaseAgent" -> "WorkflowAgent";
      }

.. autoclass:: agents.base.typed_agent.WorkflowAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.base.typed_agent.create_agent
   agents.base.typed_agent.create_executor

.. py:function:: create_agent(agent_type: str, name: str, engine: haive.core.engine.base.Engine | None = None, **kwargs) -> BaseAgent

   Factory to create appropriate agent.

   :param agent_type: Type of agent
   :param name: Name for the agent
   :param engine: Primary engine for the agent
   :param \*\*kwargs: Additional arguments

   :returns: Agent instance


   .. autolink-examples:: create_agent
      :collapse:

.. py:function:: create_executor(executor_type: str, name: str, **kwargs) -> BaseExecutor

   Factory to create appropriate executor.

   :param executor_type: Type of executor
   :param name: Name for the executor
   :param \*\*kwargs: Additional arguments

   :returns: Executor instance


   .. autolink-examples:: create_executor
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.base.typed_agent
   :collapse:
   
.. autolink-skip:: next
