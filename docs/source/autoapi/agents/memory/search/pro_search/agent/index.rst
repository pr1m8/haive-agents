agents.memory.search.pro_search.agent
=====================================

.. py:module:: agents.memory.search.pro_search.agent

.. autoapi-nested-parse::

   Pro Search Agent implementation.

   Provides deep, contextual search with user preferences and advanced reasoning.
   Similar to Perplexity's Pro Search feature that goes deeper and considers user context.


   .. autolink-examples:: agents.memory.search.pro_search.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory.search.pro_search.agent.ProSearchAgent


Functions
---------

.. autoapisummary::

   agents.memory.search.pro_search.agent.extract_contextual_insights
   agents.memory.search.pro_search.agent.generate_follow_up_questions
   agents.memory.search.pro_search.agent.generate_reasoning_steps
   agents.memory.search.pro_search.agent.get_response_model
   agents.memory.search.pro_search.agent.get_search_instructions
   agents.memory.search.pro_search.agent.get_system_prompt
   agents.memory.search.pro_search.agent.refine_query


Module Contents
---------------

.. py:class:: ProSearchAgent(name: str = 'pro_search_agent', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, search_tools: list[langchain_core.tools.Tool] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.memory.search.base.BaseSearchAgent`


   Agent for deep, contextual search with user preferences.

   Provides comprehensive search responses that consider user context,
   preferences, and search history. Performs query refinement and
   multi-step reasoning for more accurate results.

   Features:
   - Query refinement and expansion
   - User preference integration
   - Contextual insights from memory
   - Multi-step reasoning process
   - Follow-up question generation
   - Depth-based search levels

   .. rubric:: Examples

   Basic usage::

       agent = ProSearchAgent(
           name="pro_search",
           engine=AugLLMConfig(temperature=0.3)
       )

       response = await agent.process_search(
           "How can I improve my productivity?",
           context={"domain": "software_development"}
       )

   With custom depth level::

       response = await agent.process_pro_search(
           "What are the best practices for ML deployment?",
           depth_level=4,
           use_preferences=True
       )

   Initialize the Pro Search Agent.

   :param name: Agent identifier
   :param engine: LLM configuration (defaults to optimized settings)
   :param search_tools: Optional search tools
   :param \*\*kwargs: Additional arguments passed to parent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ProSearchAgent
      :collapse:

   .. py:method:: extract_contextual_insights(query: str, context: dict[str, Any]) -> list[haive.agents.memory.search.pro_search.models.ContextualInsight]

      Extract contextual insights from available context.

      :param query: Search query
      :param context: Available context

      :returns: List of contextual insights


      .. autolink-examples:: extract_contextual_insights
         :collapse:


   .. py:method:: generate_follow_up_questions(query: str, response: str, context: dict[str, Any]) -> list[str]

      Generate relevant follow-up questions.

      :param query: Original search query
      :param response: Search response
      :param context: Available context

      :returns: List of follow-up questions


      .. autolink-examples:: generate_follow_up_questions
         :collapse:


   .. py:method:: generate_reasoning_steps(query: str, context: dict[str, Any]) -> list[str]

      Generate reasoning steps for the search process.

      :param query: Search query
      :param context: Available context

      :returns: List of reasoning steps


      .. autolink-examples:: generate_reasoning_steps
         :collapse:


   .. py:method:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

      Get the response model for pro search.


      .. autolink-examples:: get_response_model
         :collapse:


   .. py:method:: get_search_instructions() -> str

      Get specific search instructions for pro search.


      .. autolink-examples:: get_search_instructions
         :collapse:


   .. py:method:: get_system_prompt() -> str

      Get the system prompt for pro search operations.


      .. autolink-examples:: get_system_prompt
         :collapse:


   .. py:method:: process_pro_search(query: str, context: dict[str, Any] | None = None, depth_level: int = 3, use_preferences: bool = True, generate_follow_ups: bool = True, include_reasoning: bool = True, save_to_memory: bool = True) -> haive.agents.memory.search.pro_search.models.ProSearchResponse
      :async:


      Process a pro search query with advanced features.

      :param query: Search query
      :param context: Optional context
      :param depth_level: Search depth (1-5)
      :param use_preferences: Whether to use user preferences
      :param generate_follow_ups: Whether to generate follow-up questions
      :param include_reasoning: Whether to include reasoning steps
      :param save_to_memory: Whether to save to memory

      :returns: Pro search response


      .. autolink-examples:: process_pro_search
         :collapse:


   .. py:method:: process_search(query: str, context: dict[str, Any] | None = None, save_to_memory: bool = True) -> haive.agents.memory.search.pro_search.models.ProSearchResponse
      :async:


      Process a search query with default pro search settings.

      :param query: Search query
      :param context: Optional context
      :param save_to_memory: Whether to save to memory

      :returns: Pro search response


      .. autolink-examples:: process_search
         :collapse:


   .. py:method:: refine_query(query: str, context: dict[str, Any]) -> haive.agents.memory.search.pro_search.models.SearchRefinement

      Refine the search query based on context and preferences.

      :param query: Original search query
      :param context: Context including user preferences and history

      :returns: Search refinement with improved query


      .. autolink-examples:: refine_query
         :collapse:


.. py:function:: extract_contextual_insights(content: str, context: dict[str, Any]) -> list[haive.agents.memory.search.pro_search.models.ContextualInsight]

   Extract contextual insights from search content.


   .. autolink-examples:: extract_contextual_insights
      :collapse:

.. py:function:: generate_follow_up_questions(query: str, insights: list[haive.agents.memory.search.pro_search.models.ContextualInsight]) -> list[str]

   Generate follow-up questions based on insights.


   .. autolink-examples:: generate_follow_up_questions
      :collapse:

.. py:function:: generate_reasoning_steps(query: str, refinement: haive.agents.memory.search.pro_search.models.SearchRefinement) -> list[str]

   Generate reasoning steps for complex queries.


   .. autolink-examples:: generate_reasoning_steps
      :collapse:

.. py:function:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

   Get the response model for pro search operations.


   .. autolink-examples:: get_response_model
      :collapse:

.. py:function:: get_search_instructions() -> str

   Get specific search instructions for pro search operations.


   .. autolink-examples:: get_search_instructions
      :collapse:

.. py:function:: get_system_prompt() -> str

   Get the system prompt for pro search operations.


   .. autolink-examples:: get_system_prompt
      :collapse:

.. py:function:: refine_query(query: str, context: dict[str, Any]) -> haive.agents.memory.search.pro_search.models.SearchRefinement

   Refine a query based on context and preferences.


   .. autolink-examples:: refine_query
      :collapse:

