# import time
# from langchain_openai import ChatOpenAI
# from app.config import DEFAULT_MODEL
# from app.classifier import classify_prompt
# from app.router import get_model,get_reasoning_model
# from services.cost_calculator import calculate_cost
# from services.logger import log_query
# from services.evaluator import evaluate_answer
# from services.rag_classifier import should_use_rag
# from services.rag_service import retrieve_content
# from graph.workflow import graph


# # llm=ChatOpenAI(
# #     model=DEFAULT_MODEL,
# #     temperature=0
# # )

# CONFIDENCE_THRESHOLD=0.6

# def generate_response(prompt:str):

#     start=time.time()

#     complexity=classify_prompt(prompt)

#     llm,model_name=get_model(complexity)

#     use_rag=should_use_rag(prompt)

#     if use_rag:

#         context=retrieve_content(prompt)

#         rag_prompt = f"""
# Use the following context to answer the question.

# Context:
# {context}

# Question:
# {prompt}
# """
        
#         response=llm.invoke(rag_prompt)

#     else:
#         response=llm.invoke(prompt)

        

#     # response=llm.invoke(prompt)

#     answer=response.content

#     confidence=evaluate_answer(prompt,answer)

#     escalated=False

#     if confidence<CONFIDENCE_THRESHOLD:
#         reasoning_llm,reasoning_model=get_reasoning_model()

#         response=reasoning_llm.invoke(prompt)
#         answer=response.content

#         model_name=reasoning_model

#         escalated=True

#     latency=time.time()-start

#     tokens=response.response_metadata['token_usage']['total_tokens']

#     cost=calculate_cost(model_name,tokens)

#     log_query(prompt,model_name,complexity,latency,tokens,cost)

#     return{
#         'response':response.content,
#         'model_used':model_name,
#         'latency':round(latency,2),
#         'complexity_level':complexity,
#         'tokens_used':tokens,
#         'cost':cost,
#         'confidence':round(confidence,2),
#         'escalated':escalated
#     }

from graph.workflow import graph
import time
from services.logger import log_query
from services.cost_calculator import calculate_cost

def generate_response(prompt:str):

    start=time.time()

    state={
        'query':prompt,
        'complexity':0,
        'model':"",
        'context':"",
        'answer':"",
        'confidence':0,
        "escalated":False,
        'llm':None,
        'tokens':0
    }

    result=graph.invoke(state)

    latency=round(time.time()-start,2)

    tokens=result.get('tokens',0)

    cost=calculate_cost(result['model'],tokens)

    log_query(
        prompt,
        result['model'],
        result['complexity'],
        latency,
        tokens,
        cost 
    )

    return {
        'response':result['answer'],
        'model_used':result['model'],
        'complexity_level':result['complexity'],
        'confidence':result['confidence'],
        'escalated':result['escalated'],
        'latency':latency,
        'tokens_used':tokens,
        'cost':cost
    }