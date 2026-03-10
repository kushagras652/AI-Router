import time
from langchain_openai import ChatOpenAI
from app.config import DEFAULT_MODEL
from app.classifier import classify_prompt

llm=ChatOpenAI(
    model=DEFAULT_MODEL,
    temperature=0
)

def generate_response(prompt:str):

    start=time.time()

    complexity=classify_prompt(prompt)

    response=llm.invoke(prompt)

    latency=time.time()-start

    return{
        'response':response.content,
        'model_used':DEFAULT_MODEL,
        'latency':round(latency,1),
        'complexity_level':complexity
    }