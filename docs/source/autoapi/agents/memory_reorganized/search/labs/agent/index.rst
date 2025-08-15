agents.memory_reorganized.search.labs.agent
===========================================

.. py:module:: agents.memory_reorganized.search.labs.agent

.. autoapi-nested-parse::

   Labs Agent implementation.

   Provides interactive project automation with tools and workflows. Similar to
   Perplexity's Labs feature that creates apps, dashboards, and automated workflows.


   .. autolink-examples:: agents.memory_reorganized.search.labs.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.search.labs.agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.search.labs.agent.LabsAgent


Module Contents
---------------

.. py:class:: LabsAgent(name: str = 'labs_agent', engine: Optional[haive.core.engine.aug_llm.AugLLMConfig] = None, search_tools: list[langchain_core.tools.Tool] | None = None, enable_code_execution: bool = True, **kwargs)

   Bases: :py:obj:`haive.agents.memory.search.base.BaseSearchAgent`


   Agent for interactive project automation with tools and workflows.

   Mimics Perplexity's Labs feature by providing comprehensive project automation,
   including data analysis, visualization creation, app development, and workflow execution.

   Features:
   - Multi-tool integration (Python, SQL, visualization libraries)
   - Interactive app creation (dashboards, websites, slideshows)
   - Code execution and data analysis
   - Asset management and organization
   - Workflow automation
   - Real-time collaboration tools

   Capabilities:
   - Data analysis and visualization
   - Interactive dashboard creation
   - Basic web app development
   - Chart and image generation
   - CSV and data processing
   - Code execution and debugging

   .. rubric:: Examples

   Basic usage::

       agent = LabsAgent(
           name="labs",
           engine=AugLLMConfig(temperature=0.3)
       )

       response = await agent.process_labs_project(
           "Create a dashboard analyzing sales data",
           data_sources=["sales_data.csv"]
       )

   With specific tools::

       response = await agent.process_labs_project(
           "Build an interactive chart showing trends",
           required_tools=["pandas", "plotly", "d3.js"],
           create_interactive_app=True
       )

   Initialize the Labs Agent.

   :param name: Agent identifier
   :param engine: LLM configuration (defaults to optimized settings)
   :param search_tools: Optional search tools
   :param enable_code_execution: Enable code execution capabilities
   :param \*\*kwargs: Additional arguments passed to parent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LabsAgent
      :collapse:

   .. py:method:: _create_labs_tools() -> list[langchain_core.tools.Tool]

      Create Labs-specific tools for project automation.


      .. autolink-examples:: _create_labs_tools
         :collapse:


   .. py:method:: create_interactive_apps(workflow_steps: list[haive.agents.memory.search.labs.models.WorkflowStep]) -> list[haive.agents.memory.search.labs.models.InteractiveApp]

      Create interactive apps from workflow results.

      :param workflow_steps: Completed workflow steps

      :returns: List of interactive apps


      .. autolink-examples:: create_interactive_apps
         :collapse:


   .. py:method:: create_project_assets(workflow_steps: list[haive.agents.memory.search.labs.models.WorkflowStep]) -> list[haive.agents.memory.search.labs.models.ProjectAsset]

      Create project assets from workflow results.

      :param workflow_steps: Completed workflow steps

      :returns: List of created assets


      .. autolink-examples:: create_project_assets
         :collapse:


   .. py:method:: execute_workflow_step(step_plan: dict[str, Any], step_index: int) -> haive.agents.memory.search.labs.models.WorkflowStep
      :async:


      Execute a single workflow step.

      :param step_plan: Planned step configuration
      :param step_index: Step index in workflow

      :returns: Executed workflow step


      .. autolink-examples:: execute_workflow_step
         :collapse:


   .. py:method:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

      Get the response model for Labs.


      .. autolink-examples:: get_response_model
         :collapse:


   .. py:method:: get_search_instructions() -> str

      Get specific search instructions for Labs operations.


      .. autolink-examples:: get_search_instructions
         :collapse:


   .. py:method:: get_system_prompt() -> str

      Get the system prompt for Labs operations.


      .. autolink-examples:: get_system_prompt
         :collapse:


   .. py:method:: plan_project_workflow(query: str, project_type: str, data_sources: list[str]) -> list[dict[str, Any]]

      Plan the workflow steps for a project.

      :param query: Project description
      :param project_type: Type of project
      :param data_sources: Available data sources

      :returns: List of planned workflow steps


      .. autolink-examples:: plan_project_workflow
         :collapse:


   .. py:method:: process_labs_project(query: str, project_type: str = 'analysis', data_sources: list[str] | None = None, required_tools: list[str] | None = None, create_interactive_app: bool = True, max_work_time: int = 600, save_to_memory: bool = True) -> haive.agents.memory.search.labs.models.LabsResponse
      :async:


      Process a Labs project with comprehensive automation.

      :param query: Project description
      :param project_type: Type of project
      :param data_sources: Available data sources
      :param required_tools: Required tools
      :param create_interactive_app: Whether to create interactive app
      :param max_work_time: Maximum work time in seconds
      :param save_to_memory: Whether to save to memory

      :returns: Labs response with project results


      .. autolink-examples:: process_labs_project
         :collapse:


   .. py:method:: process_search(query: str, context: dict[str, Any] | None = None, save_to_memory: bool = True) -> haive.agents.memory.search.labs.models.LabsResponse
      :async:


      Process a search query with default Labs settings.

      :param query: Search query
      :param context: Optional context
      :param save_to_memory: Whether to save to memory

      :returns: Labs response


      .. autolink-examples:: process_search
         :collapse:


   .. py:attribute:: enable_code_execution
      :value: True



.. py:data:: logger

