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

        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def ask(self, question):
        print("ask question")

        #add new question to message history
        self.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        completion = self.client.chat.completions.parse(

            model=MODEL_NAME,
            
            #send message history
            messages=self.messages
            
            response_format=AssemblyInstructions
        )
        print("return result")

        instructions = completion.choices[0].message.parsed
        #add response to message history
        self.messages.append(
            {
                "role": "assistant",
                "content": instructions.model_dump_json()
            }
        )

        #check for correct history length
        if len(self.messages) > MAX_HISTORY + 1:
            self.messages = (
                [self.messages[0]]
                + self.messages[-MAX_HISTORY:]
            )

        return instructions