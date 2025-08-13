
:py:mod:`agents.patterns.hybrid_multi_agent_patterns`
=====================================================

.. py:module:: agents.patterns.hybrid_multi_agent_patterns

Hybrid Multi-Agent Patterns - Advanced compositions using base patterns.

This module demonstrates advanced multi-agent patterns that combine different
agent types and execution modes, using the base agent.py and SimpleAgentV3
patterns as building blocks.

Patterns include:
1. Parallel-then-Sequential workflows
2. Conditional routing with multiple branches
3. Hierarchical agent structures
4. Dynamic agent composition


.. autolink-examples:: agents.patterns.hybrid_multi_agent_patterns
   :collapse:

Classes
-------

.. autoapisummary::

   agents.patterns.hybrid_multi_agent_patterns.AdaptiveMultiAgent
   agents.patterns.hybrid_multi_agent_patterns.CollaborativeMultiAgent
   agents.patterns.hybrid_multi_agent_patterns.HybridMultiAgent
   agents.patterns.hybrid_multi_agent_patterns.ParallelResults
   agents.patterns.hybrid_multi_agent_patterns.TaskClassification


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveMultiAgent {
        node [shape=record];
        "AdaptiveMultiAgent" [label="AdaptiveMultiAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "AdaptiveMultiAgent";
      }

.. autoclass:: agents.patterns.hybrid_multi_agent_patterns.AdaptiveMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CollaborativeMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CollaborativeMultiAgent {
        node [shape=record];
        "CollaborativeMultiAgent" [label="CollaborativeMultiAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "CollaborativeMultiAgent";
      }

.. autoclass:: agents.patterns.hybrid_multi_agent_patterns.CollaborativeMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HybridMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HybridMultiAgent {
        node [shape=record];
        "HybridMultiAgent" [label="HybridMultiAgent"];
        "haive.agents.base.agent.Agent" -> "HybridMultiAgent";
      }

.. autoclass:: agents.patterns.hybrid_multi_agent_patterns.HybridMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelResults:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelResults {
        node [shape=record];
        "ParallelResults" [label="ParallelResults"];
        "pydantic.BaseModel" -> "ParallelResults";
      }

.. autopydantic_model:: agents.patterns.hybrid_multi_agent_patterns.ParallelResults
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

   Inheritance diagram for TaskClassification:

   .. graphviz::
      :align: center

      digraph inheritance_TaskClassification {
        node [shape=record];
        "TaskClassification" [label="TaskClassification"];
        "pydantic.BaseModel" -> "TaskClassification";
      }

.. autopydantic_model:: agents.patterns.hybrid_multi_agent_patterns.TaskClassification
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



Functions
---------

.. autoapisummary::

   agents.patterns.hybrid_multi_agent_patterns.create_adaptive_agent
   agents.patterns.hybrid_multi_agent_patterns.create_collaborative_agent
   agents.patterns.hybrid_multi_agent_patterns.create_hybrid_agent
   agents.patterns.hybrid_multi_agent_patterns.example_adaptive_processing
   agents.patterns.hybrid_multi_agent_patterns.example_collaborative
   agents.patterns.hybrid_multi_agent_patterns.example_hybrid_classify_process

.. py:function:: create_adaptive_agent(name: str = 'adaptive', debug: bool = True) -> AdaptiveMultiAgent

   Create an adaptive multi-agent.


   .. autolink-examples:: create_adaptive_agent
      :collapse:

.. py:function:: create_collaborative_agent(name: str = 'collaborative', collaboration_mode: str = 'consensus', debug: bool = True) -> CollaborativeMultiAgent

   Create a collaborative multi-agent.


   .. autolink-examples:: create_collaborative_agent
      :collapse:

.. py:function:: create_hybrid_agent(name: str = 'hybrid', execution_pattern: str = 'classify_then_process', debug: bool = True) -> HybridMultiAgent

   Create a hybrid multi-agent.


   .. autolink-examples:: create_hybrid_agent
      :collapse:

.. py:function:: example_adaptive_processing()
   :async:


   Example of adaptive processing.


   .. autolink-examples:: example_adaptive_processing
      :collapse:

.. py:function:: example_collaborative()
   :async:


   Example of collaborative multi-agent.


   .. autolink-examples:: example_collaborative
      :collapse:

.. py:function:: example_hybrid_classify_process()
   :async:


   Example of classification-based processing.


   .. autolink-examples:: example_hybrid_classify_process
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.patterns.hybrid_multi_agent_patterns
   :collapse:
   
.. autolink-skip:: next
