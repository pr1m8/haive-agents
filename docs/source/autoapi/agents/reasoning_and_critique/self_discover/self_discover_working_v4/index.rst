agents.reasoning_and_critique.self_discover.self_discover_working_v4
====================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_working_v4

.. autoapi-nested-parse::

   Self-Discover Working V4 - A working implementation that properly handles agents.

   This version creates a working self-discover implementation using the patterns
   that are known to work in the codebase.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_working_v4
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_working_v4.DEFAULT_MODULES


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_working_v4.AdaptedModules
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.FinalAnswer
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.ModuleSelection
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.ReasoningPlan


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_working_v4.create_self_discover_agents
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.create_self_discover_workflow
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.main
   agents.reasoning_and_critique.self_discover.self_discover_working_v4.solve_with_self_discover


Module Contents
---------------

.. py:class:: AdaptedModules(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from adapter agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModules
      :collapse:

   .. py:attribute:: adapted
      :type:  str
      :value: None



.. py:class:: FinalAnswer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from executor agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FinalAnswer
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: explanation
      :type:  str
      :value: None



.. py:class:: ModuleSelection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from selector agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleSelection
      :collapse:

   .. py:attribute:: modules
      :type:  str
      :value: None



.. py:class:: ReasoningPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from structurer agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningPlan
      :collapse:

   .. py:attribute:: plan
      :type:  str
      :value: None



.. py:function:: create_self_discover_agents()

   Create the four agents for Self-Discover workflow.


   .. autolink-examples:: create_self_discover_agents
      :collapse:

.. py:function:: create_self_discover_workflow()

   Create the Self-Discover multi-agent workflow.


   .. autolink-examples:: create_self_discover_workflow
      :collapse:

.. py:function:: main()
   :async:


   Example of using Self-Discover workflow.


   .. autolink-examples:: main
      :collapse:

.. py:function:: solve_with_self_discover(task: str, modules: str | None = None)
   :async:


   Solve a task using Self-Discover workflow.

   :param task: The task to solve
   :param modules: Optional custom reasoning modules

   :returns: The final answer


   .. autolink-examples:: solve_with_self_discover
      :collapse:

.. py:data:: DEFAULT_MODULES
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """1. Pattern Recognition - Identify patterns and structures
      2. Logical Reasoning - Apply logical thinking
      3. Spatial Analysis - Understand spatial relationships
      4. Mathematical Thinking - Apply mathematical concepts
      5. Critical Analysis - Evaluate and analyze information
      6. Problem Decomposition - Break down complex problems
      7. Hypothesis Testing - Test assumptions
      8. Comparative Analysis - Compare different options
      9. Causal Reasoning - Understand cause and effect
      10. Systems Thinking - See the whole picture"""

   .. raw:: html

      </details>



