choice_model_supervisor
=======================

.. py:module:: choice_model_supervisor

.. autoapi-nested-parse::

   Dynamic Supervisor using DynamicChoiceModel for agent selection.

   The supervisor uses DynamicChoiceModel as a tool to select from available agents,
   and creates new ReactAgents when needed.


   .. autolink-examples:: choice_model_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   choice_model_supervisor.logger


Classes
-------

.. autoapisummary::

   choice_model_supervisor.AgentCreationTool
   choice_model_supervisor.AgentSelectionTool
   choice_model_supervisor.ChoiceModelSupervisor


Functions
---------

.. autoapisummary::

   choice_model_supervisor.test_choice_model_supervisor


Module Contents
---------------

.. py:class:: AgentCreationTool(supervisor, **kwargs)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool to create new ReactAgents based on task type.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentCreationTool
      :collapse:

   .. py:method:: _run(agent_type: str, capability_description: str) -> str

      Create a new ReactAgent.


      .. autolink-examples:: _run
         :collapse:


   .. py:attribute:: args_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None


      Pydantic model class to validate and parse the tool's input arguments.

      Args schema should be either:

      - A subclass of pydantic.BaseModel.
      or
      - A subclass of pydantic.v1.BaseModel if accessing v1 namespace in pydantic 2
      or
      - a JSON schema dict

      .. autolink-examples:: args_schema
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """Create a new ReactAgent when no suitable agent exists.
             Specify the agent type and capability needed."""

      .. raw:: html

         </details>



      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'create_agent'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


   .. py:attribute:: supervisor


.. py:class:: AgentSelectionTool(choice_model: haive.core.common.models.dynamic_choice_model.DynamicChoiceModel, **kwargs)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool that uses DynamicChoiceModel to select best agent.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentSelectionTool
      :collapse:

   .. py:method:: _run(task_description: str) -> str

      Select agent based on task description.


      .. autolink-examples:: _run
         :collapse:


   .. py:attribute:: args_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None


      Pydantic model class to validate and parse the tool's input arguments.

      Args schema should be either:

      - A subclass of pydantic.BaseModel.
      or
      - A subclass of pydantic.v1.BaseModel if accessing v1 namespace in pydantic 2
      or
      - a JSON schema dict

      .. autolink-examples:: args_schema
         :collapse:


   .. py:attribute:: choice_model


   .. py:attribute:: description
      :type:  str
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """Select the best agent for the current task.
             Use this tool to determine which agent should handle the request."""

      .. raw:: html

         </details>



      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'select_agent'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


.. py:class:: ChoiceModelSupervisor

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Supervisor that uses DynamicChoiceModel for agent selection.

   This supervisor:
   1. Uses DynamicChoiceModel to track available agents
   2. Uses tools to select best agent for each task
   3. Creates new ReactAgents when needed
   4. Routes to selected agents for execution


   .. autolink-examples:: ChoiceModelSupervisor
      :collapse:

   .. py:method:: _create_agent_executor_node()

      Create node that executes the selected agent.


      .. autolink-examples:: _create_agent_executor_node
         :collapse:


   .. py:method:: _create_supervisor_decision_node()

      Create supervisor node that uses tools for decisions.


      .. autolink-examples:: _create_supervisor_decision_node
         :collapse:


   .. py:method:: _extract_state_dict(state: Any) -> dict[str, Any]

      Extract state dict preserving messages.


      .. autolink-examples:: _extract_state_dict
         :collapse:


   .. py:method:: _route_from_supervisor(state: Any) -> str

      Route from supervisor based on decision.


      .. autolink-examples:: _route_from_supervisor
         :collapse:


   .. py:method:: _update_choice_model()

      Update choice model with current agents.


      .. autolink-examples:: _update_choice_model
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with choice model integration.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_available_agents() -> list[str]

      Get list of available agents.


      .. autolink-examples:: get_available_agents
         :collapse:


   .. py:method:: get_choice_model_status() -> dict[str, Any]

      Get status of choice model.


      .. autolink-examples:: get_choice_model_status
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up supervisor with choice model and tools.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _agent_creation_tool
      :type:  AgentCreationTool | None
      :value: None



   .. py:attribute:: _agent_selection_tool
      :type:  AgentSelectionTool | None
      :value: None



   .. py:attribute:: _agents
      :type:  dict[str, haive.agents.react.agent.ReactAgent]
      :value: None



   .. py:attribute:: _choice_model
      :type:  haive.core.common.models.dynamic_choice_model.DynamicChoiceModel | None
      :value: None



   .. py:property:: agents
      :type: dict[str, haive.agents.react.agent.ReactAgent]


      Get current agents.

      .. autolink-examples:: agents
         :collapse:


   .. py:attribute:: max_agents
      :type:  int
      :value: None



.. py:function:: test_choice_model_supervisor()
   :async:


   Test the choice model supervisor.


   .. autolink-examples:: test_choice_model_supervisor
      :collapse:

.. py:data:: logger

