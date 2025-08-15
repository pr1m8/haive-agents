agents.dynamic_supervisor.models
================================

.. py:module:: agents.dynamic_supervisor.models

.. autoapi-nested-parse::

   Data models for dynamic supervisor agent.

   This module contains Pydantic models used by the dynamic supervisor for
   agent metadata, routing information, and configuration.

   Classes:
       AgentInfo: Metadata container for agents (v1 with exclusion)
       AgentInfoV2: Experimental version with full serialization
       AgentRequest: Model for agent addition requests
       RoutingDecision: Model for routing decisions

   .. rubric:: Example

   Creating agent metadata::

       info = AgentInfo(
           agent=search_agent,
           name="search",
           description="Web search specialist",
           active=True
       )


   .. autolink-examples:: agents.dynamic_supervisor.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.dynamic_supervisor.models.AgentInfo
   agents.dynamic_supervisor.models.AgentInfoV2
   agents.dynamic_supervisor.models.AgentRequest
   agents.dynamic_supervisor.models.RoutingDecision


Module Contents
---------------

.. py:class:: AgentInfo(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Information about an agent including instance and metadata.

   This model stores agent metadata and the agent instance itself. The agent
   field is excluded from serialization to avoid msgpack serialization issues
   with complex objects.

   .. attribute:: agent

      The actual agent instance (excluded from serialization)

   .. attribute:: name

      Unique identifier for the agent

   .. attribute:: description

      Human-readable description of capabilities

   .. attribute:: active

      Whether the agent is currently active

   .. attribute:: capabilities

      List of capability keywords for discovery

   .. attribute:: metadata

      Additional metadata (versions, config, etc.)

   .. rubric:: Example

   Creating agent info::

       info = AgentInfo(
           agent=math_agent,
           name="math",
           description="Mathematics and calculation expert",
           capabilities=["math", "calculation", "statistics"]
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentInfo
      :collapse:

   .. py:method:: activate() -> None

      Activate the agent.


      .. autolink-examples:: activate
         :collapse:


   .. py:method:: deactivate() -> None

      Deactivate the agent.


      .. autolink-examples:: deactivate
         :collapse:


   .. py:method:: extract_agent_info() -> AgentInfo

      Extract name and description from agent if not provided.

      :returns: Self with extracted information


      .. autolink-examples:: extract_agent_info
         :collapse:


   .. py:method:: get_agent() -> Any

      Get the agent instance.

      :returns: The agent instance


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: is_active() -> bool

      Check if agent is active.

      :returns: True if active, False otherwise


      .. autolink-examples:: is_active
         :collapse:


   .. py:method:: matches_capability(required: str) -> bool

      Check if agent has a required capability.

      :param required: Capability keyword to check

      :returns: True if agent has the capability


      .. autolink-examples:: matches_capability
         :collapse:


   .. py:attribute:: active
      :type:  bool
      :value: None



   .. py:attribute:: agent
      :type:  Any
      :value: None



   .. py:attribute:: capabilities
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: AgentInfoV2(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Experimental version with full agent serialization.

   This version attempts to serialize the agent object. Requires custom
   serialization logic or agents that support model_dump().

   .. warning:: Experimental - may not work with all agent types.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentInfoV2
      :collapse:

   .. py:method:: serialize_agent(agent: Any) -> dict[str, Any]

      Attempt to serialize agent to dict.

      :param agent: Agent instance

      :returns: Serialized representation


      .. autolink-examples:: serialize_agent
         :collapse:


   .. py:attribute:: active
      :type:  bool
      :value: None



   .. py:attribute:: agent
      :type:  Any
      :value: None



   .. py:attribute:: capabilities
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: AgentRequest(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for requesting a new agent be added.

   Used when the supervisor identifies a missing capability and needs
   to request a new agent from an agent builder or registry.

   .. attribute:: capability

      The required capability (e.g., "translation", "code_analysis")

   .. attribute:: task_context

      Context about what task needs this capability

   .. attribute:: suggested_name

      Suggested name for the new agent

   .. attribute:: requirements

      Specific requirements or constraints

   .. rubric:: Example

   Requesting a new agent::

       request = AgentRequest(
           capability="translation",
           task_context="Need to translate search results to French",
           suggested_name="translator",
           requirements=["Support French", "Maintain formatting"]
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentRequest
      :collapse:

   .. py:attribute:: capability
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  str
      :value: None



   .. py:attribute:: requirements
      :type:  list[str]
      :value: None



   .. py:attribute:: suggested_name
      :type:  str | None
      :value: None



   .. py:attribute:: task_context
      :type:  str
      :value: None



.. py:class:: RoutingDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for supervisor routing decisions.

   Represents a decision made by the supervisor about which agent
   to route to or what action to take.

   .. attribute:: agent_name

      Name of agent to route to (or "END")

   .. attribute:: task

      Task to give to the agent

   .. attribute:: reasoning

      Explanation of the routing decision

   .. attribute:: confidence

      Confidence level in the decision (0-1)

   .. attribute:: alternatives

      Other agents that could handle this

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RoutingDecision
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: alternatives
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: task
      :type:  str
      :value: None



