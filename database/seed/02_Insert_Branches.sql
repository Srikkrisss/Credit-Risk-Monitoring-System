USE CreditRiskDB;
GO

INSERT INTO Branches
(
    BranchName,
    BranchCode,
    AddressLine,
    City,
    StateName,
    Pincode,
    Phone,
    Email,
    IFSCCode
)
VALUES

('Hyderabad Main Branch','HYD001','Jubilee Hills','Hyderabad','Telangana','500033','04040001001','hyd@creditrisk.com','CRBK0001001'),

('Bengaluru Tech Branch','BLR001','Whitefield','Bengaluru','Karnataka','560066','08040001002','blr@creditrisk.com','CRBK0001002'),

('Mumbai Corporate Branch','MUM001','BKC','Mumbai','Maharashtra','400051','02240001003','mum@creditrisk.com','CRBK0001003'),

('Chennai Central Branch','CHE001','Anna Salai','Chennai','Tamil Nadu','600002','04440001004','che@creditrisk.com','CRBK0001004'),

('Ahmedabad Business Branch','AHD001','SG Highway','Ahmedabad','Gujarat','380015','07940001005','ahd@creditrisk.com','CRBK0001005');

GO

