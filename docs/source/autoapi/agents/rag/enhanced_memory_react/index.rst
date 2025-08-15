agents.rag.enhanced_memory_react
================================

.. py:module:: agents.rag.enhanced_memory_react

.. autoapi-nested-parse::

   Enhanced Memory RAG with ReAct Pattern.

   RAG system that maintains conversation memory and uses ReAct (Reasoning + Acting)
   pattern for complex multi-step queries requiring reasoning and tool use.


   .. autolink-examples:: agents.rag.enhanced_memory_react
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.enhanced_memory_react.EnhancedResponse
   agents.rag.enhanced_memory_react.MemoryAnalysis
   agents.rag.enhanced_memory_react.MemoryEntry
   agents.rag.enhanced_memory_react.MemoryType
   agents.rag.enhanced_memory_react.ReActStep
   agents.rag.enhanced_memory_react.ReActStepResult


Functions
---------

.. autoapisummary::

   agents.rag.enhanced_memory_react.create_enhanced_memory_react_rag
   agents.rag.enhanced_memory_react.create_memory_react_with_tools
   agents.rag.enhanced_memory_react.create_simple_memory_react_rag
   agents.rag.enhanced_memory_react.get_enhanced_memory_react_io_schema


Module Contents
---------------

.. py:class:: EnhancedResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Enhanced response with memory integration.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedResponse
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: memory_used
      :type:  list[MemoryEntry]
      :value: None



   .. py:attribute:: new_memories
      :type:  list[MemoryEntry]
      :value: None



   .. py:attribute:: reasoning_chain
      :type:  list[ReActStepResult]
      :value: None



.. py:class:: MemoryAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Memory analysis result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryAnalysis
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: memory_gaps
      :type:  list[str]
      :value: None



   .. py:attribute:: relevant_memories
      :type:  list[MemoryEntry]
      :value: None



   .. py:attribute:: temporal_context
      :type:  str
      :value: None



.. py:class:: MemoryEntry(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Memory entry structure.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryEntry
      :collapse:

   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: context_tags
      :type:  list[str]
      :value: None



   .. py:attribute:: memory_type
      :type:  MemoryType
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: timestamp
      :type:  str
      :value: None



.. py:class:: MemoryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of memory.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryType
      :collapse:

   .. py:attribute:: EPISODIC
      :value: 'episodic'



   .. py:attribute:: LONG_TERM
      :value: 'long_term'



   .. py:attribute:: SEMANTIC
      :value: 'semantic'



   .. py:attribute:: SHORT_TERM
      :value: 'short_term'



.. py:class:: ReActStep

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   ReAct pattern steps.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReActStep
      :collapse:

   .. py:attribute:: ACTION
      :value: 'action'



   .. py:attribute:: OBSERVATION
      :value: 'observation'



   .. py:attribute:: REFLECTION
      :value: 'reflection'



   .. py:attribute:: THOUGHT
      :value: 'thought'



.. py:class:: ReActStepResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from a ReAct step.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReActStepResult
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: next_action
      :type:  str | None
      :value: None



   .. py:attribute:: step_type
      :type:  ReActStep
      :value: None



.. py:function:: create_enhanced_memory_react_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Enhanced Memory ReAct RAG') -> haive.agents.chain.ChainAgent

   Create an enhanced memory-aware RAG with ReAct pattern.


   .. autolink-examples:: create_enhanced_memory_react_rag
      :collapse:

.. py:function:: create_memory_react_with_tools(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create memory ReAct RAG with tool integration.


   .. autolink-examples:: create_memory_react_with_tools
      :collapse:

.. py:function:: create_simple_memory_react_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a simplified memory-aware ReAct RAG.


   .. autolink-examples:: create_simple_memory_react_rag
      :collapse:

.. py:function:: get_enhanced_memory_react_io_schema() -> dict[str, list[str]]

   Get I/O schema for enhanced memory ReAct RAG.


   .. autolink-examples:: get_enhanced_memory_react_io_schema
      :collapse:

