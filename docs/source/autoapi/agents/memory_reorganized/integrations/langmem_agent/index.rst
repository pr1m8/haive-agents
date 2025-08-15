agents.memory_reorganized.integrations.langmem_agent
====================================================

.. py:module:: agents.memory_reorganized.integrations.langmem_agent

.. autoapi-nested-parse::

   Agent core module.

   This module provides agent functionality for the Haive framework.

   Classes:
       LTMState: LTMState implementation.
       LTMAgent: LTMAgent implementation.

   Functions:
       extraction_succeeded: Extraction Succeeded functionality.
       has_processing_errors: Has Processing Errors functionality.
       needs_kg_processing: Needs Kg Processing functionality.


   .. autolink-examples:: agents.memory_reorganized.integrations.langmem_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.integrations.langmem_agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.integrations.langmem_agent.LTMAgent
   agents.memory_reorganized.integrations.langmem_agent.LTMState


Functions
---------

.. autoapisummary::

   agents.memory_reorganized.integrations.langmem_agent.extraction_succeeded
   agents.memory_reorganized.integrations.langmem_agent.has_processing_errors
   agents.memory_reorganized.integrations.langmem_agent.needs_categorization
   agents.memory_reorganized.integrations.langmem_agent.needs_consolidation
   agents.memory_reorganized.integrations.langmem_agent.needs_kg_processing
   agents.memory_reorganized.integrations.langmem_agent.needs_tool_activation
   agents.memory_reorganized.integrations.langmem_agent.processing_complete


Module Contents
---------------

.. py:class:: LTMAgent(name: str = 'LTM Agent', llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_kg_processing: bool = True, enable_categorization: bool = True, enable_consolidation: bool = True, enable_reflection: bool = True, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Long-Term Memory Agent with LangMem integration.

   This agent provides comprehensive memory management capabilities including:
   - Memory extraction from conversations using LangMem
   - Knowledge graph processing using Haive KG extraction
   - Memory categorization using TNT taxonomy
   - Memory consolidation and quality improvement
   - Tool-based memory management interface
   - Background reflection processing

   The agent follows Haive patterns with proper conditional edges and state management.

   Initialize LTM agent.

   :param name: Agent name
   :param llm_config: LLM configuration for memory processing
   :param enable_kg_processing: Enable knowledge graph extraction
   :param enable_categorization: Enable memory categorization
   :param enable_consolidation: Enable memory consolidation
   :param enable_reflection: Enable background reflection
   :param \*\*kwargs: Additional Agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LTMAgent
      :collapse:

   .. py:method:: __repr__() -> str


   .. py:method:: _calculate_extraction_quality(memories: list[dict], messages: list) -> float

      Calculate quality score for extracted memories.


      .. autolink-examples:: _calculate_extraction_quality
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build LTM graph with proper conditional edges.

      This is the FIRST PHASE - just memory extraction and basic routing.
      We'll add more nodes incrementally.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: complete_processing_node(state: LTMState) -> dict[str, Any]

      Complete processing (Phase 1 implementation).


      .. autolink-examples:: complete_processing_node
         :collapse:


   .. py:method:: extract_memories_node(state: LTMState) -> dict[str, Any]

      Extract memories using LangMem memory manager (Phase 2 implementation).


      .. autolink-examples:: extract_memories_node
         :collapse:


   .. py:method:: get_processing_summary(state: LTMState) -> dict[str, Any]

      Get summary of processing results.


      .. autolink-examples:: get_processing_summary
         :collapse:


   .. py:method:: handle_errors_node(state: LTMState) -> dict[str, Any]

      Handle processing errors.


      .. autolink-examples:: handle_errors_node
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup LTM agent engines and components.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: enable_categorization
      :type:  bool
      :value: None



   .. py:attribute:: enable_consolidation
      :type:  bool
      :value: None



   .. py:attribute:: enable_kg_processing
      :type:  bool
      :value: None



   .. py:attribute:: enable_reflection
      :type:  bool
      :value: None



   .. py:attribute:: ltm_llm_config
      :type:  haive.core.models.llm.base.LLMConfig | None
      :value: None



.. py:class:: LTMState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   LTM Agent State following Haive patterns.

   This state schema tracks the progression through memory processing stages and
   maintains all necessary data for the LTM workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LTMState
      :collapse:

   .. py:attribute:: categories
      :type:  list[str]
      :value: None



   .. py:attribute:: consolidated_memories
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: enable_categorization
      :type:  bool
      :value: None



   .. py:attribute:: enable_consolidation
      :type:  bool
      :value: None



   .. py:attribute:: enable_kg_processing
      :type:  bool
      :value: None



   .. py:attribute:: enable_reflection
      :type:  bool
      :value: None



   .. py:attribute:: extracted_memories
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: extraction_quality
      :type:  float
      :value: None



   .. py:attribute:: knowledge_graph
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.AnyMessage]
      :value: None



   .. py:attribute:: processing_complete
      :type:  bool
      :value: None



   .. py:attribute:: processing_completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: processing_errors
      :type:  list[str]
      :value: None



   .. py:attribute:: processing_quality
      :type:  float
      :value: None



   .. py:attribute:: processing_stage
      :type:  str
      :value: None



   .. py:attribute:: processing_started_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: reflection_scheduled
      :type:  bool
      :value: None



   .. py:attribute:: tool_calls_needed
      :type:  bool
      :value: None



.. py:function:: extraction_succeeded(state: LTMState) -> bool

   Check if memory extraction succeeded.


   .. autolink-examples:: extraction_succeeded
      :collapse:

.. py:function:: has_processing_errors(state: LTMState) -> bool

   Check if there are critical processing errors.


   .. autolink-examples:: has_processing_errors
      :collapse:

.. py:function:: needs_categorization(state: LTMState) -> bool

   Check if categorization is needed.


   .. autolink-examples:: needs_categorization
      :collapse:

.. py:function:: needs_consolidation(state: LTMState) -> bool

   Check if consolidation is needed.


   .. autolink-examples:: needs_consolidation
      :collapse:

.. py:function:: needs_kg_processing(state: LTMState) -> bool

   Check if KG processing is needed.


   .. autolink-examples:: needs_kg_processing
      :collapse:

.. py:function:: needs_tool_activation(state: LTMState) -> bool

   Check if memory tools should be activated.


   .. autolink-examples:: needs_tool_activation
      :collapse:

.. py:function:: processing_complete(state: LTMState) -> bool

   Check if all processing is complete.


   .. autolink-examples:: processing_complete
      :collapse:

.. py:data:: logger

