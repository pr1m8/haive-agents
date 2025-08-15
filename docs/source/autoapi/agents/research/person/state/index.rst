agents.research.person.state
============================

.. py:module:: agents.research.person.state


Attributes
----------

.. autoapisummary::

   agents.research.person.state.DEFAULT_EXTRACTION_SCHEMA


Classes
-------

.. autoapisummary::

   agents.research.person.state.Person
   agents.research.person.state.PersonResearchAgentConfig
   agents.research.person.state.PersonResearchInputState
   agents.research.person.state.PersonResearchOutputState
   agents.research.person.state.PersonResearchState


Module Contents
---------------

.. py:class:: Person(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A class representing a person to research.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Person
      :collapse:

   .. py:attribute:: company
      :type:  str | None
      :value: None


      The current company of the person.

      .. autolink-examples:: company
         :collapse:


   .. py:attribute:: email
      :type:  str

      The email of the person.

      .. autolink-examples:: email
         :collapse:


   .. py:attribute:: linkedin
      :type:  str | None
      :value: None


      The Linkedin URL of the person.

      .. autolink-examples:: linkedin
         :collapse:


   .. py:attribute:: name
      :type:  str | None
      :value: None


      The name of the person.

      .. autolink-examples:: name
         :collapse:


   .. py:attribute:: role
      :type:  str | None
      :value: None


      The current title of the person.

      .. autolink-examples:: role
         :collapse:


.. py:class:: PersonResearchAgentConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration settings for person research agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PersonResearchAgentConfig
      :collapse:

   .. py:attribute:: max_reflection_steps
      :type:  int
      :value: None



   .. py:attribute:: max_search_queries
      :type:  int
      :value: None



   .. py:attribute:: max_search_results
      :type:  int
      :value: None



.. py:class:: PersonResearchInputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input state defines the interface between the graph and the user (external API).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PersonResearchInputState
      :collapse:

   .. py:attribute:: extraction_schema
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: person
      :type:  Person
      :value: None



   .. py:attribute:: user_notes
      :type:  dict[str, Any] | None
      :value: None



.. py:class:: PersonResearchOutputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The response object for the end user.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PersonResearchOutputState
      :collapse:

   .. py:attribute:: info
      :type:  dict[str, Any]
      :value: None



.. py:class:: PersonResearchState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Overall state for the person research workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PersonResearchState
      :collapse:

   .. py:attribute:: completed_notes
      :type:  Annotated[list[str], operator.add]
      :value: None



   .. py:attribute:: extraction_schema
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: info
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: is_satisfactory
      :type:  bool | None
      :value: None



   .. py:attribute:: person
      :type:  Person
      :value: None



   .. py:attribute:: reflection_steps_taken
      :type:  int
      :value: None



   .. py:attribute:: search_queries
      :type:  list[str] | None
      :value: None



   .. py:attribute:: user_notes
      :type:  str | None
      :value: None



.. py:data:: DEFAULT_EXTRACTION_SCHEMA

