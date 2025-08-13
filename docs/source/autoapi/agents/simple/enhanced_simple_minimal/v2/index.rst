
:py:mod:`agents.simple.enhanced_simple_minimal.v2`
==================================================

.. py:module:: agents.simple.enhanced_simple_minimal.v2

Enhanced_Simple_Minimal core module.

This module provides enhanced simple minimal functionality for the Haive framework.

Classes:
    Engine: Engine implementation.
    AugLLMConfig: AugLLMConfig implementation.
    Workflow: Workflow implementation.

Functions:
    execute: Execute functionality.
    execute: Execute functionality.


.. autolink-examples:: agents.simple.enhanced_simple_minimal.v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_minimal.v2.Agent
   agents.simple.enhanced_simple_minimal.v2.AugLLMConfig
   agents.simple.enhanced_simple_minimal.v2.Engine
   agents.simple.enhanced_simple_minimal.v2.SimpleAgent
   agents.simple.enhanced_simple_minimal.v2.Workflow


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

.. autoclass:: agents.simple.enhanced_simple_minimal.v2.Agent
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

.. autoclass:: agents.simple.enhanced_simple_minimal.v2.AugLLMConfig
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

.. autoclass:: agents.simple.enhanced_simple_minimal.v2.Engine
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

.. autoclass:: agents.simple.enhanced_simple_minimal.v2.SimpleAgent
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

.. autoclass:: agents.simple.enhanced_simple_minimal.v2.Workflow
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.simple.enhanced_simple_minimal.v2
   :collapse:
   
.. autolink-skip:: next
