
:py:mod:`agents.research.open_perplexity.structured_tools`
==========================================================

.. py:module:: agents.research.open_perplexity.structured_tools


Classes
-------

.. autoapisummary::

   agents.research.open_perplexity.structured_tools.ArxivLoaderInput
   agents.research.open_perplexity.structured_tools.DocumentLoaderDescriptionInput
   agents.research.open_perplexity.structured_tools.DocumentLoaderRecommendationInput
   agents.research.open_perplexity.structured_tools.EnhancedArxivLoader
   agents.research.open_perplexity.structured_tools.EnhancedGitHubIssuesLoader
   agents.research.open_perplexity.structured_tools.EnhancedHNLoader
   agents.research.open_perplexity.structured_tools.EnhancedRecursiveUrlLoader
   agents.research.open_perplexity.structured_tools.EnhancedWebBaseLoader
   agents.research.open_perplexity.structured_tools.GitHubIssuesLoaderInput
   agents.research.open_perplexity.structured_tools.GitHubLoader
   agents.research.open_perplexity.structured_tools.HackerNewsLoaderInput
   agents.research.open_perplexity.structured_tools.RecursiveWebLoaderInput
   agents.research.open_perplexity.structured_tools.TavilySearchInput
   agents.research.open_perplexity.structured_tools.WebLoaderInput
   agents.research.open_perplexity.structured_tools.WebScraper


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ArxivLoaderInput:

   .. graphviz::
      :align: center

      digraph inheritance_ArxivLoaderInput {
        node [shape=record];
        "ArxivLoaderInput" [label="ArxivLoaderInput"];
        "pydantic.BaseModel" -> "ArxivLoaderInput";
      }

.. autopydantic_model:: agents.research.open_perplexity.structured_tools.ArxivLoaderInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentLoaderDescriptionInput:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentLoaderDescriptionInput {
        node [shape=record];
        "DocumentLoaderDescriptionInput" [label="DocumentLoaderDescriptionInput"];
        "pydantic.BaseModel" -> "DocumentLoaderDescriptionInput";
      }

.. autopydantic_model:: agents.research.open_perplexity.structured_tools.DocumentLoaderDescriptionInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentLoaderRecommendationInput:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentLoaderRecommendationInput {
        node [shape=record];
        "DocumentLoaderRecommendationInput" [label="DocumentLoaderRecommendationInput"];
        "pydantic.BaseModel" -> "DocumentLoaderRecommendationInput";
      }

.. autopydantic_model:: agents.research.open_perplexity.structured_tools.DocumentLoaderRecommendationInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedArxivLoader:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedArxivLoader {
        node [shape=record];
        "EnhancedArxivLoader" [label="EnhancedArxivLoader"];
        "langchain_community.document_loaders.ArxivLoader" -> "EnhancedArxivLoader";
      }

.. autoclass:: agents.research.open_perplexity.structured_tools.EnhancedArxivLoader
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedGitHubIssuesLoader:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedGitHubIssuesLoader {
        node [shape=record];
        "EnhancedGitHubIssuesLoader" [label="EnhancedGitHubIssuesLoader"];
        "langchain_community.document_loaders.GitHubIssuesLoader" -> "EnhancedGitHubIssuesLoader";
      }

.. autoclass:: agents.research.open_perplexity.structured_tools.EnhancedGitHubIssuesLoader
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedHNLoader:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedHNLoader {
        node [shape=record];
        "EnhancedHNLoader" [label="EnhancedHNLoader"];
        "langchain_community.document_loaders.HNLoader" -> "EnhancedHNLoader";
      }

.. autoclass:: agents.research.open_perplexity.structured_tools.EnhancedHNLoader
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedRecursiveUrlLoader:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedRecursiveUrlLoader {
        node [shape=record];
        "EnhancedRecursiveUrlLoader" [label="EnhancedRecursiveUrlLoader"];
        "langchain_community.document_loaders.RecursiveUrlLoader" -> "EnhancedRecursiveUrlLoader";
      }

.. autoclass:: agents.research.open_perplexity.structured_tools.EnhancedRecursiveUrlLoader
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedWebBaseLoader:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedWebBaseLoader {
        node [shape=record];
        "EnhancedWebBaseLoader" [label="EnhancedWebBaseLoader"];
        "langchain_community.document_loaders.WebBaseLoader" -> "EnhancedWebBaseLoader";
      }

.. autoclass:: agents.research.open_perplexity.structured_tools.EnhancedWebBaseLoader
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GitHubIssuesLoaderInput:

   .. graphviz::
      :align: center

      digraph inheritance_GitHubIssuesLoaderInput {
        node [shape=record];
        "GitHubIssuesLoaderInput" [label="GitHubIssuesLoaderInput"];
        "pydantic.BaseModel" -> "GitHubIssuesLoaderInput";
      }

.. autopydantic_model:: agents.research.open_perplexity.structured_tools.GitHubIssuesLoaderInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GitHubLoader:

   .. graphviz::
      :align: center

      digraph inheritance_GitHubLoader {
        node [shape=record];
        "GitHubLoader" [label="GitHubLoader"];
      }

.. autoclass:: agents.research.open_perplexity.structured_tools.GitHubLoader
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HackerNewsLoaderInput:

   .. graphviz::
      :align: center

      digraph inheritance_HackerNewsLoaderInput {
        node [shape=record];
        "HackerNewsLoaderInput" [label="HackerNewsLoaderInput"];
        "pydantic.BaseModel" -> "HackerNewsLoaderInput";
      }

.. autopydantic_model:: agents.research.open_perplexity.structured_tools.HackerNewsLoaderInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RecursiveWebLoaderInput:

   .. graphviz::
      :align: center

      digraph inheritance_RecursiveWebLoaderInput {
        node [shape=record];
        "RecursiveWebLoaderInput" [label="RecursiveWebLoaderInput"];
        "pydantic.BaseModel" -> "RecursiveWebLoaderInput";
      }

.. autopydantic_model:: agents.research.open_perplexity.structured_tools.RecursiveWebLoaderInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TavilySearchInput:

   .. graphviz::
      :align: center

      digraph inheritance_TavilySearchInput {
        node [shape=record];
        "TavilySearchInput" [label="TavilySearchInput"];
        "pydantic.BaseModel" -> "TavilySearchInput";
      }

.. autopydantic_model:: agents.research.open_perplexity.structured_tools.TavilySearchInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WebLoaderInput:

   .. graphviz::
      :align: center

      digraph inheritance_WebLoaderInput {
        node [shape=record];
        "WebLoaderInput" [label="WebLoaderInput"];
        "pydantic.BaseModel" -> "WebLoaderInput";
      }

.. autopydantic_model:: agents.research.open_perplexity.structured_tools.WebLoaderInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WebScraper:

   .. graphviz::
      :align: center

      digraph inheritance_WebScraper {
        node [shape=record];
        "WebScraper" [label="WebScraper"];
      }

.. autoclass:: agents.research.open_perplexity.structured_tools.WebScraper
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.research.open_perplexity.structured_tools.describe_document_loader
   agents.research.open_perplexity.structured_tools.get_available_loaders
   agents.research.open_perplexity.structured_tools.load_arxiv_papers
   agents.research.open_perplexity.structured_tools.load_github_issues
   agents.research.open_perplexity.structured_tools.load_hackernews_thread
   agents.research.open_perplexity.structured_tools.load_recursive_web
   agents.research.open_perplexity.structured_tools.load_web_page
   agents.research.open_perplexity.structured_tools.recommend_document_loaders
   agents.research.open_perplexity.structured_tools.register_document_loader

.. py:function:: describe_document_loader(loader_type: str) -> dict[str, Any]

   Get detailed description of a document loader.


   .. autolink-examples:: describe_document_loader
      :collapse:

.. py:function:: get_available_loaders() -> dict[str, dict]

   Get all available document loaders with their metadata.


   .. autolink-examples:: get_available_loaders
      :collapse:

.. py:function:: load_arxiv_papers(query: str, max_results: int = 5, load_all_available_meta: bool = True) -> dict[str, Any]

   Load papers from ArXiv.


   .. autolink-examples:: load_arxiv_papers
      :collapse:

.. py:function:: load_github_issues(repo: str, access_token: str | None = None, state: str = 'open') -> dict[str, Any]

   Load issues from a GitHub repository.


   .. autolink-examples:: load_github_issues
      :collapse:

.. py:function:: load_hackernews_thread(story_id: int) -> dict[str, Any]

   Load a Hacker News thread.


   .. autolink-examples:: load_hackernews_thread
      :collapse:

.. py:function:: load_recursive_web(url: str, max_depth: int = 2, prevent_outside: bool = True) -> dict[str, Any]

   Recursively crawl a website.


   .. autolink-examples:: load_recursive_web
      :collapse:

.. py:function:: load_web_page(url: str) -> list[dict[str, Any]]

   Load content from a web page.


   .. autolink-examples:: load_web_page
      :collapse:

.. py:function:: recommend_document_loaders(research_topic: str, research_question: str | None = None, data_types: list[str] | None = None) -> list[dict[str, Any]]

   Recommend document loaders based on research topic and question.


   .. autolink-examples:: recommend_document_loaders
      :collapse:

.. py:function:: register_document_loader(loader_type: str)

   Decorator to register document loaders with metadata.


   .. autolink-examples:: register_document_loader
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.research.open_perplexity.structured_tools
   :collapse:
   
.. autolink-skip:: next
