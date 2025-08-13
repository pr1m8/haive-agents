
:py:mod:`agents.memory.search.labs.agent`
=========================================

.. py:module:: agents.memory.search.labs.agent

Labs Agent implementation.

Provides interactive project automation with tools and workflows.
Similar to Perplexity's Labs feature that creates apps, dashboards, and automated workflows.


.. autolink-examples:: agents.memory.search.labs.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.search.labs.agent.LabsAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LabsAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LabsAgent {
        node [shape=record];
        "LabsAgent" [label="LabsAgent"];
        "haive.agents.memory.search.base.BaseSearchAgent" -> "LabsAgent";
      }

.. autoclass:: agents.memory.search.labs.agent.LabsAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory.search.labs.agent.create_interactive_app
   agents.memory.search.labs.agent.create_interactive_apps
   agents.memory.search.labs.agent.create_project_assets
   agents.memory.search.labs.agent.create_visualization
   agents.memory.search.labs.agent.execute_python_code
   agents.memory.search.labs.agent.get_response_model
   agents.memory.search.labs.agent.get_search_instructions
   agents.memory.search.labs.agent.get_system_prompt
   agents.memory.search.labs.agent.plan_project_workflow
   agents.memory.search.labs.agent.process_data_file

.. py:function:: create_interactive_app(app_type: str, title: str, description: str) -> haive.agents.memory.search.labs.models.InteractiveApp

   Create an interactive app.


   .. autolink-examples:: create_interactive_app
      :collapse:

.. py:function:: create_interactive_apps(app_specs: list[dict[str, Any]]) -> list[haive.agents.memory.search.labs.models.InteractiveApp]

   Create multiple interactive apps.


   .. autolink-examples:: create_interactive_apps
      :collapse:

.. py:function:: create_project_assets(project_name: str, asset_types: list[str]) -> list[haive.agents.memory.search.labs.models.ProjectAsset]

   Create project assets.


   .. autolink-examples:: create_project_assets
      :collapse:

.. py:function:: create_visualization(chart_type: str, data: dict[str, Any], title: str) -> dict[str, Any]

   Create a data visualization.


   .. autolink-examples:: create_visualization
      :collapse:

.. py:function:: execute_python_code(code: str, description: str = '') -> dict[str, Any]

   Execute Python code and return results.


   .. autolink-examples:: execute_python_code
      :collapse:

.. py:function:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

   Get the response model for labs operations.


   .. autolink-examples:: get_response_model
      :collapse:

.. py:function:: get_search_instructions() -> str

   Get specific search instructions for labs operations.


   .. autolink-examples:: get_search_instructions
      :collapse:

.. py:function:: get_system_prompt() -> str

   Get the system prompt for labs operations.


   .. autolink-examples:: get_system_prompt
      :collapse:

.. py:function:: plan_project_workflow(project_type: str, goals: list[str]) -> list[haive.agents.memory.search.labs.models.WorkflowStep]

   Plan a project workflow.


   .. autolink-examples:: plan_project_workflow
      :collapse:

.. py:function:: process_data_file(file_path: str, operations: list[str]) -> dict[str, Any]

   Process a data file with specified operations.


   .. autolink-examples:: process_data_file
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory.search.labs.agent
   :collapse:
   
.. autolink-skip:: next
