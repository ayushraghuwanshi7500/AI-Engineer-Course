from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

client = Groq(api_key=my_api_key)

actual_prompt="""
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of three categories namely billing, technical, return.
#OUTPUT FORMAT
Your answer should be in one word only. The one word shoud be one of the categories given in constraints
#Example
For instance if a user compalin says he wants a refund then the category is Return
#FALLBACK
If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
need to exachange my laptop.
"""

prompt={
"role": "user",
"content": actual_prompt
}

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[prompt],
)

print(response.choices[0].message.content)