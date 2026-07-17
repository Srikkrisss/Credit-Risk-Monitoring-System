from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.crud import get_customers, get_customer
from api.schemas import CustomerResponse

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("/", response_model=list[CustomerResponse])
def read_customers(db: Session = Depends(get_db)):
    return get_customers(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return get_customer(db, customer_id)