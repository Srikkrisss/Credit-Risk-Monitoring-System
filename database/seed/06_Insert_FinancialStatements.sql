USE CreditRiskDB;
GO

INSERT INTO FinancialStatements
(
    CustomerID,
    MonthlyIncome,
    MonthlyExpenses,
    ExistingEMI,
    OtherLoanAmount,
    TotalAssets,
    TotalLiabilities,
    StatementDate
)
VALUES
(
    1,
    150000,
    45000,
    12000,
    500000,
    8500000,
    1800000,
    '2026-01-12'
);
GO
