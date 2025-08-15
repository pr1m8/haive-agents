agents.supervisor.utils.routing
===============================

.. py:module:: agents.supervisor.utils.routing

.. autoapi-nested-parse::

   Dynamic Routing Engine for Haive Supervisor System.

   Handles intelligent routing decisions using DynamicChoiceModel and LLM-based analysis.
   Provides context-aware agent selection with validation and fallback mechanisms.


   .. autolink-examples:: agents.supervisor.utils.routing
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.supervisor.utils.routing.console
   agents.supervisor.utils.routing.logger


Classes
-------

.. autoapisummary::

   agents.supervisor.utils.routing.BaseRoutingStrategy
   agents.supervisor.utils.routing.DynamicRoutingEngine
   agents.supervisor.utils.routing.LLMRoutingStrategy
   agents.supervisor.utils.routing.RoutingContext
   agents.supervisor.utils.routing.RoutingDecision
   agents.supervisor.utils.routing.RuleBasedRoutingStrategy
   agents.supervisor.utils.routing.TaskClassifier


Module Contents
---------------

.. py:class:: BaseRoutingStrategy

   Bases: :py:obj:`abc.ABC`


   Abstract base for routing strategies.


   .. autolink-examples:: BaseRoutingStrategy
      :collapse:

   .. py:method:: make_routing_decision(context: RoutingContext, available_agents: list[str], agent_capabilities: dict[str, str], config: langchain_core.runnables.RunnableConfig | None = None) -> RoutingDecision
      :abstractmethod:

      :async:


      Make routing decision based on context.


      .. autolink-examples:: make_routing_decision
         :collapse:


.. py:class:: DynamicRoutingEngine(routing_model: haive.core.common.models.dynamic_choice_model.DynamicChoiceModel[str], routing_engine: haive.core.engine.base.InvokableEngine | None = None, routing_strategy: BaseRoutingStrategy | None = None, enable_context_analysis: bool = True)

   Main routing engine that orchestrates routing decisions.

   Handles context extraction, strategy selection, and routing execution
   with comprehensive error handling and fallback mechanisms.

   Initialize routing engine.

   :param routing_model: DynamicChoiceModel for available choices
   :param routing_engine: Engine for LLM-based routing (optional)
   :param routing_strategy: Custom routing strategy (optional)
   :param enable_context_analysis: Whether to perform context analysis


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DynamicRoutingEngine
      :collapse:

   .. py:method:: _create_routing_command(decision: RoutingDecision, state: Any, context: RoutingContext) -> langgraph.types.Command

      Create routing command based on decision.


      .. autolink-examples:: _create_routing_command
         :collapse:


   .. py:method:: _extract_context(state: Any) -> RoutingContext

      Extract routing context from state.


      .. autolink-examples:: _extract_context
         :collapse:


   .. py:method:: print_routing_stats() -> None

      Print routing engine statistics.


      .. autolink-examples:: print_routing_stats
         :collapse:


   .. py:method:: route_request(state: Any, agent_capabilities: dict[str, str], config: langchain_core.runnables.RunnableConfig | None = None) -> langgraph.types.Command
      :async:


      Main routing method.

      :param state: Current graph state
      :param agent_capabilities: Dict of agent capabilities
      :param config: Runnable configuration

      :returns: Command object with routing decision


      .. autolink-examples:: route_request
         :collapse:


   .. py:attribute:: enable_context_analysis
      :value: True



   .. py:attribute:: routing_engine
      :value: None



   .. py:attribute:: routing_model


.. py:class:: LLMRoutingStrategy(routing_engine: haive.core.engine.base.InvokableEngine, routing_model: haive.core.common.models.dynamic_choice_model.DynamicChoiceModel[str])

   Bases: :py:obj:`BaseRoutingStrategy`


   LLM-based routing strategy using structured output.


   .. autolink-examples:: LLMRoutingStrategy
      :collapse:

   .. py:method:: _build_routing_prompt(context: RoutingContext, available_agents: list[str], agent_capabilities: dict[str, str]) -> str

      Build context-aware routing prompt.


      .. autolink-examples:: _build_routing_prompt
         :collapse:


   .. py:method:: _extract_choice_from_response(response: str) -> str

      Extract choice from LLM response if structured output fails.


      .. autolink-examples:: _extract_choice_from_response
         :collapse:


   .. py:method:: _fallback_routing(context: RoutingContext, available_agents: list[str]) -> RoutingDecision

      Fallback routing when LLM fails.


      .. autolink-examples:: _fallback_routing
         :collapse:


   .. py:method:: make_routing_decision(context: RoutingContext, available_agents: list[str], agent_capabilities: dict[str, str], config: langchain_core.runnables.RunnableConfig | None = None) -> RoutingDecision
      :async:


      Make LLM-based routing decision.


      .. autolink-examples:: make_routing_decision
         :collapse:


   .. py:attribute:: routing_engine


   .. py:attribute:: routing_model


.. py:class:: RoutingContext(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Context extracted from state for routing decisions.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RoutingContext
      :collapse:

   .. py:attribute:: conversation_length
      :type:  int
      :value: None



   .. py:attribute:: last_message
      :type:  str
      :value: None



   .. py:attribute:: message_type
      :type:  str
      :value: None



   .. py:attribute:: previous_agent
      :type:  str | None
      :value: None



   .. py:attribute:: task_complexity
      :type:  str
      :value: None



   .. py:attribute:: task_keywords
      :type:  list[str]
      :value: None



.. py:class:: RoutingDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for routing decisions.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RoutingDecision
      :collapse:

   .. py:attribute:: choice
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float | None
      :value: None



   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



.. py:class:: RuleBasedRoutingStrategy(routing_rules: dict[str, str])

   Bases: :py:obj:`BaseRoutingStrategy`


   Rule-based routing strategy for deterministic routing.

   Initialize with routing rules.

   :param routing_rules: Dict mapping keywords to agent names


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RuleBasedRoutingStrategy
      :collapse:

   .. py:method:: make_routing_decision(context: RoutingContext, available_agents: list[str], agent_capabilities: dict[str, str], config: langchain_core.runnables.RunnableConfig | None = None) -> RoutingDecision
      :async:


      Make rule-based routing decision.


      .. autolink-examples:: make_routing_decision
         :collapse:


   .. py:attribute:: routing_rules


.. py:class:: TaskClassifier

   Classifies tasks for better routing decisions.


   .. autolink-examples:: TaskClassifier
      :collapse:

   .. py:method:: classify_task(message: str) -> list[str]
      :classmethod:


      Classify task based on message content.

      :param message: Message to classify

      :returns: List of detected task types


      .. autolink-examples:: classify_task
         :collapse:


   .. py:method:: estimate_complexity(message: str, conversation_length: int) -> str
      :classmethod:


      Estimate task complexity.

      :param message: Message content
      :param conversation_length: Length of conversation

      :returns: Simple/Medium/Complex
      :rtype: Complexity level


      .. autolink-examples:: estimate_complexity
         :collapse:


   .. py:attribute:: TASK_PATTERNS


.. py:data:: console

.. py:data:: logger

