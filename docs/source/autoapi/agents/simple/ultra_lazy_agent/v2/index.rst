agents.simple.ultra_lazy_agent.v2
=================================

.. py:module:: agents.simple.ultra_lazy_agent.v2

.. autoapi-nested-parse::

   Ultra_Lazy_Agent core module.

   This module provides ultra lazy agent functionality for the Haive framework.

   Classes:
       UltraLazyAgent: UltraLazyAgent implementation.

   Functions:
       name: Name functionality.


   .. autolink-examples:: agents.simple.ultra_lazy_agent.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.ultra_lazy_agent.v2.SimpleAgentV3


Classes
-------

.. autoapisummary::

   agents.simple.ultra_lazy_agent.v2.UltraLazyAgent


Module Contents
---------------

.. py:class:: UltraLazyAgent(name: str = 'UltraLazyAgent', **kwargs)

   Ultra-minimal agent proxy with maximum lazy loading.


   .. autolink-examples:: UltraLazyAgent
      :collapse:

   .. py:method:: __call__(*args, **kwargs)

      Make callable.


      .. autolink-examples:: __call__
         :collapse:


   .. py:method:: __getattr__(name: str)

      Proxy everything to real agent.


      .. autolink-examples:: __getattr__
         :collapse:


   .. py:method:: __repr__() -> str


   .. py:method:: __setattr__(name: str, value: Any)

      Handle attribute setting.


      .. autolink-examples:: __setattr__
         :collapse:


   .. py:method:: _load_real_agent()

      Load the real SimpleAgentV3 only when absolutely necessary.


      .. autolink-examples:: _load_real_agent
         :collapse:


   .. py:method:: arun(*args, **kwargs)
      :async:


      Async run - triggers loading.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: as_structured_tool(**kwargs)
      :classmethod:


      Class method - triggers loading.


      .. autolink-examples:: as_structured_tool
         :collapse:


   .. py:method:: as_tool(**kwargs)
      :classmethod:


      Class method - triggers loading.


      .. autolink-examples:: as_tool
         :collapse:


   .. py:method:: run(*args, **kwargs)

      Sync run - triggers loading.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: _initialized
      :value: False



   .. py:attribute:: _kwargs


   .. py:attribute:: _name
      :value: 'UltraLazyAgent'



   .. py:attribute:: _real_agent
      :value: None



   .. py:property:: name
      :type: str



.. py:data:: SimpleAgentV3

