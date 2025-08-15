agents.memory.search
====================

.. py:module:: agents.memory.search

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: agents.memory.search
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/memory/search/base/index
   /autoapi/agents/memory/search/deep_research/index
   /autoapi/agents/memory/search/labs/index
   /autoapi/agents/memory/search/pro_search/index
   /autoapi/agents/memory/search/quick_search/index


Classes
-------

.. autoapisummary::

   agents.memory.search.BaseSearchAgent
   agents.memory.search.SearchResponse


Functions
---------

.. autoapisummary::

   agents.memory.search.extract_memory_items
   agents.memory.search.format_search_context
   agents.memory.search.get_response_model
   agents.memory.search.get_search_instructions
   agents.memory.search.get_system_prompt


Package Contents
----------------

.. py:class:: BaseSearchAgent(name: str, engine: haive.core.engine.aug_llm.AugLLMConfig, search_tools: list[langchain_core.tools.Tool] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`, :py:obj:`abc.ABC`


   Abstract base class for all search agents.

   Provides common functionality for memory integration, tool management,
   and structured output formatting for search operations.

   Initialize the search agent.

   :param name: Unique identifier for the agent
   :param engine: LLM configuration for the agent
   :param search_tools: Optional list of search tools to use
   :param \*\*kwargs: Additional arguments passed to parent class


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseSearchAgent
      :collapse:

   .. py:method:: extract_memory_items(query: str, response: str) -> list[dict[str, Any]]

      Extract memory items from search interaction.

      :param query: The search query
      :param response: The search response

      :returns: List of memory items to store


      .. autolink-examples:: extract_memory_items
         :collapse:


   .. py:method:: format_search_context(query: str, context: dict[str, Any]) -> str

      Format search context for the agent.

      :param query: The user's search query
      :param context: Additional context including memory, preferences, etc.

      :returns: Formatted context string for the agent


      .. autolink-examples:: format_search_context
         :collapse:


   .. py:method:: get_response_model() -> type[SearchResponse]
      :abstractmethod:


      Get the structured response model for this search agent.


      .. autolink-examples:: get_response_model
         :collapse:


   .. py:method:: get_search_instructions() -> str
      :abstractmethod:


      Get specific search instructions for this agent type.


      .. autolink-examples:: get_search_instructions
         :collapse:


   .. py:method:: get_system_prompt() -> str
      :abstractmethod:


      Get the system prompt template for this search agent.


      .. autolink-examples:: get_system_prompt
         :collapse:


   .. py:method:: process_search(query: str, context: dict[str, Any] | None = None, save_to_memory: bool = True) -> SearchResponse
      :async:


      Process a search query with memory integration.

      :param query: The search query
      :param context: Optional context including memory and preferences
      :param save_to_memory: Whether to save results to memory

      :returns: Structured search response


      .. autolink-examples:: process_search
         :collapse:


.. py:class:: SearchResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base response model for all search agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchResponse
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: processing_time
      :type:  float
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: response
      :type:  str
      :value: None



   .. py:attribute:: search_type
      :type:  str
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



.. py:function:: extract_memory_items(memory_data: Any) -> list[str]

   Extract memory items from memory data structure.

   :param memory_data: Raw memory data from various sources

   :returns: List of formatted memory items as strings


   .. autolink-examples:: extract_memory_items
      :collapse:

.. py:function:: format_search_context(query: str, context: dict[str, Any]) -> str

   Format search context for agents (module-level utility function).

   :param query: The user's search query
   :param context: Additional context including memory, preferences, etc.

   :returns: Formatted context string for the agent


   .. autolink-examples:: format_search_context
      :collapse:

.. py:function:: get_response_model() -> type[SearchResponse]

   Get the response model for search agents.


   .. autolink-examples:: get_response_model
      :collapse:

.. py:function:: get_search_instructions() -> str

   Get generic search instructions.


   .. autolink-examples:: get_search_instructions
      :collapse:

.. py:function:: get_system_prompt() -> str

   Get generic system prompt for search agents.


   .. autolink-examples:: get_system_prompt
      :collapse:

