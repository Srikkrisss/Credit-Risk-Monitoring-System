import joblib
import pandas as pd
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

from ml.feature_engineering import engineer_features


# ---------------------------------------------------
# Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

DATASET_PATH = BASE_DIR / "data" / "ml_dataset.csv"
MODEL_PATH = BASE_DIR / "models" / "credit_risk_model.pkl"

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)

print(df.head())
print()
print(df.shape)

# ---------------------------------------------------
# Remove already engineered columns (if they exist)
# ---------------------------------------------------

engineered_columns = [
    "LoanToIncomeRatio",
    "MonthlyIncome",
    "EstimatedEMI",
    "EMIBurden",
    "CollateralCoverage",
    "IncomePerLoan",
    "CreditQuality"
]

df = df.drop(
    columns=[c for c in engineered_columns if c in df.columns],
    errors="ignore"
)

# ---------------------------------------------------
# Feature Engineering
# ---------------------------------------------------

print("\nCreating Engineered Features...")

df = engineer_features(df)

print(df.head())

# ---------------------------------------------------
# Features & Target
# ---------------------------------------------------

TARGET = "Risk"

X = df.drop(columns=["CustomerID", TARGET])

y = df[TARGET]

# ---------------------------------------------------
# Train/Test Split
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ---------------------------------------------------
# Model
# ---------------------------------------------------

print("\nTraining Model...")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ---------------------------------------------------
# Evaluation
# ---------------------------------------------------

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:, 1]

print("\nAccuracy")

accuracy = accuracy_score(
    y_test,
    predictions
)

print(round(accuracy,4))

print("\nROC AUC")

roc = roc_auc_score(
    y_test,
    probabilities
)

print(round(roc,4))

print("\nClassification Report")

print(
    classification_report(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------

joblib.dump(
    model,
    MODEL_PATH
)

print("\nModel Saved Successfully!")

print(MODEL_PATH)