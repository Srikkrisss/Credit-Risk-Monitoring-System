from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
DRIVER = os.getenv("DRIVER")
UID = os.getenv("UID")
PWD = os.getenv("PWD")