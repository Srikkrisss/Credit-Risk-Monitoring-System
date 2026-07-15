USE CreditRiskDB;
GO

INSERT INTO Loans
(
    CustomerID,
    BranchID,
    OfficerID,
    LoanNumber,
    LoanType,
    LoanAmount,
    InterestRate,
    LoanStatus,
    SanctionDate,
    TenureMonths
)
VALUES

(1,1,1,'LN100001','Home Loan',4500000,8.25,'Active','2023-01-15',240),

(2,1,2,'LN100002','Home Loan',7000000,7.90,'Active','2022-11-20',300),

(3,5,9,'LN100003','Business Loan',12000000,10.50,'Active','2021-06-10',180),

(4,4,7,'LN100004','Personal Loan',800000,11.25,'Active','2024-02-05',60),

(5,1,2,'LN100005','Education Loan',600000,8.10,'Active','2024-07-01',84),

(6,3,6,'LN100006','Home Loan',3500000,8.40,'Active','2023-03-18',180),

(7,2,3,'LN100007','Car Loan',1500000,9.20,'Active','2024-01-25',60),

(8,2,4,'LN100008','Home Loan',2500000,8.15,'Active','2022-08-14',180),

(9,3,5,'LN100009','Business Loan',9500000,10.75,'Active','2021-12-08',240),

(10,2,4,'LN100010','Car Loan',1200000,9.35,'Closed','2020-05-19',60),

(11,1,1,'LN100011','Gold Loan',500000,10.00,'Active','2025-01-10',24),

(12,2,3,'LN100012','Home Loan',4200000,8.05,'Active','2023-09-12',240),

(13,5,10,'LN100013','Business Loan',15000000,10.20,'Active','2022-04-28',300),

(14,1,2,'LN100014','Personal Loan',1000000,11.00,'Active','2024-03-15',48),

(15,3,6,'LN100015','Business Loan',9000000,10.10,'Active','2021-10-01',180),

(16,2,3,'LN100016','Car Loan',1800000,9.10,'Active','2024-05-17',72),

(17,5,9,'LN100017','Home Loan',2800000,8.30,'Active','2023-06-21',180),

(18,3,5,'LN100018','Personal Loan',950000,11.40,'Active','2024-08-11',60),

(19,1,1,'LN100019','Business Loan',6500000,10.60,'Active','2022-01-30',180),

(20,1,2,'LN100020','Home Loan',3800000,8.20,'Active','2023-02-28',240),

(21,4,8,'LN100021','Personal Loan',700000,11.50,'Active','2024-04-18',48),

(22,4,7,'LN100022','Education Loan',900000,8.45,'Active','2023-11-06',96),

(23,3,6,'LN100023','Business Loan',14000000,10.30,'Active','2022-07-12',240),

(24,3,5,'LN100024','Medical Loan',1100000,9.80,'Active','2024-06-05',60),

(25,5,10,'LN100025','Business Loan',10000000,10.15,'Active','2023-05-01',180);
GO


