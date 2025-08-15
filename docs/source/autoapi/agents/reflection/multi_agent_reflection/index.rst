agents.reflection.multi_agent_reflection
========================================

.. py:module:: agents.reflection.multi_agent_reflection

.. autoapi-nested-parse::

   Multi-agent reflection pattern using sequential coordination.

   This module implements reflection patterns using the new multi-agent system.
   It creates a sequential workflow where:
   1. ReactAgent performs initial reasoning and action
   2. SimpleAgent performs reflection using message transformer post-hooks

   The reflection flow follows the pattern discovered in project documentation:
   Main Agent → Response → Convert to prompt partial → Message Transform → Reflection


   .. autolink-examples:: agents.reflection.multi_agent_reflection
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reflection.multi_agent_reflection.logger


Classes
-------

.. autoapisummary::

   agents.reflection.multi_agent_reflection.MultiAgentReflection
   agents.reflection.multi_agent_reflection.ReflectionGrade
   agents.reflection.multi_agent_reflection.ReflectionResult


Functions
---------

.. autoapisummary::

   agents.reflection.multi_agent_reflection.create_full_reflection_system
   agents.reflection.multi_agent_reflection.create_simple_reflection_system


Module Contents
---------------

.. py:class:: MultiAgentReflection(name: str = 'reflection_system', engine_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, tools: list[langchain_core.tools.Tool] | None = None, include_improvement: bool = False, reflection_temperature: float = 0.3, main_temperature: float = 0.7)

   Multi-agent reflection system using sequential coordination.

   This class creates a coordinated reflection workflow:
   1. ReactAgent processes the initial request
   2. Reflection agent analyzes and grades the response
   3. Optional improvement agent creates enhanced response

   The pattern follows the documented message transformer post-hook approach:
   Main Agent → Response → GradingResult → Convert to prompt partial →
   Message Transform → Reflection Agent (with grade in prompt context)

   Initialize the multi-agent reflection system.

   :param name: Name for the multi-agent system
   :param engine_config: Base engine configuration (will be customized per agent)
   :param tools: Tools available to the main ReactAgent
   :param include_improvement: Whether to include an improvement agent
   :param reflection_temperature: Temperature for reflection agents (lower for consistency)
   :param main_temperature: Temperature for main agent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MultiAgentReflection
      :collapse:

   .. py:method:: _create_improvement_prompt(original_task: str, original_response: str, reflection_grade: ReflectionGrade) -> str

      Create prompt for improvement based on reflection.


      .. autolink-examples:: _create_improvement_prompt
         :collapse:


   .. py:method:: _create_reflection_prompt(original_task: str, agent_response: str, transformed_conversation: list[langchain_core.messages.BaseMessage]) -> str

      Create the reflection prompt using transformed conversation context.

      This follows the pattern: structured data flows through prompt configuration,
      not through messages directly.


      .. autolink-examples:: _create_reflection_prompt
         :collapse:


   .. py:method:: _extract_insights(reflection_grade: ReflectionGrade) -> str

      Extract key insights from the reflection grade.


      .. autolink-examples:: _extract_insights
         :collapse:


   .. py:method:: _transform_messages_for_reflection(messages: list[langchain_core.messages.BaseMessage]) -> list[langchain_core.messages.BaseMessage]

      Simple message transformation for reflection analysis.

      Converts AI messages to human perspective for better reflection analysis.
      This implements a simplified version of the AI_TO_HUMAN transformation.


      .. autolink-examples:: _transform_messages_for_reflection
         :collapse:


   .. py:method:: reflect_on_task(task: str, debug: bool = False) -> ReflectionResult
      :async:


      Perform reflection on a task using the multi-agent system.

      :param task: The task to process and reflect on
      :param debug: Whether to enable debug output

      :returns: ReflectionResult with original response, reflection, and optional improvement


      .. autolink-examples:: reflect_on_task
         :collapse:


   .. py:attribute:: improvement_agent
      :value: None



   .. py:attribute:: include_improvement
      :value: False



   .. py:attribute:: main_agent


   .. py:attribute:: multi_agent


   .. py:attribute:: name
      :value: 'reflection_system'



   .. py:attribute:: reflection_agent


.. py:class:: ReflectionGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for reflection grading.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionGrade
      :collapse:

   .. py:attribute:: action_appropriateness
      :type:  int
      :value: None



   .. py:attribute:: improvements
      :type:  list[str]
      :value: None



   .. py:attribute:: overall_assessment
      :type:  str
      :value: None



   .. py:attribute:: quality_score
      :type:  int
      :value: None



   .. py:attribute:: reasoning_clarity
      :type:  int
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: None



.. py:class:: ReflectionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from the reflection multi-agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionResult
      :collapse:

   .. py:attribute:: improved_response
      :type:  str | None
      :value: None



   .. py:attribute:: initial_response
      :type:  str
      :value: None



   .. py:attribute:: reflection_grade
      :type:  ReflectionGrade
      :value: None



   .. py:attribute:: reflection_insights
      :type:  str
      :value: None



.. py:function:: create_full_reflection_system(tools: list[langchain_core.tools.Tool] | None = None, engine_config: haive.core.engine.aug_llm.AugLLMConfig | None = None) -> MultiAgentReflection

   Create a full reflection system with ReactAgent + ReflectionAgent + ImprovementAgent.

   :param tools: Tools for the ReactAgent
   :param engine_config: Base engine configuration

   :returns: MultiAgentReflection system with improvement capability


   .. autolink-examples:: create_full_reflection_system
      :collapse:

.. py:function:: create_simple_reflection_system(tools: list[langchain_core.tools.Tool] | None = None, engine_config: haive.core.engine.aug_llm.AugLLMConfig | None = None) -> MultiAgentReflection

   Create a simple reflection system with ReactAgent + ReflectionAgent.

   :param tools: Tools for the ReactAgent
   :param engine_config: Base engine configuration

   :returns: MultiAgentReflection system ready for use


   .. autolink-examples:: create_simple_reflection_system
      :collapse:

.. py:data:: logger

