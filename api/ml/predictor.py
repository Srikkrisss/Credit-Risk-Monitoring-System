import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "credit_risk_model.pkl"

MODEL = joblib.load(MODEL_PATH)

def predict_risk(data):

    df = pd.DataFrame([data])

    # -------------------------
    # Feature Engineering
    # -------------------------

    df["LoanToIncomeRatio"] = (
        df["LoanAmount"] /
        df["AnnualIncome"]
    )

    df["MonthlyIncome"] = (
        df["AnnualIncome"] / 12
    )

    df["EstimatedEMI"] = (
        df["LoanAmount"] /
        df["LoanTerm"]
    )

    df["EMIBurden"] = (
        df["EstimatedEMI"] /
        df["MonthlyIncome"]
    )

    df["CollateralCoverage"] = (
        df["CollateralValue"] /
        df["LoanAmount"]
    )

    df["IncomePerLoan"] = (
        df["AnnualIncome"] /
        (df["ExistingLoans"] + 1)
    )

    df["CreditQuality"] = (
        df["CreditScore"] / 850
    )

    prediction = MODEL.predict(df)[0]

    probability = MODEL.predict_proba(df)[0][1]

    return prediction, probability