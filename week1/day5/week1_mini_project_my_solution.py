from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import pdfplumber
import json
load_dotenv()

skills=["AWS","Jenkins","Docker","Python", "JavaScript", "SQL", "HTML", "CSS", "React", "Node.js", "Django", "Flask", "FastAPI"]

class Skills(BaseModel):
    skill: list[str]

schema = Skills.model_json_schema()

my_api_key=os.getenv("GROQ_API_KEY")
using_model=os.getenv("GROQ_MODEL_USED")
client = Groq(api_key=my_api_key)

response_format={
    "type": "json_object"
}

system_actual_prompt=f"""
Extract the skills information from the resume strictly based on this schema and give a json output.
{schema}
"""

system_prompt={
"role": "system",
"content": system_actual_prompt
}

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_percent_match_from_resume(resume_path: str):

    current_resume=resume_path

    resume_text = extract_text_from_pdf(current_resume)

    user_prompt={
        "role": "user",
        "content": resume_text
    }

    response = client.chat.completions.create(
        model=using_model,
        messages=[system_prompt, user_prompt], 
        response_format=response_format
    )

    json_op=response.choices[0].message.content

    data=json.loads(json_op)
    current_resume_skills=Skills(**data)

    response_percent = client.chat.completions.create(
        model=using_model,
        messages=[{"role":"user", "content":"compare" + str(current_resume_skills.skill) + "with" + str(skills) + "and give a percent match for the role to the HR and just give the percent match in the output nothing else."}]
    )

    print("The percent match of '" + current_resume + "' for the role is " + response_percent.choices[0].message.content +".")

all_resumes=["resume_devops_engineer.pdf", "resume_fullstack_developer.pdf"]

for resume in all_resumes:
    extract_percent_match_from_resume(resume)