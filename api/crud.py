from sqlalchemy.orm import Session
from sqlalchemy import text
from api.models import (
    Customer,
    Loan,
    Branch,
    CreditScore,
    PredictionHistory
)

from api.models import Customer, Loan, Branch, CreditScore


# ---------------- CUSTOMER CRUD ---------------- #

def get_customers(db: Session):

    count = db.execute(text("SELECT COUNT(*) FROM Customers")).scalar()
    print(f"Customer Count = {count}")

    customers = db.query(Customer).all()
    print(f"Objects Returned = {len(customers)}")

    return customers


def get_customer(db: Session, customer_id: int):

    return (
        db.query(Customer)
        .filter(Customer.CustomerID == customer_id)
        .first()
    )


# ---------------- LOAN CRUD ---------------- #

def get_loans(db: Session):

    return db.query(Loan).all()


def get_loan(db: Session, loan_id: int):

    return (
        db.query(Loan)
        .filter(Loan.LoanID == loan_id)
        .first()
    )



def get_branches(db: Session):

    return db.query(Branch).all()


def get_branch(db: Session, branch_id: int):

    return (
        db.query(Branch)
        .filter(Branch.BranchID == branch_id)
        .first()
    )



def get_credit_scores(db: Session):

    return db.query(CreditScore).all()


def get_credit_score(db: Session, score_id: int):

    return (
        db.query(CreditScore)
        .filter(CreditScore.ScoreID == score_id)
        .first()
    )


from sqlalchemy import text

def get_high_risk_customers(db: Session):

    query = text("""

    SELECT

        c.CustomerID,
        c.FirstName,
        c.LastName,

        l.LoanAmount,

        cs.CreditScore

    FROM Customers c

    JOIN Loans l

        ON c.CustomerID=l.CustomerID

    JOIN CreditScores cs

        ON c.CustomerID=cs.CustomerID

    WHERE cs.CreditScore < 650

    """)

    result = db.execute(query)

    return result.mappings().all()

def get_loan_summary(db: Session):

    query = text("""

        SELECT

            COUNT(*) AS TotalLoans,

            SUM(LoanAmount) AS TotalLoanAmount,

            AVG(LoanAmount) AS AverageLoan,

            MAX(LoanAmount) AS HighestLoan,

            MIN(LoanAmount) AS LowestLoan

        FROM Loans

    """)

    return db.execute(query).mappings().first()

def get_branch_performance(db: Session):

    query = text("""

        SELECT

            b.BranchName,

            COUNT(l.LoanID) AS LoansIssued,

            SUM(l.LoanAmount) AS TotalLoanValue,

            AVG(l.LoanAmount) AS AverageLoan

        FROM Branches b

        JOIN Loans l
            ON b.BranchID = l.BranchID

        GROUP BY
            b.BranchName

        ORDER BY
            TotalLoanValue DESC

    """)

    return db.execute(query).mappings().all()


def get_defaulters(db: Session):

    query = text("""

        SELECT

            c.CustomerID,

            c.FirstName,

            c.LastName,

            l.LoanAmount,

            r.DueDate,

            r.PaymentStatus

        FROM Customers c

        JOIN Loans l

            ON c.CustomerID = l.CustomerID

        JOIN Repayments r

            ON l.LoanID = r.LoanID

        WHERE r.PaymentStatus = 'Missed'

    """)

    return db.execute(query).mappings().all()

def save_prediction(
    db,
    customer_id,
    prediction,
    probability,
    risk_level,
    model_version="v1.0"
):

    prediction_record = PredictionHistory(
        CustomerID=customer_id,
        Prediction=prediction,
        Probability=probability,
        RiskLevel=risk_level,
        ModelVersion=model_version
    )

    db.add(prediction_record)
    db.commit()
    db.refresh(prediction_record)

    return prediction_record


def get_prediction_history(db):

    return (
        db.query(PredictionHistory)
        .order_by(
            PredictionHistory.PredictionTime.desc()
        )
        .all()
    )


def get_prediction(db, prediction_id):

    return (
        db.query(PredictionHistory)
        .filter(
            PredictionHistory.PredictionID == prediction_id
        )
        .first()
    )