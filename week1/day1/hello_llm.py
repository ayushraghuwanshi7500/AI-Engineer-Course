from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

client = Groq(api_key=my_api_key)

prompt_one={
"role": "user",
"content": "Who is Cristiano Ronaldo?"
}

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[prompt_one],
)
#print(response)
print("############### ACTUAL RESPONSE BELOW ##########")
print(response.choices[0].message.content)