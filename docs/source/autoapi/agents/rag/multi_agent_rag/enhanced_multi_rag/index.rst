
:py:mod:`agents.rag.multi_agent_rag.enhanced_multi_rag`
=======================================================

.. py:module:: agents.rag.multi_agent_rag.enhanced_multi_rag

Enhanced Multi-Agent RAG with Built-in Compatibility.

This module demonstrates RAG systems using the compatibility-enhanced multi-agent base,
providing automatic compatibility checking and adaptation.


.. autolink-examples:: agents.rag.multi_agent_rag.enhanced_multi_rag
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGConditionalAgent
   agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGParallelAgent
   agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGSequentialAgent
   agents.rag.multi_agent_rag.enhanced_multi_rag.SmartRAGFactory


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedRAGConditionalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedRAGConditionalAgent {
        node [shape=record];
        "EnhancedRAGConditionalAgent" [label="EnhancedRAGConditionalAgent"];
        "haive.agents.multi.compatibility_enhanced_base.CompatibilityEnhancedConditionalAgent" -> "EnhancedRAGConditionalAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGConditionalAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedRAGParallelAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedRAGParallelAgent {
        node [shape=record];
        "EnhancedRAGParallelAgent" [label="EnhancedRAGParallelAgent"];
        "haive.agents.multi.compatibility_enhanced_base.CompatibilityEnhancedParallelAgent" -> "EnhancedRAGParallelAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGParallelAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedRAGSequentialAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedRAGSequentialAgent {
        node [shape=record];
        "EnhancedRAGSequentialAgent" [label="EnhancedRAGSequentialAgent"];
        "haive.agents.multi.compatibility_enhanced_base.CompatibilityEnhancedSequentialAgent" -> "EnhancedRAGSequentialAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGSequentialAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SmartRAGFactory:

   .. graphviz::
      :align: center

      digraph inheritance_SmartRAGFactory {
        node [shape=record];
        "SmartRAGFactory" [label="SmartRAGFactory"];
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_multi_rag.SmartRAGFactory
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_multi_rag.demonstrate_enhanced_rag_compatibility

.. py:function:: demonstrate_enhanced_rag_compatibility() -> None

   Demonstrate the enhanced RAG system with built-in compatibility checking.


   .. autolink-examples:: demonstrate_enhanced_rag_compatibility
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.enhanced_multi_rag
   :collapse:
   
.. autolink-skip:: next
