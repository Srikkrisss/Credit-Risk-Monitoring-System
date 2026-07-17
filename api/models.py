from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, DECIMAL

Base = declarative_base()


class Customer(Base):

    __tablename__ = "Customers"

    CustomerID = Column(Integer, primary_key=True, index=True)

    FirstName = Column(String(50))
    LastName = Column(String(50))
    DOB = Column(Date)
    Gender = Column(String(10))
    Email = Column(String(100))
    Phone = Column(String(10))
    PAN = Column(String(10))
    Aadhaar = Column(String(12))
    Occupation = Column(String(100))
    AnnualIncome = Column(DECIMAL(18,2))
    StateName = Column(String(50))
    City = Column(String(50))
    CreatedDate = Column(DateTime)