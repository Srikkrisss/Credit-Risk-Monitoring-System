from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.crud import (
    get_prediction_history,
    get_prediction
)

router = APIRouter(
    prefix="/predictions",
    tags=["Prediction History"]
)


@router.get("/")
def read_prediction_history(
    db: Session = Depends(get_db)
):
    return get_prediction_history(db)


@router.get("/{prediction_id}")
def read_prediction(
    prediction_id: int,
    db: Session = Depends(get_db)
):

    prediction = get_prediction(
        db,
        prediction_id
    )

    if prediction is None:

        raise HTTPException(
            status_code=404,
            detail="Prediction not found"
        )

    return prediction