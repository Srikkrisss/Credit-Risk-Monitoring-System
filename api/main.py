from fastapi import FastAPI
from sqlalchemy import text

from api.database import engine

app = FastAPI(
    title="Credit Risk Monitoring API",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Credit Risk Monitoring API Running"
    }


@app.get("/health")
def health():

    try:

        with engine.connect() as connection:

            connection.execute(text("SELECT 1"))

        return {
            "status": "Healthy",
            "Database": "Connected"
        }

    except Exception as e:

        return {
            "status": "Failed",
            "error": str(e)
        }