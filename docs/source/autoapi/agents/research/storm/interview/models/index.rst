agents.research.storm.interview.models
======================================

.. py:module:: agents.research.storm.interview.models

.. autoapi-nested-parse::

   Models for STORM interview functionality.


   .. autolink-examples:: agents.research.storm.interview.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.research.storm.interview.models.InterviewState


Module Contents
---------------

.. py:class:: InterviewState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for interview process in STORM research.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: InterviewState
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: answers
      :type:  list[str]
      :value: None



   .. py:attribute:: interviewee
      :type:  str
      :value: None



   .. py:attribute:: interviewer
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: questions
      :type:  list[str]
      :value: None



