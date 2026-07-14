from openai import OpenAI

from config import API_KEY, BASE_URL, MODEL_NAME
from prompts import SYSTEM_PROMPT


class ManufacturingCopilot:

    def __init__(self):

        self.client = OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
        )

    def ask(self, question):

        response = self.client.chat.completions.create(

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
            ]
        )

        return response.choices[0].message.content