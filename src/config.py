from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="dev.env")

DB_URL = os.environ.get("DB_URL")
