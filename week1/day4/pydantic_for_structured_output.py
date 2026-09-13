from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel
import json
import os

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

client = Groq(api_key=my_api_key)

class Ticket(BaseModel):
    name: str
    issue: str
    email: str
    contact_number: str

schema = Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

complain="Hello My name is Ayush. Yesterday I broke up with my girlfriend sheetal I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is 82134"

system_prompt={
"role": "system",
"content": system_prompt
}

user_prompt={
"role": "user",
"content": complain
}

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[system_prompt, user_prompt], 
    response_format=response_format
)

json_op=response.choices[0].message.content
print(json_op)
data=json.loads(json_op)
ticket=Ticket(**data)
print(ticket.name)