USE CreditRiskDB;
GO

WITH CustomerLoans AS
(

SELECT

c.FirstName,

c.LastName,

l.LoanAmount

FROM Customers c

JOIN Loans l

ON c.CustomerID=l.CustomerID

)

SELECT *

FROM CustomerLoans;

WITH LoanData AS
(

SELECT *

FROM Loans

)

SELECT *

FROM LoanData

WHERE LoanAmount>

(

SELECT AVG(LoanAmount)

FROM Loans

);

WITH HighRisk AS
(

SELECT

c.FirstName,

c.LastName,

cs.CreditScore,

l.LoanAmount

FROM Customers c

JOIN CreditScores cs

ON c.CustomerID=cs.CustomerID

JOIN Loans l

ON c.CustomerID=l.CustomerID

WHERE CreditScore<700

)

SELECT *

FROM HighRisk;

WITH RankedCustomers AS
(

SELECT

FirstName,

AnnualIncome,

RANK()

OVER

(

ORDER BY AnnualIncome DESC

)

IncomeRank

FROM Customers

)

SELECT *

FROM RankedCustomers

WHERE IncomeRank<=5;