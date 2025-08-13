
:py:mod:`agents.reflection.agent`
=================================

.. py:module:: agents.reflection.agent

Reflection agents using generic pre/post hook pattern.


.. autolink-examples:: agents.reflection.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reflection.agent.ExpertAgent
   agents.reflection.agent.ExpertiseConfig
   agents.reflection.agent.GradedReflectionMultiAgent
   agents.reflection.agent.GradingAgent
   agents.reflection.agent.GradingResult
   agents.reflection.agent.PrePostMultiAgent
   agents.reflection.agent.ReflectionAgent
   agents.reflection.agent.ReflectionConfig
   agents.reflection.agent.ReflectionMultiAgent
   agents.reflection.agent.StructuredOutputMultiAgent
   agents.reflection.agent.ToolBasedReflectionAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExpertAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ExpertAgent {
        node [shape=record];
        "ExpertAgent" [label="ExpertAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "ExpertAgent";
      }

.. autoclass:: agents.reflection.agent.ExpertAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExpertiseConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ExpertiseConfig {
        node [shape=record];
        "ExpertiseConfig" [label="ExpertiseConfig"];
        "pydantic.BaseModel" -> "ExpertiseConfig";
      }

.. autopydantic_model:: agents.reflection.agent.ExpertiseConfig
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

   Inheritance diagram for GradedReflectionMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GradedReflectionMultiAgent {
        node [shape=record];
        "GradedReflectionMultiAgent" [label="GradedReflectionMultiAgent"];
        "PrePostMultiAgent[haive.agents.simple.agent.SimpleAgent, TMainAgent, haive.agents.simple.agent.SimpleAgent]" -> "GradedReflectionMultiAgent";
      }

.. autoclass:: agents.reflection.agent.GradedReflectionMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GradingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GradingAgent {
        node [shape=record];
        "GradingAgent" [label="GradingAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "GradingAgent";
      }

.. autoclass:: agents.reflection.agent.GradingAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GradingResult:

   .. graphviz::
      :align: center

      digraph inheritance_GradingResult {
        node [shape=record];
        "GradingResult" [label="GradingResult"];
        "pydantic.BaseModel" -> "GradingResult";
      }

.. autopydantic_model:: agents.reflection.agent.GradingResult
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

   Inheritance diagram for PrePostMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_PrePostMultiAgent {
        node [shape=record];
        "PrePostMultiAgent" [label="PrePostMultiAgent"];
        "haive.agents.multi.base.agent.MultiAgent" -> "PrePostMultiAgent";
        "Generic[TPreAgent, TMainAgent, TPostAgent]" -> "PrePostMultiAgent";
      }

.. autoclass:: agents.reflection.agent.PrePostMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionAgent {
        node [shape=record];
        "ReflectionAgent" [label="ReflectionAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "ReflectionAgent";
      }

.. autoclass:: agents.reflection.agent.ReflectionAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionConfig {
        node [shape=record];
        "ReflectionConfig" [label="ReflectionConfig"];
        "pydantic.BaseModel" -> "ReflectionConfig";
      }

.. autopydantic_model:: agents.reflection.agent.ReflectionConfig
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

   Inheritance diagram for ReflectionMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionMultiAgent {
        node [shape=record];
        "ReflectionMultiAgent" [label="ReflectionMultiAgent"];
        "PrePostMultiAgent[haive.agents.base.agent.Agent, TMainAgent, haive.agents.simple.agent.SimpleAgent]" -> "ReflectionMultiAgent";
      }

.. autoclass:: agents.reflection.agent.ReflectionMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StructuredOutputMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_StructuredOutputMultiAgent {
        node [shape=record];
        "StructuredOutputMultiAgent" [label="StructuredOutputMultiAgent"];
        "PrePostMultiAgent[haive.agents.base.agent.Agent, TMainAgent, haive.agents.structured.StructuredOutputAgent]" -> "StructuredOutputMultiAgent";
      }

.. autoclass:: agents.reflection.agent.StructuredOutputMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolBasedReflectionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ToolBasedReflectionAgent {
        node [shape=record];
        "ToolBasedReflectionAgent" [label="ToolBasedReflectionAgent"];
        "haive.agents.react.agent.ReactAgent" -> "ToolBasedReflectionAgent";
      }

.. autoclass:: agents.reflection.agent.ToolBasedReflectionAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reflection.agent.create
   agents.reflection.agent.create_expert_agent
   agents.reflection.agent.create_graded_reflection_agent
   agents.reflection.agent.create_reflection_agent
   agents.reflection.agent.create_tool_based_reflection_agent
   agents.reflection.agent.model_post_init

.. py:function:: create(*args, **kwargs)

   Create a basic reflection agent (alias for create_reflection_agent).


   .. autolink-examples:: create
      :collapse:

.. py:function:: create_expert_agent(name: str, domain: str, expertise_level: Literal['beginner', 'intermediate', 'expert', 'world-class'] = 'expert', **kwargs) -> ExpertAgent

   Create an expert agent.


   .. autolink-examples:: create_expert_agent
      :collapse:

.. py:function:: create_graded_reflection_agent(name: str = 'graded_reflector', main_agent: haive.agents.base.agent.Agent | None = None, **kwargs) -> GradingAgent | GradedReflectionMultiAgent

   Create grading agent or full graded reflection system.


   .. autolink-examples:: create_graded_reflection_agent
      :collapse:

.. py:function:: create_reflection_agent(name: str = 'reflector', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, **kwargs) -> ReflectionAgent

   Create a simple reflection agent.


   .. autolink-examples:: create_reflection_agent
      :collapse:

.. py:function:: create_tool_based_reflection_agent(name: str = 'tool_reflector', tools: list | None = None, **kwargs) -> ToolBasedReflectionAgent

   Create tool-based reflection agent.


   .. autolink-examples:: create_tool_based_reflection_agent
      :collapse:

.. py:function:: model_post_init(*args, **kwargs)

   Model post-init function (placeholder for compatibility).


   .. autolink-examples:: model_post_init
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.agent
   :collapse:
   
.. autolink-skip:: next
