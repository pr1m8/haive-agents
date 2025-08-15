agents.reasoning_and_critique.self_discover.self_discover_v4
============================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_v4

.. autoapi-nested-parse::

   Self-Discover V4 - Using SimpleAgentV3 and MultiAgent.

   Clean implementation following CLAUDE.md patterns:
   - SimpleAgentV3 for individual agents
   - MultiAgent for orchestration
   - No custom __init__ overrides
   - Proper state handling


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_v4
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_v4.REASONING_MODULES


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_v4.AdaptationResult
   agents.reasoning_and_critique.self_discover.self_discover_v4.AdaptedModule
   agents.reasoning_and_critique.self_discover.self_discover_v4.FinalAnswer
   agents.reasoning_and_critique.self_discover.self_discover_v4.ModuleSelection
   agents.reasoning_and_critique.self_discover.self_discover_v4.ReasoningPlan
   agents.reasoning_and_critique.self_discover.self_discover_v4.ReasoningStep
   agents.reasoning_and_critique.self_discover.self_discover_v4.SelectedModule
   agents.reasoning_and_critique.self_discover.self_discover_v4.SelfDiscoverV4


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_v4.create_adapter
   agents.reasoning_and_critique.self_discover.self_discover_v4.create_executor
   agents.reasoning_and_critique.self_discover.self_discover_v4.create_selector
   agents.reasoning_and_critique.self_discover.self_discover_v4.create_self_discover_v4
   agents.reasoning_and_critique.self_discover.self_discover_v4.create_structurer
   agents.reasoning_and_critique.self_discover.self_discover_v4.main


Module Contents
---------------

.. py:class:: AdaptationResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from the adapter agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptationResult
      :collapse:

   .. py:method:: to_string() -> str

      Convert to string for next agent.


      .. autolink-examples:: to_string
         :collapse:


   .. py:attribute:: adapted_modules
      :type:  list[AdaptedModule]
      :value: None



.. py:class:: AdaptedModule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A module adapted for the specific task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModule
      :collapse:

   .. py:attribute:: adapted_approach
      :type:  str
      :value: None



   .. py:attribute:: module_number
      :type:  int
      :value: None



.. py:class:: FinalAnswer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from the executor agent.

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



   .. py:attribute:: confidence
      :type:  str
      :value: None



   .. py:attribute:: reasoning_process
      :type:  str
      :value: None



.. py:class:: ModuleSelection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from the selector agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleSelection
      :collapse:

   .. py:method:: to_string() -> str

      Convert to string for next agent.


      .. autolink-examples:: to_string
         :collapse:


   .. py:attribute:: selected_modules
      :type:  list[SelectedModule]
      :value: None



.. py:class:: ReasoningPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from the structurer agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningPlan
      :collapse:

   .. py:method:: to_string() -> str

      Convert to string for executor.


      .. autolink-examples:: to_string
         :collapse:


   .. py:attribute:: steps
      :type:  list[ReasoningStep]
      :value: None



.. py:class:: ReasoningStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A step in the reasoning plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStep
      :collapse:

   .. py:attribute:: action
      :type:  str
      :value: None



   .. py:attribute:: modules
      :type:  list[int]
      :value: None



   .. py:attribute:: step
      :type:  int
      :value: None



.. py:class:: SelectedModule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A reasoning module selected for the task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelectedModule
      :collapse:

   .. py:attribute:: explanation
      :type:  str
      :value: None



   .. py:attribute:: module_name
      :type:  str
      :value: None



   .. py:attribute:: module_number
      :type:  int
      :value: None



.. py:class:: SelfDiscoverV4(name: str = 'self_discover_v4', **kwargs)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Self-Discover agent using V4 architecture.

   This is a clean implementation that:
   1. Uses SimpleAgentV3 for all agents
   2. Uses MultiAgent for orchestration
   3. Properly handles state between agents
   4. No custom __init__ overrides

   Initialize with the four agents in sequence.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelfDiscoverV4
      :collapse:

   .. py:method:: prepare_initial_state(task: str, modules: str | None = None) -> dict[str, Any]

      Prepare the initial state for execution.

      :param task: The task to solve
      :param modules: Optional custom modules (defaults to REASONING_MODULES)

      :returns: Dict with initial state for the workflow


      .. autolink-examples:: prepare_initial_state
         :collapse:


   .. py:method:: solve(task: str, modules: str | None = None) -> FinalAnswer
      :async:


      Convenience method to solve a task.

      :param task: The task to solve
      :param modules: Optional custom reasoning modules

      :returns: FinalAnswer with the solution


      .. autolink-examples:: solve
         :collapse:


.. py:function:: create_adapter() -> haive.agents.simple.agent.SimpleAgent

   Create the module adapter agent.


   .. autolink-examples:: create_adapter
      :collapse:

.. py:function:: create_executor() -> haive.agents.simple.agent.SimpleAgent

   Create the plan executor agent.


   .. autolink-examples:: create_executor
      :collapse:

.. py:function:: create_selector() -> haive.agents.simple.agent.SimpleAgent

   Create the module selector agent.


   .. autolink-examples:: create_selector
      :collapse:

.. py:function:: create_self_discover_v4() -> SelfDiscoverV4

   Create a ready-to-use Self-Discover V4 agent.


   .. autolink-examples:: create_self_discover_v4
      :collapse:

.. py:function:: create_structurer() -> haive.agents.simple.agent.SimpleAgent

   Create the plan structurer agent.


   .. autolink-examples:: create_structurer
      :collapse:

.. py:function:: main()
   :async:


   Example of using Self-Discover V4.


   .. autolink-examples:: main
      :collapse:

.. py:data:: REASONING_MODULES
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """1. Critical Thinking: Question assumptions, evaluate evidence
      2. Systems Analysis: Break down complex systems and relationships
      3. Root Cause Analysis: Identify underlying causes
      4. Pattern Recognition: Identify recurring themes and structures
      5. Hypothesis Testing: Formulate and test theories
      6. Cost-Benefit Analysis: Evaluate trade-offs
      7. Risk Assessment: Identify and evaluate risks
      8. Design Thinking: User-centered problem solving
      9. Analogical Reasoning: Draw insights from similar situations
      10. Causal Analysis: Understand cause-effect relationships
      11. Scenario Planning: Consider multiple possibilities
      12. Constraint Analysis: Identify limitations
      13. Optimization: Find best solution within parameters
      14. Data Analysis: Extract insights from data
      15. Process Analysis: Examine workflows
      16. Brainstorming: Generate creative ideas
      17. Prioritization: Rank by importance
      18. Stakeholder Analysis: Consider perspectives
      19. SWOT Analysis: Strengths, weaknesses, opportunities, threats
      20. Competitive Analysis: Understand landscape"""

   .. raw:: html

      </details>



