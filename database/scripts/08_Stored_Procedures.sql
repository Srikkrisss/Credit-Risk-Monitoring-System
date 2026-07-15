CREATE PROCEDURE usp_GetCustomerLoans

@CustomerID INT

AS

BEGIN

SELECT

c.FirstName,

c.LastName,

l.LoanNumber,

l.LoanAmount,

l.LoanType,

l.LoanStatus

FROM Customers c

JOIN Loans l

ON c.CustomerID=l.CustomerID

WHERE c.CustomerID=@CustomerID;

END;
GO

CREATE PROCEDURE usp_GetHighRiskCustomers

AS

BEGIN

SELECT *

FROM vw_HighRiskCustomers;

END;
GO

CREATE PROCEDURE usp_GetBranchPortfolio

AS

BEGIN

SELECT *

FROM vw_BranchPerformance;

END;
GO

CREATE PROCEDURE usp_GetCustomerCredit

@CustomerID INT

AS

BEGIN

SELECT *

FROM vw_CustomerCreditProfile

WHERE CustomerID=@CustomerID;

END;
GO

EXEC usp_GetCustomerLoans @CustomerID = 1;

EXEC usp_GetHighRiskCustomers;

EXEC usp_GetBranchPortfolio;

EXEC usp_GetCustomerCredit @CustomerID = 10;
