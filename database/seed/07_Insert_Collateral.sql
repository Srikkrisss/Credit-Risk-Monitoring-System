USE CreditRiskDB;
GO

INSERT INTO Collateral
(
    LoanID,
    AssetType,
    AssetDescription,
    EstimatedValue,
    OwnershipVerified,
    VerificationDate
)
VALUES
(
    2,
    'Residential Property',
    '3 BHK Villa in Hyderabad',
    8500000,
    1,
    '2026-01-16'
);
GO
SELECT * FROM Collateral;
