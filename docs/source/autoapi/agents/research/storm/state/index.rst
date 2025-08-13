
:py:mod:`agents.research.storm.state`
=====================================

.. py:module:: agents.research.storm.state

State management for STORM research workflow.

This module provides Pydantic models for managing state throughout the STORM
(Synthesis of Topic Outline through Retrieval and Multi-perspective questioning)
research process, including topic definition, article generation, and research coordination.

Classes:
    TopicState: Simple state container for research topic
    ArticleState: State container for final article content
    ResearchState: Complete research workflow state management

.. rubric:: Example

Basic research state management::

    from haive.agents.research.storm.state import ResearchState

    state = ResearchState(
        topic=TopicState(topic="AI Safety"),
        outline=outline_instance,
        editors=editor_list,
        interview_results=interview_list,
        sections=section_list
    )

    draft = state.draft  # Get compiled article draft


.. autolink-examples:: agents.research.storm.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.research.storm.state.ArticleState
   agents.research.storm.state.ResearchState
   agents.research.storm.state.TopicState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ArticleState:

   .. graphviz::
      :align: center

      digraph inheritance_ArticleState {
        node [shape=record];
        "ArticleState" [label="ArticleState"];
        "pydantic.BaseModel" -> "ArticleState";
      }

.. autopydantic_model:: agents.research.storm.state.ArticleState
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

   Inheritance diagram for ResearchState:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchState {
        node [shape=record];
        "ResearchState" [label="ResearchState"];
        "TopicState" -> "ResearchState";
        "ArticleState" -> "ResearchState";
      }

.. autoclass:: agents.research.storm.state.ResearchState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TopicState:

   .. graphviz::
      :align: center

      digraph inheritance_TopicState {
        node [shape=record];
        "TopicState" [label="TopicState"];
        "pydantic.BaseModel" -> "TopicState";
      }

.. autopydantic_model:: agents.research.storm.state.TopicState
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





.. rubric:: Related Links

.. autolink-examples:: agents.research.storm.state
   :collapse:
   
.. autolink-skip:: next
