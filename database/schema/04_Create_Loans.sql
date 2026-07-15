Use CreditRiskDB;
GO

Create TABLE Loans
(
	LoanID INT IDENTITY(1,1) PRIMARY KEY,

	CustomerID INT NOT NULL,

	BranchID INT NOT NULL,

    OfficerID INT NOT NULL,

	LoanNumber VARCHAR(20) UNIQUE NOT NULL,

	LoanType VARCHAR(50) NOT NULL,

	LoanAmount DECIMAL(18,2) NOT NULL,

	InterestRate DECIMAL(5,2) NOT NULL,

	TenureMonths INT NOT NULL,
	
	LoanStatus VARCHAR(20) NOT NULL,

	SanctionDate DATE NOT NULL,



	CONSTRAINT FK_Loans_Customers
	FOREIGN KEY (CustomerID)
		REFERENCES Customers(CustomerID),

	CONSTRAINT FK_Loans_Branches
    FOREIGN KEY (BranchID)
		REFERENCES Branches(BranchID),

    CONSTRAINT FK_Loans_LoanOfficers
    FOREIGN KEY (OfficerID)
        REFERENCES LoanOfficers(OfficerID)
);
GO
