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


class LoanResponse(BaseModel):

    LoanID: int
    CustomerID: int
    LoanAmount: float
    LoanType: str
    InterestRate: float
    LoanStatus: str

    class Config:
        from_attributes = True


class BranchResponse(BaseModel):

    BranchID: int
    BranchName: str
    City: str
    StateName: str

    class Config:
        from_attributes = True


class CreditScoreResponse(BaseModel):

    ScoreID: int
    CustomerID: int
    CreditScore: int
    ScoreDate: date

    class Config:
        from_attributes = True



class HighRiskCustomerResponse(BaseModel):

    CustomerID: int
    FirstName: str
    LastName: str
    LoanAmount: float
    CreditScore: int


class LoanSummaryResponse(BaseModel):

    TotalLoans: int
    TotalLoanAmount: float
    AverageLoan: float
    HighestLoan: float
    LowestLoan: float


class BranchPerformanceResponse(BaseModel):

    BranchName: str
    LoansIssued: int
    TotalLoanValue: float
    AverageLoan: float


from datetime import date

class DefaulterResponse(BaseModel):

    CustomerID: int

    FirstName: str

    LastName: str

    LoanAmount: float

    DueDate: date

    PaymentStatus: str


from pydantic import BaseModel


class CreditRiskRequest(BaseModel):
    CustomerID: int
    Age: int
    EmploymentYears: int
    CreditScore: int
    AnnualIncome: float
    LoanAmount: float
    InterestRate: float
    LoanTerm: int
    ExistingLoans: int
    DebtToIncomeRatio: float
    CollateralValue: float


class CreditRiskResponse(BaseModel):

    Prediction: str
    RiskProbability: float