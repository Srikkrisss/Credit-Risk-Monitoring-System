USE CreditRiskDB;
GO

CREATE TABLE Collateral
(
    CollateralID INT IDENTITY(1,1) PRIMARY KEY,

    LoanID INT NOT NULL,

    AssetType VARCHAR(50) NOT NULL,

    AssetDescription VARCHAR(250),

    EstimatedValue DECIMAL(18,2) NOT NULL,

    OwnershipVerified BIT NOT NULL,

    VerificationDate DATE,

    CONSTRAINT FK_Collateral_Loans
        FOREIGN KEY(LoanID)
        REFERENCES Loans(LoanID),

    CONSTRAINT CHK_Collateral_Value
        CHECK (EstimatedValue > 0)
);
GO