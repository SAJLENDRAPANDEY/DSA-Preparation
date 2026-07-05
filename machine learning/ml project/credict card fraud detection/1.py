import pandas as pd
import numpy as np

# ==============================
# GLOBAL CONFIG
# ==============================
THRESHOLD = 0.7   # consistent threshold

# ==============================
# 1. LOAD DATA
# ==============================
data = pd.read_csv(r"C:\Users\SAJLE\Downloads\ml project\dataset credit card.csv")

# ==============================
# 2. FEATURE ENGINEERING
# ==============================
data["Hour"] = (data["Time"] // 3600) % 24
data["is_night"] = data["Hour"].apply(lambda x: 1 if x < 6 else 0)
data = data.drop("Time", axis=1)

# ==============================
# 3. FEATURE SELECTION
# ==============================
top_features = ["V14","V10","V4","V11","V16","V17","V12","V7","V3","V9"]

X = data[top_features + ["Amount","Hour","is_night"]]
y = data["Class"]

# ==============================
# 4. TRAIN TEST SPLIT
# ==============================
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 5. SCALING
# ==============================
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train["Amount"] = scaler.fit_transform(X_train[["Amount"]])
X_test["Amount"] = scaler.transform(X_test[["Amount"]])

# ==============================
# 6. SMOTE
# ==============================
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# ==============================
# 7. MODEL
# ==============================
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=50,
    max_depth=10,
    class_weight='balanced',
    n_jobs=-1
)

model.fit(X_train, y_train)

# ==============================
# 8. EVALUATION
# ==============================
from sklearn.metrics import classification_report, confusion_matrix

y_prob = model.predict_proba(X_test)[:,1]
y_pred = (y_prob > THRESHOLD).astype(int)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ==============================
# 9. PREDICTION FUNCTION
# ==============================
def predict_transaction(amount, hour):

    # Validation
    if amount < 0:
        return "❌ Amount cannot be negative", None

    if hour < 0 or hour > 23:
        return "❌ Hour must be between 0 and 23", None

    # Cap amount
    MAX_AMOUNT = 100000
    if amount > MAX_AMOUNT:
        print("⚠ Amount outside training range, capping applied")
        amount = MAX_AMOUNT

    is_night = 1 if hour < 6 else 0

    # Scale
    amount_scaled = scaler.transform(
        pd.DataFrame([[amount]], columns=["Amount"])
    )[0][0]

    input_data = {
        "Amount": amount_scaled,
        "Hour": hour,
        "is_night": is_night
    }

    df = pd.DataFrame([input_data])

    # Fill missing columns
    for col in X_train.columns:
        if col not in df.columns:
            df[col] = 0

    df = df[X_train.columns]

    # Prediction
    prob = model.predict_proba(df)[0][1]
    pred = 1 if prob > THRESHOLD else 0

    return pred, prob

# ==============================
# 10. USER INPUT
# ==============================
try:
    amount = float(input("Enter Transaction Amount: "))
    hour = int(input("Enter hour (0-23): "))

    result = predict_transaction(amount, hour)

    if isinstance(result[0], str):
        print(result[0])

    else:
        pred, prob = result

        print("\n===== RESULT =====")

        # ML Prediction
        print("Model Prediction:", "Fraud" if pred == 1 else "Safe")

        # Alerts
        alerts = []
        if amount > 50000:
            alerts.append("High Amount")
        if hour < 6:
            alerts.append("Night Transaction")

        if alerts:
            print("⚠ Alerts:", ", ".join(alerts))

        # Risk Score
        final_score = prob

        if amount > 50000:
            final_score += 0.25
        if hour < 6:
            final_score += 0.2

        final_score = min(final_score, 1)

        print(f"Final Risk Score: {final_score:.2f}")

        # FINAL DECISION
        if final_score > 0.4:
            print("🚨 FINAL: FRAUD ALERT")
        else:
            print("✅ FINAL: SAFE")

except ValueError:
    print("❌ Invalid input! Please enter numbers only.")