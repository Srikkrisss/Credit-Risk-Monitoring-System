USE CreditRiskDB;
GO

CREATE TABLE LoanOfficers
(
    OfficerID INT IDENTITY(1,1) PRIMARY KEY,

    BranchID INT NOT NULL,

    EmployeeCode VARCHAR(20) UNIQUE NOT NULL,

    FirstName VARCHAR(50) NOT NULL,

    LastName VARCHAR(50) NOT NULL,

    Email VARCHAR(100) UNIQUE NOT NULL,

    PhoneNumber VARCHAR(15) UNIQUE NOT NULL,

    Designation VARCHAR(50) NOT NULL,

    ExperienceYears INT NOT NULL,

    HireDate DATE NOT NULL,

    CONSTRAINT FK_LoanOfficers_Branches
    FOREIGN KEY (BranchID)
        REFERENCES Branches(BranchID)
);
GO
