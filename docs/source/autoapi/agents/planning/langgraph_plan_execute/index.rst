
:py:mod:`agents.planning.langgraph_plan_execute`
================================================

.. py:module:: agents.planning.langgraph_plan_execute

LangGraph Plan and Execute Implementation.

Following the official LangGraph tutorial pattern:
https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/


.. autolink-examples:: agents.planning.langgraph_plan_execute
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.langgraph_plan_execute.Act
   agents.planning.langgraph_plan_execute.Plan
   agents.planning.langgraph_plan_execute.PlanExecuteState
   agents.planning.langgraph_plan_execute.Response


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Act:

   .. graphviz::
      :align: center

      digraph inheritance_Act {
        node [shape=record];
        "Act" [label="Act"];
        "pydantic.BaseModel" -> "Act";
      }

.. autopydantic_model:: agents.planning.langgraph_plan_execute.Act
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Plan:

   .. graphviz::
      :align: center

      digraph inheritance_Plan {
        node [shape=record];
        "Plan" [label="Plan"];
        "pydantic.BaseModel" -> "Plan";
      }

.. autopydantic_model:: agents.planning.langgraph_plan_execute.Plan
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanExecuteState:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteState {
        node [shape=record];
        "PlanExecuteState" [label="PlanExecuteState"];
        "haive.core.schema.prebuilt.messages.messages_state.MessagesState" -> "PlanExecuteState";
      }

.. autoclass:: agents.planning.langgraph_plan_execute.PlanExecuteState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Response:

   .. graphviz::
      :align: center

      digraph inheritance_Response {
        node [shape=record];
        "Response" [label="Response"];
        "pydantic.BaseModel" -> "Response";
      }

.. autopydantic_model:: agents.planning.langgraph_plan_execute.Response
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.planning.langgraph_plan_execute.create_langgraph_plan_execute
   agents.planning.langgraph_plan_execute.create_plan_execute_agent
   agents.planning.langgraph_plan_execute.route_replan
   agents.planning.langgraph_plan_execute.should_continue

.. py:function:: create_langgraph_plan_execute(name: str = 'PlanExecute', model: str = 'gpt-4o-mini', tools: list | None = None) -> haive.agents.multi.archive.enhanced_base.MultiAgentBase

   Create Plan and Execute agent following official LangGraph tutorial.

   :param name: Name for the agent
   :param model: Model to use for all agents
   :param tools: Tools available to executor

   :returns: Plan and Execute system following LangGraph pattern
   :rtype: MultiAgentBase


   .. autolink-examples:: create_langgraph_plan_execute
      :collapse:

.. py:function:: create_plan_execute_agent(tools: list | None = None) -> haive.agents.multi.archive.enhanced_base.MultiAgentBase

   Create a Plan and Execute agent with default settings.


   .. autolink-examples:: create_plan_execute_agent
      :collapse:

.. py:function:: route_replan(state: PlanExecuteState) -> str

   Route after replanning.


   .. autolink-examples:: route_replan
      :collapse:

.. py:function:: should_continue(state: PlanExecuteState) -> str

   Decide whether to continue executing the plan or finish.


   .. autolink-examples:: should_continue
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.langgraph_plan_execute
   :collapse:
   
.. autolink-skip:: next
