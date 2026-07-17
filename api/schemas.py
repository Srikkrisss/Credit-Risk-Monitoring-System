from pydantic import BaseModel
from datetime import date


class CustomerResponse(BaseModel):

    CustomerID: int
    FirstName: str
    LastName: str
    AnnualIncome: float
    Occupation: str
    City: str
    StateName: str

    class Config:
        from_attributes = True