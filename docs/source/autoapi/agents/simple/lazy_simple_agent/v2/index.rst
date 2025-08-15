agents.simple.lazy_simple_agent.v2
==================================

.. py:module:: agents.simple.lazy_simple_agent.v2

.. autoapi-nested-parse::

   Lazy_Simple_Agent core module.

   This module provides lazy simple agent functionality for the Haive framework.

   Classes:
       LazyAugLLMConfig: LazyAugLLMConfig implementation.
       LazyAgent: LazyAgent implementation.
       Agent: Agent implementation.

   Functions:
       cached_import: Cached Import functionality.


   .. autolink-examples:: agents.simple.lazy_simple_agent.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.lazy_simple_agent.v2.SimpleAgentV3
   agents.simple.lazy_simple_agent.v2._CLASS_CACHE
   agents.simple.lazy_simple_agent.v2._MODULE_CACHE
   agents.simple.lazy_simple_agent.v2.logger


Classes
-------

.. autoapisummary::

   agents.simple.lazy_simple_agent.v2.LazyAgent
   agents.simple.lazy_simple_agent.v2.LazyAugLLMConfig
   agents.simple.lazy_simple_agent.v2.LazySimpleAgent


Functions
---------

.. autoapisummary::

   agents.simple.lazy_simple_agent.v2.cached_import


Module Contents
---------------

.. py:class:: LazyAgent(**kwargs)

   Lazy proxy for Agent base class.


   .. autolink-examples:: LazyAgent
      :collapse:

   .. py:method:: __getattr__(name: str)

      Proxy all method calls to real instance.


      .. autolink-examples:: __getattr__
         :collapse:


   .. py:method:: _ensure_initialized()

      Initialize real Agent only when needed.


      .. autolink-examples:: _ensure_initialized
         :collapse:


   .. py:attribute:: _init_kwargs


   .. py:attribute:: _is_initialized
      :value: False



   .. py:attribute:: _real_instance
      :value: None



   .. py:attribute:: name


.. py:class:: LazyAugLLMConfig(**kwargs)

   Lazy proxy for AugLLMConfig that defers all heavy imports.


   .. autolink-examples:: LazyAugLLMConfig
      :collapse:

   .. py:method:: __call__(*args, **kwargs)

      Make callable like real AugLLMConfig.


      .. autolink-examples:: __call__
         :collapse:


   .. py:method:: __getattr__(name: str)

      Proxy all attribute access to real instance.


      .. autolink-examples:: __getattr__
         :collapse:


   .. py:method:: __setattr__(name: str, value: Any)

      Proxy attribute setting.


      .. autolink-examples:: __setattr__
         :collapse:


   .. py:method:: _ensure_initialized()

      Initialize the real AugLLMConfig only when needed.


      .. autolink-examples:: _ensure_initialized
         :collapse:


   .. py:attribute:: _init_kwargs


   .. py:attribute:: _is_initialized
      :value: False



   .. py:attribute:: _real_instance
      :value: None



   .. py:attribute:: max_tokens


   .. py:attribute:: model


   .. py:attribute:: name


   .. py:attribute:: temperature


.. py:class:: LazySimpleAgent(name: str = 'LazySimpleAgent', engine: Any | None = None, temperature: float | None = None, max_tokens: int | None = None, model_name: str | None = None, debug: bool = True, **kwargs)

   Ultra-optimized SimpleAgent with comprehensive lazy loading.

   Initialize with minimal overhead - no heavy imports.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LazySimpleAgent
      :collapse:

   .. py:method:: __getattr__(name: str)

      Lazy proxy all attribute access to real instance.


      .. autolink-examples:: __getattr__
         :collapse:


   .. py:method:: __repr__() -> str


   .. py:method:: __setattr__(name: str, value: Any)

      Proxy attribute setting.


      .. autolink-examples:: __setattr__
         :collapse:


   .. py:method:: _ensure_initialized()

      Initialize the real SimpleAgentV3 only when actually needed.


      .. autolink-examples:: _ensure_initialized
         :collapse:


   .. py:method:: arun(*args, **kwargs)
      :async:


      Async run - triggers full initialization.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: as_structured_tool(*args, **kwargs)
      :classmethod:


      Create structured tool - triggers full initialization.


      .. autolink-examples:: as_structured_tool
         :collapse:


   .. py:method:: as_tool(*args, **kwargs)
      :classmethod:


      Create tool - triggers full initialization.


      .. autolink-examples:: as_tool
         :collapse:


   .. py:method:: run(*args, **kwargs)

      Sync run - triggers full initialization.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: _debug
      :value: True



   .. py:attribute:: _init_kwargs


   .. py:attribute:: _init_time


   .. py:attribute:: _is_initialized
      :value: False



   .. py:attribute:: _name
      :value: 'LazySimpleAgent'



   .. py:attribute:: _real_instance
      :value: None



   .. py:property:: name
      :type: str



.. py:function:: cached_import(module_path: str, class_name: str | None = None)

   Cached import with intelligent loading.


   .. autolink-examples:: cached_import
      :collapse:

.. py:data:: SimpleAgentV3

.. py:data:: _CLASS_CACHE
   :type:  dict[str, Any]

.. py:data:: _MODULE_CACHE
   :type:  dict[str, Any]

.. py:data:: logger

