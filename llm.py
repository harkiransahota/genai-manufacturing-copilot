from openai import OpenAI

from config import API_KEY, BASE_URL, MODEL_NAME
from prompts import SYSTEM_PROMPT

from models import AssemblyInstructions

class ManufacturingCopilot:

    def __init__(self):

        self.client = OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
        )

    def ask(self, question):
        print("ask question")
        completion = self.client.chat.completions.parse(

            model=MODEL_NAME,
            
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            
            response_format=AssemblyInstructions
        )
        print("return result")

        return completion.choices[0].message.parsed