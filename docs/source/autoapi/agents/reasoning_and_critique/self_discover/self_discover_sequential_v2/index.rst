agents.reasoning_and_critique.self_discover.self_discover_sequential_v2
=======================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2

.. autoapi-nested-parse::

   Self-Discover Sequential Agent V2 - Proper implementation following CLAUDE.md patterns.

   This implementation:
   1. Uses SimpleAgentV3 for enhanced features
   2. No custom __init__ overrides
   3. Uses MultiAgent for sequential composition
   4. Consolidates Pydantic models to avoid conflicts
   5. Follows "no mocks" testing philosophy


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_sequential_v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.DEFAULT_REASONING_MODULES


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.AdaptedModule
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ExecutionStep
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ModuleAdaptationResult
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ModuleSelectionResult
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningExecution
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningStep
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.ReasoningStructure
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.SelectedModule


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_adapter_agent
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_executor_agent
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_selector_agent
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_self_discover_sequential
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.create_structurer_agent
   agents.reasoning_and_critique.self_discover.self_discover_sequential_v2.main


Module Contents
---------------

.. py:class:: AdaptedModule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An adapted version of a reasoning module for a specific task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModule
      :collapse:

   .. py:attribute:: adapted_description
      :type:  str
      :value: None



   .. py:attribute:: application_strategy
      :type:  str
      :value: None



   .. py:attribute:: module_name
      :type:  str
      :value: None



   .. py:attribute:: module_number
      :type:  int
      :value: None



.. py:class:: ExecutionStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A completed step in the reasoning process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionStep
      :collapse:

   .. py:attribute:: conclusion
      :type:  str
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: step_number
      :type:  int
      :value: None



.. py:class:: ModuleAdaptationResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of the module adaptation stage.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleAdaptationResult
      :collapse:

   .. py:method:: format_for_structurer() -> str

      Format adapted modules for the structurer stage.


      .. autolink-examples:: format_for_structurer
         :collapse:


   .. py:attribute:: adapted_modules
      :type:  list[AdaptedModule]
      :value: None



.. py:class:: ModuleSelectionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of the module selection stage.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleSelectionResult
      :collapse:

   .. py:method:: format_for_adapter() -> str

      Format selected modules for the adapter stage.


      .. autolink-examples:: format_for_adapter
         :collapse:


   .. py:method:: validate_modules(modules: list[SelectedModule]) -> list[SelectedModule]
      :classmethod:


      Ensure we have 3-5 modules.


      .. autolink-examples:: validate_modules
         :collapse:


   .. py:attribute:: selected_modules
      :type:  list[SelectedModule]
      :value: None



   .. py:attribute:: selection_rationale
      :type:  str
      :value: None



   .. py:attribute:: task_summary
      :type:  str
      :value: None



.. py:class:: ReasoningExecution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete reasoning execution with all steps and final answer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningExecution
      :collapse:

   .. py:attribute:: completed_steps
      :type:  list[ExecutionStep]
      :value: None



   .. py:attribute:: confidence_level
      :type:  str
      :value: None



   .. py:attribute:: explanation
      :type:  str
      :value: None



   .. py:attribute:: final_answer
      :type:  str
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

   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: expected_output
      :type:  str
      :value: None



   .. py:attribute:: modules_used
      :type:  list[int]
      :value: None



   .. py:attribute:: step_number
      :type:  int
      :value: None



.. py:class:: ReasoningStructure(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A structured reasoning plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStructure
      :collapse:

   .. py:method:: format_for_executor() -> str

      Format reasoning structure for the executor.


      .. autolink-examples:: format_for_executor
         :collapse:


   .. py:method:: validate_steps(steps: list[ReasoningStep]) -> list[ReasoningStep]
      :classmethod:


      Ensure steps are properly numbered.


      .. autolink-examples:: validate_steps
         :collapse:


   .. py:attribute:: steps
      :type:  list[ReasoningStep]
      :value: None



.. py:class:: SelectedModule(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A reasoning module selected for a specific problem.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelectedModule
      :collapse:

   .. py:attribute:: contribution
      :type:  str
      :value: None



   .. py:attribute:: module_name
      :type:  str
      :value: None



   .. py:attribute:: module_number
      :type:  int
      :value: None



   .. py:attribute:: relevance_explanation
      :type:  str
      :value: None



.. py:function:: create_adapter_agent() -> haive.agents.simple.agent.SimpleAgent

   Create the adapter agent with proper configuration.


   .. autolink-examples:: create_adapter_agent
      :collapse:

.. py:function:: create_executor_agent() -> haive.agents.simple.agent.SimpleAgent

   Create the executor agent with proper configuration.


   .. autolink-examples:: create_executor_agent
      :collapse:

.. py:function:: create_selector_agent() -> haive.agents.simple.agent.SimpleAgent

   Create the selector agent with proper configuration.


   .. autolink-examples:: create_selector_agent
      :collapse:

.. py:function:: create_self_discover_sequential() -> haive.agents.multi.agent.MultiAgent

   Create the complete Self-Discover sequential workflow.

   This follows the proper pattern from CLAUDE.md:
   - Uses MultiAgent for composition
   - No custom classes or __init__ overrides
   - Clear sequential execution
   - Proper state handling between agents

   :returns: MultiAgent configured for Self-Discover workflow


   .. autolink-examples:: create_self_discover_sequential
      :collapse:

.. py:function:: create_structurer_agent() -> haive.agents.simple.agent.SimpleAgent

   Create the structurer agent with proper configuration.


   .. autolink-examples:: create_structurer_agent
      :collapse:

.. py:function:: main()
   :async:


   Example of using the Self-Discover sequential agent.


   .. autolink-examples:: main
      :collapse:

.. py:data:: DEFAULT_REASONING_MODULES
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """1. Critical Thinking: Question assumptions, identify biases, evaluate evidence
      2. Systems Analysis: Break down complex systems, identify components and relationships
      3. Root Cause Analysis: Identify underlying causes of problems or phenomena
      4. Stakeholder Analysis: Identify and understand different perspectives and interests
      5. SWOT Analysis: Analyze strengths, weaknesses, opportunities, and threats
      6. Cost-Benefit Analysis: Evaluate trade-offs and resource allocation
      7. Risk Assessment: Identify and evaluate potential risks and mitigation strategies
      8. Design Thinking: User-centered approach to innovation and problem-solving
      9. Analogical Reasoning: Draw insights from similar situations or domains
      10. Causal Analysis: Understand cause-and-effect relationships
      11. Scenario Planning: Consider multiple future possibilities and outcomes
      12. Constraint Analysis: Identify limitations and work within boundaries
      13. Optimization: Find the best solution within given parameters
      14. Pattern Recognition: Identify recurring themes, trends, or structures
      15. Hypothesis Testing: Formulate and test explanatory theories
      16. Brainstorming: Generate creative ideas and solutions
      17. Prioritization: Rank options by importance or impact
      18. Process Analysis: Examine workflows and procedures for improvement
      19. Competitive Analysis: Understand competitive landscape and positioning
      20. Data Analysis: Extract insights from quantitative and qualitative data"""

   .. raw:: html

      </details>



