import pandas as pd
import random
from pathlib import Path

# ==========================================
# Create Output Folder
# ==========================================

DATA_PATH = Path("data")
DATA_PATH.mkdir(parents=True, exist_ok=True)

# ==========================================
# Number of Customers
# ==========================================

NUM_CUSTOMERS = 10000

# ==========================================
# Empty Dataset
# ==========================================

dataset = []

# ==========================================
# Generate Customers
# ==========================================

for customer_id in range(1, NUM_CUSTOMERS + 1):

    # Basic Customer Details
    age = random.randint(21, 65)

    employment_years = random.randint(
        0,
        age - 21
    )

    # Financial Details
    credit_score = random.randint(300, 850)

    annual_income = random.randint(
        200000,
        3000000
    )

    loan_amount = random.randint(
        100000,
        5000000
    )

    interest_rate = round(
        random.uniform(7, 18),
        2
    )

    loan_term = random.choice(
        [12, 24, 36, 48, 60, 120, 180, 240, 360]
    )

    existing_loans = random.randint(0, 5)

    debt_to_income = round(
        random.uniform(0.10, 0.90),
        2
    )

    collateral_value = random.randint(
        0,
        10000000
    )

    # ==========================================
    # Risk Score Calculation
    # ==========================================

    risk_score = 0

    if credit_score < 650:
        risk_score += 1

    if debt_to_income > 0.50:
        risk_score += 1

    if loan_amount > annual_income:
        risk_score += 1

    if collateral_value < (loan_amount * 0.5):
        risk_score += 1

    if existing_loans >= 4:
        risk_score += 1

    # ==========================================
    # Final Risk Label
    # ==========================================

    if risk_score >= 3:
        risk = 1
    else:
        risk = 0

    # ==========================================
    # Store Customer
    # ==========================================

    dataset.append({
        "CustomerID": customer_id,
        "Age": age,
        "EmploymentYears": employment_years,
        "CreditScore": credit_score,
        "AnnualIncome": annual_income,
        "LoanAmount": loan_amount,
        "InterestRate": interest_rate,
        "LoanTerm": loan_term,
        "ExistingLoans": existing_loans,
        "DebtToIncomeRatio": debt_to_income,
        "CollateralValue": collateral_value,
        "Risk": risk
    })

# ==========================================
# Convert to DataFrame
# ==========================================

df = pd.DataFrame(dataset)

# ==========================================
# Check Dataset
# ==========================================

print("\nFirst 5 Rows\n")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ==========================================
# Save Dataset
# ==========================================

df.to_csv(
    DATA_PATH / "ml_dataset.csv",
    index=False
)

print("\n===================================")
print(f"Generated {len(df)} customer records")
print("Dataset saved successfully!")
print("Location:", DATA_PATH / "ml_dataset.csv")
print("===================================")