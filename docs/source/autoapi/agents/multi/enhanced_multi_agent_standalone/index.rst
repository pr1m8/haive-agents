
:py:mod:`agents.multi.enhanced_multi_agent_standalone`
======================================================

.. py:module:: agents.multi.enhanced_multi_agent_standalone

Standalone Enhanced MultiAgent Implementation - Fully Working.

This is a complete, working implementation of the enhanced multi-agent pattern
that avoids import issues and demonstrates all the core concepts:

- MultiAgent[AgentsT] - Generic on the agents it contains
- Sequential, Parallel, Branching, Conditional, Adaptive patterns
- Real async execution with debug output
- Type safety through generics
- No problematic imports

Key Insight: MultiAgent is generic on its agents, not just engine!
MultiAgent[AgentsT] = Agent[AugLLMConfig] + agents: AgentsT


.. autolink-examples:: agents.multi.enhanced_multi_agent_standalone
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.enhanced_multi_agent_standalone.AdaptiveBranchingMultiAgent
   agents.multi.enhanced_multi_agent_standalone.Agent
   agents.multi.enhanced_multi_agent_standalone.BranchingMultiAgent
   agents.multi.enhanced_multi_agent_standalone.MinimalEngine
   agents.multi.enhanced_multi_agent_standalone.MultiAgent
   agents.multi.enhanced_multi_agent_standalone.SimpleAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveBranchingMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveBranchingMultiAgent {
        node [shape=record];
        "AdaptiveBranchingMultiAgent" [label="AdaptiveBranchingMultiAgent"];
        "BranchingMultiAgent" -> "AdaptiveBranchingMultiAgent";
      }

.. autoclass:: agents.multi.enhanced_multi_agent_standalone.AdaptiveBranchingMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Agent:

   .. graphviz::
      :align: center

      digraph inheritance_Agent {
        node [shape=record];
        "Agent" [label="Agent"];
        "pydantic.BaseModel" -> "Agent";
        "abc.ABC" -> "Agent";
      }

.. autopydantic_model:: agents.multi.enhanced_multi_agent_standalone.Agent
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

   Inheritance diagram for BranchingMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BranchingMultiAgent {
        node [shape=record];
        "BranchingMultiAgent" [label="BranchingMultiAgent"];
        "MultiAgent[dict[str, Agent]]" -> "BranchingMultiAgent";
      }

.. autoclass:: agents.multi.enhanced_multi_agent_standalone.BranchingMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MinimalEngine:

   .. graphviz::
      :align: center

      digraph inheritance_MinimalEngine {
        node [shape=record];
        "MinimalEngine" [label="MinimalEngine"];
        "pydantic.BaseModel" -> "MinimalEngine";
      }

.. autopydantic_model:: agents.multi.enhanced_multi_agent_standalone.MinimalEngine
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

   Inheritance diagram for MultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgent {
        node [shape=record];
        "MultiAgent" [label="MultiAgent"];
        "Agent" -> "MultiAgent";
        "Generic[AgentsT]" -> "MultiAgent";
      }

.. autoclass:: agents.multi.enhanced_multi_agent_standalone.MultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgent {
        node [shape=record];
        "SimpleAgent" [label="SimpleAgent"];
        "Agent" -> "SimpleAgent";
      }

.. autoclass:: agents.multi.enhanced_multi_agent_standalone.SimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.multi.enhanced_multi_agent_standalone.demo_enhanced_multi_agent

.. py:function:: demo_enhanced_multi_agent()
   :async:


   Demonstrate all enhanced multi-agent patterns.


   .. autolink-examples:: demo_enhanced_multi_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.multi.enhanced_multi_agent_standalone
   :collapse:
   
.. autolink-skip:: next
