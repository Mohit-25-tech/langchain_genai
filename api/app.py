from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
from langserve import add_routes
import uvicorn
from langchain_ollama import OllamaLLM

load_dotenv()  # Load environment variables from .env

app = FastAPI(
    title="LangChain Google Gemini API",
    version="1.0",
    description="An API for interacting with Google Gemini models using LangChain."
)


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite")

model1 = OllamaLLM(
    model="llama3"
)

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | model1,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)