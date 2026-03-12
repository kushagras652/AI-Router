from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm=ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0
)

prompt_template = ChatPromptTemplate.from_template("""
Determine if the user query requires information from uploaded documents.

Return:
YES → if document retrieval is needed
NO → if normal LLM answer is enough

Query:
{query}
""")

def should_use_rag(query):

    prompt=prompt_template.format_messages(query=query)

    response=llm.invoke(prompt)
    decision=response.content.strip().upper()

    return decision == "YES"



