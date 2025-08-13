
:py:mod:`agents.document_modifiers.tnt.utils`
=============================================

.. py:module:: agents.document_modifiers.tnt.utils

Utility functions for taxonomy generation and document processing.

This module provides utility functions for parsing, formatting, and managing
taxonomy-related data structures. It includes functions for handling XML-formatted
outputs, document summaries, and taxonomy clusters.

.. note::

   All XML parsing functions assume well-formed XML input with specific expected tags.
   Malformed XML may raise parsing errors.

.. rubric:: Example

Basic usage for taxonomy parsing::

    xml_output = '''
        <id>1</id>
        <name>Category A</name>
        <description>Description text</description>
    '''
    taxonomy = parse_taxonomy(xml_output)


.. autolink-examples:: agents.document_modifiers.tnt.utils
   :collapse:


Functions
---------

.. autoapisummary::

   agents.document_modifiers.tnt.utils.format_docs
   agents.document_modifiers.tnt.utils.format_taxonomy
   agents.document_modifiers.tnt.utils.format_taxonomy_md
   agents.document_modifiers.tnt.utils.get_content
   agents.document_modifiers.tnt.utils.parse_labels
   agents.document_modifiers.tnt.utils.parse_summary
   agents.document_modifiers.tnt.utils.parse_taxonomy
   agents.document_modifiers.tnt.utils.reduce_summaries

.. py:function:: format_docs(docs: list[langchain_core.documents.Document]) -> str

   Format documents as XML table for taxonomy generation.

   :param docs: List of Document objects, each must have:
                - id: Document identifier
                - summary: Document summary text

   :returns: XML-formatted string containing conversation summaries
   :rtype: str

   .. rubric:: Example

   >>> docs = [Document(id="1", summary="text")]
   >>> xml = format_docs(docs)
   >>> print(xml)
   <conversations>
   <conv_summ id=1>text</conv_summ>
   </conversations>


   .. autolink-examples:: format_docs
      :collapse:

.. py:function:: format_taxonomy(clusters: list[dict]) -> str

   Convert taxonomy clusters to XML format.

   :param clusters: List of cluster dictionaries, each containing:
                    - id (str): Cluster identifier
                    - name (str): Cluster name
                    - description (str): Cluster description

   :returns: XML-formatted taxonomy string
   :rtype: str

   .. rubric:: Example

   >>> clusters = [{"id": "1", "name": "Tech", "description": "Technology"}]
   >>> xml = format_taxonomy(clusters)
   >>> print(xml)
   <cluster_table>
     <cluster>
       <id>1</id>
       <name>Tech</name>
       <description>Technology</description>
     </cluster>
   </cluster_table>


   .. autolink-examples:: format_taxonomy
      :collapse:

.. py:function:: format_taxonomy_md(clusters: list[dict]) -> str

   Format taxonomy clusters as a Markdown table.

   :param clusters: List of cluster dictionaries, each containing:
                    - id (str): Cluster identifier
                    - name (str): Cluster name
                    - description (str): Cluster description

   :returns: Markdown-formatted table string
   :rtype: str

   .. rubric:: Example

   >>> clusters = [{"id": "1", "name": "Tech", "description": "Technology"}]
   >>> md_table = format_taxonomy_md(clusters)


   .. autolink-examples:: format_taxonomy_md
      :collapse:

.. py:function:: get_content(state: haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState) -> list[dict]

   Extract document content from taxonomy generation state.

   :param state: Current state of the taxonomy generation process.
                 Must contain a 'documents' key with list of document dictionaries.

   :returns:

             List of dictionaries, each containing:
                 - content (str): The content of a document
   :rtype: list

   .. rubric:: Example

   >>> state = {"documents": [{"content": "doc1"}, {"content": "doc2"}]}
   >>> contents = get_content(state)
   >>> print(contents)
   [{'content': 'doc1'}, {'content': 'doc2'}]


   .. autolink-examples:: get_content
      :collapse:

.. py:function:: parse_labels(output_text: str) -> dict

   Parse category labels from prediction output.

   Extracts category information from XML-formatted prediction text.
   Handles multiple categories but returns only the first one.

   :param output_text: XML-formatted string containing category predictions.
                       Expected format::
                           <category>Label Name</category>

   :returns:

             Dictionary containing:
                 - category (str): The first category label found
   :rtype: dict

   .. note::

      If multiple categories are found, a warning is logged and only
      the first category is returned.

   .. rubric:: Example

   >>> text = "<category>Technology</category>"
   >>> result = parse_labels(text)
   >>> print(result)
   {'category': 'Technology'}


   .. autolink-examples:: parse_labels
      :collapse:

.. py:function:: parse_summary(xml_string: str) -> dict

   Parse summary and explanation from XML-formatted string.

   Extracts the content within <summary> and <explanation> tags from the input XML string.
   If tags are not found, returns empty strings for the missing elements.

   :param xml_string: XML-formatted string containing <summary> and <explanation> tags.
                      Example::
                          <summary>Main points...</summary>
                          <explanation>Detailed analysis...</explanation>

   :returns:

             Dictionary containing:
                 - summary (str): Content within <summary> tags
                 - explanation (str): Content within <explanation> tags
   :rtype: dict

   .. rubric:: Example

   >>> xml = "<summary>Key points</summary><explanation>Details</explanation>"
   >>> result = parse_summary(xml)
   >>> print(result)
   {'summary': 'Key points', 'explanation': 'Details'}


   .. autolink-examples:: parse_summary
      :collapse:

.. py:function:: parse_taxonomy(output_text: str) -> dict

   Parse taxonomy information from LLM-generated output.

   Extracts cluster information including IDs, names, and descriptions from
   XML-formatted output text.

   :param output_text: XML-formatted string containing taxonomy clusters.
                       Expected format::
                           <id>1</id>
                           <name>Category Name</name>
                           <description>Category Description</description>

   :returns:

             Dictionary containing:
                 - clusters (list): List of dictionaries, each with:
                     - id (str): Cluster identifier
                     - name (str): Cluster name
                     - description (str): Cluster description
   :rtype: dict

   .. rubric:: Example

   >>> text = "<id>1</id><name>Tech</name><description>Technology</description>"
   >>> taxonomy = parse_taxonomy(text)
   >>> print(taxonomy)
   {'clusters': [{'id': '1', 'name': 'Tech', 'description': 'Technology'}]}


   .. autolink-examples:: parse_taxonomy
      :collapse:

.. py:function:: reduce_summaries(combined: dict) -> haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState

   Merge summarized content with original documents.

   Takes a dictionary containing both original documents and their summaries,
   and combines them into a single state object.

   :param combined: Dictionary containing:
                    - documents (list): Original document list
                    - summaries (list): Corresponding summaries

   :returns:

             Updated state containing:
                 - documents (list): List of documents with added summaries
   :rtype: TaxonomyGenerationState

   .. rubric:: Example

   >>> combined = {
   ...     "documents": [{"id": 1, "content": "text"}],
   ...     "summaries": [{"summary": "sum", "explanation": "exp"}]
   ... }
   >>> state = reduce_summaries(combined)


   .. autolink-examples:: reduce_summaries
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.tnt.utils
   :collapse:
   
.. autolink-skip:: next
