USE CreditRiskDB;
GO

CREATE VIEW vw_CustomerLoanSummary
AS
SELECT

c.CustomerID,

c.FirstName,

c.LastName,

c.City,

c.Occupation,

l.LoanNumber,

l.LoanType,

l.LoanAmount,

l.InterestRate,

l.LoanStatus

FROM Customers c

JOIN Loans l

ON c.CustomerID=l.CustomerID;
GO

CREATE VIEW vw_CustomerCreditProfile
AS

SELECT

c.CustomerID,

c.FirstName,

c.LastName,

cs.CreditScore,

cs.RiskCategory,

c.AnnualIncome

FROM Customers c

JOIN CreditScores cs

ON c.CustomerID=cs.CustomerID;
GO

CREATE VIEW vw_BranchPerformance
AS

SELECT

b.BranchName,

COUNT(l.LoanID) AS TotalLoans,

SUM(l.LoanAmount) AS TotalLoanPortfolio,

AVG(l.InterestRate) AverageInterestRate

FROM Branches b

LEFT JOIN Loans l

ON b.BranchID=l.BranchID

GROUP BY b.BranchName;
GO

CREATE VIEW vw_HighRiskCustomers
AS

SELECT

c.FirstName,

c.LastName,

cs.CreditScore,

cs.RiskCategory,

l.LoanAmount

FROM Customers c

JOIN CreditScores cs

ON c.CustomerID=cs.CustomerID

JOIN Loans l

ON c.CustomerID=l.CustomerID

WHERE cs.CreditScore<700;
GO

CREATE VIEW vw_RepaymentStatus
AS

SELECT

c.FirstName,

c.LastName,

l.LoanNumber,

r.DueDate,

r.PaymentDate,

r.AmountPaid,

r.PaymentStatus

FROM Customers c

JOIN Loans l

ON c.CustomerID=l.CustomerID

JOIN Repayments r

ON l.LoanID=r.LoanID;
GO


SELECT * FROM vw_CustomerLoanSummary;

SELECT * FROM vw_CustomerCreditProfile;

SELECT * FROM vw_BranchPerformance;

SELECT * FROM vw_HighRiskCustomers;

SELECT * FROM vw_RepaymentStatus;