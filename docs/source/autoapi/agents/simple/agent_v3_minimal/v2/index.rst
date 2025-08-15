agents.simple.agent_v3_minimal.v2
=================================

.. py:module:: agents.simple.agent_v3_minimal.v2

.. autoapi-nested-parse::

   Agent_V3_Minimal core module.

   This module provides agent v3 minimal functionality for the Haive framework.

   Classes:
       SimpleAgentV3Minimal: SimpleAgentV3Minimal implementation.
       is: is implementation.
       return: return implementation.

   Functions:
       as_tool: As Tool functionality.
       as_structured_tool: As Structured Tool functionality.


   .. autolink-examples:: agents.simple.agent_v3_minimal.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.agent_v3_minimal.v2.SimpleAgentV3
   agents.simple.agent_v3_minimal.v2._SimpleAgentV3


Classes
-------

.. autoapisummary::

   agents.simple.agent_v3_minimal.v2.SimpleAgentV3Minimal


Module Contents
---------------

.. py:class:: SimpleAgentV3Minimal

   Minimal wrapper for SimpleAgentV3 with lazy loading.

   Dynamically import and create the real SimpleAgentV3 instance.


   .. autolink-examples:: __new__
      :collapse:


   .. autolink-examples:: SimpleAgentV3Minimal
      :collapse:

   .. py:method:: as_structured_tool(*args, **kwargs)
      :classmethod:


      Lazy loading for as_structured_tool class method.


      .. autolink-examples:: as_structured_tool
         :collapse:


   .. py:method:: as_tool(*args, **kwargs)
      :classmethod:


      Lazy loading for as_tool class method.


      .. autolink-examples:: as_tool
         :collapse:


   .. py:attribute:: _real_class
      :value: None



.. py:data:: SimpleAgentV3

.. py:data:: _SimpleAgentV3
   :value: None


