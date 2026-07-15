USE CreditRiskDB;
GO

SELECT
    c.CustomerID,
    c.FirstName,
    c.LastName,
    l.LoanNumber,
    l.LoanType,
    l.LoanAmount,
    l.LoanStatus
FROM Customers c
INNER JOIN Loans l
    ON c.CustomerID = l.CustomerID;

SELECT
    c.FirstName,
    c.LastName,
    cs.CreditScore,
    cs.RiskCategory
FROM Customers c
INNER JOIN CreditScores cs
    ON c.CustomerID = cs.CustomerID;

SELECT
    l.LoanNumber,
    l.LoanType,
    b.BranchName,
    b.City
FROM Loans l
INNER JOIN Branches b
    ON l.BranchID = b.BranchID;

SELECT
    l.LoanNumber,
    lo.FirstName,
    lo.LastName,
    lo.Designation
FROM Loans l
INNER JOIN LoanOfficers lo
    ON l.OfficerID = lo.OfficerID;

SELECT
    c.FirstName,
    c.LastName,
    fs.MonthlyIncome,
    fs.MonthlyExpenses,
    fs.ExistingEMI
FROM Customers c
INNER JOIN FinancialStatements fs
    ON c.CustomerID = fs.CustomerID;

SELECT
    c.FirstName,
    c.LastName,
    l.LoanAmount,
    cs.CreditScore
FROM Customers c
INNER JOIN Loans l
    ON c.CustomerID = l.CustomerID
INNER JOIN CreditScores cs
    ON c.CustomerID = cs.CustomerID;

SELECT
    c.FirstName + ' ' + c.LastName AS CustomerName,
    l.LoanNumber,
    l.LoanType,
    l.LoanAmount,
    b.BranchName,
    lo.FirstName + ' ' + lo.LastName AS LoanOfficer
FROM Loans l
INNER JOIN Customers c
    ON l.CustomerID = c.CustomerID
INNER JOIN Branches b
    ON l.BranchID = b.BranchID
INNER JOIN LoanOfficers lo
    ON l.OfficerID = lo.OfficerID;

SELECT
    l.LoanNumber,
    r.DueDate,
    r.PaymentDate,
    r.AmountPaid,
    r.PaymentStatus
FROM Loans l
INNER JOIN Repayments r
    ON l.LoanID = r.LoanID;

SELECT
    l.LoanNumber,
    c.AssetType,
    c.EstimatedValue
FROM Loans l
INNER JOIN Collateral c
    ON l.LoanID = c.LoanID;

SELECT
    cu.FirstName,
    cu.LastName,
    cu.City,
    cu.AnnualIncome,
    cs.CreditScore,
    l.LoanAmount,
    l.LoanStatus
FROM Customers cu
INNER JOIN CreditScores cs
    ON cu.CustomerID = cs.CustomerID
INNER JOIN Loans l
    ON cu.CustomerID = l.CustomerID;