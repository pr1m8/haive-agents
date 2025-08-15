agents.wiki_writer.interview.nodes
==================================

.. py:module:: agents.wiki_writer.interview.nodes


Functions
---------

.. autoapisummary::

   agents.wiki_writer.interview.nodes.gen_answer
   agents.wiki_writer.interview.nodes.generate_question


Module Contents
---------------

.. py:function:: gen_answer(state: haive.agents.wiki_writer.interview.state.InterviewState, config: langchain_core.runnables.RunnableConfig | None = None, name: str = 'Subject_Matter_Expert', max_str_len: int = 15000, search_engine: langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool = tavily_search_tool)
   :async:


.. py:function:: generate_question(state: haive.agents.wiki_writer.interview.state.InterviewState, aug_llm_config: haive.core.engine.aug_llm.AugLLMConfig = gen_qn_aug_llm_config)
   :async:


