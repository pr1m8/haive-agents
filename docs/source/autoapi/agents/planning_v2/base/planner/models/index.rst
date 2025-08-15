agents.planning_v2.base.planner.models
======================================

.. py:module:: agents.planning_v2.base.planner.models

.. autoapi-nested-parse::

   Concrete plan models for the planner agent.


   .. autolink-examples:: agents.planning_v2.base.planner.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning_v2.base.planner.models.TaskPlan


Module Contents
---------------

.. py:class:: TaskPlan

   Bases: :py:obj:`haive.agents.planning_v2.base.models.Plan`\ [\ :py:obj:`haive.agents.planning_v2.base.models.Task`\ ]


   Concrete plan implementation using Task steps.

   This is needed because OpenAI's function calling doesn't accept
   generic class names like Plan[Task] - it needs a simple name.


   .. autolink-examples:: TaskPlan
      :collapse:

