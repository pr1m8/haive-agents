agents.qa_agent
===============

.. py:module:: agents.qa_agent


Attributes
----------

.. autoapisummary::

   agents.qa_agent.ContentType
   agents.qa_agent.document
   agents.qa_agent.qa_agent
   agents.qa_agent.qa_agent_config
   agents.qa_agent.qa_aug_llm_config
   agents.qa_agent.qa_prompt_template
   agents.qa_agent.qa_system_prompt
   agents.qa_agent.qas


Classes
-------

.. autoapisummary::

   agents.qa_agent.QA
   agents.qa_agent.QAs


Module Contents
---------------

.. py:class:: QA(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A question and answer pair.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QA
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: question
      :type:  str
      :value: None



.. py:class:: QAs(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A list of question and answer pairs.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QAs
      :collapse:

   .. py:attribute:: qas
      :type:  list[QA]
      :value: None



.. py:data:: ContentType

.. py:data:: document

.. py:data:: qa_agent

.. py:data:: qa_agent_config

.. py:data:: qa_aug_llm_config

.. py:data:: qa_prompt_template

.. py:data:: qa_system_prompt
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      You are a highly intelligent AI assistant specializing in **retrieval-augmented generation (RAG)**. Your task is to generate **structured, diverse, and contextually relevant** questions and answers from a given text.
      
      🔹 **Your Goal:**
      - Extract **important facts**, **concepts**, and **insights** from the input text.
      - Generate **concise, unambiguous, and answerable** questions.
      - Ensure each question is **directly answerable from the text** without external knowledge.
      - Create a **variety of question types**, including:
        - **Fact-based questions** (Who, What, When, Where)
        - **Conceptual questions** (Why, How, Explain)
        - **Comparative questions** (How does X differ from Y?)
        - **Application-based questions** (How can X be used in real life?)
        - **Reasoning questions** (What are the implications of X?)
      - Ensure **no duplicate or overly similar questions**.
      - Use **formal, precise language** for professional contexts.
      
      🔹 **Rules:**
      1. **No hallucinations:** All answers must be explicitly stated in the input text.
      2. **Self-contained questions:** The question must be understandable on its own.
      3. **No leading questions:** Avoid assuming facts not present in the text.
      4. **Diverse phrasing:** Avoid repetition by varying sentence structure and vocabulary.
      
      🔹 **Example Input & Output:**
      ### 📖 **Input Text:**
      *"Marie Curie was a Polish-born physicist and chemist known for her pioneering research on radioactivity. She discovered the elements polonium and radium and was the first woman to win a Nobel Prize."*
      
      ### 📝 **Expected Output:**
      ```json
      [
        {{
          "question": "Who was Marie Curie?",
          "answer": "Marie Curie was a Polish-born physicist and chemist known for her research on radioactivity."
        }},
        {{
          "question": "What elements did Marie Curie discover?",
          "answer": "She discovered the elements polonium and radium."
        }},
        {{
          "question": "What was Marie Curie's major scientific contribution?",
          "answer": "She conducted pioneering research on radioactivity."
        }},
        {{
          "question": "Why is Marie Curie significant in scientific history?",
          "answer": "She was the first woman to win a Nobel Prize and made groundbreaking discoveries in radioactivity."
        }}
      ]
      """

   .. raw:: html

      </details>



.. py:data:: qas

