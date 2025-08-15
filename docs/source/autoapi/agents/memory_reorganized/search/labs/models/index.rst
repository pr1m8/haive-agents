agents.memory_reorganized.search.labs.models
============================================

.. py:module:: agents.memory_reorganized.search.labs.models

.. autoapi-nested-parse::

   Data models for Labs Agent.


   .. autolink-examples:: agents.memory_reorganized.search.labs.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.search.labs.models.AssetType
   agents.memory_reorganized.search.labs.models.InteractiveApp
   agents.memory_reorganized.search.labs.models.LabsRequest
   agents.memory_reorganized.search.labs.models.LabsResponse
   agents.memory_reorganized.search.labs.models.ProjectAsset
   agents.memory_reorganized.search.labs.models.WorkflowStep


Module Contents
---------------

.. py:class:: AssetType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of assets that can be created.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AssetType
      :collapse:

   .. py:attribute:: APP
      :value: 'app'



   .. py:attribute:: CHART
      :value: 'chart'



   .. py:attribute:: CODE
      :value: 'code'



   .. py:attribute:: CSV
      :value: 'csv'



   .. py:attribute:: DASHBOARD
      :value: 'dashboard'



   .. py:attribute:: DATASET
      :value: 'dataset'



   .. py:attribute:: IMAGE
      :value: 'image'



   .. py:attribute:: REPORT
      :value: 'report'



.. py:class:: InteractiveApp(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for interactive applications created in Labs.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: InteractiveApp
      :collapse:

   .. py:attribute:: app_id
      :type:  str
      :value: None



   .. py:attribute:: app_type
      :type:  str
      :value: None



   .. py:attribute:: css_styles
      :type:  str | None
      :value: None



   .. py:attribute:: data_sources
      :type:  list[str]
      :value: None



   .. py:attribute:: deployment_url
      :type:  str | None
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: html_content
      :type:  str
      :value: None



   .. py:attribute:: interactive_elements
      :type:  list[str]
      :value: None



   .. py:attribute:: javascript_code
      :type:  str | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: LabsRequest(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Request model for Labs operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LabsRequest
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:attribute:: create_interactive_app
      :type:  bool
      :value: None



   .. py:attribute:: data_sources
      :type:  list[str]
      :value: None



   .. py:attribute:: enable_code_execution
      :type:  bool
      :value: None



   .. py:attribute:: max_work_time
      :type:  int
      :value: None



   .. py:attribute:: output_format
      :type:  str
      :value: None



   .. py:attribute:: project_type
      :type:  str
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: required_tools
      :type:  list[str]
      :value: None



.. py:class:: LabsResponse

   Bases: :py:obj:`haive.agents.memory.search.base.SearchResponse`


   Response model for Labs operations.

   Extends the base SearchResponse with Labs-specific fields.


   .. autolink-examples:: LabsResponse
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:attribute:: assets_created
      :type:  list[ProjectAsset]
      :value: None



   .. py:attribute:: code_execution_results
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: data_analysis_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: interactive_apps
      :type:  list[InteractiveApp]
      :value: None



   .. py:attribute:: next_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: project_name
      :type:  str
      :value: None



   .. py:attribute:: project_summary
      :type:  str
      :value: None



   .. py:attribute:: search_type
      :type:  str
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



   .. py:attribute:: total_work_time
      :type:  float
      :value: None



   .. py:attribute:: visualizations_created
      :type:  int
      :value: None



   .. py:attribute:: workflow_steps
      :type:  list[WorkflowStep]
      :value: None



.. py:class:: ProjectAsset(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for project assets created during workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ProjectAsset
      :collapse:

   .. py:attribute:: asset_id
      :type:  str
      :value: None



   .. py:attribute:: content
      :type:  str | None
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: downloadable
      :type:  bool
      :value: None



   .. py:attribute:: file_path
      :type:  str | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: size_bytes
      :type:  int
      :value: None



   .. py:attribute:: type
      :type:  AssetType
      :value: None



.. py:class:: WorkflowStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for individual workflow steps.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WorkflowStep
      :collapse:

   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: duration_seconds
      :type:  float
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: input_data
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_data
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



   .. py:attribute:: tool_used
      :type:  str | None
      :value: None



