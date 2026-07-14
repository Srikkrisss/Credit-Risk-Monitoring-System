USE CreditRiskDB;
GO

INSERT INTO CreditScores
(
    CustomerID,
    CreditScore,
    CreditAgency,
    ScoreDate,
    RiskCategory
)
VALUES
(
    1,
    785,
    'CIBIL',
    '2026-01-10',
    'Low Risk'
);
GO
