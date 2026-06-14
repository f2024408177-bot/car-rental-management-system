from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="./.env")

print(os.getenv("DATABASE_URL"))