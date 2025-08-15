agents.document_modifiers.summarizer.iterative_refinement
=========================================================

.. py:module:: agents.document_modifiers.summarizer.iterative_refinement

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: agents.document_modifiers.summarizer.iterative_refinement
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/document_modifiers/summarizer/iterative_refinement/agent/index
   /autoapi/agents/document_modifiers/summarizer/iterative_refinement/config/index
   /autoapi/agents/document_modifiers/summarizer/iterative_refinement/engines/index
   /autoapi/agents/document_modifiers/summarizer/iterative_refinement/example/index
   /autoapi/agents/document_modifiers/summarizer/iterative_refinement/state/index


Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizer
   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerConfig
   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerInput
   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerOutput
   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerState


Functions
---------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.should_refine


Package Contents
----------------

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


.. py:class:: IterativeSummarizerConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   The configuration for the iterative summarizer.


   .. autolink-examples:: IterativeSummarizerConfig
      :collapse:

   .. py:attribute:: checkpoint_mode
      :type:  str
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: input_schema
      :type:  haive.agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerInput
      :value: None



   .. py:attribute:: output_schema
      :type:  haive.agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerOutput
      :value: None



   .. py:attribute:: state_schema
      :type:  haive.agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerState
      :value: None



.. py:class:: IterativeSummarizerInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for the summarizer – supports string, Document, message, or dict content.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativeSummarizerInput
      :collapse:

   .. py:method:: normalize_contents(value: str)
      :classmethod:


      Ensure all items are string representations.


      .. autolink-examples:: normalize_contents
         :collapse:


   .. py:attribute:: contents
      :type:  list[str | langchain_core.documents.Document | langchain_core.messages.BaseMessage | dict[str, Any]]
      :value: None



.. py:class:: IterativeSummarizerOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output for the summarizer – stores the final summary result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativeSummarizerOutput
      :collapse:

   .. py:attribute:: summary
      :type:  str
      :value: None



.. py:class:: IterativeSummarizerState(/, **data: Any)

   Bases: :py:obj:`IterativeSummarizerInput`, :py:obj:`IterativeSummarizerOutput`


   Full state for the iterative summarizer agent – tracks progress and summary.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativeSummarizerState
      :collapse:

   .. py:method:: should_refine() -> Literal['refine_summary', '__end__']


   .. py:attribute:: index
      :type:  int
      :value: None



.. py:function:: should_refine(state: state.IterativeSummarizerState) -> str

   Check if the iterative summarization should continue.


   .. autolink-examples:: should_refine
      :collapse:

