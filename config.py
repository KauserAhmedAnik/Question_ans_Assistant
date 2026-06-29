# LangChain
import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

MODEL_NAME = os.getenv("MODEL_NAME")

BASE_URL = os.getenv("BASE_URL")

llm = ChatOpenAI(
    api_key=GITHUB_API_KEY,
    model=MODEL_NAME,
    base_url=BASE_URL,
    temperature=0
)

print("✅ GitHub Model Connected")