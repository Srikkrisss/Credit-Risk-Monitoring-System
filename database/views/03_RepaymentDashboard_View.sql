USE CreditRiskDB;
GO

CREATE OR ALTER VIEW vw_RepaymentDashboard
AS
SELECT

    r.RepaymentID,
    r.LoanID,
    r.EMIAmount,
    r.DueDate,
    r.PaymentDate,
    r.AmountPaid,
    r.PaymentStatus,

    l.LoanNumber,
    l.LoanType,
    l.LoanAmount,
    l.LoanStatus,

    c.CustomerID,
    c.FirstName + ' ' + c.LastName AS CustomerName,

    b.BranchName,

    cs.CreditScore,
    cs.RiskCategory

FROM Repayments r

INNER JOIN Loans l
ON r.LoanID = l.LoanID

INNER JOIN Customers c
ON l.CustomerID = c.CustomerID

INNER JOIN Branches b
ON l.BranchID = b.BranchID

LEFT JOIN CreditScores cs
ON c.CustomerID = cs.CustomerID;
GO

SELECT * FROM vw_RepaymentDashboard;