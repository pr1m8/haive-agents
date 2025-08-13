
:py:mod:`agents.reflection.message_transformer_posthook`
========================================================

.. py:module:: agents.reflection.message_transformer_posthook

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

Classes
-------

.. autoapisummary::

   agents.reflection.message_transformer_posthook.AgentWithPostHook
   agents.reflection.message_transformer_posthook.Critique
   agents.reflection.message_transformer_posthook.MessageTransformerPostHook
   agents.reflection.message_transformer_posthook.ReflectionWithGradePostHook


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentWithPostHook:

   .. graphviz::
      :align: center

      digraph inheritance_AgentWithPostHook {
        node [shape=record];
        "AgentWithPostHook" [label="AgentWithPostHook"];
      }

.. autoclass:: agents.reflection.message_transformer_posthook.AgentWithPostHook
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Critique:

   .. graphviz::
      :align: center

      digraph inheritance_Critique {
        node [shape=record];
        "Critique" [label="Critique"];
        "pydantic.BaseModel" -> "Critique";
      }

.. autopydantic_model:: agents.reflection.message_transformer_posthook.Critique
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

   Inheritance diagram for MessageTransformerPostHook:

   .. graphviz::
      :align: center

      digraph inheritance_MessageTransformerPostHook {
        node [shape=record];
        "MessageTransformerPostHook" [label="MessageTransformerPostHook"];
      }

.. autoclass:: agents.reflection.message_transformer_posthook.MessageTransformerPostHook
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionWithGradePostHook:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionWithGradePostHook {
        node [shape=record];
        "ReflectionWithGradePostHook" [label="ReflectionWithGradePostHook"];
        "MessageTransformerPostHook" -> "ReflectionWithGradePostHook";
      }

.. autoclass:: agents.reflection.message_transformer_posthook.ReflectionWithGradePostHook
   :members:
   :undoc-members:
   :show-inheritance:


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



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.message_transformer_posthook
   :collapse:
   
.. autolink-skip:: next
