from langgraph.graph import StateGraph
from graph.state import RouterState

from app.classifier import classify_prompt
from app.router import get_model,get_reasoning_model
from services.rag_classifier import should_use_rag
from services.rag_service import retrieve_content
from services.evaluator import evaluate_answer

def classifier_node(state:RouterState):

    query=state['query']

    complexity=classify_prompt(query)

    state['complexity']=complexity

    return state

def router_node(state:RouterState):

    complexity=state['complexity']

    llm,model_name=get_model(complexity)

    state['model']=model_name

    state['llm']=llm

    return state

def rag_node(state:RouterState):

    query=state['query']

    if should_use_rag(query):

        context=retrieve_content(query)

        state['context']=context
    else:

        state['context']=""

    return state

def generate_node(state:RouterState):

    llm=state['llm']

    query=state['query']

    context=state.get('context',"")

    if context:

        prompt = f"""
Use this context to answer.

Context:
{context}

Question:
{query}
"""
        
    else:
        prompt = query

    response = llm.invoke(prompt)

    state["answer"] = response.content

    metadata = response.response_metadata

    if "token_usage" in metadata:
        tokens = metadata["token_usage"]["total_tokens"]
    else:
        tokens = 0

    state["tokens"] = tokens


    return state

def evaluate_node(state:RouterState):

    query=state['query']

    answer=state['answer']

    confidence=evaluate_answer(query,answer)

    state['confidence']=confidence

    return state

CONFIDENCE_THRESHOLD=0.6

def escalation_node(state:RouterState):

    if state['confidence']<CONFIDENCE_THRESHOLD:

        llm,model=get_reasoning_model()

        query=state['query']

        response=llm.invoke(query)

        state['answer']=response.content

        state['model']=model

        state['escalated']=True
    else:
        state['escalated']=False

    return state

builder=StateGraph(RouterState)

builder.add_node('classifier',classifier_node)
builder.add_node('router',router_node)
builder.add_node('rag',rag_node)
builder.add_node('generate',generate_node)
builder.add_node('evaluate',evaluate_node)
builder.add_node('escalate',escalation_node)

builder.set_entry_point('classifier')

builder.add_edge('classifier','router')
builder.add_edge('router','rag')
builder.add_edge('rag','generate')
builder.add_edge('generate','evaluate')
builder.add_edge('evaluate','escalate')

builder.set_finish_point('escalate')

graph=builder.compile()