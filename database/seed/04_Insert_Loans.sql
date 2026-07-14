USE CreditRiskDB;
GO

INSERT INTO Loans
(
    CustomerID,
    BranchID,
    OfficerID,
    LoanNumber,
    LoanType,
    LoanAmount,
    InterestRate,
    TenureMonths,
    LoanStatus,
    SanctionDate
)
VALUES
(
    1,
    1,
    1,
    'LN20260001',
    'Home Loan',
    5000000.00,
    8.25,
    240,
    'Active',
    '2026-01-15'
);
GO

SELECT * FROM Loans;