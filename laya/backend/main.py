from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/chat")
def chat(q: Query):
    user_query = q.query

    # Dummy logic (replace with RAG + LLM)
    response = f"Processed: {user_query}"

    return {"response": response}