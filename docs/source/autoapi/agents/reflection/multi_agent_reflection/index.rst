
:py:mod:`agents.reflection.multi_agent_reflection`
==================================================

.. py:module:: agents.reflection.multi_agent_reflection

Multi-agent reflection pattern using sequential coordination.

This module implements reflection patterns using the new multi-agent system.
It creates a sequential workflow where:
1. ReactAgent performs initial reasoning and action
2. SimpleAgent performs reflection using message transformer post-hooks

The reflection flow follows the pattern discovered in project documentation:
Main Agent → Response → Convert to prompt partial → Message Transform → Reflection


.. autolink-examples:: agents.reflection.multi_agent_reflection
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reflection.multi_agent_reflection.MultiAgentReflection
   agents.reflection.multi_agent_reflection.ReflectionGrade
   agents.reflection.multi_agent_reflection.ReflectionResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgentReflection:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentReflection {
        node [shape=record];
        "MultiAgentReflection" [label="MultiAgentReflection"];
      }

.. autoclass:: agents.reflection.multi_agent_reflection.MultiAgentReflection
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionGrade:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionGrade {
        node [shape=record];
        "ReflectionGrade" [label="ReflectionGrade"];
        "pydantic.BaseModel" -> "ReflectionGrade";
      }

.. autopydantic_model:: agents.reflection.multi_agent_reflection.ReflectionGrade
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

   Inheritance diagram for ReflectionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionResult {
        node [shape=record];
        "ReflectionResult" [label="ReflectionResult"];
        "pydantic.BaseModel" -> "ReflectionResult";
      }

.. autopydantic_model:: agents.reflection.multi_agent_reflection.ReflectionResult
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



Functions
---------

.. autoapisummary::

   agents.reflection.multi_agent_reflection.create_full_reflection_system
   agents.reflection.multi_agent_reflection.create_simple_reflection_system

.. py:function:: create_full_reflection_system(tools: list[langchain_core.tools.Tool] | None = None, engine_config: haive.core.engine.aug_llm.AugLLMConfig | None = None) -> MultiAgentReflection

   Create a full reflection system with ReactAgent + ReflectionAgent + ImprovementAgent.

   :param tools: Tools for the ReactAgent
   :param engine_config: Base engine configuration

   :returns: MultiAgentReflection system with improvement capability


   .. autolink-examples:: create_full_reflection_system
      :collapse:

.. py:function:: create_simple_reflection_system(tools: list[langchain_core.tools.Tool] | None = None, engine_config: haive.core.engine.aug_llm.AugLLMConfig | None = None) -> MultiAgentReflection

   Create a simple reflection system with ReactAgent + ReflectionAgent.

   :param tools: Tools for the ReactAgent
   :param engine_config: Base engine configuration

   :returns: MultiAgentReflection system ready for use


   .. autolink-examples:: create_simple_reflection_system
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.multi_agent_reflection
   :collapse:
   
.. autolink-skip:: next
