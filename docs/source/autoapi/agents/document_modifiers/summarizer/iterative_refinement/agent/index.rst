agents.document_modifiers.summarizer.iterative_refinement.agent
===============================================================

.. py:module:: agents.document_modifiers.summarizer.iterative_refinement.agent


Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.agent.IterativeSummarizer


Module Contents
---------------

.. py:class:: IterativeSummarizer(config: haive.agents.document_modifiers.summarizer.iterative_refinement.config.IterativeSummarizerConfig = IterativeSummarizerConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.document_modifiers.summarizer.iterative_refinement.config.IterativeSummarizerConfig`\ ]


   An agent that summarizes a document iteratively.


   .. autolink-examples:: IterativeSummarizer
      :collapse:

   .. py:method:: generate_initial_summary(state: haive.agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerState, config: langchain_core.runnables.RunnableConfig)
      :async:



   .. py:method:: refine_summary(state: haive.agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerState, config: langchain_core.runnables.RunnableConfig)
      :async:



   .. py:method:: setup_workflow() -> None


