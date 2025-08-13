
:py:mod:`agents.react_class.react_agent.agent`
==============================================

.. py:module:: agents.react_class.react_agent.agent


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent.agent.ReactAgent
   agents.react_class.react_agent.agent.ReactAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgent {
        node [shape=record];
        "ReactAgent" [label="ReactAgent"];
        "haive.core.engine.agent.agent.Agent[ReactAgentConfig]" -> "ReactAgent";
      }

.. autoclass:: agents.react_class.react_agent.agent.ReactAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgentConfig {
        node [shape=record];
        "ReactAgentConfig" [label="ReactAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "ReactAgentConfig";
      }

.. autoclass:: agents.react_class.react_agent.agent.ReactAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent.agent.chat_react_agent
   agents.react_class.react_agent.agent.chat_react_agent_with_tool_node
   agents.react_class.react_agent.agent.create_react_agent
   agents.react_class.react_agent.agent.run_react_agent
   agents.react_class.react_agent.agent.should_continue

.. py:function:: chat_react_agent(config: ReactAgentConfig = ReactAgentConfig())

   Start a chat session with ReactAgent.


   .. autolink-examples:: chat_react_agent
      :collapse:

.. py:function:: chat_react_agent_with_tool_node(config: ReactAgentConfig = ReactAgentConfig())

   Start a chat session with ReactAgent.


   .. autolink-examples:: chat_react_agent_with_tool_node
      :collapse:

.. py:function:: create_react_agent(config: ReactAgentConfig = ReactAgentConfig()) -> ReactAgent

   Factory function to create a ReactAgent.


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: run_react_agent(input_text: str, config: ReactAgentConfig = ReactAgentConfig())

   Execute ReactAgent with a given input.


   .. autolink-examples:: run_react_agent
      :collapse:

.. py:function:: should_continue(state: haive.agents.react_class.react_agent.state.ReactAgentState) -> str



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent.agent
   :collapse:
   
.. autolink-skip:: next
