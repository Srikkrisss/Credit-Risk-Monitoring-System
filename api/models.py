from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, DECIMAL
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from datetime import datetime

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

class Loan(Base):

    __tablename__ = "Loans"

    LoanID = Column(Integer, primary_key=True, index=True)

    CustomerID = Column(Integer)
    BranchID = Column(Integer)
    OfficerID = Column(Integer)
    LoanNumber = Column(String(8))

    LoanType = Column(String(50))
    LoanAmount = Column(DECIMAL(18,2))
    InterestRate = Column(DECIMAL(5,2))

    TenureMonths = Column(Integer)

    LoanStatus = Column(String(30))

    SanctionDate = Column(Date)

class Branch(Base):

    __tablename__ = "Branches"

    BranchID = Column(Integer, primary_key=True, index=True)

    BranchName = Column(String(100))
    BranchCode = Column(String(10))
    AddressLine = Column(String(50))
    City = Column(String(50))
    StateName = Column(String(50))
    Pincode = Column(String(6))
    Phone = Column(String(10))
    Email = Column(String(50))
    IFSCCode = Column(String(20))
    CreatedDate = Column(DateTime)


class CreditScore(Base):

    __tablename__ = "CreditScores"

    CreditScoreID = Column(Integer, primary_key=True)

    CustomerID = Column(Integer)
    CreditScore = Column(Integer)
    CreditAgency = Column(String(50))
    ScoreDate = Column(Date)
    RiskCategory = Column(String(20))


class PredictionHistory(Base):
    __tablename__ = "PredictionHistory"

    PredictionID = Column(Integer, primary_key=True, index=True)

    CustomerID = Column(
        Integer,
        ForeignKey("Customers.CustomerID"),
        nullable=True
    )

    Prediction = Column(String(20), nullable=False)

    Probability = Column(Float, nullable=False)

    RiskLevel = Column(String(20), nullable=False)

    ModelVersion = Column(
        String(20),
        default="v1.0"
    )

    PredictionTime = Column(
        DateTime,
        default=datetime.utcnow
    )
