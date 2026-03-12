from langchain_openai import ChatOpenAI
from app.config import SYSTEM1_MODEL,SYSTEM2_MODEL,SYSTEM3_MODEL

def get_model(complexity_level:int):
    if complexity_level==1:
        model=SYSTEM1_MODEL

    elif complexity_level==2:
        model=SYSTEM2_MODEL

    else:
        model=SYSTEM3_MODEL

    return ChatOpenAI(
        model=model,
        temperature=0
    ),model

def get_reasoning_model():

    return ChatOpenAI(
        model=SYSTEM3_MODEL,
        temperature=0
    ),SYSTEM3_MODEL