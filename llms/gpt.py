from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import time
import sys
import json
import pandas as pd
import os
from dotenv import load_dotenv
import openai
load_dotenv(override=True)


class GPTAgent:
    def __init__(self):
        api_key = os.getenv("OPENAI_KEY")
        org = os.getenv("OPENAI_ORG")
        openai.api_key = api_key
        openai.organization = org
        
        self.prompt_version = 1
        self.gpt_model = "gpt-3.5-turbo"
        
        self.getPrompts()
        self.getModels()
        self.getResponse()
        
    def getPrompts(self):
        with open(f"prompts/prompt_v{self.prompt_version}.txt", "r") as file:
            self.base_prompt = file.read()

    def getModels(self):
        self.agent = ChatOpenAI(model_name=self.gpt_model, temperature=0.7, openai_api_key=openai.api_key)
        self.memory = ConversationBufferMemory()

        self.conversation = ConversationChain(llm = self.agent, memory = self.memory)
  
    def getResponse(self):
        response = self.conversation.predict(input=f"{self.base_prompt}")
        print(response)
        
        
GPTAgent()