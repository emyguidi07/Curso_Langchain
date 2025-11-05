from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

### Exemplo com Ollama (retire as 3 aspas para rodar)
"""
llm = ChatOllama(
    model="phi3",
    temperature=0.1
)

chain3 = prompt | llm
res = chain3.invoke({"input": input})
print(res.content)"""

from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
info = api.model_info("meta-llama/Meta-Llama-3-8B-Instruct")
print(info)