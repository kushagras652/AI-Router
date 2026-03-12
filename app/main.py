from fastapi import FastAPI,UploadFile,File
from app.models import QueryRequest
from app.llm_service import generate_response
from services.rag_service import ingest_document

app=FastAPI(title='AI Router API')

@app.post("/ask")
def ask_question(request:QueryRequest):
    result=generate_response(request.query)

    return result

@app.post("/upload")
async def upload_document(file:UploadFile=File(...)):
    file_location=f"temp_{file.filename}"

    with open(file_location,'wb') as f:
        f.write(await file.read())

    result=ingest_document(file_location)

    return {'message':result}