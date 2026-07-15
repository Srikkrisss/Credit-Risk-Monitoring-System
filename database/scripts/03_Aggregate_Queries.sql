USE CreditRiskDB;
GO

SELECT COUNT(*) AS TotalCustomers
FROM Customers;

SELECT 
	SUM(LoanAmount) AS TotalLoanPortfolio
	FROM Loans;

SELECT 
	AVG(LoanAmount) AS AverageLoanAmount
	FROM Loans;

SELECT 
	MAX(LoanAmount) AS HighestLoan,
	MIN(LoanAmount) AS LowestLoan
	FROM Loans;

SELECT

LoanType,

COUNT(*) AS NumberOfLoans,

SUM(LoanAmount) AS TotalAmount

FROM Loans

GROUP BY LoanType

ORDER BY TotalAmount DESC;

SELECT

b.BranchName,

COUNT(*) AS TotalLoans,

SUM(l.LoanAmount) AS TotalLoanAmount

FROM Loans l

JOIN Branches b

ON l.BranchID=b.BranchID

GROUP BY b.BranchName

ORDER BY TotalLoanAmount DESC;

SELECT

RiskCategory,

AVG(CreditScore) AverageScore

FROM CreditScores

GROUP BY RiskCategory

ORDER BY AverageScore DESC;

SELECT

StateName,

COUNT(*) AS TotalCustomers

FROM Customers

GROUP BY StateName

ORDER BY TotalCustomers DESC;

SELECT

Occupation,

AVG(AnnualIncome) AverageIncome

FROM Customers

GROUP BY Occupation

ORDER BY AverageIncome DESC;

SELECT

LoanStatus,

SUM(LoanAmount) TotalAmount

FROM Loans

GROUP BY LoanStatus;

SELECT

b.BranchName,

SUM(l.LoanAmount) Portfolio

FROM Loans l

JOIN Branches b

ON l.BranchID=b.BranchID

GROUP BY b.BranchName

HAVING SUM(l.LoanAmount)>10000000;

SELECT

LoanType,

COUNT(*) TotalLoans

FROM Loans

GROUP BY LoanType

HAVING COUNT(*)>3;

