from fastapi import FastAPI

from api.routes.customers import router as customer_router
from api.routes.loans import router as loan_router
from api.routes.branches import router as branch_router
from api.routes.credit_scores import router as credit_score_router
from api.routes.risks import router as risk_router

app = FastAPI(
    title="Credit Risk Monitoring API",
    version="1.0.0"
)

app.include_router(customer_router)
app.include_router(loan_router)
app.include_router(branch_router)
app.include_router(credit_score_router)
app.include_router(risk_router)

@app.get("/")
def home():
    return {
        "message": "Credit Risk Monitoring API Running"
    }