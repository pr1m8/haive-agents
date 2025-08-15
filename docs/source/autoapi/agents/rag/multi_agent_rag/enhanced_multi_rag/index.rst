agents.rag.multi_agent_rag.enhanced_multi_rag
=============================================

.. py:module:: agents.rag.multi_agent_rag.enhanced_multi_rag

.. autoapi-nested-parse::

   Enhanced Multi-Agent RAG with Built-in Compatibility.

   This module demonstrates RAG systems using the compatibility-enhanced multi-agent base,
   providing automatic compatibility checking and adaptation.


   .. autolink-examples:: agents.rag.multi_agent_rag.enhanced_multi_rag
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_multi_rag.enhanced_agent_list
   agents.rag.multi_agent_rag.enhanced_multi_rag.enhanced_base_rag_agent
   agents.rag.multi_agent_rag.enhanced_multi_rag.enhanced_simple_rag_agent
   agents.rag.multi_agent_rag.enhanced_multi_rag.enhanced_simple_rag_answer_agent


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGConditionalAgent
   agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGParallelAgent
   agents.rag.multi_agent_rag.enhanced_multi_rag.EnhancedRAGSequentialAgent
   agents.rag.multi_agent_rag.enhanced_multi_rag.SmartRAGFactory


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_multi_rag.demonstrate_enhanced_rag_compatibility


Module Contents
---------------

.. py:class:: EnhancedRAGConditionalAgent(retrieval_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAgent | None = None, grading_agent: haive.agents.rag.multi_agent_rag.agents.DocumentGradingAgent | None = None, answer_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAnswerAgent | None = None, compatibility_mode: haive.agents.multi.compatibility_enhanced_base.CompatibilityMode = CompatibilityMode.AUTO_FIX, **kwargs)

   Bases: :py:obj:`haive.agents.multi.compatibility_enhanced_base.CompatibilityEnhancedConditionalAgent`


   RAG conditional agent with built-in compatibility checking and smart routing.

   This system checks compatibility at each routing decision and can adapt
   agents on-the-fly if compatibility issues are detected.


   .. autolink-examples:: EnhancedRAGConditionalAgent
      :collapse:

   .. py:method:: _setup_enhanced_conditional_routing()

      Set up conditional routing with compatibility awareness.


      .. autolink-examples:: _setup_enhanced_conditional_routing
         :collapse:


   .. py:attribute:: answer_agent


   .. py:attribute:: grading_agent


   .. py:attribute:: retrieval_agent


.. py:class:: EnhancedRAGParallelAgent(rag_variants: list[EnhancedRAGSequentialAgent] | None = None, compatibility_mode: haive.agents.multi.compatibility_enhanced_base.CompatibilityMode = CompatibilityMode.ADAPTIVE, **kwargs)

   Bases: :py:obj:`haive.agents.multi.compatibility_enhanced_base.CompatibilityEnhancedParallelAgent`


   RAG parallel agent with built-in compatibility checking for consensus building.

   This system runs multiple RAG workflows in parallel and ensures they can
   all work with the same state schema.


   .. autolink-examples:: EnhancedRAGParallelAgent
      :collapse:

.. py:class:: EnhancedRAGSequentialAgent(retrieval_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAgent | None = None, grading_agent: haive.agents.rag.multi_agent_rag.agents.DocumentGradingAgent | None = None, answer_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAnswerAgent | None = None, compatibility_mode: haive.agents.multi.compatibility_enhanced_base.CompatibilityMode = CompatibilityMode.ADAPTIVE, **kwargs)

   Bases: :py:obj:`haive.agents.multi.compatibility_enhanced_base.CompatibilityEnhancedSequentialAgent`


   RAG sequential agent with built-in compatibility checking.

   This system automatically validates that retrieval -> grading -> generation
   agents are compatible and applies adapters if needed.


   .. autolink-examples:: EnhancedRAGSequentialAgent
      :collapse:

.. py:class:: SmartRAGFactory

   Factory for creating RAG systems with automatic compatibility management.

   This factory analyzes the provided agents and creates the most appropriate
   multi-agent structure with optimal compatibility settings.


   .. autolink-examples:: SmartRAGFactory
      :collapse:

   .. py:method:: create_optimal_rag_system(agents: list[Any], documents: list[langchain_core.documents.Document] | None = None, preferred_mode: str | None = None, compatibility_mode: haive.agents.multi.compatibility_enhanced_base.CompatibilityMode = CompatibilityMode.ADAPTIVE) -> haive.agents.multi.compatibility_enhanced_base.CompatibilityEnhancedMultiAgent
      :staticmethod:


      Create an optimal RAG system based on provided agents.

      :param agents: List of agents to include
      :param documents: Optional documents for RAG agents
      :param preferred_mode: Preferred execution mode ("sequential", "conditional", "parallel")
      :param compatibility_mode: How to handle compatibility issues

      :returns: Optimally configured RAG system with compatibility checking


      .. autolink-examples:: create_optimal_rag_system
         :collapse:


   .. py:method:: create_safe_rag_system(documents: list[langchain_core.documents.Document] | None = None, include_grading: bool = True, use_iterative_grading: bool = False, compatibility_mode: haive.agents.multi.compatibility_enhanced_base.CompatibilityMode = CompatibilityMode.STRICT) -> EnhancedRAGSequentialAgent
      :staticmethod:


      Create a safe RAG system with strict compatibility checking.

      This method creates a RAG system that is guaranteed to be compatible
      or will fail with clear error messages.


      .. autolink-examples:: create_safe_rag_system
         :collapse:


.. py:function:: demonstrate_enhanced_rag_compatibility() -> None

   Demonstrate the enhanced RAG system with built-in compatibility checking.


   .. autolink-examples:: demonstrate_enhanced_rag_compatibility
      :collapse:

.. py:data:: enhanced_agent_list

.. py:data:: enhanced_base_rag_agent

.. py:data:: enhanced_simple_rag_agent

.. py:data:: enhanced_simple_rag_answer_agent

