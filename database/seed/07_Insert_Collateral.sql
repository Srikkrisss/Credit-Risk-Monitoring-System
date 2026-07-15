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

(1,'House','3BHK Villa, Hyderabad',6500000,1,'2023-01-12'),
(2,'House','Luxury Villa, Hyderabad',10000000,1,'2022-11-18'),
(3,'Commercial Property','Factory, Ahmedabad',18000000,1,'2021-06-08'),
(4,'Gold','250 grams Gold',1400000,1,'2024-02-04'),
(5,'Education Bond','Education Security',900000,1,'2024-07-01'),
(6,'Apartment','2BHK Flat, Pune',5200000,1,'2023-03-16'),
(7,'Vehicle','Toyota Fortuner',2100000,1,'2024-01-22'),
(8,'Apartment','Flat, Bengaluru',3800000,1,'2022-08-12'),
(9,'Commercial Building','Office Building',14000000,1,'2021-12-05'),
(10,'Vehicle','Hyundai Creta',1800000,1,'2020-05-17'),
(11,'Gold','Gold Jewellery',850000,1,'2025-01-09'),
(12,'House','Independent House',6000000,1,'2023-09-10'),
(13,'Industrial Land','Manufacturing Unit',22000000,1,'2022-04-26'),
(14,'Fixed Deposit','FD Receipt',1500000,1,'2024-03-14'),
(15,'Commercial Property','Warehouse',13500000,1,'2021-09-28'),
(16,'Vehicle','BMW 3 Series',2800000,1,'2024-05-15'),
(17,'Apartment','Residential Flat',4200000,1,'2023-06-20'),
(18,'Gold','Gold Coins',1500000,1,'2024-08-10'),
(19,'Commercial Land','Industrial Plot',9500000,1,'2022-01-28'),
(20,'House','Duplex House',5500000,1,'2023-02-26'),
(21,'Fixed Deposit','FD Security',1200000,1,'2024-04-16'),
(22,'Education Bond','Education Deposit',1300000,1,'2023-11-04'),
(23,'Industrial Property','Manufacturing Plant',20000000,1,'2022-07-10'),
(24,'Medical Equipment','Hospital Equipment',1800000,1,'2024-06-03'),
(25,'Commercial Complex','Shopping Complex',16500000,1,'2023-04-28');
GO
