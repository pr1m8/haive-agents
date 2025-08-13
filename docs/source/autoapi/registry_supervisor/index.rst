
:py:mod:`registry_supervisor`
=============================

.. py:module:: registry_supervisor

Registry-Based Dynamic Supervisor using DynamicChoiceModel.

The supervisor gets agents from an agent registry instead of creating them.
Uses DynamicChoiceModel for selection and all agents are ReactAgents.


.. autolink-examples:: registry_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   registry_supervisor.AgentRegistry
   registry_supervisor.AgentRetrievalTool
   registry_supervisor.AgentSelectionTool
   registry_supervisor.RegistrySupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentRegistry:

   .. graphviz::
      :align: center

      digraph inheritance_AgentRegistry {
        node [shape=record];
        "AgentRegistry" [label="AgentRegistry"];
      }

.. autoclass:: registry_supervisor.AgentRegistry
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentRetrievalTool:

   .. graphviz::
      :align: center

      digraph inheritance_AgentRetrievalTool {
        node [shape=record];
        "AgentRetrievalTool" [label="AgentRetrievalTool"];
        "langchain_core.tools.BaseTool" -> "AgentRetrievalTool";
      }

.. autoclass:: registry_supervisor.AgentRetrievalTool
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

.. autoclass:: registry_supervisor.AgentSelectionTool
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RegistrySupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_RegistrySupervisor {
        node [shape=record];
        "RegistrySupervisor" [label="RegistrySupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "RegistrySupervisor";
      }

.. autoclass:: registry_supervisor.RegistrySupervisor
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   registry_supervisor.test_registry_supervisor

.. py:function:: test_registry_supervisor()
   :async:


   Test the registry supervisor.


   .. autolink-examples:: test_registry_supervisor
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: registry_supervisor
   :collapse:
   
.. autolink-skip:: next
