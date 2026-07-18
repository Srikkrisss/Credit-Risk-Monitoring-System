from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.crud import get_high_risk_customers
from api.schemas import HighRiskCustomerResponse
from api.crud import get_loan_summary
from api.schemas import LoanSummaryResponse
from api.crud import get_branch_performance
from api.schemas import BranchPerformanceResponse
from api.crud import get_defaulters
from api.schemas import DefaulterResponse


router = APIRouter(
    prefix="/risk",
    tags=["Risk Analytics"]
)


@router.get(
    "/high-risk-customers",
    response_model=list[HighRiskCustomerResponse]
)
def high_risk_customers(
    db: Session = Depends(get_db)
):

    return get_high_risk_customers(db)


from api.crud import get_loan_summary

from api.schemas import LoanSummaryResponse


@router.get(
    "/loan-summary",
    response_model=LoanSummaryResponse
)
def loan_summary(
    db: Session = Depends(get_db)
):

    return get_loan_summary(db)


@router.get(
    "/branch-performance",
    response_model=list[BranchPerformanceResponse]
)
def branch_performance(
    db: Session = Depends(get_db)
):

    return get_branch_performance(db)



@router.get(
    "/defaulters",
    response_model=list[DefaulterResponse]
)
def defaulters(
    db: Session = Depends(get_db)
):

    return get_defaulters(db)