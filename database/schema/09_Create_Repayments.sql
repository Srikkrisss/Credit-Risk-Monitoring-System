USE CreditRiskDB;
GO

CREATE TABLE Repayments
(
    RepaymentID INT IDENTITY(1,1) PRIMARY KEY,

    LoanID INT NOT NULL,

    EMIAmount DECIMAL(18,2) NOT NULL,

    DueDate DATE NOT NULL,

    PaymentDate DATE NULL,

    AmountPaid DECIMAL(18,2) NOT NULL,

    PaymentStatus VARCHAR(20) NOT NULL,

    CONSTRAINT FK_Repayments_Loans
        FOREIGN KEY (LoanID)
        REFERENCES Loans(LoanID),

    CONSTRAINT CHK_EMIAmount
        CHECK (EMIAmount > 0),

    CONSTRAINT CHK_AmountPaid
        CHECK (AmountPaid >= 0)
);
GO