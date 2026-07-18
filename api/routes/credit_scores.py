from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.crud import get_credit_scores, get_credit_score
from api.schemas import CreditScoreResponse

router = APIRouter(
    prefix="/credit-scores",
    tags=["Credit Scores"]
)


@router.get("/", response_model=list[CreditScoreResponse])
def read_scores(db: Session = Depends(get_db)):
    return get_credit_scores(db)


@router.get("/{score_id}", response_model=CreditScoreResponse)
def read_score(score_id: int,
               db: Session = Depends(get_db)):
    return get_credit_score(db, score_id)