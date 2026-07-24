from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

from config import *

connection_string = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER},1433;"
    f"DATABASE={DATABASE};"
    f"UID={UID};"
    f"PWD={PWD};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
    "Connection Timeout=5;"
)
DATABASE_URL = (
    f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()