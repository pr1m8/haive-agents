
:py:mod:`agents.rag.factories.rag_workflow_factory`
===================================================

.. py:module:: agents.rag.factories.rag_workflow_factory

RAG Workflow Factory.

Generic factory for creating RAG workflows by composing callable functions
into different agent patterns. This provides a clean, modular approach to
building complex RAG systems.


.. autolink-examples:: agents.rag.factories.rag_workflow_factory
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.factories.rag_workflow_factory.ConditionalCallableAgent
   agents.rag.factories.rag_workflow_factory.GenericCallableAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConditionalCallableAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalCallableAgent {
        node [shape=record];
        "ConditionalCallableAgent" [label="ConditionalCallableAgent"];
        "haive.agents.base.agent.Agent" -> "ConditionalCallableAgent";
      }

.. autoclass:: agents.rag.factories.rag_workflow_factory.ConditionalCallableAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GenericCallableAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GenericCallableAgent {
        node [shape=record];
        "GenericCallableAgent" [label="GenericCallableAgent"];
        "haive.agents.base.agent.Agent" -> "GenericCallableAgent";
      }

.. autoclass:: agents.rag.factories.rag_workflow_factory.GenericCallableAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.factories.rag_workflow_factory.create_adaptive_rag_agent
   agents.rag.factories.rag_workflow_factory.create_corrective_rag_agent
   agents.rag.factories.rag_workflow_factory.create_hyde_rag_agent
   agents.rag.factories.rag_workflow_factory.create_multi_query_rag_agent
   agents.rag.factories.rag_workflow_factory.create_rag_workflow
   agents.rag.factories.rag_workflow_factory.create_self_rag_agent
   agents.rag.factories.rag_workflow_factory.create_step_back_rag_agent

.. py:function:: create_adaptive_rag_agent(documents: list[langchain_core.documents.Document] | None = None, name: str = 'Adaptive RAG Agent') -> haive.agents.base.agent.Agent

   Create an adaptive RAG agent with complexity-based routing.


   .. autolink-examples:: create_adaptive_rag_agent
      :collapse:

.. py:function:: create_corrective_rag_agent(documents: list[langchain_core.documents.Document] | None = None, name: str = 'Corrective RAG Agent') -> haive.agents.base.agent.Agent

   Create a CRAG agent with web search fallback.


   .. autolink-examples:: create_corrective_rag_agent
      :collapse:

.. py:function:: create_hyde_rag_agent(documents: list[langchain_core.documents.Document] | None = None, name: str = 'HYDE RAG Agent') -> haive.agents.base.agent.Agent

   Create a HYDE RAG agent with hypothesis generation.


   .. autolink-examples:: create_hyde_rag_agent
      :collapse:

.. py:function:: create_multi_query_rag_agent(documents: list[langchain_core.documents.Document] | None = None, name: str = 'Multi-Query RAG Agent') -> haive.agents.base.agent.Agent

   Create a multi-query RAG agent with query variations.


   .. autolink-examples:: create_multi_query_rag_agent
      :collapse:

.. py:function:: create_rag_workflow(workflow_type: str, documents: list[langchain_core.documents.Document] | None = None, custom_callables: dict[str, collections.abc.Callable] | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Main factory function for creating RAG workflows.

   :param workflow_type: Type of RAG workflow to create
   :param documents: Documents for retrieval
   :param custom_callables: Custom callable functions to override defaults
   :param \*\*kwargs: Additional arguments

   :returns: Configured RAG agent

   Available workflow types:
       - 'corrective' / 'crag': Corrective RAG with web search
       - 'self_rag': Self-RAG with reflection tokens
       - 'adaptive': Adaptive RAG with complexity routing
       - 'hyde': HYDE RAG with hypothesis generation
       - 'step_back': Step-back prompting RAG
       - 'multi_query': Multi-query RAG with variations
       - 'simple': Basic sequential RAG


   .. autolink-examples:: create_rag_workflow
      :collapse:

.. py:function:: create_self_rag_agent(documents: list[langchain_core.documents.Document] | None = None, name: str = 'Self-RAG Agent') -> haive.agents.base.agent.Agent

   Create a Self-RAG agent with reflection tokens.


   .. autolink-examples:: create_self_rag_agent
      :collapse:

.. py:function:: create_step_back_rag_agent(documents: list[langchain_core.documents.Document] | None = None, name: str = 'Step-Back RAG Agent') -> haive.agents.base.agent.Agent

   Create a step-back prompting RAG agent.


   .. autolink-examples:: create_step_back_rag_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.factories.rag_workflow_factory
   :collapse:
   
.. autolink-skip:: next
