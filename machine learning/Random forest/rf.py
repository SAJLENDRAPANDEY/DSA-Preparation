# ==============================
# 📌 1. Import Libraries
# ==============================
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ==============================
# 📌 2. Load Dataset
# ==============================
data = pd.read_excel(r"C:\Users\SAJLE\Downloads\random_forest_dataset.xlsx")


# ==============================
# 📌 3. Data Preprocessing
# ==============================
# Convert categorical → numerical (One-Hot Encoding)
data = pd.get_dummies(data, columns=['Education_Level', 'City'], drop_first=True)


# ==============================
# 📌 4. Feature & Target Split
# ==============================
X = data.drop("Target", axis=1)
y = data["Target"]


# ==============================
# 📌 5. Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==============================
# 📌 6. Model Initialization
# ==============================
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features='sqrt',
    random_state=42
)


# ==============================
# 📌 7. Model Training
# ==============================
model.fit(X_train, y_train)


# ==============================
# 📌 8. Prediction
# ==============================
y_pred = model.predict(X_test)


# ==============================
# 📌 9. Model Evaluation
# ==============================
print("✅ Accuracy:", accuracy_score(y_test, y_pred))

print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n📈 Classification Report:")
print(classification_report(y_test, y_pred))


# ==============================
# 📌 10. Feature Importance Visualization
# ==============================
importances = model.feature_importances_

plt.figure(figsize=(10, 8))
plt.barh(X.columns, importances)
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.title("Feature Importance - Random Forest")
plt.tight_layout()
plt.show()




# kal random forest and descion ki acuracy compare krna h 