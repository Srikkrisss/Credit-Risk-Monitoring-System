import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/ml_dataset.csv")

# ==========================================
# Features and Target
# ==========================================

X = df.drop(
    columns=[
        "CustomerID",
        "Risk"
    ]
)

y = df["Risk"]

print("\nFeatures")

print(X.columns)

print("\nTarget")

print(y.head())

# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ==========================================
# Create Model
# ==========================================

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42,

    max_depth=10

)

# ==========================================
# Train
# ==========================================

print("\nTraining Model...")

model.fit(
    X_train,
    y_train
)

print("Training Complete")

# ==========================================
# Predictions
# ==========================================

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:,1]

# ==========================================
# Evaluation
# ==========================================

accuracy = accuracy_score(
    y_test,
    predictions
)

roc = roc_auc_score(
    y_test,
    probabilities
)

print("\n==========================")

print("Accuracy")

print(accuracy)

print("\nROC AUC")

print(roc)

print("\nConfusion Matrix")

print(confusion_matrix(
    y_test,
    predictions
))

print("\nClassification Report")

print(classification_report(
    y_test,
    predictions
))

# ==========================================
# Feature Importance
# ==========================================

importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print("\n==========================")

print("Feature Importance")

print(importance)

# ==========================================
# Save Model
# ==========================================

MODEL_PATH = Path("models")

MODEL_PATH.mkdir(

    exist_ok=True

)

joblib.dump(

    model,

    MODEL_PATH / "credit_risk_model.pkl"

)

print("\nModel Saved Successfully")