USE CreditRiskDB;
GO

CREATE OR ALTER VIEW vw_CustomerRiskDashboard
AS
SELECT
    c.CustomerID,
    c.FirstName + ' ' + c.LastName AS CustomerName,
    c.Gender,
    c.City,
    c.StateName,
    c.Occupation,
    c.AnnualIncome,

    l.LoanID,
    l.LoanNumber,
    l.LoanType,
    l.LoanAmount,
    l.InterestRate,
    l.LoanStatus,

    cs.CreditScore,
    cs.RiskCategory,

    fs.MonthlyIncome,
    fs.MonthlyExpenses,
    fs.ExistingEMI,

    b.BranchName

FROM Customers c

INNER JOIN Loans l
ON c.CustomerID = l.CustomerID

LEFT JOIN CreditScores cs
ON c.CustomerID = cs.CustomerID

LEFT JOIN FinancialStatements fs
ON c.CustomerID = fs.CustomerID

LEFT JOIN Branches b
ON l.BranchID = b.BranchID;
GO

SELECT * FROM vw_CustomerRiskDashboard;             