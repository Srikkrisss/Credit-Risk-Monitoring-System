from sqlalchemy.orm import Session
from api.models import Customer


def get_customers(db: Session):
    return db.query(Customer).all()


def get_customer(db: Session, customer_id: int):
    return (
        db.query(Customer)
        .filter(Customer.CustomerID == customer_id)
        .first()
    )