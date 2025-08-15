agents.planning.langgraph_plan_execute
======================================

.. py:module:: agents.planning.langgraph_plan_execute

.. autoapi-nested-parse::

   LangGraph Plan and Execute Implementation.

   Following the official LangGraph tutorial pattern:
   https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/


   .. autolink-examples:: agents.planning.langgraph_plan_execute
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.langgraph_plan_execute.EXECUTOR_PROMPT
   agents.planning.langgraph_plan_execute.PLANNER_PROMPT
   agents.planning.langgraph_plan_execute.REPLANNER_PROMPT
   agents.planning.langgraph_plan_execute.agent


Classes
-------

.. autoapisummary::

   agents.planning.langgraph_plan_execute.Act
   agents.planning.langgraph_plan_execute.Plan
   agents.planning.langgraph_plan_execute.PlanExecuteState
   agents.planning.langgraph_plan_execute.Response


Functions
---------

.. autoapisummary::

   agents.planning.langgraph_plan_execute.create_langgraph_plan_execute
   agents.planning.langgraph_plan_execute.create_plan_execute_agent
   agents.planning.langgraph_plan_execute.route_replan
   agents.planning.langgraph_plan_execute.should_continue


Module Contents
---------------

.. py:class:: Act(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Action to perform - either respond or continue.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Act
      :collapse:

   .. py:attribute:: action
      :type:  Response | Plan
      :value: None



.. py:class:: Plan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A plan to follow for solving a task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Plan
      :collapse:

   .. py:attribute:: steps
      :type:  list[str]
      :value: None



.. py:class:: PlanExecuteState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages.messages_state.MessagesState`


   State for the plan-and-execute agent.


   .. autolink-examples:: PlanExecuteState
      :collapse:

   .. py:attribute:: past_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: plan
      :type:  list[str]
      :value: None



   .. py:attribute:: response
      :type:  str
      :value: None



.. py:class:: Response(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Response to user.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Response
      :collapse:

   .. py:attribute:: response
      :type:  str
      :value: None



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

.. py:data:: EXECUTOR_PROMPT
   :value: 'Execute the given task using the available tools. Return the result when you have completed the task.'


.. py:data:: PLANNER_PROMPT
   :value: 'For the given objective, come up with a simple step by step plan. This plan should involve...


.. py:data:: REPLANNER_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """For the given objective, come up with a simple step by step plan. This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.
      
      Your objective was this:
      {input}
      
      Your original plan was this:
      {plan}
      
      You have currently done the follow steps:
      {past_steps}
      
      Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan."""

   .. raw:: html

      </details>



.. py:data:: agent

