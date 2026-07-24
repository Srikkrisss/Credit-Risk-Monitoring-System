from sqlalchemy.orm import Session

from api.ml.predictor import predict_risk
from api.crud import save_prediction
from api.services.explanation_service import generate_reasons


def generate_prediction(data: dict, db: Session):

    prediction, probability = predict_risk(data)

    # -------------------------
    # Prediction Label
    # -------------------------

    prediction_text = "Low Risk"

    if prediction == 1:
        prediction_text = "High Risk"

    # -------------------------
    # Risk Level
    # -------------------------

    if probability >= 0.80:
        risk_level = "Critical"

    elif probability >= 0.60:
        risk_level = "High"

    elif probability >= 0.40:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    # -------------------------
    # Save Prediction
    # -------------------------

    save_prediction(
        db=db,
        customer_id=data.get("CustomerID"),
        prediction=prediction_text,
        probability=float(probability),
        risk_level=risk_level
    )

    return {

    "Prediction": prediction_text,

    "Probability": round(float(probability),4),

    "RiskLevel": risk_level,

    "Reasons": generate_reasons(data)

}