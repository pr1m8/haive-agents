
:py:mod:`agents.reflection.structured_output`
=============================================

.. py:module:: agents.reflection.structured_output

Structured output reflection agents and examples.

This module provides reflection agents that use structured output models
combined with a post-processing hook pattern for extracting results.


.. autolink-examples:: agents.reflection.structured_output
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reflection.structured_output.ReflectionLoop
   agents.reflection.structured_output.ReflectionResult
   agents.reflection.structured_output.StructuredImprovementAgent
   agents.reflection.structured_output.StructuredReflectionAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionLoop:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionLoop {
        node [shape=record];
        "ReflectionLoop" [label="ReflectionLoop"];
      }

.. autoclass:: agents.reflection.structured_output.ReflectionLoop
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionResult {
        node [shape=record];
        "ReflectionResult" [label="ReflectionResult"];
        "pydantic.BaseModel" -> "ReflectionResult";
      }

.. autopydantic_model:: agents.reflection.structured_output.ReflectionResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StructuredImprovementAgent:

   .. graphviz::
      :align: center

      digraph inheritance_StructuredImprovementAgent {
        node [shape=record];
        "StructuredImprovementAgent" [label="StructuredImprovementAgent"];
      }

.. autoclass:: agents.reflection.structured_output.StructuredImprovementAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StructuredReflectionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_StructuredReflectionAgent {
        node [shape=record];
        "StructuredReflectionAgent" [label="StructuredReflectionAgent"];
      }

.. autoclass:: agents.reflection.structured_output.StructuredReflectionAgent
   :members:
   :undoc-members:
   :show-inheritance:


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



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.structured_output
   :collapse:
   
.. autolink-skip:: next
