agents.react_class.react_v2.graph_utils
=======================================

.. py:module:: agents.react_class.react_v2.graph_utils


Attributes
----------

.. autoapisummary::

   agents.react_class.react_v2.graph_utils.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_v2.graph_utils.ReactGraphBuilder


Module Contents
---------------

.. py:class:: ReactGraphBuilder(components=None, custom_fields=None, state_schema=None)

   Bases: :py:obj:`haive.core.graph.dynamic_graph_builder.DynamicGraph`


   Enhanced graph builder for React agents with support for human interaction.

   Initialize the React graph builder.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactGraphBuilder
      :collapse:

   .. py:method:: add_human_node(name: str, handler: collections.abc.Callable, goto: str | None = None)

      Add a human interaction node to the graph.

      :param name: Name for the human node
      :param handler: Function to handle the human interaction
      :param goto: Where to route after human input (or None for conditional)

      :returns: Self for chaining


      .. autolink-examples:: add_human_node
         :collapse:


   .. py:method:: add_tool_node(name: str, tools: list[langchain_core.tools.BaseTool], support_human_input: bool = True, parallel_tools: bool = True, human_node_name: str | None = 'human_input', command_goto: str | None = None)

      Add an enhanced tool node with optional human interaction support.

      :param name: Name of the node
      :param tools: List of tools
      :param support_human_input: Whether to support human interaction
      :param parallel_tools: Whether to run tools in parallel
      :param human_node_name: Name for the human input node
      :param command_goto: Where to route after tool execution

      :returns: Self for chaining


      .. autolink-examples:: add_tool_node
         :collapse:


   .. py:attribute:: has_human_node
      :value: False



.. py:data:: logger

