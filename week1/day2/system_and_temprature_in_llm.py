from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

client = Groq(api_key=my_api_key)

set_system = {
    "role" : "system",
    "content" : "you are marketing or content manager head"
}

actual_prompt={
"role": "user",
"content": "think of a clothing  app name, one work only, suggest one name only"
}

temperature=2

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[set_system, actual_prompt],
    temperature=temperature
)
print(response)
print("############### ACTUAL RESPONSE BELOW ##########")
print(response.choices[0].message.content)