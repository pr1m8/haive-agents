agents.planning.llm_compiler.tools.math_tools
=============================================

.. py:module:: agents.planning.llm_compiler.tools.math_tools


Attributes
----------

.. autoapisummary::

   agents.planning.llm_compiler.tools.math_tools._ADDITIONAL_CONTEXT_PROMPT
   agents.planning.llm_compiler.tools.math_tools._MATH_DESCRIPTION
   agents.planning.llm_compiler.tools.math_tools._SYSTEM_PROMPT


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler.tools.math_tools._evaluate_expression
   agents.planning.llm_compiler.tools.math_tools.get_math_tool


Module Contents
---------------

.. py:function:: _evaluate_expression(expression: str) -> str

.. py:function:: get_math_tool(llm: langchain_openai.ChatOpenAI)

.. py:data:: _ADDITIONAL_CONTEXT_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """The following additional context is provided from other functions.    Use it to substitute into any ${{#}} variables or other words in the problem.    
      
      ${context}
      
      Note that context variables are not defined in code yet.You must extract the relevant numbers and directly put them in code."""

   .. raw:: html

      </details>



.. py:data:: _MATH_DESCRIPTION
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """math(problem: str, context: Optional[list[str]]) -> float:
       - Solves the provided math problem.
       - `problem` can be either a simple math problem (e.g. "1 + 3") or a word problem (e.g. "how many apples are there if there are 3 apples and 2 apples").
       - You cannot calculate multiple expressions in one call. For instance, `math('1 + 3, 2 + 4')` does not work. If you need to calculate multiple expressions, you need to call them separately like `math('1 + 3')` and then `math('2 + 4')`
       - Minimize the number of `math` actions as much as possible. For instance, instead of calling 2. math("what is the 10% of $1") and then call 3. math("$1 + $2"), you MUST call 2. math("what is the 110% of $1") instead, which will reduce the number of math actions.
       - You can optionally provide a list of strings as `context` to help the agent solve the problem. If there are multiple contexts you need to answer the question, you can provide them as a list of strings.
       - `math` action will not see the output of the previous actions unless you provide it as `context`. You MUST provide the output of the previous actions as `context` if you need to do math on it.
       - You MUST NEVER provide `search` type action's outputs as a variable in the `problem` argument. This is because `search` returns a text blob that contains the information about the entity, not a number or value. Therefore, when you need to provide an output of `search` action, you MUST provide it as a `context` argument to `math` action. For example, 1. search("Barack Obama") and then 2. math("age of $1") is NEVER allowed. Use 2. math("age of Barack Obama", context=["$1"]) instead.
       - When you ask a question about `context`, specify the units. For instance, "what is xx in height?" or "what is xx in millions?" instead of "what is xx?"
      """

   .. raw:: html

      </details>



.. py:data:: _SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Translate a math problem into a expression that can be executed using Python's numexpr library. Use the output of running this code to answer the question.
      
      Question: ${{Question with math problem.}}
      
      
      ${{single line mathematical expression that solves the problem}}
      
      ...numexpr.evaluate(text)...
      
      
      ${{Output of running the code}}
      
      Answer: ${{Answer}}
      
      Begin.
      
      Question: What is 37593 * 67?
      ExecuteCode({{code: "37593 * 67"}})
      ...numexpr.evaluate("37593 * 67")...
      
      
      2518731
      
      Answer: 2518731
      
      Question: 37593^(1/5)
      ExecuteCode({{code: "37593**(1/5)"}})
      ...numexpr.evaluate("37593**(1/5)")...
      
      
      8.222831614237718
      
      Answer: 8.222831614237718
      """

   .. raw:: html

      </details>



