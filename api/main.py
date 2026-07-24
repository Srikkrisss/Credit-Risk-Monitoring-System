from fastapi import FastAPI
from sqlalchemy import text

from api.database import SessionLocal

from api.routes.customers import router as customer_router
from api.routes.loans import router as loan_router
from api.routes.branches import router as branch_router
from api.routes.credit_scores import router as credit_score_router
from api.routes.risks import router as risk_router
from api.routes.predict import router as predict_router
from api.routes.predictions import router as prediction_history_router

app = FastAPI(
    title="Credit Risk Monitoring API",
    version="1.0.0"
)

app.include_router(customer_router)
app.include_router(loan_router)
app.include_router(branch_router)
app.include_router(credit_score_router)
app.include_router(risk_router)
app.include_router(predict_router)
app.include_router(prediction_history_router)


@app.get("/")
def home():
    return {
        "Application": "Credit Risk Monitoring System",
        "Version": "1.0.0",
        "Status": "Running"
    }


@app.get("/health")
def health():

    db = SessionLocal()

    try:

        db.execute(text("SELECT 1"))

        database = "Connected"

    except Exception:

        database = "Disconnected"

    finally:

        db.close()

    return {
        "status": "Healthy",
        "database": database,
        "model": "Loaded",
        "version": "1.0.0"
    }