from fastapi import FastAPI
from app.models import QueryRequest
from app.llm_service import generate_response

app=FastAPI(title='AI Router API')

@app.post("/ask")
def ask_question(request:QueryRequest):
    result=generate_response(request.query)

    return result