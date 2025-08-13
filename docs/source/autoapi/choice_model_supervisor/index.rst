
:py:mod:`choice_model_supervisor`
=================================

.. py:module:: choice_model_supervisor

Dynamic Supervisor using DynamicChoiceModel for agent selection.

The supervisor uses DynamicChoiceModel as a tool to select from available agents,
and creates new ReactAgents when needed.


.. autolink-examples:: choice_model_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   choice_model_supervisor.AgentCreationTool
   choice_model_supervisor.AgentSelectionTool
   choice_model_supervisor.ChoiceModelSupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentCreationTool:

   .. graphviz::
      :align: center

      digraph inheritance_AgentCreationTool {
        node [shape=record];
        "AgentCreationTool" [label="AgentCreationTool"];
        "langchain_core.tools.BaseTool" -> "AgentCreationTool";
      }

.. autoclass:: choice_model_supervisor.AgentCreationTool
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentSelectionTool:

   .. graphviz::
      :align: center

      digraph inheritance_AgentSelectionTool {
        node [shape=record];
        "AgentSelectionTool" [label="AgentSelectionTool"];
        "langchain_core.tools.BaseTool" -> "AgentSelectionTool";
      }

.. autoclass:: choice_model_supervisor.AgentSelectionTool
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChoiceModelSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_ChoiceModelSupervisor {
        node [shape=record];
        "ChoiceModelSupervisor" [label="ChoiceModelSupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "ChoiceModelSupervisor";
      }

.. autoclass:: choice_model_supervisor.ChoiceModelSupervisor
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   choice_model_supervisor.test_choice_model_supervisor

.. py:function:: test_choice_model_supervisor()
   :async:


   Test the choice model supervisor.


   .. autolink-examples:: test_choice_model_supervisor
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: choice_model_supervisor
   :collapse:
   
.. autolink-skip:: next
