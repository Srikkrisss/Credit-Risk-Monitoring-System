import os
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
DRIVER = os.getenv("DRIVER")
TRUSTED_CONNECTION = os.getenv("TRUSTED_CONNECTION")