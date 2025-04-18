from haive_core.engine.aug_llm import AugLLMConfig,compose_runnable
#from haive_core.runnables.runnable import CustomRunnableConfig,RunnableFactory,compose_runnable
#from haive_core.prompts.base import PromptTemplateFactory,PromptTemplateConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from haive_agents.document_agents.summarizer.map_branch.prompts import MAP_PROMPT,REDUCE_PROMPT 
#map_prompt_template_config = PromptTemplateConfig(chat_prompt_template=map_prompt)
map_aug_llm_config = AugLLMConfig(
    name='summarizer_map',
    prompt_template=MAP_PROMPT,
    output_parser = StrOutputParser()
)

reduce_augllm_config = AugLLMConfig(
    name='summarizer_reduce',
    prompt_template=REDUCE_PROMPT,
    output_parser = StrOutputParser()
)
#reduce_runnable = compose_runnable(reduce_runnable_config)