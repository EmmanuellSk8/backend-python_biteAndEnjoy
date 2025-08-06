from dotenv import load_dotenv
import os

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
BACKEND_URL = os.getenv("DATABASE_URL")