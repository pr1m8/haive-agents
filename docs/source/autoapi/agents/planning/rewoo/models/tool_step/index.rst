agents.planning.rewoo.models.tool_step
======================================

.. py:module:: agents.planning.rewoo.models.tool_step

.. autoapi-nested-parse::

   Tool Step Model - Generic step that validates against a tool list.

   A concrete step implementation that works with LangChain tools and validates:
   - Tool exists in provided tool list
   - Tool arguments match tool schema
   - Tool can be executed with given parameters


   .. autolink-examples:: agents.planning.rewoo.models.tool_step
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.rewoo.models.tool_step.ToolStep


Functions
---------

.. autoapisummary::

   agents.planning.rewoo.models.tool_step.create_tool_steps_from_plan
   agents.planning.rewoo.models.tool_step.validate_tool_compatibility


Module Contents
---------------

.. py:class:: ToolStep

   Bases: :py:obj:`agents.planning.rewoo.models.steps.AbstractStep`


   A step that executes a specific tool with validated arguments.


   .. autolink-examples:: ToolStep
      :collapse:

   .. py:method:: _are_args_valid() -> bool

      Check if tool arguments are valid.


      .. autolink-examples:: _are_args_valid
         :collapse:


   .. py:method:: can_execute(completed_steps: set[str]) -> bool

      Check if this step can execute.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: clear_tool_args() -> None

      Clear all tool arguments.


      .. autolink-examples:: clear_tool_args
         :collapse:


   .. py:method:: create_from_tool(tool: langchain_core.tools.BaseTool, tool_args: dict[str, Any], available_tools: list[langchain_core.tools.BaseTool], description: str | None = None, **kwargs) -> ToolStep
      :classmethod:


      Factory method to create ToolStep from a tool instance.


      .. autolink-examples:: create_from_tool
         :collapse:


   .. py:method:: execute(context: dict[str, Any]) -> Any

      Execute the tool with the provided arguments.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: get_tool_info() -> dict[str, Any]

      Get comprehensive tool information.


      .. autolink-examples:: get_tool_info
         :collapse:


   .. py:method:: update_tool_args(**kwargs) -> None

      Update tool arguments and revalidate.


      .. autolink-examples:: update_tool_args
         :collapse:


   .. py:method:: validate_tool_exists_and_args() -> ToolStep

      Validate tool exists and arguments are correct.


      .. autolink-examples:: validate_tool_exists_and_args
         :collapse:


   .. py:method:: validate_tool_name(v: str, info) -> str
      :classmethod:


      Validate tool name exists in available tools.


      .. autolink-examples:: validate_tool_name
         :collapse:


   .. py:method:: validate_tools_not_empty(v: list[langchain_core.tools.BaseTool]) -> list[langchain_core.tools.BaseTool]
      :classmethod:


      Validate tools list is not empty.


      .. autolink-examples:: validate_tools_not_empty
         :collapse:


   .. py:attribute:: available_tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



   .. py:property:: is_tool_valid
      :type: bool


      Whether the tool setup is valid.

      .. autolink-examples:: is_tool_valid
         :collapse:


   .. py:property:: optional_args
      :type: list[str]


      Optional arguments for the selected tool.

      .. autolink-examples:: optional_args
         :collapse:


   .. py:property:: required_args
      :type: list[str]


      Required arguments for the selected tool.

      .. autolink-examples:: required_args
         :collapse:


   .. py:attribute:: result
      :type:  Any | None
      :value: None



   .. py:property:: selected_tool
      :type: langchain_core.tools.BaseTool | None


      The selected tool instance.

      .. autolink-examples:: selected_tool
         :collapse:


   .. py:attribute:: tool_args
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: tool_name
      :type:  str
      :value: None



   .. py:property:: tool_names
      :type: list[str]


      List of available tool names.

      .. autolink-examples:: tool_names
         :collapse:


   .. py:property:: tool_schema
      :type: dict[str, Any] | None


      Schema of the selected tool.

      .. autolink-examples:: tool_schema
         :collapse:


.. py:function:: create_tool_steps_from_plan(tool_plan: list[dict[str, Any]], available_tools: list[langchain_core.tools.BaseTool]) -> list[ToolStep]

   Create a list of ToolSteps from a plan description.


   .. autolink-examples:: create_tool_steps_from_plan
      :collapse:

.. py:function:: validate_tool_compatibility(tools: list[langchain_core.tools.BaseTool]) -> dict[str, Any]

   Validate a list of tools for compatibility issues.


   .. autolink-examples:: validate_tool_compatibility
      :collapse:

