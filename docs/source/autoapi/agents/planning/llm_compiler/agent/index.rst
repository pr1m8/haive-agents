
:py:mod:`agents.planning.llm_compiler.agent`
============================================

.. py:module:: agents.planning.llm_compiler.agent

LLM Compiler Agent Implementation.

from typing import Any, Dict
This implementation follows the LLM Compiler architecture from the paper by Kim et al.,
focusing on parallelizable task execution through a DAG structure.


.. autolink-examples:: agents.planning.llm_compiler.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.agent.CompilerPlan
   agents.planning.llm_compiler.agent.CompilerState
   agents.planning.llm_compiler.agent.CompilerStep
   agents.planning.llm_compiler.agent.FinalResponse
   agents.planning.llm_compiler.agent.JoinerOutput
   agents.planning.llm_compiler.agent.LLMCompilerAgent
   agents.planning.llm_compiler.agent.LLMCompilerAgentConfig
   agents.planning.llm_compiler.agent.LLMCompilerPlanParser


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompilerPlan:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerPlan {
        node [shape=record];
        "CompilerPlan" [label="CompilerPlan"];
        "haive.agents.planning.plan_and_execute.models.Plan" -> "CompilerPlan";
      }

.. autoclass:: agents.planning.llm_compiler.agent.CompilerPlan
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompilerState:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerState {
        node [shape=record];
        "CompilerState" [label="CompilerState"];
        "pydantic.BaseModel" -> "CompilerState";
      }

.. autopydantic_model:: agents.planning.llm_compiler.agent.CompilerState
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompilerStep:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerStep {
        node [shape=record];
        "CompilerStep" [label="CompilerStep"];
        "haive.agents.planning.plan_and_execute.models.Step" -> "CompilerStep";
      }

.. autoclass:: agents.planning.llm_compiler.agent.CompilerStep
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FinalResponse:

   .. graphviz::
      :align: center

      digraph inheritance_FinalResponse {
        node [shape=record];
        "FinalResponse" [label="FinalResponse"];
        "pydantic.BaseModel" -> "FinalResponse";
      }

.. autopydantic_model:: agents.planning.llm_compiler.agent.FinalResponse
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for JoinerOutput:

   .. graphviz::
      :align: center

      digraph inheritance_JoinerOutput {
        node [shape=record];
        "JoinerOutput" [label="JoinerOutput"];
        "pydantic.BaseModel" -> "JoinerOutput";
      }

.. autopydantic_model:: agents.planning.llm_compiler.agent.JoinerOutput
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

   Inheritance diagram for LLMCompilerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LLMCompilerAgent {
        node [shape=record];
        "LLMCompilerAgent" [label="LLMCompilerAgent"];
        "haive.core.engine.agent.agent.AgentArchitecture" -> "LLMCompilerAgent";
      }

.. autoclass:: agents.planning.llm_compiler.agent.LLMCompilerAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LLMCompilerAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_LLMCompilerAgentConfig {
        node [shape=record];
        "LLMCompilerAgentConfig" [label="LLMCompilerAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "LLMCompilerAgentConfig";
      }

.. autoclass:: agents.planning.llm_compiler.agent.LLMCompilerAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LLMCompilerPlanParser:

   .. graphviz::
      :align: center

      digraph inheritance_LLMCompilerPlanParser {
        node [shape=record];
        "LLMCompilerPlanParser" [label="LLMCompilerPlanParser"];
        "langchain_core.output_parsers.transform.BaseTransformOutputParser[dict]" -> "LLMCompilerPlanParser";
      }

.. autoclass:: agents.planning.llm_compiler.agent.LLMCompilerPlanParser
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler.agent.main

.. py:function:: main() -> None



.. rubric:: Related Links

.. autolink-examples:: agents.planning.llm_compiler.agent
   :collapse:
   
.. autolink-skip:: next
