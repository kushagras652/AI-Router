from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.config import OPENAI_API_KEY

classifier_llm=ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0
)

prompt_template=ChatPromptTemplate.from_template("""
You are an AI prompt complexity classifier.

Classify the user's prompt into one of these categories:

1 = Simple query (greeting, basic facts, short answer)
2 = Moderate query (explanations, summaries, conceptual questions)
3 = Complex reasoning (analysis, architecture design, deep reasoning)

Return ONLY the number: 1, 2, or 3.

Prompt:
{user_prompt}

""")

def classify_prompt(user_prompt:str):
    prompt=prompt_template.format_messages(user_prompt=user_prompt)

    response=classifier_llm.invoke(prompt)

    level=response.content.strip()

    return int(level)