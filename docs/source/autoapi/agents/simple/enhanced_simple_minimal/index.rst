agents.simple.enhanced_simple_minimal
=====================================

.. py:module:: agents.simple.enhanced_simple_minimal

.. autoapi-nested-parse::

   Minimal Enhanced SimpleAgent - showing the pattern in action.

   This is the absolute minimal version showing SimpleAgent as Agent[AugLLMConfig].
   It's self-contained to avoid import issues.


   .. autolink-examples:: agents.simple.enhanced_simple_minimal
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/simple/enhanced_simple_minimal/v2/index


Attributes
----------

.. autoapisummary::

   agents.simple.enhanced_simple_minimal.EngineT
   agents.simple.enhanced_simple_minimal.config


Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_minimal.Agent
   agents.simple.enhanced_simple_minimal.AugLLMConfig
   agents.simple.enhanced_simple_minimal.Engine
   agents.simple.enhanced_simple_minimal.SimpleAgent
   agents.simple.enhanced_simple_minimal.Workflow


Module Contents
---------------

.. py:class:: Agent(name: str, engine: EngineT)

   Bases: :py:obj:`Workflow`, :py:obj:`Generic`\ [\ :py:obj:`EngineT`\ ]


   Agent = Workflow + Engine with engine-focused generics.


   .. autolink-examples:: Agent
      :collapse:

   .. py:method:: __repr__() -> str


   .. py:method:: execute(input_data: Any) -> Any
      :async:


      Execute using the engine.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: engine


   .. py:attribute:: name


.. py:class:: AugLLMConfig

   Bases: :py:obj:`Engine`


.. py:class:: Engine

.. py:class:: SimpleAgent(name: str, engine: EngineT)

   Bases: :py:obj:`Agent`\ [\ :py:obj:`AugLLMConfig`\ ]


   SimpleAgent is nothing more than Agent[AugLLMConfig].

   This demonstrates the power of engine-focused generics:
   - SimpleAgent = Agent[AugLLMConfig]
   - ReactAgent = Agent[AugLLMConfig] + reasoning loop
   - RAGAgent = Agent[RetrieverEngine]
   - etc.

   The engine type IS the primary differentiator between agent types.


   .. autolink-examples:: SimpleAgent
      :collapse:

.. py:class:: Workflow

   Bases: :py:obj:`abc.ABC`


   Pure workflow - no engine.


   .. autolink-examples:: Workflow
      :collapse:

   .. py:method:: execute(input_data: Any) -> Any
      :abstractmethod:

      :async:


      Execute workflow logic.


      .. autolink-examples:: execute
         :collapse:


.. py:data:: EngineT

.. py:data:: config

