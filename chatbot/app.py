from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant .Please answer our questions"),
        ("user","Question: {question}")
    ]
)

st.title("problem solver")
input_text = st.text_area("Enter your question here", height=200)

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
)

output_parser=StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write("Answer:")
    st.write(response)