agents.research.open_perplexity.structured_tools
================================================

.. py:module:: agents.research.open_perplexity.structured_tools


Attributes
----------

.. autoapisummary::

   agents.research.open_perplexity.structured_tools.DOCUMENT_LOADERS
   agents.research.open_perplexity.structured_tools.DOCUMENT_LOADER_TOOLS
   agents.research.open_perplexity.structured_tools.RESEARCH_TOOLS
   agents.research.open_perplexity.structured_tools.TAVILY_API_KEY
   agents.research.open_perplexity.structured_tools.TavilyClient
   agents.research.open_perplexity.structured_tools.arxiv_loader_tool
   agents.research.open_perplexity.structured_tools.document_loader_description_tool
   agents.research.open_perplexity.structured_tools.github_issues_loader_tool
   agents.research.open_perplexity.structured_tools.hackernews_loader_tool
   agents.research.open_perplexity.structured_tools.recommend_document_loaders_tool
   agents.research.open_perplexity.structured_tools.recursive_web_loader_tool
   agents.research.open_perplexity.structured_tools.web_loader_tool


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


Module Contents
---------------

.. py:class:: ArxivLoaderInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for ArXiv loader.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ArxivLoaderInput
      :collapse:

   .. py:attribute:: load_all_available_meta
      :type:  bool
      :value: None



   .. py:attribute:: max_results
      :type:  int
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



.. py:class:: DocumentLoaderDescriptionInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for document loader description.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentLoaderDescriptionInput
      :collapse:

   .. py:attribute:: loader_type
      :type:  str
      :value: None



.. py:class:: DocumentLoaderRecommendationInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for document loader recommendation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentLoaderRecommendationInput
      :collapse:

   .. py:attribute:: data_types
      :type:  list[str] | None
      :value: None



   .. py:attribute:: research_question
      :type:  str | None
      :value: None



   .. py:attribute:: research_topic
      :type:  str
      :value: None



.. py:class:: EnhancedArxivLoader(query: str, doc_content_chars_max: Optional[int] = None, **kwargs: Any)

   Bases: :py:obj:`langchain_community.document_loaders.ArxivLoader`


   Enhanced Arxiv paper loader with metadata extraction.

   Initialize with search query to find documents in the Arxiv.
   Supports all arguments of `ArxivAPIWrapper`.

   :param query: free text which used to find documents in the Arxiv
   :param doc_content_chars_max: cut limit for the length of a document's content


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedArxivLoader
      :collapse:

   .. py:method:: load() -> Any

      Override load method to add metadata.


      .. autolink-examples:: load
         :collapse:


   .. py:attribute:: loader_metadata


.. py:class:: EnhancedGitHubIssuesLoader(/, **data: Any)

   Bases: :py:obj:`langchain_community.document_loaders.GitHubIssuesLoader`


   Enhanced GitHub issues loader with metadata extraction.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedGitHubIssuesLoader
      :collapse:

   .. py:method:: load() -> Any

      Override load method to add metadata.


      .. autolink-examples:: load
         :collapse:


   .. py:attribute:: loader_metadata
      :type:  dict


.. py:class:: EnhancedHNLoader(web_path: Union[str, Sequence[str]] = '', header_template: Optional[dict] = None, verify_ssl: bool = True, proxies: Optional[dict] = None, continue_on_failure: bool = False, autoset_encoding: bool = True, encoding: Optional[str] = None, web_paths: Sequence[str] = (), requests_per_second: int = 2, default_parser: str = 'html.parser', requests_kwargs: Optional[Dict[str, Any]] = None, raise_for_status: bool = False, bs_get_text_kwargs: Optional[Dict[str, Any]] = None, bs_kwargs: Optional[Dict[str, Any]] = None, session: Any = None, *, show_progress: bool = True, trust_env: bool = False)

   Bases: :py:obj:`langchain_community.document_loaders.HNLoader`


   Enhanced Hacker News loader with metadata extraction.

   Initialize loader.

   :param web_paths: Web paths to load from.
   :param requests_per_second: Max number of concurrent requests to make.
   :param default_parser: Default parser to use for BeautifulSoup.
   :param requests_kwargs: kwargs for requests
   :param raise_for_status: Raise an exception if http status code denotes an error.
   :param bs_get_text_kwargs: kwargs for beatifulsoup4 get_text
   :param bs_kwargs: kwargs for beatifulsoup4 web page parsing
   :param show_progress: Show progress bar when loading pages.
   :param trust_env: set to True if using proxy to make web requests, for example
                     using http(s)_proxy environment variables. Defaults to False.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedHNLoader
      :collapse:

   .. py:method:: load() -> Any

      Override load method to add metadata.


      .. autolink-examples:: load
         :collapse:


   .. py:attribute:: loader_metadata


.. py:class:: EnhancedRecursiveUrlLoader(url: str, max_depth=2, extractor=None, prevent_outside=True)

   Bases: :py:obj:`langchain_community.document_loaders.RecursiveUrlLoader`


   Enhanced recursive web crawler with metadata extraction.

   Initialize with URL to crawl and any subdirectories to exclude.

   :param url: The URL to crawl.
   :param max_depth: The max depth of the recursive loading.
   :param use_async: Whether to use asynchronous loading.
                     If ``True``, ``lazy_load()`` will not be lazy, but it will still work in
                     the expected way, just not lazy.
   :param extractor: A function to extract document contents from raw HTML.
                     When extract function returns an empty string, the document is
                     ignored. Default returns the raw HTML.
   :param metadata_extractor: A function to extract metadata from args: raw HTML, the
                              source url, and the requests.Response/aiohttp.ClientResponse object
                              (args in that order).

                              Default extractor will attempt to use BeautifulSoup4 to extract the
                              title, description and language of the page.

                              ..code-block:: python

                                  import requests
                                  import aiohttp

                                  def simple_metadata_extractor(
                                      raw_html: str, url: str, response: Union[requests.Response, aiohttp.ClientResponse]
                                  ) -> dict:
                                      content_type = getattr(response, "headers").get("Content-Type", "")
                                      return {"source": url, "content_type": content_type}
   :param exclude_dirs: A list of subdirectories to exclude.
   :param timeout: The timeout for the requests, in the unit of seconds. If ``None``
                   then connection will not timeout.
   :param prevent_outside: If ``True``, prevent loading from urls which are not children
                           of the root url.
   :param link_regex: Regex for extracting sub-links from the raw html of a web page.
   :param headers: Default request headers to use for all requests.
   :param check_response_status: If ``True``, check HTTP response status and skip
                                 URLs with error responses (``400-599``).
   :param continue_on_failure: If ``True``, continue if getting or parsing a link raises
                               an exception. Otherwise, raise the exception.
   :param base_url: The base url to check for outside links against.
   :param autoset_encoding: Whether to automatically set the encoding of the response.
                            If ``True``, the encoding of the response will be set to the apparent
                            encoding, unless the ``encoding`` argument has already been explicitly set.
   :param encoding: The encoding of the response. If manually set, the encoding will be
                    set to given value, regardless of the ``autoset_encoding`` argument.
   :param proxies: A dictionary mapping protocol names to the proxy URLs to be used for requests.
                   This allows the crawler to route its requests through specified proxy servers.
                   If ``None``, no proxies will be used and requests will go directly to the target URL.

                   Example usage:

                   ..code-block:: python

                       proxies = {
                           "http": "http://10.10.1.10:3128",
                           "https": "https://10.10.1.10:1080",
                       }
   :param ssl: Whether to verify SSL certificates during requests.
               By default, SSL certificate verification is enabled (``ssl=True``),
               ensuring secure HTTPS connections. Setting this to ``False`` disables SSL
               certificate verification, which can be useful when crawling internal
               services, development environments, or sites with misconfigured or
               self-signed certificates.

               **Use with caution:** Disabling SSL verification exposes your crawler to
               man-in-the-middle (MitM) attacks, data tampering, and potential
               interception of sensitive information. This significantly compromises
               the security and integrity of the communication. It should never be
               used in production or when handling sensitive data.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedRecursiveUrlLoader
      :collapse:

   .. py:method:: _default_extractor(html)
      :staticmethod:


      Default extractor using BeautifulSoup.


      .. autolink-examples:: _default_extractor
         :collapse:


   .. py:method:: load() -> Any

      Override load method to add metadata.


      .. autolink-examples:: load
         :collapse:


   .. py:attribute:: loader_metadata


   .. py:attribute:: root_url


.. py:class:: EnhancedWebBaseLoader(web_path)

   Bases: :py:obj:`langchain_community.document_loaders.WebBaseLoader`


   Enhanced web page loader with metadata extraction.

   Initialize loader.

   :param web_paths: Web paths to load from.
   :param requests_per_second: Max number of concurrent requests to make.
   :param default_parser: Default parser to use for BeautifulSoup.
   :param requests_kwargs: kwargs for requests
   :param raise_for_status: Raise an exception if http status code denotes an error.
   :param bs_get_text_kwargs: kwargs for beatifulsoup4 get_text
   :param bs_kwargs: kwargs for beatifulsoup4 web page parsing
   :param show_progress: Show progress bar when loading pages.
   :param trust_env: set to True if using proxy to make web requests, for example
                     using http(s)_proxy environment variables. Defaults to False.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedWebBaseLoader
      :collapse:

   .. py:method:: load() -> Any

      Override load method to add metadata.


      .. autolink-examples:: load
         :collapse:


   .. py:attribute:: loader_metadata


   .. py:attribute:: web_path


.. py:class:: GitHubIssuesLoaderInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for GitHub issues loader.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GitHubIssuesLoaderInput
      :collapse:

   .. py:attribute:: access_token
      :type:  str | None
      :value: None



   .. py:attribute:: repo
      :type:  str
      :value: None



   .. py:attribute:: state
      :type:  str
      :value: None



.. py:class:: GitHubLoader

   GitHub repository loader compatible with MCP documentation loader.


   .. autolink-examples:: GitHubLoader
      :collapse:

   .. py:method:: load(repo: str, content_type: str = 'readme') -> list
      :async:


      Load content from GitHub repository.

      :param repo: Repository in format 'owner/repo'
      :param content_type: Type of content to load (default: 'readme')

      :returns: List of Document objects


      .. autolink-examples:: load
         :collapse:


.. py:class:: HackerNewsLoaderInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for Hacker News loader.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HackerNewsLoaderInput
      :collapse:

   .. py:attribute:: story_id
      :type:  int
      :value: None



.. py:class:: RecursiveWebLoaderInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for recursive web loader.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RecursiveWebLoaderInput
      :collapse:

   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: prevent_outside
      :type:  bool
      :value: None



   .. py:attribute:: url
      :type:  str
      :value: None



.. py:class:: TavilySearchInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for Tavily search.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TavilySearchInput
      :collapse:

   .. py:attribute:: max_results
      :type:  int | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: search_depth
      :type:  str | None
      :value: None



.. py:class:: WebLoaderInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for web page loader.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WebLoaderInput
      :collapse:

   .. py:attribute:: url
      :type:  str
      :value: None



.. py:class:: WebScraper

   Web scraper compatible with MCP documentation loader.


   .. autolink-examples:: WebScraper
      :collapse:

   .. py:method:: load(url: str) -> list
      :async:


      Scrape content from a web URL.

      :param url: URL to scrape

      :returns: List of Document objects


      .. autolink-examples:: load
         :collapse:


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

.. py:data:: DOCUMENT_LOADERS

.. py:data:: DOCUMENT_LOADER_TOOLS

.. py:data:: RESEARCH_TOOLS

.. py:data:: TAVILY_API_KEY

.. py:data:: TavilyClient
   :value: None


.. py:data:: arxiv_loader_tool

.. py:data:: document_loader_description_tool

.. py:data:: github_issues_loader_tool

.. py:data:: hackernews_loader_tool

.. py:data:: recommend_document_loaders_tool

.. py:data:: recursive_web_loader_tool

.. py:data:: web_loader_tool

