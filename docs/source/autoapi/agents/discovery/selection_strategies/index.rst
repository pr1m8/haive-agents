agents.discovery.selection_strategies
=====================================

.. py:module:: agents.discovery.selection_strategies

.. autoapi-nested-parse::

   Tool selection strategies for dynamic tool selection.

   This module implements various strategies for selecting tools based on
   different criteria and approaches, providing flexibility in how tools
   are chosen for different contexts and use cases.


   .. autolink-examples:: agents.discovery.selection_strategies
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.discovery.selection_strategies.ToolSelectionResult
   agents.discovery.selection_strategies.logger


Classes
-------

.. autoapisummary::

   agents.discovery.selection_strategies.AdaptiveSelectionStrategy
   agents.discovery.selection_strategies.BaseSelectionStrategy
   agents.discovery.selection_strategies.CapabilityBasedStrategy
   agents.discovery.selection_strategies.ContextualSelectionStrategy
   agents.discovery.selection_strategies.EnsembleSelectionStrategy
   agents.discovery.selection_strategies.LearningSelectionStrategy
   agents.discovery.selection_strategies.SemanticSelectionStrategy


Functions
---------

.. autoapisummary::

   agents.discovery.selection_strategies._get_tool_selection_result
   agents.discovery.selection_strategies.create_selection_strategy


Module Contents
---------------

.. py:class:: AdaptiveSelectionStrategy(learning_rate: float = 0.1)

   Bases: :py:obj:`BaseSelectionStrategy`


   Adaptive selection that learns from usage patterns.


   .. autolink-examples:: AdaptiveSelectionStrategy
      :collapse:

   .. py:method:: _calculate_semantic_score(query: str, tool: haive.agents.discovery.semantic_discovery.ComponentMetadata) -> float

      Calculate basic semantic similarity score.


      .. autolink-examples:: _calculate_semantic_score
         :collapse:


   .. py:method:: select_tools(query: str, available_tools: list[haive.agents.discovery.semantic_discovery.ComponentMetadata], context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState, max_tools: int = 5) -> haive.agents.discovery.dynamic_tool_selector.ToolSelectionResult
      :async:


      Select tools using adaptive learning.


      .. autolink-examples:: select_tools
         :collapse:


   .. py:method:: update_performance(tool_name: str, success: bool) -> None

      Update tool performance based on execution results.


      .. autolink-examples:: update_performance
         :collapse:


   .. py:attribute:: learning_rate
      :value: 0.1



   .. py:attribute:: tool_performance
      :type:  dict[str, float]


.. py:class:: BaseSelectionStrategy

   Bases: :py:obj:`abc.ABC`


   Base class for tool selection strategies.


   .. autolink-examples:: BaseSelectionStrategy
      :collapse:

   .. py:method:: select_tools(query: str, available_tools: list[haive.agents.discovery.semantic_discovery.ComponentMetadata], context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState, max_tools: int = 5) -> haive.agents.discovery.dynamic_tool_selector.ToolSelectionResult
      :abstractmethod:

      :async:


      Select tools based on strategy.


      .. autolink-examples:: select_tools
         :collapse:


.. py:class:: CapabilityBasedStrategy(capability_weights: dict[str, float] | None = None)

   Bases: :py:obj:`BaseSelectionStrategy`


   Capability-based tool selection.


   .. autolink-examples:: CapabilityBasedStrategy
      :collapse:

   .. py:method:: _calculate_capability_match(required: list[str], available: list[str]) -> float

      Calculate capability match score.


      .. autolink-examples:: _calculate_capability_match
         :collapse:


   .. py:method:: _extract_capabilities_from_query(query: str) -> list[str]

      Extract required capabilities from query.


      .. autolink-examples:: _extract_capabilities_from_query
         :collapse:


   .. py:method:: select_tools(query: str, available_tools: list[haive.agents.discovery.semantic_discovery.ComponentMetadata], context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState, max_tools: int = 5) -> haive.agents.discovery.dynamic_tool_selector.ToolSelectionResult
      :async:


      Select tools based on capability matching.


      .. autolink-examples:: select_tools
         :collapse:


   .. py:attribute:: capability_weights


.. py:class:: ContextualSelectionStrategy(context_weight: float = 0.3)

   Bases: :py:obj:`BaseSelectionStrategy`


   Context-aware tool selection considering conversation history.


   .. autolink-examples:: ContextualSelectionStrategy
      :collapse:

   .. py:method:: _calculate_context_relevance(tool: haive.agents.discovery.semantic_discovery.ComponentMetadata, context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState) -> float

      Calculate how relevant tool is to current context.


      .. autolink-examples:: _calculate_context_relevance
         :collapse:


   .. py:method:: _calculate_history_relevance(tool: haive.agents.discovery.semantic_discovery.ComponentMetadata, context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState) -> float

      Calculate tool relevance based on conversation history.


      .. autolink-examples:: _calculate_history_relevance
         :collapse:


   .. py:method:: _calculate_semantic_score(query: str, tool: haive.agents.discovery.semantic_discovery.ComponentMetadata) -> float

      Calculate semantic similarity.


      .. autolink-examples:: _calculate_semantic_score
         :collapse:


   .. py:method:: select_tools(query: str, available_tools: list[haive.agents.discovery.semantic_discovery.ComponentMetadata], context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState, max_tools: int = 5) -> haive.agents.discovery.dynamic_tool_selector.ToolSelectionResult
      :async:


      Select tools considering full context.


      .. autolink-examples:: select_tools
         :collapse:


   .. py:attribute:: context_weight
      :value: 0.3



.. py:class:: EnsembleSelectionStrategy(strategies: list[BaseSelectionStrategy] | None = None)

   Bases: :py:obj:`BaseSelectionStrategy`


   Ensemble strategy combining multiple selection approaches.


   .. autolink-examples:: EnsembleSelectionStrategy
      :collapse:

   .. py:method:: select_tools(query: str, available_tools: list[haive.agents.discovery.semantic_discovery.ComponentMetadata], context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState, max_tools: int = 5) -> haive.agents.discovery.dynamic_tool_selector.ToolSelectionResult
      :async:


      Select tools using ensemble of strategies.


      .. autolink-examples:: select_tools
         :collapse:


   .. py:attribute:: strategies


   .. py:attribute:: strategy_weights
      :value: [0.4, 0.3, 0.3]



.. py:class:: LearningSelectionStrategy

   Bases: :py:obj:`BaseSelectionStrategy`


   Selection strategy that learns from user feedback and tool performance.


   .. autolink-examples:: LearningSelectionStrategy
      :collapse:

   .. py:method:: _calculate_base_compatibility(query: str, tool: haive.agents.discovery.semantic_discovery.ComponentMetadata) -> float

      Calculate basic query-tool compatibility.


      .. autolink-examples:: _calculate_base_compatibility
         :collapse:


   .. py:method:: _get_context_learning_score(tool_name: str, context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState) -> float

      Get context-based learning score.


      .. autolink-examples:: _get_context_learning_score
         :collapse:


   .. py:method:: _get_learned_performance(tool_name: str) -> float

      Get learned performance score for tool.


      .. autolink-examples:: _get_learned_performance
         :collapse:


   .. py:method:: add_feedback(tool_name: str, rating: float, context: str, feedback_data: dict[str, Any]) -> None

      Add user feedback for learning.


      .. autolink-examples:: add_feedback
         :collapse:


   .. py:method:: select_tools(query: str, available_tools: list[haive.agents.discovery.semantic_discovery.ComponentMetadata], context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState, max_tools: int = 5) -> haive.agents.discovery.dynamic_tool_selector.ToolSelectionResult
      :async:


      Select tools using learned patterns and feedback.


      .. autolink-examples:: select_tools
         :collapse:


   .. py:attribute:: context_patterns
      :type:  dict[str, list[str]]


   .. py:attribute:: tool_ratings
      :type:  dict[str, list[float]]


   .. py:attribute:: user_feedback
      :type:  dict[str, list[dict[str, Any]]]


.. py:class:: SemanticSelectionStrategy(similarity_threshold: float = 0.7)

   Bases: :py:obj:`BaseSelectionStrategy`


   Semantic similarity-based tool selection.


   .. autolink-examples:: SemanticSelectionStrategy
      :collapse:

   .. py:method:: select_tools(query: str, available_tools: list[haive.agents.discovery.semantic_discovery.ComponentMetadata], context: haive.agents.discovery.dynamic_tool_selector.ContextAwareState, max_tools: int = 5) -> haive.agents.discovery.dynamic_tool_selector.ToolSelectionResult
      :async:


      Select tools based on semantic similarity to query.


      .. autolink-examples:: select_tools
         :collapse:


   .. py:attribute:: similarity_threshold
      :value: 0.7



.. py:function:: _get_tool_selection_result()

   Lazy import of ToolSelectionResult to avoid circular imports.


   .. autolink-examples:: _get_tool_selection_result
      :collapse:

.. py:function:: create_selection_strategy(strategy_name: str, **kwargs) -> BaseSelectionStrategy

   Create a selection strategy by name.


   .. autolink-examples:: create_selection_strategy
      :collapse:

.. py:data:: ToolSelectionResult
   :value: None


.. py:data:: logger

