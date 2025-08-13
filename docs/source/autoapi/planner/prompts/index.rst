
:py:mod:`planner.prompts`
=========================

.. py:module:: planner.prompts

Planner Prompts - Advanced prompt templates for strategic planning.

This module provides sophisticated prompt templates designed for creating
comprehensive, actionable plans using modern prompt engineering techniques.


.. autolink-examples:: planner.prompts
   :collapse:


Functions
---------

.. autoapisummary::

   planner.prompts.create_planning_context
   planner.prompts.format_previous_attempts
   planner.prompts.format_tools_list
   planner.prompts.get_planning_template

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



.. rubric:: Related Links

.. autolink-examples:: planner.prompts
   :collapse:
   
.. autolink-skip:: next
