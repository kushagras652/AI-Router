from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

evaluator_llm=ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0
)

prompt_template = ChatPromptTemplate.from_template("""
You are evaluating an AI assistant response.

User Question:
{question}

AI Answer:
{answer}

Rate the confidence of the answer from 0 to 1.

0 = completely wrong
1 = perfect answer

Return ONLY the number.
""")

def evaluate_answer(question,answer):
    prompt=prompt_template.format_messages(
        question=question,
        answer=answer
    )

    response=evaluator_llm.invoke(prompt)

    try:
        score=float(response.content.strip())
    except:
        score=0.5

    return score