CREATE INDEX IX_Loans_CustomerID
ON Loans(CustomerID);
GO

CREATE INDEX IX_Loans_BranchID
ON Loans(BranchID);
GO

CREATE INDEX IX_CreditScores_CustomerID
ON CreditScores(CustomerID);
GO

CREATE INDEX IX_Repayments_LoanID
ON Repayments(LoanID);
GO

SELECT
    name AS IndexName,
    OBJECT_NAME(object_id) AS TableName
FROM sys.indexes
WHERE name LIKE 'IX_%';