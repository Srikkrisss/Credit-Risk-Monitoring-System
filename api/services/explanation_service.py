def generate_reasons(data):

    reasons = []

    # -----------------------------
    # Credit Score
    # -----------------------------

    if data["CreditScore"] < 600:
        reasons.append(
            "Credit Score below 600"
        )

    elif data["CreditScore"] < 700:
        reasons.append(
            "Average Credit Score"
        )

    else:
        reasons.append(
            "Good Credit Score"
        )

    # -----------------------------
    # Debt Ratio
    # -----------------------------

    if data["DebtToIncomeRatio"] > 0.40:
        reasons.append(
            "High Debt-to-Income Ratio"
        )

    # -----------------------------
    # Loan vs Income
    # -----------------------------

    if data["LoanAmount"] > data["AnnualIncome"]:
        reasons.append(
            "Loan amount exceeds annual income"
        )

    # -----------------------------
    # Employment
    # -----------------------------

    if data["EmploymentYears"] < 2:
        reasons.append(
            "Limited employment history"
        )

    # -----------------------------
    # Existing Loans
    # -----------------------------

    if data["ExistingLoans"] >= 3:
        reasons.append(
            "Multiple active loans"
        )

    # -----------------------------
    # Collateral
    # -----------------------------

    coverage = (
        data["CollateralValue"] /
        data["LoanAmount"]
    )

    if coverage < 1:
        reasons.append(
            "Collateral coverage is insufficient"
        )

    return reasons