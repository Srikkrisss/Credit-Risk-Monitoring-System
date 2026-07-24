import pandas as pd


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs all feature engineering required by the ML model.
    This function is used during both model training and prediction.
    """

    df = df.copy()

    # Prevent division errors
    df["AnnualIncome"] = df["AnnualIncome"].replace(0, 1)
    df["LoanAmount"] = df["LoanAmount"].replace(0, 1)
    df["LoanTerm"] = df["LoanTerm"].replace(0, 1)

    # -----------------------------
    # Engineered Features
    # -----------------------------

    df["LoanToIncomeRatio"] = (
        df["LoanAmount"] / df["AnnualIncome"]
    )

    df["MonthlyIncome"] = (
        df["AnnualIncome"] / 12
    )

    df["EstimatedEMI"] = (
        df["LoanAmount"] / df["LoanTerm"]
    )

    df["EMIBurden"] = (
        df["EstimatedEMI"] / df["MonthlyIncome"]
    )

    df["CollateralCoverage"] = (
        df["CollateralValue"] / df["LoanAmount"]
    )

    df["IncomePerLoan"] = (
        df["AnnualIncome"] /
        (df["ExistingLoans"] + 1)
    )

    df["CreditQuality"] = (
        df["CreditScore"] / 850
    )

    return df