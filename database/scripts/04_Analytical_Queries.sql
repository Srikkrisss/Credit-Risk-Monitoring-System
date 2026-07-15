USE CreditRiskDB;
GO
SELECT TOP 5

c.FirstName,
c.LastName,

l.LoanType,

l.LoanAmount

FROM Customers c

JOIN Loans l
ON c.CustomerID=l.CustomerID

ORDER BY l.LoanAmount DESC;

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

WHERE cs.CreditScore<700

ORDER BY cs.CreditScore;

SELECT

c.FirstName,
c.LastName,

fs.MonthlyIncome,

fs.ExistingEMI,

ROUND(
(fs.ExistingEMI*100.0)/fs.MonthlyIncome,
2
) AS EMI_Percentage

FROM Customers c

JOIN FinancialStatements fs

ON c.CustomerID=fs.CustomerID

ORDER BY EMI_Percentage DESC;

SELECT

c.FirstName,

c.LastName,

c.AnnualIncome,

cs.CreditScore

FROM Customers c

JOIN CreditScores cs

ON c.CustomerID=cs.CustomerID

WHERE

AnnualIncome>3000000

AND CreditScore<700;

SELECT

c.FirstName,

c.LastName,

c.AnnualIncome,

l.LoanAmount,

ROUND(

l.LoanAmount/c.AnnualIncome,

2

) AS LoanIncomeRatio

FROM Customers c

JOIN Loans l

ON c.CustomerID=l.CustomerID

ORDER BY LoanIncomeRatio DESC;

SELECT

b.BranchName,

SUM(l.LoanAmount) Portfolio

FROM Branches b

JOIN Loans l

ON b.BranchID=l.BranchID

GROUP BY b.BranchName

ORDER BY Portfolio DESC;

SELECT

RiskCategory,

COUNT(*) Customers

FROM CreditScores

GROUP BY RiskCategory

ORDER BY Customers DESC;

SELECT

c.FirstName,

c.LastName,

l.LoanNumber,

r.PaymentStatus

FROM Customers c

JOIN Loans l

ON c.CustomerID=l.CustomerID

JOIN Repayments r

ON l.LoanID=r.LoanID

WHERE r.PaymentStatus='Pending';

SELECT

b.BranchName,

AVG(cs.CreditScore) AverageCreditScore

FROM Branches b

JOIN Loans l

ON b.BranchID=l.BranchID

JOIN CreditScores cs

ON l.CustomerID=cs.CustomerID

GROUP BY b.BranchName

ORDER BY AverageCreditScore DESC;

SELECT

COUNT(DISTINCT c.CustomerID) AS TotalCustomers,

COUNT(DISTINCT l.LoanID) AS TotalLoans,

SUM(l.LoanAmount) AS LoanPortfolio,

AVG(cs.CreditScore) AvgCreditScore

FROM Customers c

JOIN Loans l

ON c.CustomerID=l.CustomerID

JOIN CreditScores cs

ON c.CustomerID=cs.CustomerID;