from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.crud import get_loans, get_loan
from api.schemas import LoanResponse

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)


@router.get("/", response_model=list[LoanResponse])
def read_loans(db: Session = Depends(get_db)):

    return get_loans(db)


@router.get("/{loan_id}", response_model=LoanResponse)
def read_loan(
    loan_id: int,
    db: Session = Depends(get_db)
):

    return get_loan(db, loan_id)