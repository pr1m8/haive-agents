agents.reasoning_and_critique.tot.modular.models
================================================

.. py:module:: agents.reasoning_and_critique.tot.modular.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.models.Candidate
   agents.reasoning_and_critique.tot.modular.models.CandidateContent
   agents.reasoning_and_critique.tot.modular.models.CandidateList
   agents.reasoning_and_critique.tot.modular.models.CandidateScore


Module Contents
---------------

.. py:class:: Candidate(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A candidate solution in the Tree of Thoughts algorithm.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Candidate
      :collapse:

   .. py:method:: __str__() -> str

      String representation of the candidate.


      .. autolink-examples:: __str__
         :collapse:


   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: feedback
      :type:  str | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: score
      :type:  float | None
      :value: None



.. py:class:: CandidateContent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A potential solution to the problem.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateContent
      :collapse:

   .. py:attribute:: content
      :type:  str
      :value: None



.. py:class:: CandidateList(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A list of candidate solutions.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateList
      :collapse:

   .. py:attribute:: candidates
      :type:  list[CandidateContent]
      :value: None



   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



.. py:class:: CandidateScore(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Score and feedback for a candidate solution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateScore
      :collapse:

   .. py:attribute:: feedback
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  float
      :value: None



