agents.memory_reorganized.search.quick_search.agent
===================================================

.. py:module:: agents.memory_reorganized.search.quick_search.agent

.. autoapi-nested-parse::

   Quick Search Agent implementation.

   Provides fast, basic search responses optimized for speed and concise answers. Similar
   to Perplexity's Quick Search feature.


   .. autolink-examples:: agents.memory_reorganized.search.quick_search.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.search.quick_search.agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.search.quick_search.agent.QuickSearchAgent


Module Contents
---------------

.. py:class:: QuickSearchAgent(name: str = 'quick_search_agent', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, search_tools: list[langchain_core.tools.Tool] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.memory.search.base.BaseSearchAgent`


   Agent for fast, basic search responses.

   Optimized for speed and concise answers. Provides quick factual responses
   without deep research or complex analysis.

   Features:
   - Fast response times (< 2 seconds target)
   - Concise, direct answers
   - Basic source attribution
   - Memory integration for context
   - Key extraction

   .. rubric:: Examples

   Basic usage::

       agent = QuickSearchAgent(
           name="quick_search",
           engine=AugLLMConfig(temperature=0.1)
       )

       response = await agent.process_search("What is the capital of France?")
       print(response.response)  # "The capital of France is Paris..."

   With custom configuration::

       agent = QuickSearchAgent(
           name="quick_search",
           engine=AugLLMConfig(
               temperature=0.0,  # Deterministic for facts
               max_tokens=150    # Keep responses short
           )
       )

   Initialize the Quick Search Agent.

   :param name: Agent identifier
   :param engine: LLM configuration (defaults to optimized settings)
   :param search_tools: Optional search tools
   :param \*\*kwargs: Additional arguments passed to parent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QuickSearchAgent
      :collapse:

   .. py:method:: batch_search(queries: list[str]) -> list[haive.agents.memory.search.quick_search.models.QuickSearchResponse]
      :async:


      Process multiple quick search queries efficiently.

      :param queries: List of search queries

      :returns: List of quick search responses


      .. autolink-examples:: batch_search
         :collapse:


   .. py:method:: determine_answer_type(query: str) -> str

      Determine the type of answer needed.

      :param query: The search query

      :returns: Answer type classification


      .. autolink-examples:: determine_answer_type
         :collapse:


   .. py:method:: extract_keywords(query: str) -> list[str]

      Extract key terms from the search query.

      :param query: The search query

      :returns: List of key terms


      .. autolink-examples:: extract_keywords
         :collapse:


   .. py:method:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

      Get the response model for quick search.


      .. autolink-examples:: get_response_model
         :collapse:


   .. py:method:: get_search_instructions() -> str

      Get specific search instructions for quick search.


      .. autolink-examples:: get_search_instructions
         :collapse:


   .. py:method:: get_system_prompt() -> str

      Get the system prompt for quick search operations.


      .. autolink-examples:: get_system_prompt
         :collapse:


   .. py:method:: process_search(query: str, context: dict[str, Any] | None = None, save_to_memory: bool = True) -> haive.agents.memory.search.quick_search.models.QuickSearchResponse
      :async:


      Process a quick search query.

      :param query: The search query
      :param context: Optional context
      :param save_to_memory: Whether to save to memory

      :returns: Quick search response


      .. autolink-examples:: process_search
         :collapse:


.. py:data:: logger

