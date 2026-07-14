USE CreditRiskDB;
GO

INSERT INTO Repayments
(
    LoanID,
    EMIAmount,
    DueDate,
    PaymentDate,
    AmountPaid,
    PaymentStatus
)
VALUES
(
    2,
    42500.00,
    '2026-02-01',
    '2026-02-01',
    42500.00,
    'Paid'
);
GO