agents.simple.agent_v3_minimal
==============================

.. py:module:: agents.simple.agent_v3_minimal

.. autoapi-nested-parse::

   SimpleAgent v3 implementation with minimal import overhead.

   This implementation provides the same SimpleAgentV3 functionality but with
   lazy loading of all heavy dependencies to achieve sub-5 second import times.

   Usage:
       # Fast import - no heavy dependencies loaded
       from haive.agents.simple.agent_v3_minimal import SimpleAgentV3Minimal as SimpleAgentV3

       # Full functionality available when actually used
       agent = SimpleAgent(name="test")
       result = await agent.arun("Hello")


   .. autolink-examples:: agents.simple.agent_v3_minimal
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/simple/agent_v3_minimal/v2/index


Attributes
----------

.. autoapisummary::

   agents.simple.agent_v3_minimal.SimpleAgentV3
   agents.simple.agent_v3_minimal._SimpleAgentV3


Classes
-------

.. autoapisummary::

   agents.simple.agent_v3_minimal.SimpleAgentV3Minimal


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


