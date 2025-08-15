agents.planning_v2.base.replanner_models
========================================

.. py:module:: agents.planning_v2.base.replanner_models

.. autoapi-nested-parse::

   Models for the replanner component.

   This module contains the Answer and Response models used by the replanner
   to return either a final answer or a new plan.


   .. autolink-examples:: agents.planning_v2.base.replanner_models
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning_v2.base.replanner_models.T


Classes
-------

.. autoapisummary::

   agents.planning_v2.base.replanner_models.Answer
   agents.planning_v2.base.replanner_models.Response


Module Contents
---------------

.. py:class:: Answer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Simple answer response model.

   Used when the replanner determines that the objective has been
   completed and can provide a final answer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Answer
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



.. py:class:: Response(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Generic response model that can contain different response types.

   This model provides a flexible container for replanner outputs,
   supporting either an Answer response OR a Plan response.

   .. rubric:: Examples

   Answer response:
       Response[Union[Answer, Plan[Task]]](
           result=Answer(content="The task is complete"),
           response_type="answer"
       )

   Plan response:
       Response[Union[Answer, Plan[Task]]](
           result=Plan(objective="Continue with phase 2", steps=[...]),
           response_type="plan"
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Response
      :collapse:

   .. py:method:: is_answer() -> bool

      Check if this is an answer response.


      .. autolink-examples:: is_answer
         :collapse:


   .. py:method:: is_plan() -> bool

      Check if this is a plan response.


      .. autolink-examples:: is_plan
         :collapse:


   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: response_type
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  T
      :value: None



.. py:data:: T

