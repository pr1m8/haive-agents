agents.reflection.structured_output
===================================

.. py:module:: agents.reflection.structured_output

.. autoapi-nested-parse::

   Structured output reflection agents and examples.

   This module provides reflection agents that use structured output models
   combined with a post-processing hook pattern for extracting results.


   .. autolink-examples:: agents.reflection.structured_output
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reflection.structured_output.T


Classes
-------

.. autoapisummary::

   agents.reflection.structured_output.ReflectionLoop
   agents.reflection.structured_output.StructuredImprovementAgent
   agents.reflection.structured_output.StructuredReflectionAgent


Functions
---------

.. autoapisummary::

   agents.reflection.structured_output.create_improvement_agent
   agents.reflection.structured_output.create_reflection_agent
   agents.reflection.structured_output.create_reflection_loop
   agents.reflection.structured_output.example_basic_reflection
   agents.reflection.structured_output.example_iterative_reflection
   agents.reflection.structured_output.example_reflection_with_improvement
   agents.reflection.structured_output.extract_structured_output
   agents.reflection.structured_output.main


Module Contents
---------------

.. py:class:: ReflectionLoop(reflector: StructuredReflectionAgent, improver: StructuredImprovementAgent, max_iterations: int = 3, quality_threshold: float = 0.8)

   Manages iterative reflection and improvement process.

   Initialize the reflection loop.

   :param reflector: The reflection agent
   :param improver: The improvement agent
   :param max_iterations: Maximum iterations before stopping
   :param quality_threshold: Quality score to stop iterating


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionLoop
      :collapse:

   .. py:method:: iterate(query: str, initial_response: str) -> dict[str, Any]
      :async:


      Run iterative reflection and improvement.

      :param query: The original query
      :param initial_response: Starting response to improve

      :returns: Dictionary with final response, iterations, and quality progression


      .. autolink-examples:: iterate
         :collapse:


   .. py:attribute:: improver


   .. py:attribute:: max_iterations
      :value: 3



   .. py:attribute:: quality_threshold
      :value: 0.8



   .. py:attribute:: reflector


.. py:class:: StructuredImprovementAgent(name: str = 'improvement_agent', temperature: float = 0.5)

   Agent that improves responses based on reflection feedback.

   Initialize the improvement agent.

   :param name: Name for the agent
   :param temperature: Temperature for LLM generation


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StructuredImprovementAgent
      :collapse:

   .. py:method:: improve(query: str, response: str, reflection: agents.reflection.models.ReflectionResult) -> str
      :async:


      Improve a response based on reflection feedback.

      :param query: The original query
      :param response: The response to improve
      :param reflection: The reflection analysis

      :returns: Improved response text


      .. autolink-examples:: improve
         :collapse:


   .. py:attribute:: agent


   .. py:attribute:: name
      :value: 'improvement_agent'



.. py:class:: StructuredReflectionAgent(name: str = 'reflection_agent', system_prompt: str | None = None, temperature: float = 0.3)

   Agent that performs reflection with structured output extraction.

   Initialize the structured reflection agent.

   :param name: Name for the agent
   :param system_prompt: Custom system prompt (optional)
   :param temperature: Temperature for LLM generation


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StructuredReflectionAgent
      :collapse:

   .. py:method:: reflect(query: str, response: str) -> agents.reflection.models.ReflectionResult | None
      :async:


      Perform reflection analysis on a response.

      :param query: The original query
      :param response: The response to analyze

      :returns: ReflectionResult with structured analysis, or None if extraction fails


      .. autolink-examples:: reflect
         :collapse:


   .. py:attribute:: agent


   .. py:attribute:: name
      :value: 'reflection_agent'



   .. py:attribute:: prompt_template


.. py:function:: create_improvement_agent(name: str = 'improver', temperature: float = 0.5, **kwargs) -> StructuredImprovementAgent

   Create a structured improvement agent.


   .. autolink-examples:: create_improvement_agent
      :collapse:

.. py:function:: create_reflection_agent(name: str = 'reflector', temperature: float = 0.3, **kwargs) -> StructuredReflectionAgent

   Create a structured reflection agent.


   .. autolink-examples:: create_reflection_agent
      :collapse:

.. py:function:: create_reflection_loop(max_iterations: int = 3, quality_threshold: float = 0.8, reflector_name: str = 'reflector', improver_name: str = 'improver') -> ReflectionLoop

   Create a complete reflection loop system.


   .. autolink-examples:: create_reflection_loop
      :collapse:

.. py:function:: example_basic_reflection()
   :async:


   Example: Basic response reflection with structured analysis.


   .. autolink-examples:: example_basic_reflection
      :collapse:

.. py:function:: example_iterative_reflection()
   :async:


   Example: Iterative reflection until quality threshold is met.


   .. autolink-examples:: example_iterative_reflection
      :collapse:

.. py:function:: example_reflection_with_improvement()
   :async:


   Example: Full reflection loop with improvement.


   .. autolink-examples:: example_reflection_with_improvement
      :collapse:

.. py:function:: extract_structured_output(agent_result: dict[str, Any], model_class: type[T]) -> T | None

   Generic post-processing hook to extract structured output from agent results.

   :param agent_result: The dict returned by agent.arun()
   :param model_class: The Pydantic model class to extract

   :returns: Instance of the model class, or None if not found


   .. autolink-examples:: extract_structured_output
      :collapse:

.. py:function:: main()
   :async:


   Run all structured reflection examples.


   .. autolink-examples:: main
      :collapse:

.. py:data:: T

