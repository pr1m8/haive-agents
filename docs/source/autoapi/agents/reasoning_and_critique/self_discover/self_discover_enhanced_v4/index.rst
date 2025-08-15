agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4
=====================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4

.. autoapi-nested-parse::

   Self-Discover Agent Implementation following LangGraph tutorial pattern.

   Based on the official LangGraph Self-Discover tutorial:
   https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/

   This implementation follows the exact pattern from the tutorial with proper
   state management and structured output parsing.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.DEFAULT_REASONING_MODULES


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.AdaptedModulesOutput
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.FinalAnswerOutput
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.ModuleSelectionOutput
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.ReasoningStructureOutput
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverAdapter
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverExecutor
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverSelector
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverState
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.SelfDiscoverStructurer


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.main
   agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4.run_self_discover_workflow


Module Contents
---------------

.. py:class:: AdaptedModulesOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from module adapter - string format.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModulesOutput
      :collapse:

   .. py:attribute:: adapted_modules
      :type:  str
      :value: None



.. py:class:: FinalAnswerOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from final reasoner - string format.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FinalAnswerOutput
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



.. py:class:: ModuleSelectionOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from module selector - string format.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleSelectionOutput
      :collapse:

   .. py:attribute:: selected_modules
      :type:  str
      :value: None



.. py:class:: ReasoningStructureOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from structure creator - string format.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStructureOutput
      :collapse:

   .. py:attribute:: reasoning_structure
      :type:  str
      :value: None



.. py:class:: SelfDiscoverAdapter

   Bases: :py:obj:`SimpleAgentV3`


   Agent that adapts modules to be task-specific.


   .. autolink-examples:: SelfDiscoverAdapter
      :collapse:

   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



.. py:class:: SelfDiscoverExecutor

   Bases: :py:obj:`SimpleAgentV3`


   Agent that executes the reasoning plan.


   .. autolink-examples:: SelfDiscoverExecutor
      :collapse:

   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



.. py:class:: SelfDiscoverSelector

   Bases: :py:obj:`SimpleAgentV3`


   Agent that selects relevant reasoning modules.


   .. autolink-examples:: SelfDiscoverSelector
      :collapse:

   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



.. py:class:: SelfDiscoverState

   Bases: :py:obj:`TypedDict`


   State for Self-Discover workflow following LangGraph tutorial.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelfDiscoverState
      :collapse:

   .. py:attribute:: adapted_modules
      :type:  str | None


   .. py:attribute:: answer
      :type:  str | None


   .. py:attribute:: reasoning_modules
      :type:  str


   .. py:attribute:: reasoning_structure
      :type:  str | None


   .. py:attribute:: selected_modules
      :type:  str | None


   .. py:attribute:: task_description
      :type:  str


.. py:class:: SelfDiscoverStructurer

   Bases: :py:obj:`SimpleAgentV3`


   Agent that creates a structured reasoning plan.


   .. autolink-examples:: SelfDiscoverStructurer
      :collapse:

   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



.. py:function:: main()
   :async:


   Example of using Self-Discover Enhanced V4.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_self_discover_workflow(task: str, modules: str | None = None) -> dict[str, Any]
   :async:


   Run the Self-Discover workflow sequentially.

   :param task: The task to solve
   :param modules: Optional custom reasoning modules

   :returns: Dict containing the final answer and reasoning


   .. autolink-examples:: run_self_discover_workflow
      :collapse:

.. py:data:: DEFAULT_REASONING_MODULES
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """1. Pattern Recognition - Identify patterns, shapes, and structures
      2. Spatial Analysis - Understand spatial relationships and geometry
      3. Logical Reasoning - Apply logical thinking and deduction
      4. Mathematical Analysis - Use mathematical concepts and calculations
      5. Visual Interpretation - Interpret visual information and diagrams
      6. Problem Decomposition - Break complex problems into parts
      7. Critical Thinking - Evaluate information and assumptions
      8. Systems Analysis - Understand systems and relationships
      9. Comparative Analysis - Compare and contrast options
      10. Hypothesis Testing - Form and test hypotheses"""

   .. raw:: html

      </details>



