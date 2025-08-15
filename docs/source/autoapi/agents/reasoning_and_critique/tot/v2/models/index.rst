agents.reasoning_and_critique.tot.v2.models
===========================================

.. py:module:: agents.reasoning_and_critique.tot.v2.models


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.models.T


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.models.Candidate
   agents.reasoning_and_critique.tot.v2.models.CandidateEvaluation
   agents.reasoning_and_critique.tot.v2.models.CandidateGeneration
   agents.reasoning_and_critique.tot.v2.models.ScoredCandidate
   agents.reasoning_and_critique.tot.v2.models.SearchControl


Module Contents
---------------

.. py:class:: Candidate(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Generic candidate that can hold any type of content.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Candidate
      :collapse:

   .. py:method:: __str__() -> str

      String representation for use in prompts.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: get_content_str() -> str

      Get string representation of content for prompts.


      .. autolink-examples:: get_content_str
         :collapse:


   .. py:method:: validate_content(v: Any) -> Any
      :classmethod:


      Convert various types to a consistent format.


      .. autolink-examples:: validate_content
         :collapse:


   .. py:attribute:: content
      :type:  T


   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: depth
      :type:  int
      :value: 0



   .. py:attribute:: expansion_index
      :type:  int
      :value: 0



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: parent_id
      :type:  str | None
      :value: None



.. py:class:: CandidateEvaluation(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from scoring agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateEvaluation
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: feedback
      :type:  str


   .. py:attribute:: score
      :type:  float
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: None



   .. py:attribute:: weaknesses
      :type:  list[str]
      :value: None



.. py:class:: CandidateGeneration(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from expansion agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateGeneration
      :collapse:

   .. py:attribute:: candidates
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: strategy
      :type:  Literal['explore', 'exploit', 'refine']
      :value: None



.. py:class:: ScoredCandidate

   Bases: :py:obj:`Candidate`\ [\ :py:obj:`T`\ ], :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   A candidate that has been evaluated with a score.


   .. autolink-examples:: ScoredCandidate
      :collapse:

   .. py:method:: __str__() -> str

      Enhanced string representation with score.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: from_candidate(candidate: Candidate[T], score: float, feedback: str, **kwargs) -> ScoredCandidate[T]
      :classmethod:


      Create a ScoredCandidate from a Candidate.


      .. autolink-examples:: from_candidate
         :collapse:


   .. py:method:: validate_score(v: float) -> float
      :classmethod:


      Ensure score is in valid range.


      .. autolink-examples:: validate_score
         :collapse:


   .. py:attribute:: feedback
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  float
      :value: None



   .. py:attribute:: scoring_metadata
      :type:  dict[str, Any]
      :value: None



.. py:class:: SearchControl(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from control/pruning agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchControl
      :collapse:

   .. py:attribute:: next_strategy
      :type:  Literal['explore', 'exploit', 'refine', 'terminate']
      :value: None



   .. py:attribute:: selected_indices
      :type:  list[int]
      :value: None



   .. py:attribute:: should_terminate
      :type:  bool


   .. py:attribute:: termination_reason
      :type:  str | None
      :value: None



.. py:data:: T

