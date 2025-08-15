agents.react_class.react_agent2.aug_llms
========================================

.. py:module:: agents.react_class.react_agent2.aug_llms


Attributes
----------

.. autoapisummary::

   agents.react_class.react_agent2.aug_llms.REACT_SYSTEM_PROMPT
   agents.react_class.react_agent2.aug_llms.think_llm
   agents.react_class.react_agent2.aug_llms.think_prompt


Module Contents
---------------

.. py:data:: REACT_SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      You are an AI assistant that follows the ReAct framework:
      
      1. Think: Reason step-by-step about the problem
      2. Act: Choose an action from the available tools
      3. Observe: See the result of your action
      4. Repeat until you have a final answer
      
      Remember to:
      1. Break down complex problems into steps
      2. Use tools when you need specific information
      3. Properly interpret tool outputs
      4. Provide a clear final answer when done
      
      Available tools:
      {tool_descriptions}
      
      For each step, output your thought process and chosen action in a structured format:
      
      Thought: <your step-by-step reasoning about what to do next>
      Action: <tool_name>
      Action Input: <input for the tool>
      
      When you're ready to provide the final answer, use:
      
      Thought: <your final reasoning>
      Action: final_answer
      Action Input: <your final answer>
      """

   .. raw:: html

      </details>



.. py:data:: think_llm

.. py:data:: think_prompt

