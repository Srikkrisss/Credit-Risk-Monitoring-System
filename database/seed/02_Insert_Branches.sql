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
(
    'HDFC Jubilee Hills',
    'HYD001',
    'Road No. 36, Jubilee Hills',
    'Hyderabad',
    'Telangana',
    '500033',
    '04012345678',
    'jubileehills@hdfc.com',
    'HDFC0001001'
);
GO
