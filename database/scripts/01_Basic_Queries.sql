USE CreditRiskDB;
GO

-- 1. View all customers
SELECT *
FROM Customers;

-- 2. View all loans
SELECT *
FROM Loans;

-- 3. View all branches
SELECT *
FROM Branches;

-- 4. View all loan officers
SELECT *
FROM LoanOfficers;

-- 5. View all credit scores
SELECT *
FROM CreditScores;

-- Active loans
SELECT *
FROM Loans
WHERE LoanStatus = 'Active';

-- Home loans
SELECT *
FROM Loans
WHERE LoanType = 'Home Loan';

-- Customers from Hyderabad
SELECT *
FROM Customers
WHERE City = 'Hyderabad';

-- Customers earning above 20 lakhs
SELECT *
FROM Customers
WHERE AnnualIncome > 2000000;

-- Credit score below 700
SELECT *
FROM CreditScores
WHERE CreditScore < 700;

-- Highest income customers
SELECT *
FROM Customers
ORDER BY AnnualIncome DESC;

-- Highest loan amount
SELECT *
FROM Loans
ORDER BY LoanAmount DESC;

-- Lowest credit score
SELECT *
FROM CreditScores
ORDER BY CreditScore;

-- Top 5 highest income customers
SELECT TOP 5 *
FROM Customers
ORDER BY AnnualIncome DESC;

-- Top 5 biggest loans
SELECT TOP 5 *
FROM Loans
ORDER BY LoanAmount DESC;

-- Total customers
SELECT COUNT(*) AS TotalCustomers
FROM Customers;

-- Total loans
SELECT COUNT(*) AS TotalLoans
FROM Loans;

-- Total loan amount
SELECT SUM(LoanAmount) AS TotalLoanAmount
FROM Loans;

-- Average loan amount
SELECT AVG(LoanAmount) AS AvgLoanAmount
FROM Loans;

-- Maximum loan
SELECT MAX(LoanAmount) AS HighestLoan
FROM Loans;

-- Minimum loan
SELECT MIN(LoanAmount) AS SmallestLoan
FROM Loans;

-- Average credit score
SELECT AVG(CreditScore) AS AvgCreditScore
FROM CreditScores;

SELECT DISTINCT LoanType
FROM Loans;

SELECT DISTINCT City
FROM Customers;

SELECT DISTINCT RiskCategory
FROM CreditScores;