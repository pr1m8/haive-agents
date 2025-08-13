
:py:mod:`agents.planning.llm_compiler.config`
=============================================

.. py:module:: agents.planning.llm_compiler.config

Configuration for the LLMCompiler agent using AugLLMConfig system.


.. autolink-examples:: agents.planning.llm_compiler.config
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.config.CompilerState
   agents.planning.llm_compiler.config.JoinerOutput
   agents.planning.llm_compiler.config.LLMCompilerAgentConfig


Module Contents
---------------

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

.. autopydantic_model:: agents.planning.llm_compiler.config.CompilerState
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

.. autopydantic_model:: agents.planning.llm_compiler.config.JoinerOutput
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

   Inheritance diagram for LLMCompilerAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_LLMCompilerAgentConfig {
        node [shape=record];
        "LLMCompilerAgentConfig" [label="LLMCompilerAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "LLMCompilerAgentConfig";
      }

.. autoclass:: agents.planning.llm_compiler.config.LLMCompilerAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.planning.llm_compiler.config
   :collapse:
   
.. autolink-skip:: next
