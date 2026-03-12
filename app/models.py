from pydantic import BaseModel

class QueryRequest(BaseModel):
    query:str

class QueryResponse(BaseModel):
    response:str
    model_used:str
    latency:float
    complexity_level:int
    tokens_used:int
    cost:float
    confidence:float
    escalated:bool