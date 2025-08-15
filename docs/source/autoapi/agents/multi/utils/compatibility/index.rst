agents.multi.utils.compatibility
================================

.. py:module:: agents.multi.utils.compatibility

.. autoapi-nested-parse::

   Compatibility module for legacy multi-agent imports.

   This module provides backward compatibility for code that imports from:
   - haive.agents.multi.base
   - haive.agents.multi.multi_agent
   - haive.agents.multi.base_multi_agent

   New code should use:
   - haive.agents.multi.clean.MultiAgent (current default)
   - haive.agents.multi.enhanced_multi_agent_v4.MultiAgent (recommended)


   .. autolink-examples:: agents.multi.utils.compatibility
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.multi.utils.compatibility.BaseMultiAgent
   agents.multi.utils.compatibility.BranchAgent
   agents.multi.utils.compatibility.ConditionalAgent
   agents.multi.utils.compatibility.ParallelAgent
   agents.multi.utils.compatibility.SequentialAgent


Classes
-------

.. autoapisummary::

   agents.multi.utils.compatibility.ExecutionMode


Module Contents
---------------

.. py:class:: ExecutionMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Legacy ExecutionMode enum for backward compatibility.

   Modern implementations use string literals instead:
   - "sequential"
   - "parallel"
   - "conditional"
   - "branch"
   - "infer"

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionMode
      :collapse:

   .. py:attribute:: BRANCH
      :value: 'branch'



   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: INFER
      :value: 'infer'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



.. py:data:: BaseMultiAgent

.. py:data:: BranchAgent

.. py:data:: ConditionalAgent

.. py:data:: ParallelAgent

.. py:data:: SequentialAgent

