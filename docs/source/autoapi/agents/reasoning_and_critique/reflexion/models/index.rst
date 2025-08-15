agents.reasoning_and_critique.reflexion.models
==============================================

.. py:module:: agents.reasoning_and_critique.reflexion.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflexion.models.AnswerQuestion
   agents.reasoning_and_critique.reflexion.models.Reflection
   agents.reasoning_and_critique.reflexion.models.ReviseAnswer


Module Contents
---------------

.. py:class:: AnswerQuestion(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Answer the question. Provide an answer, reflection, and follow up with search queries to improve the answer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AnswerQuestion
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: reflection
      :type:  Reflection
      :value: None



   .. py:attribute:: search_queries
      :type:  list[str]
      :value: None



.. py:class:: Reflection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Reflection on the answer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Reflection
      :collapse:

   .. py:attribute:: missing
      :type:  str
      :value: None



   .. py:attribute:: superfluous
      :type:  str
      :value: None



.. py:class:: ReviseAnswer(/, **data: Any)

   Bases: :py:obj:`AnswerQuestion`


   Revise your original answer to your question. Provide an answer, reflection,.

   cite your reflection with references, and finally
   add search queries to improve the answer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReviseAnswer
      :collapse:

   .. py:attribute:: references
      :type:  list[str]
      :value: None



