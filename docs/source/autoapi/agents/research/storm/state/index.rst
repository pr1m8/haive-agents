agents.research.storm.state
===========================

.. py:module:: agents.research.storm.state

.. autoapi-nested-parse::

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

.. py:class:: ArticleState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State container for final article content.

   .. attribute:: article

      The complete final article text.

   .. rubric:: Example

   >>> state = ArticleState(article="This is the final article...")
   >>> print(len(state.article))
   25

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ArticleState
      :collapse:

   .. py:attribute:: article
      :type:  str
      :value: None



.. py:class:: ResearchState(/, **data: Any)

   Bases: :py:obj:`TopicState`, :py:obj:`ArticleState`


   Complete research workflow state management.

   This class manages the entire STORM research process state, including
   topic definition, outline generation, editor perspectives, interview
   results, and final section compilation.

   .. attribute:: topic

      The research topic state container.

   .. attribute:: outline

      Generated outline for the research article.

   .. attribute:: editors

      List of editor perspectives for multi-angle research.

   .. attribute:: interview_results

      Results from perspective-based interviews.

   .. attribute:: sections

      Final compiled sections for the article.

   Properties:
       draft: Compiled draft article from all sections.

   .. rubric:: Example

   Complete research workflow::

       from haive.agents.research.storm.state import ResearchState

       state = ResearchState(
           topic=TopicState(topic="Climate Change"),
           outline=generated_outline,
           editors=editor_perspectives,
           interview_results=interview_data,
           sections=compiled_sections
       )

       # Get the complete draft
       article_draft = state.draft
       print(f"Draft length: {len(article_draft)} characters")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchState
      :collapse:

   .. py:property:: draft
      :type: str


      Compile all sections into a single draft article.

      :returns: Complete article draft with all sections joined by double newlines.
      :rtype: str

      .. rubric:: Example

      >>> draft_text = research_state.draft
      >>> print(draft_text[:100])
      # Introduction

      Climate change refers to...

      .. autolink-examples:: draft
         :collapse:


   .. py:attribute:: editors
      :type:  list[haive.agents.research.storm.generate_perspectives.models.Editor]
      :value: None



   .. py:attribute:: interview_results
      :type:  list[haive.agents.research.storm.interview.models.InterviewState]
      :value: None



   .. py:attribute:: outline
      :type:  haive.agents.research.storm.outline_generator.models.Outline
      :value: None



   .. py:attribute:: sections
      :type:  list[haive.agents.research.storm.section_writer.models.WikiSection]
      :value: None



   .. py:attribute:: topic
      :type:  TopicState
      :value: None



.. py:class:: TopicState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Simple state container for research topic.

   .. attribute:: topic

      The research topic as a string.

   .. rubric:: Example

   >>> state = TopicState(topic="Machine Learning Ethics")
   >>> print(state.topic)
   Machine Learning Ethics

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TopicState
      :collapse:

   .. py:attribute:: topic
      :type:  str
      :value: None



