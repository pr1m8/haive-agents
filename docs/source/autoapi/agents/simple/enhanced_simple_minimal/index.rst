
:py:mod:`agents.simple.enhanced_simple_minimal`
===============================================

.. py:module:: agents.simple.enhanced_simple_minimal

Minimal Enhanced SimpleAgent - showing the pattern in action.

This is the absolute minimal version showing SimpleAgent as Agent[AugLLMConfig].
It's self-contained to avoid import issues.


.. autolink-examples:: agents.simple.enhanced_simple_minimal
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_minimal.Agent
   agents.simple.enhanced_simple_minimal.AugLLMConfig
   agents.simple.enhanced_simple_minimal.Engine
   agents.simple.enhanced_simple_minimal.SimpleAgent
   agents.simple.enhanced_simple_minimal.Workflow


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Agent:

   .. graphviz::
      :align: center

      digraph inheritance_Agent {
        node [shape=record];
        "Agent" [label="Agent"];
        "Workflow" -> "Agent";
        "Generic[EngineT]" -> "Agent";
      }

.. autoclass:: agents.simple.enhanced_simple_minimal.Agent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AugLLMConfig:

   .. graphviz::
      :align: center

      digraph inheritance_AugLLMConfig {
        node [shape=record];
        "AugLLMConfig" [label="AugLLMConfig"];
        "Engine" -> "AugLLMConfig";
      }

.. autoclass:: agents.simple.enhanced_simple_minimal.AugLLMConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Engine:

   .. graphviz::
      :align: center

      digraph inheritance_Engine {
        node [shape=record];
        "Engine" [label="Engine"];
      }

.. autoclass:: agents.simple.enhanced_simple_minimal.Engine
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
        "Agent[AugLLMConfig]" -> "SimpleAgent";
      }

.. autoclass:: agents.simple.enhanced_simple_minimal.SimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Workflow:

   .. graphviz::
      :align: center

      digraph inheritance_Workflow {
        node [shape=record];
        "Workflow" [label="Workflow"];
        "abc.ABC" -> "Workflow";
      }

.. autoclass:: agents.simple.enhanced_simple_minimal.Workflow
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.simple.enhanced_simple_minimal
   :collapse:
   
.. autolink-skip:: next
