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

(1,812,'CIBIL','2025-01-10','Excellent'),
(2,845,'CIBIL','2025-01-10','Excellent'),
(3,785,'Experian','2025-01-10','Very Good'),
(4,702,'CIBIL','2025-01-10','Good'),
(5,688,'Experian','2025-01-10','Fair'),
(6,760,'CRIF','2025-01-10','Very Good'),
(7,820,'CIBIL','2025-01-10','Excellent'),
(8,748,'Experian','2025-01-10','Good'),
(9,790,'CRIF','2025-01-10','Very Good'),
(10,735,'CIBIL','2025-01-10','Good'),
(11,680,'Experian','2025-01-10','Fair'),
(12,830,'CIBIL','2025-01-10','Excellent'),
(13,795,'CRIF','2025-01-10','Very Good'),
(14,755,'Experian','2025-01-10','Very Good'),
(15,805,'CIBIL','2025-01-10','Excellent'),
(16,710,'CRIF','2025-01-10','Good'),
(17,690,'Experian','2025-01-10','Fair'),
(18,665,'CIBIL','2025-01-10','Fair'),
(19,775,'CRIF','2025-01-10','Very Good'),
(20,815,'Experian','2025-01-10','Excellent'),
(21,640,'CIBIL','2025-01-10','Poor'),
(22,605,'CRIF','2025-01-10','Poor'),
(23,790,'Experian','2025-01-10','Very Good'),
(24,725,'CIBIL','2025-01-10','Good'),
(25,840,'CRIF','2025-01-10','Excellent');
GO

