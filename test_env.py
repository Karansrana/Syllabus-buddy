import os
from dotenv import load_dotenv

load_dotenv()                      # reads .env into environment variables

key = os.getenv("NASA_API_KEY")
print("Key loaded:", key is not None)