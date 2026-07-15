from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("NEBIUS_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
BASE_URL = os.getenv("BASE_URL")

MAX_HISTORY=os.getenv("MAX_HISTORY")