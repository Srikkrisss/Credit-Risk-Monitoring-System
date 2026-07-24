from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.schemas import CreditRiskRequest
from api.database import get_db

from api.services.prediction_service import generate_prediction

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post("/")
def predict(
    request: CreditRiskRequest,
    db: Session = Depends(get_db)
):

    return generate_prediction(
        request.dict(),
        db
    )