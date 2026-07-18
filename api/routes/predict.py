from fastapi import APIRouter

from api.schemas import (
    CreditRiskRequest,
    CreditRiskResponse
)

from api.ml.predictor import predict_risk

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post(
    "/",
    response_model=CreditRiskResponse
)
def predict(request: CreditRiskRequest):

    prediction, probability = predict_risk(
        request.dict()
    )

    result = "High Risk"

    if prediction == 0:
        result = "Low Risk"

    return {

        "Prediction": result,

        "RiskProbability": round(
            probability,
            4
        )

    }