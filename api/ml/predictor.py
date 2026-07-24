import joblib
import pandas as pd
from pathlib import Path

from ml.feature_engineering import engineer_features

MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "credit_risk_model.pkl"
)

MODEL = joblib.load(MODEL_PATH)


def predict_risk(data):

    df = pd.DataFrame([data])

    # Remove non-ML fields
    df = df.drop(columns=["CustomerID"], errors="ignore")

    df = engineer_features(df)

    prediction = MODEL.predict(df)[0]

    probability = MODEL.predict_proba(df)[0][1]

    return prediction, probability