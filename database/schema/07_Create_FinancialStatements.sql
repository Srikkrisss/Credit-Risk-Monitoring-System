USE CreditRiskDB;
GO

CREATE TABLE FinancialStatements
(
    StatementID INT IDENTITY(1,1) PRIMARY KEY,

    CustomerID INT NOT NULL,

    MonthlyIncome DECIMAL(18,2) NOT NULL,

    MonthlyExpenses DECIMAL(18,2) NOT NULL,

    ExistingEMI DECIMAL(18,2) NOT NULL,

    OtherLoanAmount DECIMAL(18,2) DEFAULT 0,

    TotalAssets DECIMAL(18,2),

    TotalLiabilities DECIMAL(18,2),

    StatementDate DATE NOT NULL,

    CONSTRAINT FK_FinancialStatements_Customers
        FOREIGN KEY(CustomerID)
        REFERENCES Customers(CustomerID),

    CONSTRAINT CHK_Income
        CHECK (MonthlyIncome >= 0),

    CONSTRAINT CHK_Expenses
        CHECK (MonthlyExpenses >= 0)
);
GO
