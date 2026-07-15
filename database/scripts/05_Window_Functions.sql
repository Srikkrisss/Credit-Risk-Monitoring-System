USE CreditRiskDB;
GO

SELECT

CustomerID,
FirstName,
LastName,
AnnualIncome,

RANK() OVER
(
ORDER BY AnnualIncome DESC
) AS IncomeRank

FROM Customers;

SELECT

LoanNumber,

LoanAmount,

LoanType,

RANK() OVER
(
ORDER BY LoanAmount DESC
) AS LoanRank

FROM Loans;

SELECT

CustomerID,

FirstName,

AnnualIncome,

DENSE_RANK() OVER
(
ORDER BY AnnualIncome DESC
) IncomeRank

FROM Customers;

SELECT

CustomerID,

FirstName,

ROW_NUMBER()

OVER

(
ORDER BY AnnualIncome DESC
)

AS RowNum

FROM Customers;

SELECT

b.BranchName,

l.LoanAmount,

RANK()

OVER

(

PARTITION BY b.BranchName

ORDER BY LoanAmount DESC

)

AS RankWithinBranch

FROM Loans l

JOIN Branches b

ON l.BranchID=b.BranchID;

SELECT

LoanID,

LoanAmount,

SUM(LoanAmount)

OVER

(

ORDER BY LoanID

)

AS RunningPortfolio

FROM Loans;

SELECT

LoanNumber,

LoanType,

LoanAmount,

AVG(LoanAmount)

OVER

(

PARTITION BY LoanType

)

AS AvgLoanType

FROM Loans;

SELECT

FirstName,

AnnualIncome,

AVG(AnnualIncome)

OVER()

AS OverallAverageIncome

FROM Customers;