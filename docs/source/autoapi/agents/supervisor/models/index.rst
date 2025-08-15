agents.supervisor.models
========================

.. py:module:: agents.supervisor.models

.. autoapi-nested-parse::

   Data models for Dynamic Supervisor V2.

   This module contains all the Pydantic models and enums used by the dynamic supervisor
   for agent specifications, capabilities, and configuration.


   .. autolink-examples:: agents.supervisor.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.supervisor.models.AgentCapability
   agents.supervisor.models.AgentDiscoveryMode
   agents.supervisor.models.AgentSpec
   agents.supervisor.models.DiscoveryConfig


Module Contents
---------------

.. py:class:: AgentCapability(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Rich metadata describing an agent's capabilities.

   This model captures comprehensive information about what an agent can do,
   enabling intelligent task-to-agent matching.

   .. attribute:: name

      Unique identifier for the agent

   .. attribute:: agent_type

      Type of agent (e.g., SimpleAgentV3, ReactAgent)

   .. attribute:: description

      Human-readable description of agent's purpose

   .. attribute:: specialties

      List of task domains the agent excels at

   .. attribute:: tools

      Names of tools available to this agent

   .. attribute:: active

      Whether the agent is currently active

   .. attribute:: performance_score

      Historical performance metric (0-1)

   .. attribute:: usage_count

      Number of times this agent has been used

   .. attribute:: last_used

      Timestamp of last usage (ISO format)

   .. attribute:: metadata

      Additional custom metadata

   .. rubric:: Example

   >>> capability = AgentCapability(
   ...     name="research_expert",
   ...     agent_type="ReactAgent",
   ...     description="Expert at research and information gathering",
   ...     specialties=["research", "analysis", "web search"],
   ...     tools=["web_search", "document_reader"]
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentCapability
      :collapse:

   .. py:method:: matches_task(task: str, threshold: float = 0.3) -> float

      Calculate match score between this agent's capabilities and a task.

      :param task: The task description to match against
      :param threshold: Minimum score to consider a match (0-1)

      :returns: Match score between 0 and 1


      .. autolink-examples:: matches_task
         :collapse:


   .. py:method:: validate_specialties(v: list[str]) -> list[str]
      :classmethod:


      Ensure specialties are lowercase for consistent matching.


      .. autolink-examples:: validate_specialties
         :collapse:


   .. py:attribute:: active
      :type:  bool
      :value: None



   .. py:attribute:: agent_type
      :type:  str
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: last_used
      :type:  str | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: performance_score
      :type:  float
      :value: None



   .. py:attribute:: specialties
      :type:  list[str]
      :value: None



   .. py:attribute:: tools
      :type:  list[str]
      :value: None



   .. py:attribute:: usage_count
      :type:  int
      :value: None



.. py:class:: AgentDiscoveryMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Agent discovery modes for the dynamic supervisor.

   .. attribute:: MANUAL

      Use manually provided agent specifications

   .. attribute:: COMPONENT_DISCOVERY

      Discover agents from installed components

   .. attribute:: RAG_DISCOVERY

      Use RAG to find relevant agent implementations

   .. attribute:: MCP_DISCOVERY

      Discover agents via Model Context Protocol

   .. attribute:: HYBRID

      Combine multiple discovery methods

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentDiscoveryMode
      :collapse:

   .. py:attribute:: COMPONENT_DISCOVERY
      :value: 'component_discovery'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: MANUAL
      :value: 'manual'



   .. py:attribute:: MCP_DISCOVERY
      :value: 'mcp_discovery'



   .. py:attribute:: RAG_DISCOVERY
      :value: 'rag_discovery'



.. py:class:: AgentSpec(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Specification for creating an agent dynamically.

   This model defines everything needed to instantiate a new agent at runtime,
   including its type, configuration, and capabilities.

   .. attribute:: name

      Unique identifier for the agent

   .. attribute:: agent_type

      Type of agent to create (e.g., "SimpleAgentV3", "ReactAgent")

   .. attribute:: description

      Human-readable description

   .. attribute:: specialties

      Task domains this agent should handle

   .. attribute:: tools

      Tool names or instances to provide to the agent

   .. attribute:: config

      Configuration dictionary for agent initialization

   .. attribute:: priority

      Priority level for agent selection (higher = preferred)

   .. attribute:: enabled

      Whether this spec can be used to create agents

   .. rubric:: Example

   >>> spec = AgentSpec(
   ...     name="code_reviewer",
   ...     agent_type="ReactAgent",
   ...     description="Expert code reviewer and analyzer",
   ...     specialties=["code review", "analysis", "best practices"],
   ...     tools=["file_reader", "code_analyzer"],
   ...     config={
   ...         "temperature": 0.2,
   ...         "system_message": "You are an expert code reviewer."
   ...     }
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentSpec
      :collapse:

   .. py:method:: to_capability() -> AgentCapability

      Convert this spec to an AgentCapability.


      .. autolink-examples:: to_capability
         :collapse:


   .. py:method:: validate_specialties(v: list[str]) -> list[str]
      :classmethod:


      Ensure specialties are lowercase for consistent matching.


      .. autolink-examples:: validate_specialties
         :collapse:


   .. py:attribute:: agent_type
      :type:  str
      :value: None



   .. py:attribute:: config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: enabled
      :type:  bool
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: specialties
      :type:  list[str]
      :value: None



   .. py:attribute:: tools
      :type:  list[Any]
      :value: None



.. py:class:: DiscoveryConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for agent discovery mechanisms.

   .. attribute:: mode

      Discovery mode to use

   .. attribute:: component_paths

      Paths to search for component discovery

   .. attribute:: rag_collection

      Collection name for RAG discovery

   .. attribute:: mcp_endpoints

      MCP server endpoints for discovery

   .. attribute:: cache_discoveries

      Whether to cache discovered agents

   .. attribute:: discovery_timeout

      Timeout for discovery operations (seconds)

   .. attribute:: max_discoveries_per_request

      Maximum agents to discover per request

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DiscoveryConfig
      :collapse:

   .. py:attribute:: cache_discoveries
      :type:  bool
      :value: None



   .. py:attribute:: component_paths
      :type:  list[str]
      :value: None



   .. py:attribute:: discovery_timeout
      :type:  float
      :value: None



   .. py:attribute:: max_discoveries_per_request
      :type:  int
      :value: None



   .. py:attribute:: mcp_endpoints
      :type:  list[str]
      :value: None



   .. py:attribute:: mode
      :type:  AgentDiscoveryMode
      :value: None



   .. py:attribute:: rag_collection
      :type:  str | None
      :value: None



