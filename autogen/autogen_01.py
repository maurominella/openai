#!/usr/bin/env python
# coding: utf-8
# %%

# %%


from typing import Dict, Union

from IPython import get_ipython
from IPython.display import display, Image
import csv


# %%


import autogen, os
import json
from dotenv import load_dotenv

load_dotenv("./../credentials_my.env")

my_models = [
    {
        'model': os.environ['GPT4-1106-128k'],
        'api_key': os.environ['AZURE_OPENAI_API_KEY'],
        "base_url": os.environ['AZURE_OPENAI_ENDPOINT'],
        "api_type": os.environ['OPENAI_API_TYPE'],
        "api_version": os.environ['AZURE_OPENAI_API_VERSION']
    },
    {
        'model': os.environ['GPT432-0613-32k'],
        'api_key': os.environ['AZURE_OPENAI_API_KEY'],
        "base_url": os.environ['AZURE_OPENAI_ENDPOINT'],
        "api_type": os.environ['OPENAI_API_TYPE'],
        "api_version": os.environ['AZURE_OPENAI_API_VERSION']
    }
]

# need for converting to string
os.environ['models_var'] = json.dumps(my_models)

# Setting configurations for autogen
config_list = autogen.config_list_from_json(
    env_or_file='models_var',
    filter_dict={
        "model": {
            "gpt4-1106-128k",
            "gpt4-0613-32k"
        }
    }
)

config_list


# %%


# create a UserProxyAgent instance named "user_proxy"

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,

    # if the x["content"] ends by "TERMINATE", is_termination_msg-->True; otherwise, is_termination_msg--> False
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    
    code_execution_config={
        "work_dir": "coding",
        
        # Using docker is safer than running the generated code directly.
        # set use_docker=True if docker is available to run the generated code. 
        "use_docker": False,  
        
    }
)

user_proxy


# %%


# create an AssistantAgent named "assistant"

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "cache_seed": 53,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    },  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)

assistant


# %%


get_ipython().run_cell_magic('time', '', '# the assistant receives a message from the user_proxy, which contains the task description\n\n\nchat_res = user_proxy.initiate_chat(\n    assistant,\n    message="""What date is today? Compare the year-to-date gain for META and TESLA.""",\n    summary_method="reflection_with_llm",\n)\n')


# %%


autogen.Completion.clear_cache(seed=53)

