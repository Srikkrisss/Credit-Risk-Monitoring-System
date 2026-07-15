USE CreditRiskDB;
GO

CREATE TABLE Customers
(
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,

    FirstName VARCHAR(50) NOT NULL,

    LastName VARCHAR(50) NOT NULL,

    DOB DATE,

    Gender VARCHAR(10),

    Email VARCHAR(100) UNIQUE,

    Phone VARCHAR(10),

    PAN VARCHAR(10) UNIQUE,

    Aadhaar VARCHAR(12) UNIQUE,

    Occupation VARCHAR(100),

    AnnualIncome DECIMAL(18,2),

    StateName VARCHAR(50),

    City VARCHAR(50),

    CustomerStatus VARCHAR(20) DEFAULT 'Active',

    CreatedDate DATETIME DEFAULT GETDATE()
);
GO

