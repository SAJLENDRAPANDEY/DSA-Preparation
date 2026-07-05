from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
data = pd.read_excel(r"C:\Users\SAJLE\Downloads\iris dataset.xlsx")

# features & target
X = data.iloc[:, :-1]
y = data['species']

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 🔥 STEP 1: Scaling FIRST
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 🔥 STEP 2: Find best K (after scaling)
scores = []
k_range = range(1, 21)

for i in k_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)
    scores.append(accuracy_score(y_test, y_pred))

# plot
plt.figure(figsize=(8,5))
plt.plot(k_range, scores)
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("K vs Accuracy")
plt.show()

# best K
best_k = np.argmax(scores) + 1
print("Best K:", best_k)

# 🔥 STEP 3: Final Model
knn = KNeighborsClassifier(n_neighbors=best_k, weights='distance')
knn.fit(X_train, y_train)

# prediction
y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 🔥 STEP 4: New Prediction
new_data = [[7, 3.2, 4.7, 1.4]]
new_data_scaled = scaler.transform(new_data)

prediction = knn.predict(new_data_scaled)
print("Predicted class:", prediction[0])

# class distribution
print(data['species'].value_counts())