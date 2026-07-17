from fastapi import FastAPI

from api.routes.customers import router as customer_router

app = FastAPI(
    title="Credit Risk Monitoring API",
    version="1.0.0"
)

app.include_router(customer_router)


@app.get("/")
def home():

    return {
        "message": "Credit Risk Monitoring API Running"
    }