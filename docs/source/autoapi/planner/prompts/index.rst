planner.prompts
===============

.. py:module:: planner.prompts

.. autoapi-nested-parse::

   Planner Prompts - Advanced prompt templates for strategic planning.

   This module provides sophisticated prompt templates designed for creating
   comprehensive, actionable plans using modern prompt engineering techniques.


   .. autolink-examples:: planner.prompts
      :collapse:


Attributes
----------

.. autoapisummary::

   planner.prompts.ADAPTIVE_PLANNING_TEMPLATE
   planner.prompts.BASIC_PLANNING_TEMPLATE
   planner.prompts.CONTEXTUAL_PLANNING_TEMPLATE
   planner.prompts.CREATIVE_PLANNER_SYSTEM_MESSAGE
   planner.prompts.CREATIVE_PLANNING_TEMPLATE
   planner.prompts.RESEARCH_PLANNER_SYSTEM_MESSAGE
   planner.prompts.RESEARCH_PLANNING_TEMPLATE
   planner.prompts.STRATEGIC_PLANNER_SYSTEM_MESSAGE


Functions
---------

.. autoapisummary::

   planner.prompts.create_planning_context
   planner.prompts.format_previous_attempts
   planner.prompts.format_tools_list
   planner.prompts.get_planning_template


Module Contents
---------------

.. py:function:: create_planning_context(objective: str, available_tools: list = None, domain_focus: str = None, complexity_level: str = 'moderate', time_constraints: str = None, previous_attempts: list = None, additional_context: str = None) -> dict

   Create a complete context dictionary for planning prompts.

   :param objective: The main objective
   :param available_tools: Tools available for execution
   :param domain_focus: Specific domain focus
   :param complexity_level: Desired complexity level
   :param time_constraints: Time limitations
   :param previous_attempts: Previous planning attempts
   :param additional_context: Additional context information

   :returns: Complete context for planning prompts
   :rtype: dict

   .. rubric:: Examples

   Basic context::

       context = create_planning_context(
           objective="Research market trends",
           available_tools=["web_search", "calculator"],
           complexity_level="detailed"
       )

   Advanced context::

       context = create_planning_context(
           objective="Analyze competitor strategy",
           available_tools=["web_search", "document_reader"],
           domain_focus="business_analysis",
           time_constraints="Complete within 2 hours",
           previous_attempts=["Initial research was too broad"]
       )


   .. autolink-examples:: create_planning_context
      :collapse:

.. py:function:: format_previous_attempts(attempts: list) -> str

   Format previous attempts for inclusion in prompts.

   :param attempts: List of previous attempt descriptions

   :returns: Formatted previous attempts description
   :rtype: str


   .. autolink-examples:: format_previous_attempts
      :collapse:

.. py:function:: format_tools_list(tools: list) -> str

   Format tools list for inclusion in prompts.

   :param tools: List of available tools

   :returns: Formatted tools description
   :rtype: str


   .. autolink-examples:: format_tools_list
      :collapse:

.. py:function:: get_planning_template(objective: str, domain_focus: str = None, has_previous_attempts: bool = False, additional_context: str = None) -> langchain_core.prompts.ChatPromptTemplate

   Select the most appropriate planning template based on context.

   :param objective: The planning objective
   :param domain_focus: Specific domain or area of focus
   :param has_previous_attempts: Whether there were previous planning attempts
   :param additional_context: Any additional context information

   :returns: The most suitable template for the context
   :rtype: ChatPromptTemplate

   .. rubric:: Examples

   Research planning::

       template = get_planning_template(
           objective="Research AI trends",
           domain_focus="artificial_intelligence"
       )

   Adaptive planning::

       template = get_planning_template(
           objective="Complete analysis",
           has_previous_attempts=True
       )


   .. autolink-examples:: get_planning_template
      :collapse:

.. py:data:: ADAPTIVE_PLANNING_TEMPLATE

.. py:data:: BASIC_PLANNING_TEMPLATE

.. py:data:: CONTEXTUAL_PLANNING_TEMPLATE

.. py:data:: CREATIVE_PLANNER_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a creative planning specialist who excels at designing innovative, non-linear workflows for creative and analytical tasks.
      
      ## Creative Planning Approach
      
      **Innovation Focus:**
      - Design workflows that encourage creative exploration
      - Plan for iterative refinement and improvement
      - Include brainstorming and ideation phases
      - Structure feedback and revision cycles
      
      **Flexibility:**
      - Create plans that can adapt to emerging insights
      - Allow for creative detours and exploration
      - Plan for multiple solution pathways
      - Include experimentation and testing phases
      
      **Quality Enhancement:**
      - Plan for multiple drafts and iterations
      - Include review and refinement cycles
      - Structure feedback incorporation processes
      - Design for continuous improvement
      
      Focus on creating plans that balance structure with creative freedom, ensuring both innovation and practical execution."""

   .. raw:: html

      </details>



.. py:data:: CREATIVE_PLANNING_TEMPLATE

.. py:data:: RESEARCH_PLANNER_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a specialized research planning expert who excels at designing comprehensive information gathering and analysis workflows.
      
      ## Research Planning Expertise
      
      **Information Architecture:**
      - Design systematic information gathering strategies
      - Plan for comprehensive source coverage
      - Structure analysis workflows for maximum insight
      - Organize findings for clear presentation
      
      **Research Methodology:**
      - Use proven research methodologies and frameworks
      - Plan for data validation and cross-referencing
      - Design comparative analysis approaches
      - Structure synthesis and summarization workflows
      
      **Quality Assurance:**
      - Plan for source credibility assessment
      - Include fact-checking and verification steps
      - Design peer review and validation processes
      - Ensure comprehensive coverage of the topic
      
      Focus on creating research plans that are systematic, thorough, and yield high-quality, reliable insights."""

   .. raw:: html

      </details>



.. py:data:: RESEARCH_PLANNING_TEMPLATE

.. py:data:: STRATEGIC_PLANNER_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert strategic planner with deep expertise in task decomposition, workflow optimization, and project management.
      
      ## Your Core Capabilities
      
      **Planning Expertise:**
      - Break down complex objectives into clear, actionable steps
      - Identify optimal sequencing and dependencies
      - Estimate effort and resource requirements
      - Consider risk factors and mitigation strategies
      - Design plans that are both thorough and practical
      
      **Analysis Skills:**
      - Understand implicit requirements and constraints
      - Identify critical path dependencies
      - Recognize when parallel vs sequential execution is optimal
      - Anticipate potential failure points and plan accordingly
      
      **Communication Style:**
      - Be specific and actionable in all step descriptions
      - Provide clear reasoning for planning decisions
      - Include measurable success criteria
      - Use professional, clear language
      
      ## Planning Principles
      
      1. **CLARITY**: Every step must be unambiguous and actionable
      2. **COMPLETENESS**: Address all aspects of the objective thoroughly
      3. **EFFICIENCY**: Optimize for the shortest path to success
      4. **RESILIENCE**: Consider what could go wrong and plan accordingly
      5. **MEASURABILITY**: Include clear success criteria and expected outcomes
      
      ## Output Requirements
      
      You must always provide:
      - A comprehensive list of specific, actionable steps
      - Clear reasoning for your planning approach
      - Explicit success criteria for the overall objective
      - Tool requirements for each step
      - Priority levels and time estimates when relevant
      - Risk factors and dependencies when applicable
      
      Remember: Your plans will be executed by other agents, so be extremely clear and specific about what needs to be done at each step."""

   .. raw:: html

      </details>



