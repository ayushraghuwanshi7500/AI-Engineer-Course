from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

client = Groq(api_key=my_api_key)

using_model="openai/gpt-oss-20b"

prompt_number_one="Hi!"
prompt_number_two="Explain time travel in brief."
prompt_number_three="Write an essay on Machine Learning in 1000 words."

list_of_prompts=[prompt_number_one, prompt_number_two, prompt_number_three]

for prompt in list_of_prompts:

    message={
    "role": "user",
    "content": prompt
    }

    response = client.chat.completions.create(
        model=using_model,
        messages=[message],
        max_tokens=1000
    )
    print(f"Prompt -> {prompt}")
    print(f"number of prompt token -> {response.usage.prompt_tokens}")
    print(f"response -> {response.choices[0].message.content}")
    print(f"number of completions (response) token -> {response.usage.completion_tokens}")
    print(f"Finish Reason -> {response.choices[0].finish_reason}")
    print("######################")