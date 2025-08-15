agents.react_class.react_agent2.models
======================================

.. py:module:: agents.react_class.react_agent2.models


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.models.Action
   agents.react_class.react_agent2.models.ActionType
   agents.react_class.react_agent2.models.ReactState
   agents.react_class.react_agent2.models.ReactionData
   agents.react_class.react_agent2.models.Thought


Module Contents
---------------

.. py:class:: Action(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An action that the agent decides to take.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Action
      :collapse:

   .. py:method:: __str__()


   .. py:attribute:: action_input
      :type:  str


   .. py:attribute:: action_type
      :type:  ActionType


.. py:class:: ActionType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of actions that the agent can take.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ActionType
      :collapse:

   .. py:attribute:: CALCULATOR
      :value: 'calculator'



   .. py:attribute:: DATABASE
      :value: 'database'



   .. py:attribute:: FINAL_ANSWER
      :value: 'final_answer'



   .. py:attribute:: SEARCH
      :value: 'search'



   .. py:attribute:: WEATHER
      :value: 'weather'



.. py:class:: ReactState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State schema for React agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactState
      :collapse:

   .. py:attribute:: current_action
      :type:  Action | None
      :value: None



   .. py:attribute:: current_thought
      :type:  Thought | None
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: intermediate_steps
      :type:  list[dict[str, Any] | tuple[Action, str]]
      :value: None



   .. py:attribute:: iteration_count
      :type:  int
      :value: 0



   .. py:attribute:: max_iterations
      :type:  int
      :value: 10



   .. py:attribute:: max_retry_attempts
      :type:  int
      :value: 3



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.AnyMessage]
      :value: None



   .. py:attribute:: observations
      :type:  list[str]
      :value: None



   .. py:attribute:: retry_attempts
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: status
      :type:  str
      :value: 'thinking'



   .. py:attribute:: thoughts
      :type:  list[Thought]
      :value: None



   .. py:attribute:: tool_names
      :type:  list[str]
      :value: None



   .. py:attribute:: tools
      :type:  dict[str, Any]
      :value: None



.. py:class:: ReactionData(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Data for agent reasoning and action.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactionData
      :collapse:

   .. py:attribute:: action
      :type:  str | None
      :value: None



   .. py:attribute:: action_input
      :type:  str | dict[str, Any] | None
      :value: None



   .. py:attribute:: thought
      :type:  str | None
      :value: None



.. py:class:: Thought(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The agent's reasoning process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Thought
      :collapse:

   .. py:method:: __str__()


   .. py:attribute:: action
      :type:  Action


   .. py:attribute:: thought
      :type:  str


