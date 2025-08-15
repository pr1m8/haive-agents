agents.memory_v2.react_memory_coordinator
=========================================

.. py:module:: agents.memory_v2.react_memory_coordinator

.. autoapi-nested-parse::

   ReactAgent Memory Coordinator with Tool Integration.

   This implements the ReactAgent version with memory tools as requested:
   - Uses ReactAgent for reasoning and planning
   - Integrates LongTermMemoryAgent as a tool
   - Provides memory search, storage, and analysis capabilities
   - Follows the "get into the react version with the tools" directive

   Architecture:
   - ReactAgent with memory tools for reasoning about memory operations
   - LongTermMemoryAgent tool for persistent memory operations
   - ConversationMemoryAgent tool for conversation context
   - Memory analysis and coordination through ReactAgent reasoning


   .. autolink-examples:: agents.memory_v2.react_memory_coordinator
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.react_memory_coordinator.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.react_memory_coordinator.MemoryCoordinatorConfig
   agents.memory_v2.react_memory_coordinator.ReactMemoryCoordinator


Functions
---------

.. autoapisummary::

   agents.memory_v2.react_memory_coordinator.demo_react_memory_coordinator


Module Contents
---------------

.. py:class:: MemoryCoordinatorConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for ReactMemoryCoordinator.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryCoordinatorConfig
      :collapse:

   .. py:attribute:: auto_extract_memories
      :type:  bool
      :value: None



   .. py:attribute:: conversation_memory_path
      :type:  str
      :value: None



   .. py:attribute:: enable_conversation_memory
      :type:  bool
      :value: None



   .. py:attribute:: enable_long_term_memory
      :type:  bool
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig | None
      :value: None



   .. py:attribute:: long_term_memory_path
      :type:  str
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: temperature
      :type:  float
      :value: None



.. py:class:: ReactMemoryCoordinator(user_id: str, config: MemoryCoordinatorConfig | None = None, name: str = 'react_memory_coordinator')

   ReactAgent-based memory coordinator with tool integration.

   This implements the ReactAgent pattern for memory coordination:
   1. Uses ReactAgent for reasoning about memory operations
   2. Provides memory tools for search, storage, and analysis
   3. Coordinates between different memory types
   4. Enables complex memory reasoning and planning

   Key Features:
   - ReactAgent with memory tools for reasoning
   - Long-term memory search and storage
   - Conversation memory retrieval
   - Memory analysis and insights
   - Cross-memory coordination

   .. rubric:: Examples

   Basic usage::

       coordinator = ReactMemoryCoordinator(user_id="user123")
       await coordinator.initialize()

       # Memory-enhanced conversation with reasoning
       response = await coordinator.run(
           "What do you remember about my work preferences and how should I schedule my week?"
       )

   With custom LLM config::

       config = MemoryCoordinatorConfig(
           llm_config=AzureLLMConfig(deployment_name="gpt-4"),
           temperature=0.3  # Lower temp for more focused reasoning
       )
       coordinator = ReactMemoryCoordinator(
           user_id="user123", config=config)

   Initialize ReactMemoryCoordinator.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactMemoryCoordinator
      :collapse:

   .. py:method:: _create_memory_tools() -> list

      Create memory tools for ReactAgent.


      .. autolink-examples:: _create_memory_tools
         :collapse:


   .. py:method:: _get_system_message() -> str

      Get system message for ReactAgent.


      .. autolink-examples:: _get_system_message
         :collapse:


   .. py:method:: add_conversation_batch(messages: list[langchain_core.messages.BaseMessage]) -> dict[str, Any]
      :async:


      Add a batch of conversation messages to memory.


      .. autolink-examples:: add_conversation_batch
         :collapse:


   .. py:method:: create(user_id: str, llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_all_memory: bool = True, name: str = 'react_memory_coordinator') -> ReactMemoryCoordinator
      :classmethod:


      Factory method to create ReactMemoryCoordinator.


      .. autolink-examples:: create
         :collapse:


   .. py:method:: create_focused(user_id: str, llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'focused_memory_coordinator') -> ReactMemoryCoordinator
      :classmethod:


      Create coordinator optimized for focused reasoning.


      .. autolink-examples:: create_focused
         :collapse:


   .. py:method:: get_comprehensive_memory_summary() -> dict[str, Any]
      :async:


      Get comprehensive summary of all memory systems.


      .. autolink-examples:: get_comprehensive_memory_summary
         :collapse:


   .. py:method:: initialize() -> None
      :async:


      Initialize the ReactAgent and memory agents.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: run(query: str, add_to_conversation: bool = True) -> dict[str, Any]
      :async:


      Run memory-enhanced conversation with ReactAgent reasoning.

      This implements the ReactAgent pattern for memory operations:
      1. ReactAgent reasons about what memory operations are needed
      2. Uses memory tools to search, store, and analyze information
      3. Provides comprehensive response with memory context
      4. Optionally stores the conversation for future reference


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: _initialized
      :value: False



   .. py:attribute:: config


   .. py:attribute:: conversation_memory
      :type:  haive.agents.memory_v2.conversation_memory_agent.ConversationMemoryAgent | None
      :value: None



   .. py:attribute:: long_term_memory
      :type:  haive.agents.memory_v2.long_term_memory_agent.LongTermMemoryAgent | None
      :value: None



   .. py:attribute:: name
      :value: 'react_memory_coordinator'



   .. py:attribute:: react_agent
      :type:  haive.agents.react.agent.ReactAgent | None
      :value: None



   .. py:attribute:: user_id


.. py:function:: demo_react_memory_coordinator()
   :async:


   Demo ReactAgent memory coordinator functionality.


   .. autolink-examples:: demo_react_memory_coordinator
      :collapse:

.. py:data:: logger

