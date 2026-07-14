USE CreditRiskDB;
GO

CREATE TABLE CreditScores
(
	CreditScoreID INT IDENTITY(1,1) PRIMARY KEY,

	CustomerID INT NOT NULL,

	CreditScore INT NOT NULL,

	CreditAgency VARCHAR(50) NOT NULL,

	ScoreDate DATE NOT NULL,

	RiskCategory VARCHAR(20) NOT NULL,

	CONSTRAINT FK_CreditScores_Customers
		FOREIGN KEY(CustomerID)
		REFERENCES Customers(CustomerID),

	CONSTRAINT CHK_CreditScore
    CHECK (CreditScore BETWEEN 300 AND 900)

);
GO
