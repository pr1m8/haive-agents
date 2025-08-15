agents.reflection.message_transformer_posthook
==============================================

.. py:module:: agents.reflection.message_transformer_posthook

.. autoapi-nested-parse::

   Message Transformer Reflection Post-Hook Pattern.

   This implements the correct reflection pattern using message transformation
   as a POST-HOOK following the insights from 2025-01-18:

   1. Don't fight the message-only interface - use prompt engineering instead
   2. Structured data flows through prompt configuration, not messages
   3. Message transformation + prompt partials = powerful combination
   4. The flow: Main Agent → Response → Convert to prompt partial → Message Transform → Reflection

   This follows the pattern documented in:
   - project_docs/memory_index/by_date/2025-01-18/reflection_pattern_insights.md
   - project_docs/sessions/active/hook_pattern_conceptual_exploration.md


   .. autolink-examples:: agents.reflection.message_transformer_posthook
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reflection.message_transformer_posthook.MESSAGE_TRANSFORMER_AVAILABLE
   agents.reflection.message_transformer_posthook.T


Classes
-------

.. autoapisummary::

   agents.reflection.message_transformer_posthook.AgentWithPostHook
   agents.reflection.message_transformer_posthook.MessageTransformerPostHook
   agents.reflection.message_transformer_posthook.ReflectionWithGradePostHook


Functions
---------

.. autoapisummary::

   agents.reflection.message_transformer_posthook.create_agent_with_reflection
   agents.reflection.message_transformer_posthook.create_graded_reflection_post_hook
   agents.reflection.message_transformer_posthook.create_reflection_post_hook
   agents.reflection.message_transformer_posthook.example_basic_post_hook
   agents.reflection.message_transformer_posthook.example_factory_pattern
   agents.reflection.message_transformer_posthook.example_graded_reflection_post_hook
   agents.reflection.message_transformer_posthook.main


Module Contents
---------------

.. py:class:: AgentWithPostHook(base_agent: haive.agents.simple.agent.SimpleAgent, post_hooks: list[MessageTransformerPostHook] | None = None)

   Agent wrapper that applies post-hooks after execution.

   This implements the proper hook pattern where:
   1. Base agent executes normally
   2. Post-hooks transform the result
   3. Enhanced result is returned

   Initialize agent with post-hooks.

   :param base_agent: The base agent to wrap
   :param post_hooks: List of post-hooks to apply


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentWithPostHook
      :collapse:

   .. py:method:: add_post_hook(hook: MessageTransformerPostHook)

      Add a post-hook.


      .. autolink-examples:: add_post_hook
         :collapse:


   .. py:method:: arun(input_data: Any) -> dict[str, Any]
      :async:


      Run agent with post-hook processing.

      :param input_data: Input for the base agent

      :returns: Result after all post-hooks have been applied


      .. autolink-examples:: arun
         :collapse:


   .. py:attribute:: base_agent


   .. py:attribute:: post_hooks
      :value: []



.. py:class:: MessageTransformerPostHook(reflection_agent: haive.agents.simple.agent.SimpleAgent, transform_type: str = 'reflection', preserve_first_message: bool = True)

   Post-hook that applies message transformation for reflection.

   This follows the correct pattern:
   1. Agent produces response (messages)
   2. Extract structured data from messages
   3. Convert to prompt partial (NOT message!)
   4. Apply message transformation
   5. Feed to reflection agent with grade in prompt context

   Initialize the post-hook.

   :param reflection_agent: Agent that will do the reflection
   :param transform_type: Type of message transformation to apply
   :param preserve_first_message: Whether to preserve first message


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MessageTransformerPostHook
      :collapse:

   .. py:method:: __call__(agent_result: dict[str, Any], original_input: Any = None, structured_data: pydantic.BaseModel | None = None) -> dict[str, Any]
      :async:


      Apply message transformation and reflection.

      :param agent_result: Result from the main agent
      :param original_input: Original input to the agent
      :param structured_data: Optional structured data to inject into prompt

      :returns: Enhanced result with reflection applied


      .. autolink-examples:: __call__
         :collapse:


   .. py:attribute:: reflection_agent


   .. py:attribute:: transform_type
      :value: 'reflection'



.. py:class:: ReflectionWithGradePostHook(grading_agent: haive.agents.simple.agent.SimpleAgent, reflection_agent: haive.agents.simple.agent.SimpleAgent, preserve_first_message: bool = True)

   Bases: :py:obj:`MessageTransformerPostHook`


   Post-hook that combines grading + message transformation + reflection.

   This implements the exact pattern from the 2025-01-18 insights:
   Main Agent → Response → GradingResult → Convert to prompt partial →
   Message Transform → Reflection Agent (with grade in prompt context)

   Initialize graded reflection post-hook.

   :param grading_agent: Agent that produces structured grading
   :param reflection_agent: Agent that does reflection with grade context
   :param preserve_first_message: Whether to preserve first message


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionWithGradePostHook
      :collapse:

   .. py:method:: __call__(agent_result: dict[str, Any], original_input: Any = None) -> dict[str, Any]
      :async:


      Apply grading → message transform → reflection with grade context.

      :param agent_result: Result from the main agent
      :param original_input: Original input to the agent

      :returns: Enhanced result with grading and reflection applied


      .. autolink-examples:: __call__
         :collapse:


   .. py:attribute:: grading_agent


   .. py:attribute:: reflection_prompt


.. py:function:: create_agent_with_reflection(base_agent: haive.agents.simple.agent.SimpleAgent, reflection_type: str = 'basic') -> AgentWithPostHook

   Create an agent with reflection post-hook.

   :param base_agent: The base agent to enhance
   :param reflection_type: Type of reflection ("basic" or "graded")

   :returns: Agent wrapped with reflection post-hook


   .. autolink-examples:: create_agent_with_reflection
      :collapse:

.. py:function:: create_graded_reflection_post_hook(grading_model: type[pydantic.BaseModel], temperature: float = 0.2) -> ReflectionWithGradePostHook

   Create a graded reflection post-hook.


   .. autolink-examples:: create_graded_reflection_post_hook
      :collapse:

.. py:function:: create_reflection_post_hook(reflection_prompt_template: langchain_core.prompts.ChatPromptTemplate | None = None, temperature: float = 0.3) -> MessageTransformerPostHook

   Create a basic reflection post-hook.


   .. autolink-examples:: create_reflection_post_hook
      :collapse:

.. py:function:: example_basic_post_hook()
   :async:


   Example: Basic message transformer post-hook.


   .. autolink-examples:: example_basic_post_hook
      :collapse:

.. py:function:: example_factory_pattern()
   :async:


   Example: Using factory function for quick setup.


   .. autolink-examples:: example_factory_pattern
      :collapse:

.. py:function:: example_graded_reflection_post_hook()
   :async:


   Example: Graded reflection with message transformation.


   .. autolink-examples:: example_graded_reflection_post_hook
      :collapse:

.. py:function:: main()
   :async:


   Run all post-hook examples.


   .. autolink-examples:: main
      :collapse:

.. py:data:: MESSAGE_TRANSFORMER_AVAILABLE
   :value: True


.. py:data:: T

