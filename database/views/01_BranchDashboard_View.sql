USE CreditRiskDB;
GO

CREATE OR ALTER VIEW vw_BranchDashboard
AS
SELECT
    b.BranchID,
    b.BranchName,
    b.City,
    b.StateName,

    l.LoanID,
    l.LoanNumber,
    l.LoanType,
    l.LoanAmount,
    l.InterestRate,
    l.LoanStatus,

    c.CustomerID,
    c.FirstName + ' ' + c.LastName AS CustomerName,
    c.Occupation,
    c.AnnualIncome,

    lo.OfficerID,
    lo.FirstName + ' ' + lo.LastName AS OfficerName,
    lo.Designation,

    cs.CreditScore,
    cs.RiskCategory

FROM Loans l

INNER JOIN Customers c
ON l.CustomerID = c.CustomerID

INNER JOIN Branches b
ON l.BranchID = b.BranchID

INNER JOIN LoanOfficers lo
ON l.OfficerID = lo.OfficerID

LEFT JOIN CreditScores cs
ON c.CustomerID = cs.CustomerID;
GO

SELECT * FROM vw_BranchDashboard;