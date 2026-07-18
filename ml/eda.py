import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/ml_dataset.csv")

# ==========================================
# Basic Dataset Information
# ==========================================

print("\n==============================")
print("FIRST 5 ROWS")
print("==============================")
print(df.head())

print("\n==============================")
print("DATASET SHAPE")
print("==============================")
print(df.shape)

print("\n==============================")
print("DATA TYPES")
print("==============================")
print(df.info())

print("\n==============================")
print("MISSING VALUES")
print("==============================")
print(df.isnull().sum())

print("\n==============================")
print("DUPLICATE ROWS")
print("==============================")
print(df.duplicated().sum())

print("\n==============================")
print("STATISTICAL SUMMARY")
print("==============================")
print(df.describe())

print("\n==============================")
print("RISK DISTRIBUTION")
print("==============================")
print(df["Risk"].value_counts())

# ==========================================
# Graph 1 - Risk Distribution
# ==========================================

df["Risk"].value_counts().plot(kind="bar")

plt.title("Risk Distribution")
plt.xlabel("Risk")
plt.ylabel("Number of Customers")
plt.show()

# ==========================================
# Graph 2 - Credit Score
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(df["CreditScore"], bins=20)

plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Customers")
plt.show()

# ==========================================
# Graph 3 - Annual Income
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(df["AnnualIncome"], bins=20)

plt.title("Annual Income Distribution")
plt.xlabel("Annual Income")
plt.ylabel("Customers")
plt.show()

# ==========================================
# Graph 4 - Loan Amount
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(df["LoanAmount"], bins=20)

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Customers")
plt.show()

# ==========================================
# FEATURE ENGINEERING
# ==========================================

print("\n==============================")
print("FEATURE ENGINEERING")
print("==============================")

# Loan / Income Ratio
df["LoanToIncomeRatio"] = (
    df["LoanAmount"] /
    df["AnnualIncome"]
)

# Monthly Income
df["MonthlyIncome"] = (
    df["AnnualIncome"] / 12
)

# Estimated EMI
df["EstimatedEMI"] = (
    df["LoanAmount"] /
    df["LoanTerm"]
)

# EMI Burden
df["EMIBurden"] = (
    df["EstimatedEMI"] /
    df["MonthlyIncome"]
)

# Collateral Coverage
df["CollateralCoverage"] = (
    df["CollateralValue"] /
    df["LoanAmount"]
)

# Income Per Loan
df["IncomePerLoan"] = (
    df["AnnualIncome"] /
    (df["ExistingLoans"] + 1)
)

# Credit Quality
df["CreditQuality"] = (
    df["CreditScore"] / 850
)

print("\nNEW DATASET")

print(df.head())

print("\nNEW SHAPE")

print(df.shape)

print("\nNEW COLUMNS")

print(df.columns)

# ==========================================
# Save Updated Dataset
# ==========================================

df.to_csv(
    "data/ml_dataset.csv",
    index=False
)

print("\n=====================================")
print("Feature Engineering Completed")
print("Dataset Updated Successfully")
print("=====================================")