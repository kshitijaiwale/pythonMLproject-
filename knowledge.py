import json

from dotenv import load_dotenv
import os
load_dotenv()

import google.generativeai as genai
genai.configure(api_key=os.getenv("API_KEY"))

with open("raw.jsonl","r") as file:
 for line in file:
    record = json.loads(line)
    report_text = record["text"]

    prompt = f"""
    extract the following fields from this text as JSON:
    - crop 
    - disease
    - location 
    - cause 
    - severity
    Text:"{report_text}"
    """

    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)

    llm_op = response.text

    print(llm_op)




