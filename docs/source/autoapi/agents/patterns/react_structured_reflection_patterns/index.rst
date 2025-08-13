
:py:mod:`agents.patterns.react_structured_reflection_patterns`
==============================================================

.. py:module:: agents.patterns.react_structured_reflection_patterns

Comprehensive ReactAgent → SimpleAgent Patterns with V3, V4, and Enhanced Base Agent.

This demonstrates all variations of ReactAgent → SimpleAgent workflows:
1. V3: ReactAgent → SimpleAgent (structured output)
2. V4: MultiAgent composition
3. Enhanced Base: Using enhanced base agent with hooks
4. Reflection: ReactAgent → SimpleAgentV3 → ReflectionAgent
5. Graded Reflection: ReactAgent → GradingAgent → SimpleAgentV3 → ReflectionAgent

Each pattern showcases the generalized hook system and different architectural approaches.


.. autolink-examples:: agents.patterns.react_structured_reflection_patterns
   :collapse:

Classes
-------

.. autoapisummary::

   agents.patterns.react_structured_reflection_patterns.ProblemAnalysis
   agents.patterns.react_structured_reflection_patterns.ReactToStructuredV3
   agents.patterns.react_structured_reflection_patterns.ReactToStructuredV4
   agents.patterns.react_structured_reflection_patterns.ReactWithGradedReflection
   agents.patterns.react_structured_reflection_patterns.ReactWithReflection
   agents.patterns.react_structured_reflection_patterns.ResearchFindings
   agents.patterns.react_structured_reflection_patterns.TaskAnalysis


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ProblemAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_ProblemAnalysis {
        node [shape=record];
        "ProblemAnalysis" [label="ProblemAnalysis"];
        "pydantic.BaseModel" -> "ProblemAnalysis";
      }

.. autopydantic_model:: agents.patterns.react_structured_reflection_patterns.ProblemAnalysis
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

   Inheritance diagram for ReactToStructuredV3:

   .. graphviz::
      :align: center

      digraph inheritance_ReactToStructuredV3 {
        node [shape=record];
        "ReactToStructuredV3" [label="ReactToStructuredV3"];
      }

.. autoclass:: agents.patterns.react_structured_reflection_patterns.ReactToStructuredV3
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactToStructuredV4:

   .. graphviz::
      :align: center

      digraph inheritance_ReactToStructuredV4 {
        node [shape=record];
        "ReactToStructuredV4" [label="ReactToStructuredV4"];
        "haive.agents.multi.agent.MultiAgent" -> "ReactToStructuredV4";
      }

.. autoclass:: agents.patterns.react_structured_reflection_patterns.ReactToStructuredV4
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactWithGradedReflection:

   .. graphviz::
      :align: center

      digraph inheritance_ReactWithGradedReflection {
        node [shape=record];
        "ReactWithGradedReflection" [label="ReactWithGradedReflection"];
      }

.. autoclass:: agents.patterns.react_structured_reflection_patterns.ReactWithGradedReflection
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactWithReflection:

   .. graphviz::
      :align: center

      digraph inheritance_ReactWithReflection {
        node [shape=record];
        "ReactWithReflection" [label="ReactWithReflection"];
      }

.. autoclass:: agents.patterns.react_structured_reflection_patterns.ReactWithReflection
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResearchFindings:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchFindings {
        node [shape=record];
        "ResearchFindings" [label="ResearchFindings"];
        "pydantic.BaseModel" -> "ResearchFindings";
      }

.. autopydantic_model:: agents.patterns.react_structured_reflection_patterns.ResearchFindings
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

   Inheritance diagram for TaskAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_TaskAnalysis {
        node [shape=record];
        "TaskAnalysis" [label="TaskAnalysis"];
        "pydantic.BaseModel" -> "TaskAnalysis";
      }

.. autopydantic_model:: agents.patterns.react_structured_reflection_patterns.TaskAnalysis
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

   agents.patterns.react_structured_reflection_patterns.create_graded_reflection_pattern
   agents.patterns.react_structured_reflection_patterns.create_reflection_pattern
   agents.patterns.react_structured_reflection_patterns.create_v3_pattern
   agents.patterns.react_structured_reflection_patterns.create_v4_pattern
   agents.patterns.react_structured_reflection_patterns.data_analysis
   agents.patterns.react_structured_reflection_patterns.example_graded_reflection_pattern
   agents.patterns.react_structured_reflection_patterns.example_reflection_pattern
   agents.patterns.react_structured_reflection_patterns.example_v3_pattern
   agents.patterns.react_structured_reflection_patterns.example_v4_pattern
   agents.patterns.react_structured_reflection_patterns.main
   agents.patterns.react_structured_reflection_patterns.stakeholder_analysis
   agents.patterns.react_structured_reflection_patterns.web_research

.. py:function:: create_graded_reflection_pattern(name: str = 'react_graded_reflection', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactWithGradedReflection

   Create graded reflection pattern.


   .. autolink-examples:: create_graded_reflection_pattern
      :collapse:

.. py:function:: create_reflection_pattern(name: str = 'react_with_reflection', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactWithReflection

   Create Enhanced Base Agent pattern with reflection.


   .. autolink-examples:: create_reflection_pattern
      :collapse:

.. py:function:: create_v3_pattern(name: str = 'react_structured_v3', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactToStructuredV3

   Create V3 pattern: ReactAgent → SimpleAgentV3.


   .. autolink-examples:: create_v3_pattern
      :collapse:

.. py:function:: create_v4_pattern(name: str = 'react_structured_v4', tools: list | None = None, structured_output_model: type[pydantic.BaseModel] = TaskAnalysis) -> ReactToStructuredV4

   Create V4 pattern: MultiAgent composition.


   .. autolink-examples:: create_v4_pattern
      :collapse:

.. py:function:: data_analysis(data_description: str) -> str

   Analyze data and extract insights.


   .. autolink-examples:: data_analysis
      :collapse:

.. py:function:: example_graded_reflection_pattern()
   :async:


   Example: Graded Reflection Pattern.


   .. autolink-examples:: example_graded_reflection_pattern
      :collapse:

.. py:function:: example_reflection_pattern()
   :async:


   Example: Enhanced Base Agent with Reflection.


   .. autolink-examples:: example_reflection_pattern
      :collapse:

.. py:function:: example_v3_pattern()
   :async:


   Example: V3 Architecture Pattern.


   .. autolink-examples:: example_v3_pattern
      :collapse:

.. py:function:: example_v4_pattern()
   :async:


   Example: V4 Architecture Pattern.


   .. autolink-examples:: example_v4_pattern
      :collapse:

.. py:function:: main()
   :async:


   Run all pattern examples.


   .. autolink-examples:: main
      :collapse:

.. py:function:: stakeholder_analysis(context: str) -> str

   Analyze stakeholders for a given context.


   .. autolink-examples:: stakeholder_analysis
      :collapse:

.. py:function:: web_research(topic: str) -> str

   Research a topic using web sources.


   .. autolink-examples:: web_research
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.patterns.react_structured_reflection_patterns
   :collapse:
   
.. autolink-skip:: next
