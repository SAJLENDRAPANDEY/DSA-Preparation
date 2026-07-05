# ==============================
# 📌 Decision Tree Classification Project
# ==============================

# 🔹 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# 🔹 2. Load Dataset
data = pd.read_excel(r"C:\Users\SAJLE\Downloads\decision_tree_dataset.xlsx")


# 🔹 3. Data Preprocessing
# Drop unnecessary columns
data.drop(['Participation', 'Extra_Classes', 'Parent_Education'], axis=1, inplace=True)

# Define features & target
X = data.drop('Pass', axis=1)
y = data['Pass'].map({'No': 0, 'Yes': 1})


# 🔹 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 🔹 5. Model Building
model = DecisionTreeClassifier(max_depth=2)


# 🔹 6. Model Training
model.fit(X_train, y_train)


# 🔹 7. Prediction
y_pred = model.predict(X_test)


# 🔹 8. Model Evaluation

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("📊 Accuracy:", accuracy)

# Confusion Matrix
print("\n📌 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\n📌 Classification Report:")
print(classification_report(y_test, y_pred))


# 🔹 9. Visualization of Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(
    model,
    filled=True,
    feature_names=X.columns,
    class_names=['No', 'Yes']
)
plt.title("Decision Tree Visualization")
plt.show()