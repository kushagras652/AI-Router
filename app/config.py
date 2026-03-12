import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")


DEFAULT_MODEL='gpt-4o-mini'
SYSTEM1_MODEL='gpt-4o-mini'
SYSTEM2_MODEL='gpt-4o'
SYSTEM3_MODEL='gpt-4o'