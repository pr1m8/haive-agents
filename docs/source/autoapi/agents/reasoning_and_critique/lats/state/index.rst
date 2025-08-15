agents.reasoning_and_critique.lats.state
========================================

.. py:module:: agents.reasoning_and_critique.lats.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.state.TreeState


Module Contents
---------------

.. py:class:: TreeState

   Bases: :py:obj:`typing_extensions.TypedDict`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TreeState
      :collapse:

   .. py:attribute:: input
      :type:  str


   .. py:attribute:: root
      :type:  haive.agents.reasoning_and_critique.lats.node.Node


