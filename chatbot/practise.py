from dotenv import load_dotenv
import os

load_dotenv()

print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("Endpoint:", os.getenv("LANGSMITH_ENDPOINT"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))
print("API Key exists:", os.getenv("LANGSMITH_API_KEY") is not None)