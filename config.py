import os
from dotenv import load_dotenv

load_dotenv()

HF_AIP_KEY = os.getenv("HF_API_KEY", "")
GROQ_API_KEY= os.getenv("GROQ_API_KEY", "")

