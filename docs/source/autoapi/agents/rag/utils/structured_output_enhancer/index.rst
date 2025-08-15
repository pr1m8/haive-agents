agents.rag.utils.structured_output_enhancer
===========================================

.. py:module:: agents.rag.utils.structured_output_enhancer

.. autoapi-nested-parse::

   Structured Output Enhancer for RAG Agents.

   from typing import Any, Dict
   This utility enables any agent to be enhanced with structured output by appending
   a SimpleAgent with the appropriate prompt template and Pydantic model. This follows
   the pattern of keeping prompts focused on generation while parsers handle structure.


   .. autolink-examples:: agents.rag.utils.structured_output_enhancer
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.utils.structured_output_enhancer.RAGEnhancementFactory
   agents.rag.utils.structured_output_enhancer.StructuredOutputEnhancer


Functions
---------

.. autoapisummary::

   agents.rag.utils.structured_output_enhancer.create_fusion_enhancer
   agents.rag.utils.structured_output_enhancer.create_hyde_enhancer
   agents.rag.utils.structured_output_enhancer.create_memory_enhancer
   agents.rag.utils.structured_output_enhancer.create_speculative_enhancer
   agents.rag.utils.structured_output_enhancer.demonstrate_enhancement_patterns


Module Contents
---------------

.. py:class:: RAGEnhancementFactory

   Factory for creating enhanced RAG agents with structured output.


   .. autolink-examples:: RAGEnhancementFactory
      :collapse:

   .. py:method:: enhance_simple_rag(llm_config: haive.core.models.llm.base.LLMConfig, enhancement_type: str = 'hyde') -> list[haive.agents.simple.agent.SimpleAgent]
      :staticmethod:


      Create a simple RAG with structured output enhancement.

      :param llm_config: LLM configuration
      :param enhancement_type: Type of enhancement (hyde, fusion, speculative, memory)

      :returns: List of agents forming an enhanced RAG pipeline


      .. autolink-examples:: enhance_simple_rag
         :collapse:


.. py:class:: StructuredOutputEnhancer(output_model: type[pydantic.BaseModel], prompt_style: haive.core.utils.pydantic_utils.base_model_to_prompt.PromptStyle = PromptStyle.DESCRIPTIVE, structured_output_version: str = 'v1')

   Utility for enhancing any agent with structured output capabilities.

   This class provides a clean pattern for appending structured output processing
   to any existing agent, following the principle that prompts focus on generation
   while parsers handle structure.

   .. rubric:: Example

   >>> from haive.agents.rag.models import HyDEResult
   >>>
   >>> # Enhance any agent with HyDE structured output
   >>> enhancer = StructuredOutputEnhancer(HyDEResult)
   >>> structured_agent = enhancer.create_enhancement_agent(
   ...     llm_config=llm_config,
   ...     context_prompt="Based on the retrieved documents, generate a hypothetical document analysis"
   ... )
   >>>
   >>> # Or enhance an existing agent pipeline
   >>> enhanced_pipeline = enhancer.enhance_agent_sequence([base_agent, retrieval_agent], llm_config)

   Initialize the enhancer with a Pydantic output model.

   :param output_model: Pydantic model for structured output
   :param prompt_style: Style for generating format instructions
   :param structured_output_version: v1 (parser-based) or v2 (tool-based)


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StructuredOutputEnhancer
      :collapse:

   .. py:method:: create_enhancement_agent(llm_config: haive.core.models.llm.base.LLMConfig, context_prompt: str, agent_name: str | None = None, include_state_context: bool = True, **engine_kwargs) -> haive.agents.simple.agent.SimpleAgent

      Create a SimpleAgent for structured output enhancement.

      :param llm_config: LLM configuration
      :param context_prompt: Main instruction for what to generate
      :param agent_name: Name for the enhancement agent
      :param include_state_context: Whether to include previous state context
      :param \*\*engine_kwargs: Additional arguments for AugLLMConfig

      :returns: SimpleAgent configured for structured output


      .. autolink-examples:: create_enhancement_agent
         :collapse:


   .. py:method:: create_enhancement_prompt(context_prompt: str, include_state_context: bool = True) -> langchain_core.prompts.ChatPromptTemplate

      Create a prompt template for structured output enhancement.

      :param context_prompt: The main instruction for what to generate
      :param include_state_context: Whether to include previous state context

      :returns: ChatPromptTemplate configured for structured output


      .. autolink-examples:: create_enhancement_prompt
         :collapse:


   .. py:method:: create_format_instructions() -> str

      Generate format instructions for the output model.


      .. autolink-examples:: create_format_instructions
         :collapse:


   .. py:method:: enhance_agent_sequence(agents: list[Any], llm_config: haive.core.models.llm.base.LLMConfig, context_prompt: str | None = None, **kwargs) -> list[Any]

      Enhance a sequence of agents by appending structured output processing.

      :param agents: List of existing agents
      :param llm_config: LLM configuration
      :param context_prompt: Custom context prompt (auto-generated if None)
      :param \*\*kwargs: Additional arguments for the enhancement agent

      :returns: List of agents with structured output enhancement appended


      .. autolink-examples:: enhance_agent_sequence
         :collapse:


   .. py:attribute:: output_model


   .. py:attribute:: prompt_generator


   .. py:attribute:: prompt_style


   .. py:attribute:: structured_output_version
      :value: 'v1'



.. py:function:: create_fusion_enhancer() -> StructuredOutputEnhancer

   Create an enhancer for Fusion RAG structured output.


   .. autolink-examples:: create_fusion_enhancer
      :collapse:

.. py:function:: create_hyde_enhancer() -> StructuredOutputEnhancer

   Create an enhancer for HyDE structured output.


   .. autolink-examples:: create_hyde_enhancer
      :collapse:

.. py:function:: create_memory_enhancer() -> StructuredOutputEnhancer

   Create an enhancer for Memory-aware RAG structured output.


   .. autolink-examples:: create_memory_enhancer
      :collapse:

.. py:function:: create_speculative_enhancer() -> StructuredOutputEnhancer

   Create an enhancer for Speculative RAG structured output.


   .. autolink-examples:: create_speculative_enhancer
      :collapse:

.. py:function:: demonstrate_enhancement_patterns() -> dict[str, Any]

   Demonstrate various enhancement patterns.


   .. autolink-examples:: demonstrate_enhancement_patterns
      :collapse:

