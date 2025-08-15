agents.experiments.dynamic_supervisor_enhanced
==============================================

.. py:module:: agents.experiments.dynamic_supervisor_enhanced

.. autoapi-nested-parse::

   Enhanced Dynamic Supervisor with self-modification capabilities.


   .. autolink-examples:: agents.experiments.dynamic_supervisor_enhanced
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.experiments.dynamic_supervisor_enhanced.logger


Classes
-------

.. autoapisummary::

   agents.experiments.dynamic_supervisor_enhanced.SelfModifyingSupervisor


Functions
---------

.. autoapisummary::

   agents.experiments.dynamic_supervisor_enhanced.create_agent_management_tools
   agents.experiments.dynamic_supervisor_enhanced.demo_self_modifying_supervisor


Module Contents
---------------

.. py:class:: SelfModifyingSupervisor(*args, enable_self_modification: bool = True, **kwargs)

   Bases: :py:obj:`haive.agents.experiments.dynamic_supervisor.DynamicSupervisorAgent`


   A supervisor that can modify its own agent registry based on task requirements.

   Initialize with self-modification capabilities.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelfModifyingSupervisor
      :collapse:

   .. py:method:: _create_dynamic_tools() -> list

      Create tools including self-modification capabilities.


      .. autolink-examples:: _create_dynamic_tools
         :collapse:


   .. py:attribute:: _enable_self_modification
      :value: True



.. py:function:: create_agent_management_tools(supervisor_instance) -> Any

   Create tools that allow the supervisor to manage its own agent registry.


   .. autolink-examples:: create_agent_management_tools
      :collapse:

.. py:function:: demo_self_modifying_supervisor()
   :async:


.. py:data:: logger

