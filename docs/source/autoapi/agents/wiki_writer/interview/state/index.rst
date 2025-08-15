agents.wiki_writer.interview.state
==================================

.. py:module:: agents.wiki_writer.interview.state


Classes
-------

.. autoapisummary::

   agents.wiki_writer.interview.state.InterviewState


Module Contents
---------------

.. py:class:: InterviewState

   Bases: :py:obj:`TypedDict`


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


   .. autolink-examples:: InterviewState
      :collapse:

   .. py:attribute:: editor
      :type:  Annotated[haive.agents.wiki_writer.interview.models.Editor | None, haive.agents.wiki_writer.interview.utils.update_editor]


   .. py:attribute:: messages
      :type:  Annotated[list[langchain_core.messages.AnyMessage], haive.agents.wiki_writer.interview.utils.add_messages]


   .. py:attribute:: references
      :type:  Annotated[dict | None, haive.agents.wiki_writer.interview.utils.update_references]


