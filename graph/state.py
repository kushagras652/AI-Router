from typing import TypedDict,Any

class RouterState(TypedDict):
    query:str
    complexity:int
    model:str
    context:str
    answer:str
    confidence:float
    escalated:bool
    llm:Any

